import nltk ,re,pprint
from nltk import word_tokenize
from urllib import request
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
html[:60]
from bs4 import BeautifulSoup
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
tokens
tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')

import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
llog['feed']['title']
len(llog.entries)
post = llog.entries[2]
post.title
content = post.content[0].value
content[:70]
raw = BeautifulSoup(content).get_text()
word_tokenize(raw)
import os
os.listdir('.')
f= open('New Text.txt')
raw = f.read()
path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw = open(path, 'rU').read()
s = input("Enter some text: ")
print("You typed", len(word_tokenize(s)),"words.")
query = 'Who knows?'
beatles = ['John','Paul','George','Ringo']
query[2]
beatles[2]
query + "I don't"
beatles + 'Brian'
beatles + ['Brian']
beatles[0] = "John Lennon"
del beatles[-1]
beatles
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line)

f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
ord('n')
nacute = '\u0144'
nacute
nacute.encode('utf8')

import unicodedata
lines = open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
for c in line:
    if ord(c)>127:
        print('{} U+{:04x} {}'.format(c.('utf8'),ord(c),unicodedata.name(c)))

