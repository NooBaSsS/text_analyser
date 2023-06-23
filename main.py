from typing import NoReturn
import re
import pymorphy3
all_pos = [
    'NOUN',
    'ADJF',
    'ADJS',
    'VERB',
    'ADVB',
    'NPRO',
    'NUMR',
    'PREP',
    'CONJ',
    'PRCL',
    'INTJ',
]


class TextAnalyser:
    def __init__(self, file_path=None, mode='r', encoding='UTF-8') -> None:
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.check_empty(file_path)
        self.prepare_text()
        self.make_analysed_words('')
        self.print_file()

    def open_file(self, file_path) -> None | NoReturn:
        try:
            with open(self.text, 'r', encoding=self.encoding) as text:
                self.text = text
                self.text = self.text.read()
        except FileNotFoundError:
            raise Exception(f'Файл "{file_path}" не найден')

    def prepare_text(self) -> None:
        self.text = self.text.lower()
        self.words = re.findall(r'\w+[\w-]*\w+', self.text)

    def check_empty(self, file_path) -> None | NoReturn:
        if not self.text:
            raise RuntimeError(f'Файл "{file_path}" пустой')

    def print_file(self) -> None:
        print(self.words)
        print(self.result)
        print(f'длина {len(self.words)} слов')

    def make_analysed_words(self, pos=['VERB']) -> None:
        if not self.words:
            raise Exception('Текста нет')
        if pos not in all_pos:
            raise Exception('Неправильная часть речи')
        self.result = []
        morph = pymorphy3.MorphAnalyzer()
        for word in self.words:
            parse = morph.parse(word)[0]
            if parse.tag.POS == pos:
                self.result.append(morph.parse(word)[0].normal_form)

        '''
        self.parsed_word = self.parse[0]
        self.part_of_speech = self.parsed_word.tag.POS
        print('Обозначение части речи:', self.part_of_speech)

        for word in self.words:
            self.parse = self.morph.parse(word)
            if word.parse[0].tag.POS == pos:
                print(word)
        '''


test = TextAnalyser(file_path='text.txt', encoding='UTF-8')
