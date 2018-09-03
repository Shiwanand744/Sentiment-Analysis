# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:44:03 2018

@author: Shiwanand Chaurasiya
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from NLTKLexiconCreationModule import createLexicon 
import FeatureSetCreationModule as FSCM
import SentimentAnalysisUsingSKLearn as SAUSK
import SentimentAnalysisModule as s

consumer_key="TiSxqstonIEoJu6MXtUvar3AC"
consumer_secret="2OpT5dzYs7h8QwVObYp8OURU6KKQEdc7xxZ1RXz0yQneJOBQRc"
access_token="755430588329365505-emrm2pItz60DYGUWP3xYtRyPsXhNdEp"
access_token_secret="jPPCDr9Squuipe7W0vP6l4yIR340nw19oKcR87iimk6bv"

#uncomment for creating Lexicon and training to models
#createLexicon()
#FSCM.createFeatureSet()
#SAUSK.trainTestModels()
s.loadPickles()
classifier = s.classifier( s.LR,s.DT,s.RF,s.NB,s.SV )

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        print(tweet)
        features = s.create_features( tweet )
        print ( classifier.predict(features) )

        

    def on_error(self, status):
        print("Error")
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["PMO"])