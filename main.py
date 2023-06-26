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
    None,
]


class TextAnalyser:
    def __init__(self,
                 file_path=None,
                 mode='r',
                 encoding='UTF-8',
                 pos=['NOUN', None, None, None],
                 ) -> None:
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.check_empty(file_path)
        self.prepare_text()
        self.make_analysed_words(pos)  # до 4 частей речи
        self.print_results()

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

    def print_results(self) -> None:
        print(self.words)
        print(self.result)
        if self.result_1:
            print(self.result_1)
        if self.result_2:
            print(self.result_2)
        if self.result_3:
            print(self.result_3)
        print(f'длина {len(self.words)} слов')

    def make_analysed_words(self,
                            pos=['NOUN', None, None, None],
                            ) -> None:
        if not self.words:
            raise Exception('Текста нет')
        if pos[0] not in all_pos:
            raise Exception('Неправильная часть речи')
        if pos[1] not in all_pos:
            raise Exception('Неправильная часть речи')
        if pos[2] not in all_pos:
            raise Exception('Неправильная часть речи')
        if pos[3] not in all_pos:
            raise Exception('Неправильная часть речи')
        self.result = []
        self.result_1 = []
        self.result_2 = []
        self.result_3 = []
        morph = pymorphy3.MorphAnalyzer()

        for word in self.words:
            parse = morph.parse(word)[0]
            if parse.tag.POS == pos[0]:
                self.result.append(morph.parse(word)[0].normal_form)
            elif parse.tag.POS == pos[1]:
                self.result_1.append(morph.parse(word)[0].normal_form)
            elif parse.tag.POS == pos[2]:
                self.result_2.append(morph.parse(word)[0].normal_form)
            if parse.tag.POS == pos[3]:
                self.result_3.append(morph.parse(word)[0].normal_form)


test = TextAnalyser(file_path='text.txt',
                    encoding='UTF-8',
                    pos=['VERB', None, None, None],
                    )
