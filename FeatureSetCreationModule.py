import numpy as np
from nltk.corpus import movie_reviews
import pickle
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def createFeatureSet():
    with open("lexicon.pickle","rb") as f:
         lexicon = pickle.load( f )

    feature_set = []

    for fileid in movie_reviews.fileids("neg"):
        features = np.zeros( len(lexicon) )
        for word in list(movie_reviews.words(fileid)):
            w = lemmatizer.lemmatize( word.lower() )
            if w in lexicon:
               idx = lexicon.index( w )
               features[idx] = 1
        features = list( features )
        feature_set.append( (features,0) )

    for fileid in movie_reviews.fileids("pos"):
        features = np.zeros( len(lexicon) )
        for word in list( movie_reviews.words(fileid) ):
            w = lemmatizer.lemmatize( word.lower() )
            if w in lexicon:
               idx = lexicon.index( w )
               features[idx] = 1
        features = list( features )
        feature_set.append( (features,1) )

    with open("feature_set.pickle","wb") as f:
         pickle.dump( feature_set,f )

    with open("feature_set_deepLearning.pickle", "wb") as f:
         pickle.dump( feature_set,f )

#createFeatureSet()