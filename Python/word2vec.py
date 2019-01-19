# -*- coding: utf-8 -*-
"""Word2Vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZOJkCj3C2AlCgkk-2ALMny3ubkk6Y1q
"""

# Loading imports
import logging
import gensim
import pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def loadData():
  with open('C:\\Users\\Eduard\\Nextcloud\\DeeptechAI\\findingnouns\\taggedwords.pickle', 'rb') as f:
    data = pickle.load(f)
    return data
  
data = loadData()
print(data)
# create data for model
#file = ""
#dictonary = pickle.load(open(file))

document = []

for key,value in data.items():
 document.append(value)


logging.info ("Done reading data file")

model = gensim.models.Word2Vec (document, size=4, window=1, min_count=1, workers=2)
model.train(document,total_examples=len(document),epochs=10)

#save
save = {}

for key,value in data.items():
  v = []
  for k in value:
    v.append(model.wv.get_vector(k))
  flat_list = [item for sublist in v for item in sublist]
  tmp = {key : flat_list}
  save.update(tmp)

print(save)
pickle.dump(save, open("words2vec.pickle", "wb"))

"""# Test other models"""

# Load Google's pre-trained Word2Vec model.
google_model = "C:\\Users\\Eduard\\Downloads\\GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(google_model, binary=True)

#save
save = {}

for key,value in data.items():
  v = []
  for k in value:
    v.append(model.wv.get_vector(k))
  flat_list = [item for sublist in v for item in sublist]
  tmp = {key : flat_list}
  save.update(tmp)

print(save)
pickle.dump(save, open("words2vec_google.pickle", "wb"))  # save it into a file named save.p