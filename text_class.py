# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 00:46:54 2016

@author: mythcard
"""

import pymongo
import sys
from bson.objectid import ObjectId

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the student database

def get_class(id1):
    db=connection.test 
    tweet_det = db.tweet_det
#    print(id1)
    tweet_det_cur =  tweet_det.find({"_id":ObjectId(id1)},{"_id":1,"class":1})
    return tweet_det_cur[0]['class']

def next_tweet_for_update():
    print("Next record for update")
    db=connection.test
    tweet_det = db.tweet_det
    dict1 = {}
    try:
        
        # get the doc
        tweet_det_cur = tweet_det.find({"classified_status":"C"},{"_id" : 1,"text":1,"class":1})
        for cur in tweet_det_cur:
            dict1.update({cur["_id"]:cur["text"]})
#        print("before: ", tweet_det_cur[1]['_id'], tweet_det_cur[1]['text'])
#        print("before: ", tweet_det_cur[0]['_id'], tweet_det_cur[0]['text'])
        return dict1

    except Exception as e:
        raise
        
def next_tweet_for_update_unclassified():
    print("Next record for update")
    db=connection.test
    tweet_det = db.tweet_det

    try:
        # get the doc
        tweet_det_cur = tweet_det.find({"classified_status":"U"},{"_id" : 1,"text":1}).limit(1);
#        print("before: ", tweet_det_cur[1]['_id'], tweet_det_cur[1]['text'])
#        print("before: ", tweet_det_cur[0]['_id'], tweet_det_cur[0]['text'])
        return tweet_det_cur[0]['text'], tweet_det_cur[0]['_id']

    except Exception as e:
        raise        
        
#print(next_tweet_for_update())   

#print(next_tweet_for_update())       