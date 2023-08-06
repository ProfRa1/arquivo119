import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

words = []
classes=[]
word_tags_list=[]
ignore_word=['?', '!', ',', '.', 's']

train_data_file = open('intents.json').read()
intents=json.loads(train_data_file)

