from typing import NoReturn
import re
import pymorphy3
from collections import Counter
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt


class TextAnalyser:
    def __init__(self,
                 file_path=None,
                 mode='r',
                 encoding='UTF-8',
                 pos=['NOUN', None, None, None],
                 contour_color='black',
                 bgc='white',
                 contour_width=3,
                 max_words=500,
                 figsize=[10, 7]
                 ) -> None:
        if file_path is None:
            raise Exception('Файл не указан')
        self.text = file_path
        self.encoding = encoding
        self.open_file(file_path)
        self.check_empty(file_path)
        self.prepare_text()
        self.make_analysed_words(pos)
        self.make_wordcloud(contour_color=contour_color,
                            bgc=bgc,
                            contour_width=contour_width,
                            max_words=max_words,
                            figsize=figsize
                            )
        self.print_results()

    def open_file(self, file_path) -> None | NoReturn:
        try:
            with open(self.text, 'r', encoding=self.encoding) as text:
                self.text = text
                self.text = self.text.read()
        except FileNotFoundError:
            raise Exception(f'Файл "{file_path}" не найден')
        self.mask = np.array(Image.open('mask.jpg'))

    def prepare_text(self) -> None:
        self.text = self.text.lower()
        self.words = re.findall(r'\w+[\w-]*\w+', self.text)
        word_counts = Counter(self.words)
        self.sorted_words = sorted(
            word_counts.items(), key=lambda item: item[1], reverse=True
        )

    def check_empty(self, file_path) -> None | NoReturn:
        if not self.text:
            raise RuntimeError(f'Файл "{file_path}" пустой')

    def print_results(self) -> None:
        print(self.result)
        for i, result in enumerate(self.additional_results):
            if result:
                print(f'{i+1}-я часть речи: {result}')
        print(f'рейтинг из 10 слов: {self.sorted_words[:10]}')

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
                        self.additional_results[i-1].append(
                            morph.parse(word)[0].normal_form
                        )

    def make_wordcloud(self,
                       contour_color='black',
                       bgc='white',
                       contour_width=3,
                       max_words=500,
                       figsize=[10, 7],
                       ):
        wc = WordCloud(
            background_color=bgc,
            max_words=max_words,
            mask=self.mask,
            stopwords=set(STOPWORDS),
            contour_width=contour_width,
            contour_color=contour_color
        )
        wc.generate(' '.join(self.words))
        num_colors = len(wc.words_)
        rand_cmap = plt.cm.get_cmap('hsv', num_colors)

        def random_color_func(word=None,
                              font_size=None,
                              position=None,
                              orientation=None,
                              font_path=None,
                              random_state=None
                              ):
            return tuple(int(x * 255) for x in rand_cmap(
                np.random.randint(num_colors)
            ))

        plt.figure(figsize=figsize)
        plt.imshow(wc.recolor(color_func=random_color_func),
                   interpolation='bilinear')
        plt.axis('off')
        plt.savefig('wordcloud.png', format='PNG')
        plt.show()


test = TextAnalyser(file_path='text.txt',
                    encoding='UTF-8',
                    pos=['VERB', 'ADJF', 'NOUN', 'ADVB'],
                    contour_color='black',
                    bgc='white',
                    contour_width=3,
                    )
