import codecs

text = codecs.open('./data/02.txt', 'r', 'utf-8', 'ignore').read()

print(text)
print(type(text))
