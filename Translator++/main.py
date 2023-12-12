from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from pynput import mouse

from googletrans import Translator#работает только 3.1.0a0

class TRgoogle():
    def translate(self,txt):
        try:
            translator = Translator()
            perevedeno = translator.translate(text=txt,dest="ru")#language в заначении "ru"- русский

        except Exception as ex:
            perevedeno = ex
            
        print(perevedeno.text)
        
        return perevedeno.text


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.googl = TRgoogle()#костыленок т.к скоро будет выбор переводчика
        
        self.clipboard = QApplication.clipboard()  # Получаем доступ к буферу обмена
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)#настройка окна
        self.setWindowOpacity(0.5)#прозрачность
        
        self.label = QLabel(self)  # Создаем метку
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.listener = mouse.Listener(on_click=self.on_mouse_click)# запуск слушателя и указывание фунции которая будет вызвана при нажатии
        self.listener.start()

    def on_mouse_click(self, x, y, key, pressed):
        
        if key == mouse.Button.middle and pressed:
            self.label.setText(self.googl.translate(self.clipboard.text()))#переделать не забыть....
            self.label.adjustSize()
            
            self.setFixedSize(self.label.sizeHint())#окно размером с метку
            self.move(x, y)# Перемещаем окно на координаты курсора
            
            self.show()
            print("Действия при нажатии колеса кнопки мыши")
            
        elif not self.geometry().contains(x, y):
            self.hide()
            print("нажатие за пределом окна ")
        
    def closeEvent(self, event):
        self.listener.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

