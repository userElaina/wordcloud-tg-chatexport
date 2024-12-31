import jieba

with open('cleaned.data', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', ' ')

words = jieba.cut(text, cut_all=False)

_l = list()

for i in words:
    _l.append(i)

s = ' '.join(_l)

# open('words.data', 'w', encoding='utf-8').write(s)
open('wordset.data', 'w', encoding='utf-8').write(' '.join(sorted(set(_l))))
