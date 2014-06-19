#!/usr/bin/env python2
#-*- coding: utf8 -*-

import codecs
import nltk 
from math import log
from nltk.probability import *
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords

punct = ['.', ',', '!', '?', '-', '.-', '...', '..']
punct = [w.decode('utf-8') for w in punct]

rank = 0

fd = codecs.open('doriangray.txt', 'r', encoding='utf-8')    
raw = fd.read()
raw = raw.lower()
fd.close()

tokens = WordPunctTokenizer().tokenize(raw)                            
freq_dict = nltk.FreqDist(tokens)  

for k,v in freq_dict.items():                                         # delete punctions
    if unicode(k) in punct:
        del freq_dict[k]
        freq_dict.update(k)    

zipf_result = codecs.open('zipf_result.csv', 'w', encoding='cp1251')
for k,v in freq_dict.items():
    rank += 1
    zipf_result.write(unicode(k) + u';' + unicode(v) + u';' + unicode(rank) + u';' + unicode(log(v)) + u';' + unicode(log(rank)) + u'\n')      
zipf_result.close()
