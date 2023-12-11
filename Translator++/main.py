from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QClipboard

from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller

from translator.TRgoogle import TRgoogle


class KeyListener(QObject):
    SignalListener = pyqtSignal(int, str, bool)
    def __init__(self):
        super().__init__()
        self.listener = mouse.Listener(on_press=self.key_press)

    def start(self):
        self.listener.start()

    def key_press(self, x, y, key, press):
        self.SignalListener.emit(int(x), int(y), str(key), bool(press))


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("тест") 
        self.setWindowFlags(Qt.WindowStaysOnTopHint)#по верх других окн
        self.setWindowFlags(Qt.FramelessWindowHint)#без верхний часть
        
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setCentralWidget(self.label)
        
        self.keylistener = KeyListener()# на основе класса которы мы зделали
        self.keylistener.SignalListener.connect(self.key_press)#конект сигнала 
        self.keylistener.start()#старт слушателя

    
    
    def key_press(self,x,y,key,press):
        if key == mouse.Button.middle and press:
            clipboard = QApplication.clipboard()# Получаем доступ к буферу обмена
            text = clipboard.text()# Получаем текст из буфера обмена

            # копи энд преревод

            self.label.setText(txt)

            self.setGeometry(x,y,0,0)

            # короче надо зделать копирование тхт,
            # табличка с текстом
            # c переведным
            #прорабоать мех закрытия 
            # ну и все... ainWiMndow
            # а еще зделать обработчик нажатия 
        if key != mouse.Button.middle and pressed:
            pass

