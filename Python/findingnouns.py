# -*- coding: utf-8 -*-
"""FindingNouns.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_oh86QC7iF5DS_rIA-zeuur0qXQVPmg5

# Create Model
"""

import nltk
import random
from ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
import pickle

corp = nltk.corpus.ConllCorpusReader('.', 'tiger.conll09',
                                     ['ignore', 'words', 'ignore', 'ignore', 'pos'],
                                     encoding='utf-8')

tagged_sents = corp.tagged_sents()

# set a split size: use 90% for training, 10% for testing
split_perc = 0.1
split_size = int(len(tagged_sents) * split_perc)
train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

tagger = ClassifierBasedGermanTagger(train=train_sents)

accuracy = tagger.evaluate(test_sents)
print("ACCURACY: " + accuracy)

with open('nltk_german_classifier_data.pickle', 'wb') as f:
    pickle.dump(tagger, f, protocol=2)

"""# Load Model from File"""

import nltk
import random
import pickle
import time
from tqdm import tqdm
from joblib import Parallel, delayed
from nltk.tag import pos_tag
from random import shuffle

def loadData():
  with open('C:\\Users\\Adjek\\Nextcloud\\DeeptechAI\\websiteData\\websiteContent.pickle', 'rb') as f:
    data = pickle.load(f)
    return data
  
def tagData(text):
  result = dict()
  for i,j in zip(tqdm(range(len(text.keys()))),text.keys()):
    tagged_sent = pos_tag(text[j].split())

    propernouns = [word for word,pos in tagged_sent if ((pos == 'NNP') & (len(word) > 5) & (len(word) < 25))]
    
    propernouns = list(set(propernouns))
    
    filt = ['Webseite', 'Cookie']
    propernouns = [k for k in propernouns if k not in filt]
    
    shuffle(propernouns)
    
    result[j] = propernouns[0:5:1]
    
  return result

data = loadData()
taggedData = tagData(data)
print(type(data))
print(len(data))
print(len(taggedData))

print(taggedData["www.astrazeneca.de"])

with open('taggedwords.pickle', 'wb') as f:
    pickle.dump(taggedData, f, protocol=2)