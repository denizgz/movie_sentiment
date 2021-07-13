#!/usr/bin/env python
# coding: utf-8

# In[42]:


from pyhive import hive
import pandas as pd
#import pyhs2 as hive
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import preprocessor as p
from textblob import TextBlob
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[43]:

# connect to hiv
conn = hive.connect('seneca1.lehre.hwr-berlin.de', port=10000, username='nitish_acharya', database= 'default', password='BIPMinitial', auth='LDAP')


# In[45]:

# function for adjective
def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]

analyzer = SentimentIntensityAnalyzer()
# In[46]:

#import the data and use vader sentiment analysis
df = pd.read_sql("SELECT * FROM movierater", conn)
df1 = df[['movierater.tweet', 'movierater.keyword_new','movierater.retweets','movierater.location']]
df1['prep']=[p.clean(doc) for doc in df1['movierater.tweet']]
df1['movierater.location']=[p.clean(doc) for doc in df1['movierater.location']]
df1['sentiment_tb'] = df1['prep'].apply(analyzer.polarity_scores)
df1 = pd.concat([df1.drop(['sentiment_tb'], axis=1), df1['sentiment_tb'].apply(pd.Series)], axis=1)
df1


# In[47]:

df1['sentiment_tb_desc']=df1['compound'].apply(lambda x: 'positive' if x >= 0.05  else 'negative' if x < -0.05 else 'neutral')
df1


# In[48]:


df1.to_csv(r'C:/Users/nitis/OneDrive/Dokumente/movie_sentiment/streamlit_app/others.csv',index = True)


# In[49]:


df2 = pd.concat([df1,pd.get_dummies(df1['sentiment_tb_desc'], prefix='rating')],axis=1)
df2 = df2.groupby('movierater.keyword_new')['rating_neutral','rating_positive','rating_negative'].sum()
df2


# In[50]:


df2['neutral_percentage']= df2['rating_neutral']/(df2['rating_neutral']+df2['rating_positive'] + df2['rating_negative'])*100
df2['positive_percentage']= df2['rating_positive']/(df2['rating_neutral']+df2['rating_positive'] + df2['rating_negative'])*100
df2['negative_percentage']= df2['rating_negative']/(df2['rating_neutral']+df2['rating_positive'] + df2['rating_negative'])*100
df2


# In[51]:


df2.to_csv(r'C:/Users/nitis/OneDrive/Dokumente/movie_sentiment/streamlit_app/streamlitdata.csv',index = True)


# In[52]:


df1


# In[53]:


df1.to_csv(r'C:/Users/nitis/OneDrive/Dokumente/movie_sentiment/streamlit_app/wordcloud.csv',index = True)


# In[ ]:




