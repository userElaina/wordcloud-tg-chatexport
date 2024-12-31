import re

s = open('./ChatExport_2024-12-31/messages.html', 'r', encoding='utf8').read()

pattern = re.compile(r'<div class="text">(.*?)</div>', re.S)
tag_pattern = r'<a href="" onclick="return ShowHashtag\(&quot;.*&quot;\)">'
tag_pattern = re.compile(tag_pattern)
link_pattern = re.compile(r'<a href[^>]*>[^<]*</a>', re.S)
html_pattern = re.compile(r'<[^>]*>')
quot_pattern = re.compile(r'&[^;]*;')

_spoiler = '<span class="spoiler hidden" onclick="ShowSpoiler(this)">'
_spoiler += '<span aria-hidden="true">'

_l = list()
check_html = list()
check_quot = list()

for i in pattern.findall(s):
    i: str
    i = i.replace('<br>', ' ')  # \n
    i = i.replace('<strong>', '').replace('</strong>', '')  # bold
    i = i.replace('<em>', '').replace('</em>', '')  # italic
    i = i.replace('<u>', '').replace('</u>', '')  # underline
    i = i.replace('<s>', '"').replace('</s>', '"')  # del
    i = i.replace('<blockquote>', '"').replace('</blockquote>', '"')  # quote
    i = i.replace('<pre>', '"').replace('</pre>', '"')  # ``
    i = i.replace('<code>', ' ').replace('</code>', ' ')  # code
    i = i.replace(_spoiler, '"').replace('</span></span>', '"')  # spoiler
    i = tag_pattern.sub(' ', i)
    i = link_pattern.sub(' ', i)
    i = i.replace('</a>', ' ')

    i = i.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    i = i.replace('&quot;', '"').replace('&apos;', "'")

    i = i.replace('，', ', ').replace('。', '. ').replace('、', ', ')
    i = i.replace('？', '? ').replace('！', '! ').replace('：', ': ')
    i = i.replace('；', '; ').replace('“', '"').replace('”', '"')
    i = i.replace('‘', "'").replace('’', "'").replace('…', '...')
    i = i.replace('（', '(').replace('）', ')')
    i = i.replace('【', '[').replace('】', ']')
    i = i.replace('《', '<').replace('》', '>')
    i = i.replace('—', '-').replace('～', '~')

    i = i.replace('\n', ' ').replace('\t', ' ')
    i = i.strip()

    i = i.replace('爱莉希雅', '爱莉').replace('爱莉', '爱莉希雅')
    i = i.replace('妖精爱莉希雅', '妖精爱莉')
    i = i.replace('格雷修', '格蕾修')
    i = i.replace('希尔', '希儿')
    i = i.replace('Jia Tan', 'JiaTan')

    i = i.replace('       ', ' ').replace('      ', ' ').replace('     ', ' ')
    i = i.replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
    if i:
        _l.append(i)
    check_html += html_pattern.findall(i)
    check_quot += quot_pattern.findall(i)

# assert len(check_html) == 0
# assert len(check_quot) == 0
print(check_html)
print(check_quot)

open('cleaned.data', 'w', encoding='utf8').write('\n'.join(_l))
