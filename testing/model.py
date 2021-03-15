#!/usr/bin/python3

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv('../Main Files/spam.csv')
messages = pd.DataFrame(df, columns=['rating', 'message'])

message_train = messages['message']
rating_train = messages['rating']

model = CountVectorizer()

transformed_message_train = model.fit_transform(message_train)

Multi = MultinomialNB()
Multi.fit(transformed_message_train, rating_train)

joblib.dump(Multi,'model.joblib')
joblib.dump(model,'vectorizer.pkl')
