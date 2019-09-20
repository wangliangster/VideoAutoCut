import codecs
import os
import re
import urllib.request

from bs4 import BeautifulSoup

PROJECTROOT = os.path.abspath(os.path.dirname(os.getcwd()))


def ReadArticle(filepath=None, encoding='utf-8', linkpath=None):
    text = ''
    if filepath:
        with codecs.open(str(filepath), 'r', encoding, 'ignore') as f:
            text = f.read()
    elif linkpath:
        page = urllib.request.urlopen(linkpath)
        html = BeautifulSoup(page.read(), 'html.parser')
        text = html.get_text()
        # only get chinese and numbers/chars of any less than 18 between two chinese character.
        text = re.findall('[“《\u4E00-\u9FFF]+.{0,18}[\u4E00-\u9FFF！？，。；：!?》]+', text)

    return text


def PreProcess(text):
    if text:
        text = re.sub('[\n\r]+', '', text)
        text = re.sub('[\u3000]+', '', text)
        text = re.sub('百度首页.*反馈退出', ' ', text)
    return text


# sep are list as ['第一章', '第二章', '第三章', '第四章', '第五章'], not only single as blank or ','
def Cut2Parts(text, sep=None):
    res = []
    for sp in sep:
        res.append(text.split(sp)[0])
        text = sp + '\n' + text.split(sp)[1]
    res.append(text)
    return res


def AvergeCut(text=None, limit=37915):
    if not limit:
        return text
    res = []
    start, end = 0, 0
    numparts = len(text) // limit
    for i in range(numparts):
        start = i * limit
        end = start + limit
        res.append(text[start:end])
    if end != len(text):
        res.append(text[end:])
    return res


#### list remove [] internal
####input: li = [[[[[[1],2],3],4],5]
####output:li =[1,2,3,4,5]
def flat(L):
    out = []
    for e in L:
        if isinstance(e, list):
            out += flat(e)
        else:
            out.append(e)
    return out


if __name__ == '__main__':
    pass
