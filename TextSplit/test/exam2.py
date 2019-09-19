from TextSplit.textrank4zh import TextRank4Keyword

# text = "这间酒店位于北京东三环，里面摆放很多雕塑，文艺气息十足。答谢宴于晚上8点开始。"
text = '在进行最优化的求解过程中：从隐藏层到输出的Softmax层的计算量很大，因为要计算所有词的Softmax概率，再去找概率最大的值。'
tr4ke = TextRank4Keyword()

tr4ke.analyze(text=text, lower=True, window=2)

print('sentences:')
for s in tr4ke.sentences:
    print(s)

print()
print('words_no_filter:')
for words in tr4ke.words_no_filter:
    print('/'.join(words))

print()
print('words_no_stop_words:')
for words in tr4ke.words_no_stop_words:
    print('/'.join(words))

print()
print('words_all_filters:')
for words in tr4ke.words_all_filters:
    print('/'.join(words))
