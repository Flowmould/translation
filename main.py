from googletrans import Translator#работает только 3.1.0a0
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
import tkinter as tk
import pyperclip
import threading


translator = Translator()
keyb = keyboard.Controller()

global Stop
Stop = False


def pereved():

    #почему бы не зделать фильтрацию хотя бы для значений...
    #скоро будет, ждите... 

    keyb.press(keyboard.Key.ctrl)# нажатие кнтрл + с 
    keyb.press('c')    

    copyBufferTxt = pyperclip.paste()#создаем переменую для хранения последнего сохраненого текста в буфере

    keyb.release('c')# отжатие кнтрл + с 
    keyb.release(keyboard.Key.ctrl)
    
    try:
        perevedeno = translator.translate(text=copyBufferTxt,dest="ru")
        print(perevedeno)
    except Exception as ex:
        perevedeno = ex
    
    txtArray =  perevedeno.text

    maxWidth = 0
    maxHeight = len(txtArray) * 2


    for widthSentence in txtArray:
        if len(widthSentence) >= maxWidth:
            maxWidth = len(widthSentence)
    
    print(perevedeno.text,"длина-",maxWidth,"высота-",maxHeight)

    return perevedeno.text, maxWidth, maxHeight


def guiSet(x,y,txt, maxWidth, maxHeight):
    window = tk.Tk()# Создание окна

    window.attributes('-topmost', True)# Установка окна поверх других окон
    window.overrideredirect(True)# Установка окна без стандартной верхней части
    window.attributes('-alpha', 0.8)#прозрачности окна
    Label = tk.Label( #создаем  табличку с текстом,делаем ее только для чтения, делаем текст белым 
            window,
            text = txt,
            state = tk.DISABLED,
            width = maxWidth,
            height = maxHeight,
            bg = "black",
            fg = "white",
            anchor="nw"
        ) 
    Label.pack()#добавляем табличку в окно 
    window.update()

    window.geometry(f"+{x}+{y}")

    window.after(20, updateGui)
    window.mainloop()#создаем окно


def updateGui():
    if Stop == True:
            window.destroy()
            Stop = False

    else:
        window.after(10, updateGui)


def update(x, y, button,pressed):

    if button == mouse.Button.middle and pressed:#создание окна при нажатии на колесико мыши 
        txt = pereved()
        
        thread = threading.Thread(target=guiSet, args=(x, y, txt[1],txt[2],txt[3]))
        thread.start()



with mouse.Listener(on_click=update) as listener:#ну что же,использование лямбы для того чтобы GUIwork был 4 аргументом это гениально?))
    pyperclip.copy('')
    listener.join()
