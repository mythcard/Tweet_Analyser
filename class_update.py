# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:26:50 2016

@author: mythcard
"""

import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def next_tweet_for_update():
    print("Next record for update")
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cur = tweet_det.find({"classified_status":"U"},{"_id" : 1,"text":1}).limit(1);
#        print("before: ", tweet_det_cur[1]['_id'], tweet_det_cur[1]['text'])
#        print("before: ", tweet_det_cur[0]['_id'], tweet_det_cur[0]['text'])
        return tweet_det_cur[0]['text']

    except Exception as e:
        raise
        
def repo_total_count():
    print("Repo Total count proc started")
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cnt = tweet_det.find().count();
        return tweet_det_cnt

    except Exception as e:
        raise

def repo_total_count_classified():
    print("Repo Classified count proc started")
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cnt = tweet_det.find({"classified_status":"C"}).count();
        return tweet_det_cnt

    except Exception as e:
        raise   
        
def repo_total_count_not_classified():
    print("Repo Not Classified count proc started")
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cnt = tweet_det.find({"classified_status":"U"}).count();
        return tweet_det_cnt

    except Exception as e:
        raise        


# add a review date to a single record using update_one
def update_status_specific(value, class_pred):

    print("updating record using update_one and $set")
    # get a handle to the school database
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cur = tweet_det.find({"classified_status":"U"},{"_id" : 1,"text":1}).limit(1);
#        print("before: ", tweet_det_cur[1]['_id'], tweet_det_cur[1]['text'])
#        print("before: ", tweet_det_cur[0]['_id'], tweet_det_cur[0]['text'])

#        # update using set
#        record_id = score['_id']
        print("Checking class pred before execution: ",class_pred)
        for tweet_id in tweet_det_cur:
            print("Here1",tweet_id['_id'])
            result = tweet_det.update_one({'_id':tweet_id['_id']},{'$set':{'classified_status':'C' , 'class':value, 'class_idf_pred':class_pred}})
        print("num matched: ", result.matched_count)

    except Exception as e:
        raise

# add a review date to all records
def add_text_status():

    print("updating record using update_many and $set")
    # get a handle to the school database
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # update all the docs
        result = tweet_det.update_many({"classified_status": {"$exists":0}},{'$set':{'classified_status':'U'}})
        print("num matched: ", result.matched_count)

    except Exception as e:
        raise
        
# add a default idf status to all unclassifed records
def add_class_pred():

    print("updating record using update_many and $set")
    # get a handle to the school database
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # update all the docs
        result = tweet_det.update_many({"classified_status": 'U'},{'$set':{'class_idf_pred':'none'}})
        print("num matched: ", result.matched_count)

    except Exception as e:
        raise        

#add_text_status()

#add_class_pred()

#value = 'ignore'
#update_status_specific(value)

#next_tweet_for_update()

#print(repo_total_count())
#print(repo_total_count_classified())