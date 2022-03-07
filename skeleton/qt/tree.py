import pickle
from skeleton.qimport import QtWidgets, QtCore, QtGui, Signal, Slot


class TreeModel(QtCore.QAbstractItemModel):
    """see also: http://stackoverflow.com/questions/1985936/creating-qt-models-for-tree-views
    """

    def __init__(self, root, parent=None):
        super().__init__(parent)
        self.root = root

    # ************ Re-implemented virtual functions **************

    def data(self, index, role):
        """Returns the data stored under the given role for the item referred to by the index.
        index == QModelIndex
        """
        if not index.isValid():
            return None
        if role != QtCore.Qt.DisplayRole:
            return None

        item = index.internalPointer()
        return item.data(index.column())

    def index(self, row, column, parent):
        """Returns the index of the item in the model specified by the given row, column and parent index.
        row, column == int, parent == QModelIndex
        """

        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.root
        else:
            # So, here we go from QModelIndex to the actual object .. ?
            parentItem = parent.internalPointer()

        # the only place where a child item is queried
        childItem = parentItem.getChild(row)
        if childItem:
            # return self.createIndex(row, column)
            return self.createIndex(row, column, childItem)
            """
            # .. that one does not work for PySide 5.12+
            TypeError: 'PyQt5.QtCore.QAbstractItemModel.createIndex' called with wrong argument types:
            PyQt5.QtCore.QAbstractItemModel.createIndex(int, int, ServerListItem)
            Supported signatures:
            PyQt5.QtCore.QAbstractItemModel.createIndex(int, int, quintptr = 0)
            PyQt5.QtCore.QAbstractItemModel.createIndex(int, int, void = nullptr)
            """
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        """Returns the parent of the model item with the given index. If the item has no parent, an invalid QModelIndex is returned.
        """
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        # the only place where the parent item is queried
        parentItem = childItem.getParent()

        if parentItem == self.root:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def columnCount(self, parent):
        """Returns the number of columns for the children of the given parent.
        """
        # print("columnCount:",self)
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.root.columnCount()

    def rowCount(self, parent):
        """Returns the number of rows under the given parent. When the parent is valid it means that rowCount is returning the number of children of parent.
        """

        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.root
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def headerData(self, section, orientation, role):
        """Returns the data for the given role and section in the header with the specified orientation.
        """

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.root.data(section)

        return None

    def flags(self, index):
        """Returns the item flags for the given index.
        """

        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        item = index.internalPointer()

        # return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable |
        # QtCore.Qt.ItemIsDragEnabled
        return item.getFlags()
    
    def removeRows(self, row: int, count: int, parent: QtCore.QModelIndex):
        if (not parent.isValid()):
            parentItem = self.root
        else:
            parentItem = parent.internalPointer()

        if (row < 0 or row >= parentItem.childCount()):
            return False

        self.beginRemoveRows(parent, row, row + count - 1)
        for i in range(0, count):
            if (not parentItem.removeChild(row)):
                break
        self.endRemoveRows()
    
    # ***************************************************'

    # **** drag'n'drop ****

    def mimeTypes(self):
        # print("data model: mime types")
        # return ["application/vnd.text.list"]
        return ["application/octet-stream"]

    def mimeData(self, par):
        # print("data model: mime data",par) # [QModelIndex, QModelIndex]
        mimeData = QtCore.QMimeData()
        index = par[0]
        item = index.internalPointer()
        # print("data model: mime data: item=",item,item.getSlot())
        # mimeData.setText("kokkelis")
        # mimeData.setText(pickle.dumps(item.getMimeData()))
        # mimeData.setData("application/octet-stream",pickle.dumps(item.getMimeData()))
        mimeData.setData(
            "application/octet-stream",
            pickle.dumps(
                item.getMimeData()))
        return mimeData



class BasicTreeView(QtWidgets.QTreeView):
    """A Tree view
    """
    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.root = root
        self.setMinimumWidth(600)
        self.initTree()

    def initTree(self):
        self.model = TreeModel(self.root)
        self.setModel(self.model)
        self.setColumnWidth(0, 300)
        # self.expandAll() # has no effect here..
    
    def reset_(self):
        self.model.removeRows(0, self.root.childCount(), self.rootIndex())
            
    def showEvent(self, e):
        super().showEvent(e)
        self.expandAll()
        


class ListItem:
    """A drag'n'droppable item in the Qt tree list
    """

    def __init__(self, parent = None):
        self.parent = parent
        self.init()

    def init(self):
        if (self.parent is not None):  # must be another ListItem instance
            assert(issubclass(self.parent.__class__, ListItem))
            # so, we now about our parent
            self.parent.addChild(self)
            # .. now parent knows about us
        self.children = []
        self.makeFlags()
        self.makeItemData()  # what is shown in the table/tree view

    def makeItemData(self):
        """A list that is used by the tree view to create a label
        """
        raise(AssertionError("virtual method"))
        # self.itemData =

    def getMimeData(self):
        """The data structure that passed in drag'n'drop
        """
        raise(AssertionError("virtual method"))

    def getItemData(self):
        return self.itemData

    def makeFlags(self):
        self.flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled

    def addChild(self, child):
        self.children.append(child)
        
    """
    def removeChild(self):
        for child in self.children:
            child.removeChildren()
        self.parent = None # detach
        self.children = []
        # self.itemData = None
    """

    # ****** An Item must re-implement these methods for nested tables ******
    def getFlags(self):
        return self.flags

    def getChild(self, row):   # return my children with index "Device classes for the cameralistrow"
        return self.children[row]

    def childCount(self):   # how many children I have
        return len(self.children)

    def removeChild(self, row):
        try:
            self.children.pop(row)
        except IndexError:
            return False
        else:
            return True
            
    def columnCount(self):  # how many data columns we have
        return len(self.itemData)

    def data(self, col):    # the actual data/text in the columns
        if (col >= len(self.itemData)):
            return None
        else:
            return self.itemData[col]

    def getParent(self):       # my parent
        return self.parent

    def row(self):          # my row index according to my parent
        if self.parent is not None:
            return self.parent.children.index(self)
        return 0
    # ***********************************************************************


class HeaderListItem(ListItem):
    """A root item that's in the tree lists header

    Defines table's columns
    """
    def makeItemData(self):
        self.itemData = ["Name", "Surname"]

    def getMimeData(self):
        return None


class NameListItem(ListItem):


    def __init__(self, name, surname, parent = None):
        self.name = name
        self.surname = surname
        self.parent = parent
        self.init()

    def makeItemData(self):
        self.itemData = [self.name, self.surname]

    def getMimeData(self):
        return None
    


class TestGui(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setGeometry(QtCore.QRect(100,100,800,800))
        self.w=QtWidgets.QWidget(self)
        self.setCentralWidget(self.w)
        self.lay=QtWidgets.QVBoxLayout(self.w)

        self.root = HeaderListItem()
        NameListItem("John", "Doe", parent = self.root)
        NameListItem("Joanna", "Doe", parent = self.root)
        self.treelist = BasicTreeView(parent=self.w, root=self.root)
        self.lay.addWidget(self.treelist)


def main():
    app=QtWidgets.QApplication(["test_app"])
    mg=TestGui()
    mg.show()
    app.exec_()


if __name__ == "__main__":
    main()

