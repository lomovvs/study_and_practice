from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Example')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    sys.exit(app.exec_())