#!/usr/bin/env python2
#-*- coding: utf8 -*-

import codecs
import nltk
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer


fd = codecs.open('doriangray.txt', 'r', encoding='utf-8')
raw = fd.read()
raw = raw.lower()
fd.close()

tokens = WordPunctTokenizer().tokenize(raw)                                      # tokenization

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(tokens)

finder.apply_freq_filter(4)                                                      # collocation frequency filter

ignored_words = nltk.corpus.stopwords.words('russian')
ignored_words = [w.decode('utf-8') for w in ignored_words]
finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)     # stopwords filter


pmi_collocations = finder.score_ngrams(bigram_measures.pmi)[:100]                # calculating collocation measures
likelihood_colloc = finder.score_ngrams(bigram_measures.likelihood_ratio)[:100]
chi_colloc = finder.score_ngrams(bigram_measures.chi_sq)[:100]
t_colloc = finder.score_ngrams(bigram_measures.student_t)[:100]


result_pmi = codecs.open('collocationsPMI.csv', 'w', encoding='cp1251')
for i in pmi_collocations:
    result_pmi.write(unicode(i[0][0]) + u';' + unicode(i[0][1]) + u';' + unicode(i[1]) + u'\n')
result_pmi.close()


result_log = codecs.open('collocationsLOG.csv', 'w', encoding = 'cp1251')
for i in likelihood_colloc:
    result_log.write(unicode(i[0][0]) + u';' + unicode(i[0][1]) + u';' + unicode(i[1]) + u'\n')
result_log.close()


result_chi = codecs.open('collocationsCHI.csv', 'w', encoding = 'cp1251')
for i in chi_colloc:
    result_chi.write(unicode(i[0][0]) + u';' + unicode(i[0][1]) + u';' + unicode(i[1]) + u'\n')
result_chi.close()


result_t = codecs.open('collocationsT.csv', 'w', encoding = 'cp1251')
for i in t_colloc:
    result_t.write(unicode(i[0][0]) + u';' + unicode(i[0][1]) + u';' + unicode(i[1]) + u'\n')
result_t.close()
