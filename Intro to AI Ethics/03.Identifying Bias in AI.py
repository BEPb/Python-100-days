# Identifying Bias in AI
# Set up feedback system
from learntools.core import binder
binder.bind(globals())
from learntools.ethics.ex3 import *

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# Get the same results each time
np.random.seed(0)

# Load the training data
data = pd.read_csv("../input/jigsaw-snapshot/data.csv")
comments = data["comment_text"]
target = (data["target"]>0.7).astype(int)

# Break into training and test sets
comments_train, comments_test, y_train, y_test = train_test_split(comments, target, test_size=0.30, stratify=target)

# Get vocabulary from training data
vectorizer = CountVectorizer()
vectorizer.fit(comments_train)

# Get word counts for training and test sets
X_train = vectorizer.transform(comments_train)
X_test = vectorizer.transform(comments_test)

# Preview the dataset
print("Data successfully loaded!\n")
print("Sample toxic comment:", comments_train.iloc[22])
print("Sample not-toxic comment:", comments_train.iloc[17])

from sklearn.linear_model import LogisticRegression

# Train a model and evaluate performance on test dataset
classifier = LogisticRegression(max_iter=2000)
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print("Accuracy:", score)

# Function to classify any string
def classify_string(string, investigate=False):
    prediction = classifier.predict(vectorizer.transform([string]))[0]
    if prediction == 0:
        print("NOT TOXIC:", string)
    else:
        print("TOXIC:", string)


# Comment to pass through the model
my_comment = "I love apples"

# Do not change the code below
classify_string(my_comment)

coefficients = pd.DataFrame({"word": sorted(list(vectorizer.vocabulary_.keys())), "coeff": classifier.coef_[0]})
coefficients.sort_values(by=['coeff']).tail(10)

# Set the value of new_comment
new_comment = "I have a christian friend"

# Do not change the code below
classify_string(new_comment)
coefficients[coefficients.word.isin(new_comment.split())]



