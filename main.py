'''
content = open('test.txt', 'r', encoding='UTF-8')
text = content.read()
print(text)
'''

#TODO разобрать строки на отдельные слова 

class Text_analyser:
    def __init__(self, file_path, encoding):
        self.text = file_path
        self.encoding = encoding
        self.open_file()
        self.read_file()
        self.print_file()
    def open_file(self):
        self.text = open(self.text, 'r', encoding=self.encoding)
    def read_file(self):
        self.text = self.text.read()
    def print_file(self):
        print(self.text)
        
        

test = Text_analyser('text.txt', 'UTF-8')
