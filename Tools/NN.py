import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
import nltk
import re

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.layers import Dense, Embedding,GlobalMaxPooling1D
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Embedding, Conv1D



def clean_data(review):
    review = re.sub('[^a-zA-Z]', ' ',review)
    review = review.lower()
    return review

sw = stopwords.words('english')
sw += ['food','place','good',"great"]

def remove_stop_words(review):
    review_minus_sw = []
    stop_words = sw
    review = review.split()
    review = [review_minus_sw.append(word) for word in review if word not in stop_words]
    review = ' '.join(review_minus_sw)
    return review



###################################################### 
def NN_cleaning(original_df):
    
    original_df['review'] = original_df['review'].apply(clean_data)
    original_df['review'] = original_df['review'].apply(remove_stop_words)
    corpus = list(original_df['review'])
    cv = CountVectorizer(max_features = 1000)
    X = cv.fit_transform(corpus).toarray()
    y = original_df['target'].values
    tf_transformer = TfidfTransformer()
    X = tf_transformer.fit_transform(X).toarray()
    tfidfVectorizer = TfidfVectorizer(max_features =1000)
    X = tfidfVectorizer.fit_transform(corpus).toarray()
    docs = original_df['review']
    labels = original_df['target']
    vocab_size = 5000

    docs = [one_hot(d, vocab_size,filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~',lower=True, split=' ') for d in docs]

    max_length = 100
    docs = pad_sequences(docs, maxlen=max_length, padding='post')
    return docs, labels


def text_to_fn(text):
    frame = pd.DataFrame([text], columns = ['review'])
    frame['target'] = 0
    return frame



def NN_cleaning_st(text):
    original_df = pd.DataFrame([text], columns = ['review'])
    original_df['review'] = original_df['review'].apply(clean_data)
    original_df['review'] = original_df['review'].apply(remove_stop_words)
    corpus = list(original_df)
    cv = CountVectorizer(max_features = 1000)
    X = cv.fit_transform(corpus).toarray()

    tf_transformer = TfidfTransformer()
    X = tf_transformer.fit_transform(X).toarray()
    tfidfVectorizer = TfidfVectorizer(max_features =1000)
    X = tfidfVectorizer.fit_transform(corpus).toarray()
    docs = original_df
    vocab_size = 5000
    docs = [one_hot(d, vocab_size,filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~',lower=True, split=' ') for d in docs]
    max_length = 100
    docs = pad_sequences(docs, maxlen=max_length, padding='post')
    return docs