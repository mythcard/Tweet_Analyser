# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:46:34 2016

@author: mythcard
"""
import nltk
import string
import os
from text_class import *

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems
    
def return_pred_class_tfidf(lst3,token_dict):
    key1 = ''
    class1 = 'ignore'
    lst4 = lst3.tolist()
    lst5 = lst4[0]
    ### index retreival part
    max_score_index = lst5.index(max(lst5))
    print(max_score_index) 
    cnt = 0 
    ### iteratively proceed till the instances where the instance number in the dictonary
    ### equals index number retreived from tfidf cosine normalized matrix
    for key in token_dict.keys():
        if cnt == max_score_index:
            print(key)
            key1 = key
            print(get_class(key))
            class1 = get_class(key)
            break
        else:
            cnt = cnt + 1
    return key1, class1 
    
        
#this can take some time
#### get all manually classified tweets as training set for unclassified tfidf classification
def get_class_pred():
    key1 = ''
    class1 = 'ignore'        
    token_dict = next_tweet_for_update()        
        
    tfidf_vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs_matrix = tfidf_vectorizer.fit_transform(token_dict.values())
#arr = cosine_similarity(tfs_matrix[0:1], tfs_matrix)
#lst2= arr.tolist()
 
    tweet_text, object_id = next_tweet_for_update_unclassified()
    response = tfidf_vectorizer.transform([tweet_text])
    lst3 = cosine_similarity(response, tfs_matrix)

    key1, class1 = return_pred_class_tfidf(lst3,token_dict)
    return class1

        