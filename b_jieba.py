import jieba

with open('cleaned.data', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', ' ')

words = jieba.cut(text, cut_all=False)

l = list()
for i in words:
    l.append(i)

s = ' '.join(l)

# open('words.data', 'w', encoding='utf-8').write(s)
open('wordset.data', 'w', encoding='utf-8').write(' '.join(sorted(set(l))))
