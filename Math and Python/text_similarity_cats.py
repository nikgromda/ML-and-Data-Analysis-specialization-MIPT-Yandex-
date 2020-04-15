#!/usr/bin/env python
# coding: utf-8

# In[132]:


import numpy as np
import scipy 
import re


# In[133]:


txt_open = open('sentences.txt')
data_txt = txt_open.readlines()
txt_open.close()


# In[134]:


print(data_txt)


# In[135]:


filtered_sentences = []

for item in data_txt:
    low_words = re.split('[^a-z]', item.lower())
    filtered_sentences.append(list(filter(None,  low_words)))

num_of_sentences = len(filtered_sentences)


# In[136]:


print(num_of_sentences)
print(filtered_sentences)


# In[137]:


words_dict = {}
i = 0

for sentence in filtered_sentences:
    for word in sentence:
        if word not in words_dict:
            words_dict[word] = i
            i += 1

num_of_words = len(words_dict)


# In[138]:


print(num_of_words)
print(words_dict)


# In[139]:


matrix = np.zeros((num_of_sentences, num_of_words))  
        
for index, sentence in enumerate(filtered_sentences):
    for word in sentence:
        matrix[index][words_dict[word]] = sentence.count(word)


# In[140]:


print(matrix.shape)
print(matrix)


# In[141]:


from scipy.spatial import distance

distances = []

for i in range(num_of_sentences): 
    distances.append(distance.cosine(matrix[0], matrix[i]))
    
dist_copy = distances.copy() 
dist_copy.remove(0)


# In[142]:


first_index = distances.index(min(dist_copy))
dist_copy.remove(dist_copy[first_index - 1])
second_index = distances.index(min(dist_copy))

print(first_index, second_index)
print(distances[first_index], distances[second_index])


# In[143]:


file = open('solution.txt', 'w')
file.write(str(first_index) + " ")
file.write(str(second_index))
file.close()


# In[158]:


dist = distances.copy()
dist.sort()
#index = distances.index(dist[???])  ??? - choose index more 2


# In[159]:


print(distances[index])
print(index)


# In[ ]:




