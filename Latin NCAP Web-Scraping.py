#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests --upgrade --quiet')
import requests


# In[3]:


NCAP_url = 'https://www.latinncap.com/en/results'


# In[4]:


response = requests.get('https://www.latinncap.com/en/results')


# In[5]:


response.status_code


# In[6]:


page_contents = response.text


# In[7]:


with open('webpage.html','w') as f:
    f.write(page_contents)


# In[8]:


get_ipython().system('pip install beautifulsoup4 --upgrade --quiet')


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


doc = BeautifulSoup(page_contents, 'html.parser')


# Data Format - 
# Brand, Model, Date,stars,Protection of Adult Occupant,Protection of Child Occupant,Protection of Pedestrian and vulnerable users, Safety Assit systems

# In[11]:


selection_class = "tit-marca"
brand_tags = doc.find_all('span',{'class': selection_class})


# In[12]:


len(brand_tags)


# In[13]:


brand_tags[:5]


# In[14]:


brand_titles = []

for tag in brand_tags:
    brand_titles.append(tag.text)
len(brand_titles)


# In[15]:


model_tags = doc.find_all('h3',class_ = False,id = False)


# In[16]:


len(model_tags)


# In[17]:


model_tags[:15]


# In[18]:


model_titles = []

for tag in model_tags:
    model_titles.append(tag.text)
len(model_titles)


# In[19]:


date_class = "colum colum-fecha"
date_tags = doc.find_all('div',{'class': date_class})


# In[20]:


date_tags[:5]


# In[21]:


date_titles = []

for tag in date_tags:
    date_titles.append(tag.text)
len(date_titles)


# In[22]:


char = '\n\t'
result = [ele.replace(char, '') for ele in date_titles]
result[0]


# In[23]:


char = '\t'
res = [ele.replace(char, '') for ele in result]
res[0]


# In[24]:


adult_class = "porcentaje adulto"
adult_tags = doc.find_all('div',{'class': adult_class})


# In[25]:


adult_tags[:5]


# In[26]:


adult_titles = []

for tag in adult_tags:
    adult_titles.append(tag.text)
len(adult_titles)


# In[27]:


child_class = "porcentaje nino"
child_tags = doc.find_all('div',{'class': child_class})


# In[28]:


child_tags[:5]


# In[29]:


child_titles = []

for tag in child_tags:
    child_titles.append(tag.text)
len(child_titles)


# In[30]:


pedestrian_class = "porcentaje usuarios"
pedestrian_tags = doc.find_all('div',{'class': pedestrian_class})


# In[31]:


pedestrian_tags[:5]


# In[32]:


pedestrian_titles = []

for tag in pedestrian_tags:
    pedestrian_titles.append(tag.text)
len(pedestrian_titles)


# In[33]:


safety_class = "porcentaje asistentes"
safety_tags = doc.find_all('div',{'class': safety_class})


# In[34]:


safety_tags[:5]


# In[35]:


safety_titles = []

for tag in safety_tags:
    safety_titles.append(tag.text)
len(safety_titles)


# In[36]:


get_ipython().system('pip install pandas --quiet')


# In[37]:


import pandas as pd


# In[38]:


ncap_dict = {
    
    'Model': model_titles[:14],
    'Date': res[:14],
    'Adult': adult_titles,
    'Child': child_titles,
    'Pedestrian':pedestrian_titles,
    'Safety': safety_titles}
    


# In[39]:


ncap_df = pd.DataFrame(ncap_dict)
ncap_df


# In[40]:


driver_class = "colum colum-240 adulto"
adult_occupant = doc.find_all('div',{'class': driver_class})


# In[41]:


len(adult_occupant)


# In[42]:


driversafety_titles = []

for tag in adult_occupant:
    driversafety_titles.append(tag.text)
len(driversafety_titles)


# In[43]:


char = '\n'
result1 = [ele.replace(char, '') for ele in driversafety_titles]
result1[0]


# In[44]:


back_class = "colum colum-240 nino"
child_occupant = doc.find_all('div',{'class': back_class})
child_occupant[0].text


# In[45]:


backsafety_titles = []

for tag in child_occupant:
    backsafety_titles.append(tag.text)
len(backsafety_titles)


# In[46]:


char = '\n'
result2 = [ele.replace(char, '') for ele in backsafety_titles]
result2[0]


# In[52]:


ncap1_dict = {
    'Model': model_titles[14:],
    'Adult Occupant': result1,
    'Child Occupant': result2,
    }


# In[53]:


ncap1_df = pd.DataFrame(ncap1_dict)
ncap1_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




