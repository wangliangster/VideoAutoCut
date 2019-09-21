import re

import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from Utils import utils


def split_sentence(text, punc='！？。!?.'):
    specialnext = '》《'
    sent = []
    in_pos = 0
    chr_pos = 0
    for char in text:
        chr_pos += 1
        if char in punc:
            next_char = list(text[in_pos:chr_pos + 1]).pop()
            if next_char not in punc and next_char not in specialnext:
                sent.append(text[in_pos:chr_pos])
                in_pos = chr_pos
    if in_pos < len(text):
        sent.append(text[in_pos:])
    sent_with_index = {i: snt for i, snt in enumerate(sent)}
    return sent, sent_with_index


def get_tfidf_matrix(sents, stop_word):
    corpus = []
    for sent in sents:
        sent_cut = jieba.cut(sent)
        sent_list = [word for word in sent_cut if word not in stop_word]
        sent_str = ''.join(sent_list)
        corpus.append(sent_str)
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    tfidf_matrix = tfidf.toarray()
    return np.array(tfidf_matrix)


def similarity(sent1, sent2):
    return np.sum(sent1 * sent2) / 1e-6 + (np.sqrt(np.sum(sent1 * sent1)) * np.sqrt(np.sum(sent2 * sent2)))


def get_sent_with_words_weight(tfidfmat):
    sent_with_words_weight = {}
    sent_num = len(tfidfmat)
    for i in range(sent_num):
        sent_with_words_weight[i] = np.sum(tfidfmat[i])
    max_w, min_w = max(sent_with_words_weight), min(sent_with_words_weight)
    for key in sent_with_words_weight.keys():
        x = sent_with_words_weight[key]
        sent_with_words_weight[key] = (x - min_w) / (max_w - min_w)
    return sent_with_words_weight


def get_sent_with_pos_weight(sentences):
    sent_with_pos_weight = {}
    total_sent = len(sentences)
    for i in range(total_sent):
        sent_with_pos_weight[i] = (total_sent - i) / total_sent
    return sent_with_pos_weight


def get_sent_similarity_weight(tfidfmat):
    sent_similarity_score = {}
    for i in range(len(tfidfmat)):
        score_i = 0.0
        for j in range(len(tfidfmat)):
            score_i += similarity(tfidfmat[i], tfidfmat[j])
        sent_similarity_score[i] = score_i

    max_s, min_s = max(sent_similarity_score), min(sent_similarity_score)
    for key in sent_similarity_score.keys():
        x = sent_similarity_score[key]
        sent_similarity_score[key] = (x - min_s) / (max_s - min_s)

    return sent_similarity_score


def ranking_sent_base_on_weight(sent_base_word_w,
                                sent_base_pos_w,
                                sent_base_sim_w,
                                feature_w=[1, 1, 1],
                                ):
    sents_weight = {}
    for sent in sent_base_sim_w.keys():
        sents_weight[sent] = feature_w[0] * sent_base_word_w[sent] + \
                             feature_w[1] * sent_base_pos_w[sent] + \
                             feature_w[2] * sent_base_sim_w[sent]

    sort_sents_weight = sorted(sents_weight.items(), key=lambda d: d[1], reverse=True)
    return sort_sents_weight


def get_summer(sent_with_index, sorted_sent_weight, topKRate):
    topK = int(len(sorted_sent_weight) * topKRate)
    topIndex = sorted([sent[0] for sent in sorted_sent_weight[:topK]])

    summer = []
    for index in topIndex:
        summer.append((sent_with_index[index]))

    return summer


if __name__ == '__main__':
    # test_text = '/Users/liang/PycharmProjects/VideoAutoCut/Data/train2.txt'
    # test_text = utils.PROJECTROOT + "/Data/train2.txt"
    # test_text = utils.PROJECTROOT + "/Data/training17.txt"
    # test_text = "../Data/training17.txt"
    test_text = "../Data/wav2text.txt"
    stopWords_file = utils.PROJECTROOT + '/Data/stopWordList.txt'

    linkpath = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B"nid"%3A"news_9458947891947278527"%7D&n_type=0&p_from=1'
    linkpath2 = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B"nid"%3A"news_9106912512394455832"%7D&n_type=0&p_from=1'
    linkpath3 = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_8970543984864835078%22%7D&n_type=0&p_from=1'
    linknovel = 'http://mm.hengyan.com/article/1036192.aspx'

    # with open(test_text, 'r') as f:
    #    text = f.read()

    # text = utils.ReadArticle(linkpath=linkpath2)
    text = utils.ReadArticle(filepath='../Data/围城.txt', encoding='GBK')

    text = utils.PreProcess(''.join(text))

    sep = re.findall('第.章', text)
    textlist = utils.Cut2Parts(text, sep)
    # print(len(textlist))

    for part in textlist:
        index = textlist.index(part)
        textlist[index] = utils.AvergeCut(part, 5000)

    ### flatten list
    textlist = utils.flat(textlist)
    # print(len(textlist))

    text = textlist[8]

    stopWords = []
    with open(stopWords_file, 'r') as f:
        for line in f.readlines():
            stopWords.append(line.strip())

    sent_set, sent_with_index = split_sentence(text, punc='!?。！？')
    TFIDF = get_tfidf_matrix(sent_set, stopWords)
    sent_with_words_weight = get_sent_with_words_weight(TFIDF)
    sent_with_pos_weight = get_sent_with_pos_weight(sent_set)
    sent_score = get_sent_similarity_weight(TFIDF)
    sort_sent_weight = ranking_sent_base_on_weight(sent_base_word_w=sent_with_words_weight,
                                                   sent_base_pos_w=sent_with_pos_weight
                                                   , sent_base_sim_w=sent_score, feature_w=[1, 1, 1])

    summer = get_summer(sent_with_index, sort_sent_weight, topKRate=0.1)

    # print summary
    for sent in summer:
        print(sent)
