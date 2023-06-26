from typing import NoReturn
import re
import pymorphy3


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
        print(self.result)
        for i, result in enumerate(self.additional_results):
            if result:
                print(f'{i+1}-я часть речи: {result}')

    def make_analysed_words(self,
                            pos=['NOUN', None, None, None],
                            ) -> None:
        if not self.words:
            raise Exception('Текста нет')
        for p in pos:
            if p not in pos:
                raise Exception(f'Неправильная часть речи: {p}')
        morph = pymorphy3.MorphAnalyzer()

        self.result = []
        self.additional_results = [[] for _ in range(len(pos) - 1)]

        for word in self.words:
            parse = morph.parse(word)[0]
            if parse.tag.POS == pos[0]:
                self.result.append(morph.parse(word)[0].normal_form)
            else:
                for i, p in enumerate(pos[1:], start=1):
                    if parse.tag.POS == p:
                        self.additional_results[i-1].append(morph.parse(word)[0].normal_form)


test = TextAnalyser(file_path='text.txt',
                    encoding='UTF-8',
                    pos=['VERB', 'ADJF', 'NOUN', 'ADVB'],
                    )
