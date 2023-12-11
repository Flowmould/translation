from googletrans import Translator#работает только 3.1.0a0

class TRgoogle():
    def translate(txt,language):
        try:
            translator = Translator()
            perevedeno = translator.translate(text=txt,dest=language)#language в заначении "ru"- русский

        except Exception as ex:
            perevedeno = ex

        return perevedeno.text

    def size(txt):
        txtArray = txt.splitlines()

        maxWidth = 0
        maxHeight = len(txtArray) * 2

        for widthSentence in txtArray:
            if len(widthSentence) >= maxWidth:
                maxWidth = len(widthSentence)
                
        return maxWidth,maxHeight

    def pereved(txt,language):# шуточный перевод, вместо "привет" мы получим "privet"
        try:
            translator = Translator()
            perevedeno = translator.translate(text=txt,dest=language)#language в заначении "ru"- русский

        except Exception as ex:
            perevedeno = ex

        return perevedeno.pronunciation

translator = Translator()
perevedeno = translator.translate(text="ихихихихиих привет",dest="ru")#language в заначении "ru"- русский
print(perevedeno.extra_data)