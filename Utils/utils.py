import os
import re
import urllib.request

from bs4 import BeautifulSoup

PROJECTROOT = os.path.abspath(os.path.dirname(os.getcwd()))


def ReadArticle(filepath=None, linkpath=None):
    text = ''
    if filepath:
        with open(str(filepath), 'r') as f:
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
        text = re.sub('[\n]+', '', text)
        text = re.sub('[\u3000]+', '', text)
        text = re.sub('百度首页.*反馈退出', ' ', text)
    return text
