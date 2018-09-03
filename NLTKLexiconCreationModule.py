# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:37:32 2018

@author: Shiwanand Chaurasiya
"""

import pickle
from nltk.corpus import movie_reviews
from nltk.stem import WordNetLemmatizer
from collections import Counter 

lemmatizer = WordNetLemmatizer()

def createLexicon():
    all_words = []
    for word in movie_reviews.words():
        w = word.lower()
        all_words.append(w) 

    all_words = [ lemmatizer.lemmatize(word) for word in all_words ]

    all_words = Counter(all_words)
    lexicon = []

    for word in all_words.keys():
        if all_words[word] > 50 and all_words[word] < 5000 and len(word) > 3:
           lexicon.append( word )

    with open("lexicon.pickle","wb") as f:
         pickle.dump( lexicon,f )

#createLexicon()