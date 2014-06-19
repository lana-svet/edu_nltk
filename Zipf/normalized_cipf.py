#!/usr/bin/env python2
#-*- coding: utf8 -*-

import codecs
import nltk 
import pymorphy2
from math import log
from nltk.probability import *
from nltk.tokenize import WordPunctTokenizer

rank = 0
normal_tokens = []
punct = ['.', ',', '!', '?', '-', '.-', '...', '..']
punct = [w.decode('utf-8') for w in punct]

fd = codecs.open('doriangray.txt', 'r', encoding='utf-8')
raw = fd.read()
raw = raw.lower()
fd.close()

tokens = WordPunctTokenizer().tokenize(raw)
morph_analyze = pymorphy2.MorphAnalyzer()

for token in tokens:
    norm_word = morph_analyze.parse(token)[0].normal_form
    normal_tokens.append(norm_word)

normal_freq = nltk.FreqDist(normal_tokens)

for k,v in normal_freq.items():                                         # delete punctions
    if unicode(k) in punct:
        del normal_freq[k]
        normal_freq.update(k)   

normal_zipf = codecs.open('normal_cipf.csv', 'w', encoding='cp1251')
for k,v in normal_freq.items():
    rank += 1
    normal_zipf.write(unicode(k) + u';' + unicode(v) + u';' + unicode(rank) + u';' + unicode(log(v)) + u';' + unicode(log(rank)) + u'\n')        
normal_zipf.close()
