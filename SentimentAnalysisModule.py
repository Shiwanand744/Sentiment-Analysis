# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:29:15 2018

@author: Shiwanand Chaurasiya
"""

import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from statistics import mode

with open("lexicon.pickle", "rb") as f:
    lexicon = pickle.load( f )

lemmatizer = WordNetLemmatizer()

def create_features( text ):
    features = np.zeros( len(lexicon) )
    for word in word_tokenize( text ):
        w = lemmatizer.lemmatize( word.lower() )
        if w in lexicon:
            index = lexicon.index(w)
            features[index] = 1
    features = list(features)
    return features

def loadPickles():
    global LR
    global DT
    global RF
    global  NB
    global SV
    with open("LogisticRegressionClassifier.pickle","rb") as f:
         LR = pickle.load( f )

    with open("DecisionTreeClassifier.pickle", "rb") as f:
         DT = pickle.load( f )
    
    with open("RandomForestClassifier.pickle", "rb") as f:
         RF = pickle.load( f )
    
    with open("NaiveBayesClassiifer.pickle", "rb") as f:
         NB = pickle.load( f )
    
    with open("SVMclassifier.pickle","rb") as f:
         SV = pickle.load( f )
    
class classifier( object ):
    def __init__(self,LR,DT,RF,NB,SV):
        self.LR = LR
        self.DT = DT
        self.RF = RF
        self.NB = NB
        self.SV = SV
        
    def predict(self,features):
        values = []
        values.append( self.LR.predict(features) )
        values.append( self.DT.predict(features) )
        values.append( self.RF.predict(features) )
        values.append( self.NB.predict(features) )
        values.append( self.SV.predict(features) )
        
        maximum_value = mode( values )
        if maximum_vlaue == 0:
            return "Negative"
        else:
            return "Positive"