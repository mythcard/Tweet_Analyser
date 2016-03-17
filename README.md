# Tweet_Analyser

Tweet Analyser is still in the developmentment phase:
Its currently a single page single user system
Its job is to extract tweets from user timeline and try classify tweets from future timeline

Currently we are in labelling phase where we are labeling tweets directly from the user.
The labelling are of 2 categories:
1. Very Important
2. Important
3. Ignore

We also have a small prediction engine which is already trying to predict tweet on one on one basis as to which category the tweet belongs to.

Current Development is to calculate the Precision and Recall for the first Prediction engine.

The platform used here are:
Data Extracion: R
Database: MongoDB
Programming and Algorithmic computations: Python and Scikit Learn
Web engine: Flask

Initial Files:
1. hello.py  : main program
2. class_update.py : Python files using Pymongo to fetch data from MongoDB
3. text_class.py : Python files using Pymongo to fetch data from MongoDB
4. tf_idf_vectorizer.py : Prediction engine
5. tweet_extract.R : Extraction engine
6. Page_screenshot: How the page looks like