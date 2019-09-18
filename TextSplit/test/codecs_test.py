import codecs

# text = codecs.open('./data/02.txt', 'r', 'utf-8', 'ignore').read()
text = codecs.open('../../Data/围城.txt', 'r', 'GBK', 'ignore').read()

print(text)
print(type(text))
