#TODO разобрать строки на отдельные слова 

class TextAnalyser:
    def __init__(self, file_path=None, mode='r', encoding='UTF-8'):
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.check_file(file_path)
        self.prepare_text()
        self.print_file()

    def open_file(self, file_path):
        try:
            with open(self.text, 'r', encoding=self.encoding) as text:
                self.text = text
                self.text = self.text.read()
        except FileNotFoundError:
            raise Exception(f'Файл "{file_path}" не найден')

    def check_file(self, file_path):
        if not self.text:
            raise Exception(f'Файл "{file_path}" пустой')

    def prepare_text(self):
        self.text = self.text.lower()

    def print_file(self):
        print(self.text)
    
        

test = TextAnalyser(file_path='text.txt', encoding='UTF-8')
