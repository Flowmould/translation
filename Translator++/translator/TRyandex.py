from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QClipboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Метка в левом верхнем углу")
        self.setGeometry(100, 100, 500, 500)

        label = QLabel(self)
        label.setText("Метка")
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setGeometry(0, 0, self.width(), self.height())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()