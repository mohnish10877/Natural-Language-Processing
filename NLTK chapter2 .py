import nltk
from nltk.corpus import gutenberg
gutenberg.fileids()
for fileid in gutenberg.fileids():  
     num_chars = len(gutenberg.raw(fileid))
     num_words = len(gutenberg.words(fileid))
     num_sents = len(gutenberg.sents(fileid))
     num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
     print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid )
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]
longest_len = max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s) == longest_len]

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65],'...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

from nltk.corpus import brown
brown.categories()
brown.words(categories='news') 
brown.words(fileids=['cg22'])
brown.sents(categories=['news','editorial','reviews',])

news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can','could','may','might','must','will']
for m in modals:
    print( m + ':',fdist[m], end =' ')

cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre))
genre = ['news','religion','hobbies','science_fiction','romance','humor']            
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions=genre, samples=modals)

from nltk.corpus import reuters
reuters.fileids()
reuters.categories('training/9865')
reuters.categories(['training/9865','training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley','corn'])

from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]
cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america','citizen']
           if(w.lower().startswith(target))

from nltk.corpus import inaugural
inaugural.fileids()
cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america', 'citizen']
           if w.lower().startswith(target))
cfd.plot()

text = ['The','Fulton','County','Grand','Jury','said',]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County')]

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in ['news','romance']
            for word in brown.words(categories=genre)