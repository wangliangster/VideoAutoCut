import numpy as np
import pandas as pd

import urllib.request
from bs4 import BeautifulSoup
import re

from Utils import utils

import codecs


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


def PreProcess(text=None):
    pass


def Cut2Parts(num=None):
    pass


def SplitSentence(text=None, punctuation_list='！？。!?.'):
    pass


def GetTFIDF(sent_set=None, stop_word=None):
    pass


def RankSentence(sent_set=None):
    pass


def GetTopNSentence(TopNum=3):
    pass


def ConventSent2Poem(sent_list=None):
    pass


def GetSummaryOfEachPart():
    pass


if __name__ == '__main__':
    # textpath = '/Users/liang/Documents/kkb/nlp-demo/text-summarization/train2.txt'
    textpath = '../Data/train2.txt'
    linkpath = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B"nid"%3A"news_9458947891947278527"%7D&n_type=0&p_from=1'
    linkpath2 = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B"nid"%3A"news_9106912512394455832"%7D&n_type=0&p_from=1'
    linkpath3 = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_8970543984864835078%22%7D&n_type=0&p_from=1'
    linknovel = 'http://mm.hengyan.com/article/1036192.aspx'
    TextContent = ''

    # TextContent = ReadArticle(filepath=textpath)
    #TextContent = ReadArticle(linkpath=linkpath)
    # TextContent = ReadArticle(filepath='../Data/wav2text.txt')
    TextContent = ReadArticle(filepath='../Data/围城.txt', encoding='GBK')

    PreProcess()
    # use utils.PreProcess() temp
    TextContent = utils.PreProcess(''.join(TextContent))

    print(TextContent)

    #print(type(TextContent))

    Cut2Parts()

    SplitSentence()

    ### other embending methold
    GetTFIDF()
    RankSentence()

    GetTopNSentence()
    ConventSent2Poem()

    GetSummaryOfEachPart()

    print('sucess')
