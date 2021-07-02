#!/usr/bin/env python
# coding: utf-8

# In[106]:
from pyhive import hive
import pandas as pd
#import pyhs2 as hive
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import preprocessor as p
from textblob import TextBlob
import streamlit as st
# In[107]:
conn = hive.connect('seneca1.lehre.hwr-berlin.de', port=10000, username='nitish_acharya', database= 'default', password='BIPMinitial', auth='LDAP')

# In[108]:
df = pd.read_sql("SELECT * FROM movierater", conn)
df1 = df[['movierater.tweet', 'movierater.keyword_new']]
df1['prep']=[p.clean(doc) for doc in df1['movierater.tweet']]
polarity = lambda x: TextBlob(x).sentiment.polarity
df1['sentiment_tb'] = df1['prep'].apply(polarity)
df1['sentiment_tb_desc']=df1['sentiment_tb'].apply(lambda x: 'positive' if x > 0  else 'negative' if x < -0 else 'neutral')
polarity = lambda x: TextBlob(x).sentiment.polarity
df1['sentiment_tb'] = df1['prep'].apply(polarity)
df1['sentiment_tb_desc'].value_counts()
df1 = pd.concat([df1,pd.get_dummies(df1['sentiment_tb_desc'], prefix='rating')],axis=1)
df1 = df1.groupby('movierater.keyword_new')['rating_neutral','rating_positive','rating_negative'].sum()



# In[109]:
df2 = pd.read_csv(r'C:\Users\nitis\OneDrive\Dokumente\movie_sentiment\rotten_tomatoes.csv',sep=',')
result  = pd.merge(left=df1, right=df2, left_on='movierater.keyword_new', right_on='Series')
result['neutral_percentage']= result['rating_neutral']/(result['rating_neutral']+result['rating_positive'] + result['rating_negative'])*100
result['positive_percentage']= result['rating_positive']/(result['rating_neutral']+result['rating_positive'] + result['rating_negative'])*100
result['negative_percentage']= result['rating_negative']/(result['rating_neutral']+result['rating_positive'] + result['rating_negative'])*100



# In[110]:
st.text('SERIES NOW AND THEN')





# 

# In[111]:






# In[112]:





# In[113]:






# In[114]:






# In[115]:





# In[116]:





# In[117]:






# In[118]:






# In[121]:





# In[124]:





# In[135]:





# In[136]:





# In[ ]:




