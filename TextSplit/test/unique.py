'''
accumulate file list content to one file, and unique them, see each line as one item unit


'''

import numpy as np
import sys

inputfilelist = ['/Users/liang/Documents/kkb/TextRank4ZH/textrank4zh/stopwords.txt',
                 '/Users/liang/PycharmProjects/VideoAutoCut/Data/stopWordList.txt']

outputfilename = '/Users/liang/PycharmProjects/VideoAutoCut/Data/stopwords.txt'
alloutputlist = []
alloutputset = set()

# print(len(alloutputlist), len(alloutputset))

for item in inputfilelist:
    with open(item, 'r') as f:
        alloutputlist += f.readlines()

# print(len(alloutputlist), len(alloutputset))

for item in alloutputlist:
    if item not in alloutputset:
        alloutputset.add(item)

# print(len(alloutputlist), len(alloutputset))

with open(outputfilename, 'w+') as f:
    for item in sorted(alloutputset):
        f.write(item)
