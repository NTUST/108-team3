#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1=response.text
book1


# In[2]:


book1[:]


# In[3]:


book1[200:]


# In[4]:


book1[::-3]


# In[5]:


book1[:66]


# In[8]:


book1[0:2]


# In[9]:


book1[0:-1:66]


# In[10]:


book1[:-1:77]


# In[13]:


book1[45::66]


# In[ ]:




