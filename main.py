#TODO разобрать строки на отдельные слова 

class TextAnalyser:
    def __init__(self, file_path=None, mode='r', encoding='UTF-8'):
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.print_file(file_path)

    def open_file(self, file_path):
        try:
            with open(self.text, 'r', encoding=self.encoding) as text:
                self.text = text
                self.text = self.text.read()
                self.text = self.text.lower()
        except FileNotFoundError:
            raise Exception(f'Файл "{file_path}" не найден')

    def print_file(self, file_path):
        if not self.text:
            raise Exception(f'Файл "{file_path}" пустой')
        else:
            print(self.text)
    
        

test = TextAnalyser(file_path='empty.txt', encoding='UTF-8')
