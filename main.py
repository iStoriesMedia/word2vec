from pymystem3 import Mystem
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import word2vec
import gensim
import pandas as pd
import re 

"""""
df = pd.read_csv('migrants_date_Karaulny.csv', sep=';')
df = df.dropna()

file = open('Karaulny.txt', 'w')

for text in df['message']:
    text = text.lower()

    res = re.findall('[а-яё]+', text)
    for i in res:
        file.write(i)
        file.write(' ')
    file.write('.')
file.close() 


file = open('Karaulny.txt')
text = file.read()
posts = text.split('.') 

m = Mystem()

with open('Karaulny_lemma.txt',"w") as output_file:
    for post in posts:    
        output_file.write("".join(m.lemmatize(post)))


word2vec.word2phrase('Karaulny_lemma.txt',
                     'Karaulny_lemma.txt-phrases', verbose=True)

word2vec.word2vec('Karaulny_lemma.txt-phrases', 
                  'Karaulny_lemma.txt.bin', verbose=True) 

"""""

model = gensim.models.KeyedVectors.load_word2vec_format('Karaulny_lemma.txt.bin', binary=True)

file = open('Karaulny_migrant.txt', 'w')
                                                        
for i in model.most_similar(positive=['мигрант'], topn=200):

    file.write(str(i))
    file.write('\n')

file.close()


