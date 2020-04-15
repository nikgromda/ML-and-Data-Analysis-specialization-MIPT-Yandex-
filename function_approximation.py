#!/usr/bin/env python
# coding: utf-8

# In[141]:


import numpy as np
import scipy
from scipy import sin,exp
from scipy import linalg
import matplotlib.pyplot as plt


# In[142]:


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


# In[143]:


# w0 + w1*x1 = f(x1)
# w0 + w1*x2 = f(x2)

a = np.array([[1,1],[1,15]])
b = np.array([f(1), f(15)])
w = linalg.solve(a,b)


# In[144]:


def f1(x):
    return w[0] + w[1]*x


# In[145]:


dx = 0.01
x_list = np.arange(1, 15, dx)
y_list = [f(x) for x in x_list]
y2_list = [f1(x) for x in x_list]

plt.plot(x_list, y_list)
plt.plot(x_list, y2_list)
plt.show()


# In[146]:


# w0 + w1*x1 + w2*x1^2 = f(x1)
# w0 + w1*x2 + w2*x2^2 = f(x2)
# w0 + w1*x3 + w2*x3^2 = f(x3)

a = np.array([[1, 1, 1], [1, 8, 8**2], [1, 15, 15**2]])
b = np.array([f(1), f(8), f(15)])
w = linalg.solve(a,b)


# In[147]:


def f2(x):
    return w[0] + w[1]*x + w[2]*x**2


# In[148]:


dx = 0.01
x_list = np.arange(1, 15, dx)
y_list = [f(x) for x in x_list]
y2_list = [f2(x) for x in x_list]

plt.plot(x_list, y_list)
plt.plot(x_list, y2_list)
plt.show()


# In[149]:


# w0 + w1*x1 + w2*x1^2 + w3*x1^3 = f(x1)
# w0 + w1*x2 + w2*x2^2 + w2*x2^3 = f(x2)
# w0 + w1*x3 + w2*x3^2 + w3*x3^3 = f(x3)
# w0 + w1*x4 + w2*x4^2 + w3*x4^3 = f(x4)

a = np.array([[1, 1, 1, 1], [1, 4, 4**2, 4**3], [1, 10, 10**2, 10**3], [1, 15, 15**2, 15**3]])
b = np.array([f(1), f(4), f(10), f(15)])
w = linalg.solve(a,b)


# In[150]:


def f3(x):
    return w[0] + w[1]*x + w[2]*x**2 + w[3]*x**3


# In[151]:


dx = 0.01
x_list = np.arange(1, 15, dx)
y_list = [f(x) for x in x_list]
y2_list = [f3(x) for x in x_list]

plt.plot(x_list, y_list)
plt.plot(x_list, y2_list)
plt.show()


# In[152]:


print(w)


# In[153]:


file = open('solution.txt', 'w')
for i in range(0, 4):
    file.write(str(w[i]) + " ")
file.close()


# In[ ]:




