import string
import numpy as np
from wordcloud import WordCloud
from c_pub import pub_names, stop_words
from c_priv import priv_names

with open('cleaned.data', 'r', encoding='utf-8') as file:
    text = file.read()

for name in pub_names:
    text = text.replace(name, ' ' + name + ' ')
for name in priv_names:
    text = text.replace(name, ' ' + name + ' ')
text = text.strip()
text = text.replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
text = text.replace(' \n', '\n').replace('\n ', '\n')

stop_words += priv_names
stop_words += list(string.ascii_lowercase)


def color_func(
    word,
    font_size, position, orientation,
    random_state=None,
    **kwargs
):
    if word in pub_names:
        return 'rgb(228, 119, 214)'
    if any([s in string.printable for s in word]):
        return np.random.choice([
            'rgb(128, 219, 214)',
            'rgb(128, 219, 114)',
            'rgb(228, 219, 114)'
        ])
    return 'rgb(128, 119, 214)'


wc = WordCloud(
    font_path='LXGWNeoXiHei.ttf',
    width=1024,
    height=1024,
    color_func=color_func,
    max_words=128,
    # max_words=256,
    stopwords=stop_words,
    random_state=3407,
    background_color='white',
    max_font_size=256,
    collocations=False
)
wc.generate(text)
print(wc.words_.keys())
wc.to_file('wordcloud.png')
