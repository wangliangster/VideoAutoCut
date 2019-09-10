import re
import os

PROJECTROOT = os.path.abspath(os.path.dirname(os.getcwd()))


def PreProcess(text):
    if text:
        text = re.sub('[\n]+', '', text)
    return text
