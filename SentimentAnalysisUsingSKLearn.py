# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:40:24 2018

@author: Shiwanand Chaurasiya
"""

import pickle
import random
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

x = []
y = []

def loadFeature():
    with open("feature_set.pickle","rb") as f:
         feature_set = pickle.load(f)
    random.shuffle( feature_set )
    return feature_set

def createTrainTestData():
    feature_set = loadFeature()
    for feature in feature_set:
        x.append(feature[0])
        y.append(feature[1])


def trainTestModels():
    loadFeature()
    createTrainTestData()
    train_x = x[:1500] 
    train_y = y[:1500] 
    test_x = x[1500:] 
    test_y = y[1500:]
    LR = LogisticRegression()
    LR.fit(train_x,train_y)
    print ("Accuracy : ", LR.score(test_x,test_y))

    DT = DecisionTreeClassifier()
    DT.fit(train_x,train_y)
    print ("Accuracy : ", DT.score(test_x,test_y))

    s = svm.SVC()
    s.fit(train_x,train_y)
    print ("Accuracy :", s.score(test_x,test_y))

    RF = RandomForestClassifier()
    RF.fit(train_x,train_y)
    print ("Accuracy :", RF.score(test_x,test_y))

    NB = GaussianNB()
    NB.fit(train_x,train_y)
    print ("Accuracy :",NB.score(test_x,test_y) )

    with open("LogisticRegressionClassifier.pickle","wb") as f:
         pickle.dump( LR,f )
    
    with open("DecisionTreeClassifier.pickle", "wb") as f:
         pickle.dump( DT,f )

    with open("RandomForestClassifier.pickle", "wb") as f:
         pickle.dump( RF,f )
    
    with open("NaiveBayesClassiifer.pickle","wb") as f:
         pickle.dump( NB,f )

    with open("SVMclassifier.pickle","wb") as f:
         pickle.dump( s,f )

#trainTestModels()



