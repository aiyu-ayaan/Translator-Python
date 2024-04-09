# import libraries

from colorama import init
from translate import Translator

# initialize colorama
init()


class TranslatorEngine:
    def __init__(self, from_lang='en', to_lang='bn'):
        self.translator = Translator(from_lang=from_lang, to_lang=to_lang)

    def translate(self, from_lang='en', to_lang='hi', text=''):
        self.translator = Translator(from_lang=from_lang, to_lang=to_lang)
        return self.translator.translate(text)
