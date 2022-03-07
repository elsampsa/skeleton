from skeleton.qimport import QtWidgets, QtCore, QtGui, Signal, Slot


class MyGui(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()
    

    def setupUi(self):
        self.setGeometry(QtCore.QRect(100,100,800,800))
        self.w=QtWidgets.QWidget(self)
        self.setCentralWidget(self.w)
        self.lay=QtWidgets.QVBoxLayout(self.w)
        # self.lay.addWidget(self.timelinewidget)
        
    
def main():
    app=QtWidgets.QApplication(["test_app"])
    mg=MyGui()
    mg.show()
    app.exec_()


if (__name__ == "__main__"):
    main()

