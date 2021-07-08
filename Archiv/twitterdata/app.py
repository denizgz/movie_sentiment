#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
#import pyhs2 as hive
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import preprocessor as p
from textblob import TextBlob
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import nltk
nltk.download('punkt')
# In[4]:


result = pd.read_csv('streamlitdata.csv')
df = pd.read_csv('wordcloud.csv')

# In[5]:


def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]


# In[6]:


st.header('Series Sentiment Analysis :Pre and post corona')
movie = list(result['Series'])
option = st.sidebar.selectbox('Select the series:', movie)
st.sidebar.write('You selected:', option)


# In[ ]:


st.subheader('Pre-Corona (Rotten Tomato)')
top_positive_rotten = result.sort_values(by="score",ascending=False).head(3)
fig = px.bar(top_positive_rotten, x='Series', y='score',color="score",title= 'Most  postively rated web-series (Top 3)')
fig.layout.yaxis.tickformat = ',.0%'


# In[ ]:


top_positive_rotten = result.sort_values(by="score",ascending=True).head(3)
fig1 = px.bar(top_positive_rotten, x='Series', y='score',color="score",title= 'Least positively rated web-series (Top 3)')
fig1.layout.yaxis.tickformat = ',.0%'


# In[ ]:


col1,col2 =st.beta_columns(2)
with col1:
    
    st.plotly_chart(fig,use_container_width=True)
with col2:
    st.plotly_chart(fig1,use_container_width=True)



# In[ ]:


filtered_data2 =  result[(result['Series'] == option)]
new = filtered_data2[['Series', 'neutral_percentage','positive_percentage','negative_percentage']]
st.header(option+ ' Web-series Rater')
new
fig2 = px.pie(new, values= new.mean(), title='Current ratings',names=['neutral_percentage', 'positive_percentage','negative_percentage'])
#st.plotly_chart(fig2)

#filtered_data2

# In[116]:
trace = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value =filtered_data2.iloc[0,5]*100 ,
    mode = "gauge+number+delta",
    title = {'text': "Rotten Tomato Positivity Rating (Percentage)"},
    delta = {'reference': new.iloc[0,2]},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

#st.plotly_chart(trace)

#st.plotly_chart(trace)
# In[118]:
col3,col4 =st.beta_columns(2)
with col3:
    
    st.plotly_chart(fig2,use_container_width=True)
with col4:
    st.plotly_chart(trace,use_container_width=True)
# In[113]:
positive_top = result.sort_values(by="positive_percentage",ascending=False).head(1)
positive_top_value = list(positive_top['positive_percentage'])
positive_top_name = list(positive_top['Series'])
if st.sidebar.header("Current top positively rated series"):
        st.sidebar.text(positive_top_name)
        st.sidebar.text(positive_top_value)

    
neutral_top = result.sort_values(by="neutral_percentage",ascending=False).head(1)
neutral_top_value = list(neutral_top['neutral_percentage'])
neutral_top_name = list(neutral_top['Series'])
if st.sidebar.header("Current top neutrally rated series"):
        st.sidebar.text(neutral_top_name)
        st.sidebar.text(neutral_top_value)


negative_top = result.sort_values(by="negative_percentage",ascending=False).head(1)
negative_top_value = list(negative_top['negative_percentage'])
negative_top_name = list(negative_top['Series'])
if st.sidebar.header("Current top negatively rated series"):
        st.sidebar.text(negative_top_name)
        st.sidebar.text(negative_top_value)



# In[121]:
st.header('MOST USED WORDS IN TWEETS')
word_cloud =df
word_cloud = word_cloud[['movierater.tweet', 'movierater.keyword_new']]
#word_cloud['word']=[p.clean(doc) for doc in word_cloud['movierater.tweet']]
word_cloud['adjectives'] = word_cloud['movierater.tweet'].apply(get_adjectives)
word_cloud['liststring'] = [','.join(map(str, l)) for l in word_cloud['adjectives']]

serie_text = word_cloud[(word_cloud['movierater.keyword_new'] == option)]
text3 = ' '.join(serie_text['liststring'])
wordcloud2 = WordCloud(background_color='white',width=600, height=400).generate(text3)
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()



