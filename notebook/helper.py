"""Some random quick'n'dirty helper functions for your notebook
"""
import cv2

class ImageDir:

    def __init__(self, di, bw = False):
        self.bw = bw
        filenames = glob.glob(di + "/*")
        self.names = {}
        for filename in filenames:
            name = filename.split("/")[-1]
            self.names[name] = filename

    def __str__(self):
        st = ""
        for name in self.names.keys():
            st += name + "\n"
        return st

    def __getitem__(self, name):
        assert(name in self.names)
        if self.bw:
            return cv2.imread(self.names[name], 0)
        else:
            return cv2.cvtColor(
                cv2.imread(self.names[name]),
                cv2.COLOR_BGR2RGB
            )

