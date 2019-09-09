import numpy as np
import pandas as pd

import urllib.request
from bs4 import BeautifulSoup
import re


def ReadArticle(filepath=None, linkpath=None):
    text = ''
    if filepath:
        with open(str(filepath), 'r') as f:
            text = f.read()
    elif linkpath:
        page = urllib.request.urlopen(linkpath)
        html = BeautifulSoup(page.read(), 'html.parser')
        text = html.get_text()
        # only get chinese and numbers
        text = re.findall('[\u4E00-\u9FFF0-9]+', text)
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
    textpath = '/Users/liang/Documents/kkb/nlp-demo/text-summarization/train2.txt'
    linkpath = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B"nid"%3A"news_9458947891947278527"%7D&n_type=0&p_from=1'
    TextContent = ''

    # TextContent=ReadArticle(filepath=textpath)
    TextContent = ReadArticle(linkpath=linkpath)

    print(TextContent)

    print(type(TextContent))

    PreProcess()

    Cut2Parts()
    SplitSentence()

    ### other embending methold
    GetTFIDF()
    RankSentence()

    GetTopNSentence()
    ConventSent2Poem()

    GetSummaryOfEachPart()

    print('sucess')
