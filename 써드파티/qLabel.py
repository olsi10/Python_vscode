from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 GUI")

        label1 = QtWidgets.QLabel("Lable", self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.resize(80, 20)

        label2 = QtWidgets.QLabel("LAALALAL", self)
        label2.setAlignment(QtCore.Qt.AligRight)
        label2.resile(80, 30)


        layout = QtWidgets.QBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.layout(layout)
        self.resize(400, 300)
        self.show()

app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()