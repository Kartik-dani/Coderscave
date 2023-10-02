#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt
import seaborn as sea
import warnings
warnings.filterwarnings('ignore')


# In[3]:


define = pd.read_csv("globalterrorismdb_0718dist.csv",encoding='latin-1')
define.head()
define.tail()
define.info()
define.describe()


# In[4]:


date_cole = ['approxdate','resolution']
for col in date_cole:
    define[col] = pd.to_datetime(define[col], errors='coerce')
    
missing_data = define.isnull().sum()


# In[5]:


#Distribution of Terrorist Attacks across the countries
mplt.figure(figsize=(16,8))
sea.countplot(x='region_txt', data=define, order=define['region_txt'].value_counts().index)
mplt.title('Distribution of Terrorist Attacks across regions')
mplt.xlabel('Region')
mplt.ylabel('Nuber of Attacks')
mplt.xticks(rotation=45)
mplt.show()


# In[6]:


mplt.figure(figsize=(16,8))
top_countries = define['country_txt'].value_counts().nlargest(10)
sea.barplot(x = top_countries.index, y = top_countries.values)
mplt.title('Top 10 Countries that are targated')
mplt.xlabel('Country')
mplt.ylabel('Number of Attacks')
mplt.xticks(rotation=45)
mplt.show()


# In[7]:


# Overall trend of Terrorist Attacks over years
mplt.figure(figsize=(16,8))
define['year'] = define['iyear'] + define['imonth'] / 12 #Combining year and month for better representation
sea.lineplot(x = 'year', y = 'iyear', data=define)
mplt.title('Trend of Terrorist Attacks Over Years')
mplt.xlabel('Year')
mplt.ylabel('Number of Attacks')
mplt.show()


# In[8]:


# Some Common Attack Types
mplt.figure(figsize=(16,8))
sea.countplot(x = 'attacktype1_txt', data=define, order=define['attacktype1_txt'].value_counts().index)
mplt.title('Most Common Attack Types')
mplt.xlabel('Attack Type')
mplt.ylabel('Count')
mplt.xticks(rotation=45)
mplt.show()


# In[9]:


# Casualties and Human Loss Analysis
mplt.figure(figsize=(16,8))
sea.scatterplot(x = 'nkill',y = 'nwound',data=define, hue='attacktype1_txt',palette='viridis',size='nkill')
mplt.title('Casualties and Human Loss Analysis')
mplt.xlabel('Number of Killed')
mplt.ylabel('Number of Injured')
mplt.legend(title = 'Attack Type', bbox_to_anchor=(2,2))
mplt.show()


# In[10]:


# Analysis of Specific Terrorist Groups
mplt.figure(figsize=(16,8))
top_terrorist_groups = define['gname'].value_counts().nlargest(10)
sea.barplot(x = top_terrorist_groups.index, y = top_terrorist_groups.values, palette ='Set2')
mplt.title('Top 10 Most Active Terriost Groups')
mplt.xlabel('Terrorist Groups')
mplt.ylabel('Number of Attacks')
mplt.xticks(rotation=45)
mplt.show()


# In[ ]:


# Correlation Analysis
correlation_matrix = define.corr()

# Display Correlation Matrix as a Table
print("Correlation Matrix:") 
print(correlation matrix)


# In[13]:


# Statical Analysis
from scipy.stats import ttest_ind

successful_attacks = define[define['success']==1]['nkill']
unsuccessful_attacks = define[define['success']==0]['nkill']
t_statics , p_value = ttest_ind(successful_attacks.dropna(), unsuccessful_attacks.dropna(), equal_var=False)
print(f"T-Statics = {t_statics}, p-value = {p_value}")


# In[ ]:





# In[ ]:





# In[ ]:




