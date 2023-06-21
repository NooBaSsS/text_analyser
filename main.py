from typing import NoReturn
from string import punctuation
import re
punctuation += '—'


class TextAnalyser:
    def __init__(self, file_path=None, mode='r', encoding='UTF-8') -> None:
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.check_empty(file_path)
        self.prepare_text()
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
        for char in punctuation.replace('-', '-'):
            self.text = self.text.replace(char, '')
        self.words = re.findall(r'\w+', self.text)

    def check_empty(self, file_path) -> None | NoReturn:
        if not self.text:
            raise RuntimeError(f'Файл "{file_path}" пустой')

    def print_file(self) -> None:
        print(self.words)
        print(f'длина {len(self.words)} слов')


test = TextAnalyser(file_path='text.txt', encoding='UTF-8')
