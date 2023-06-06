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
    def read_file(self):
        text = open(self.text, 'r', encoding=self.encoding)
        print(text.read())

test = Text_analyser('text.txt', 'UTF-8')
test.read_file()
