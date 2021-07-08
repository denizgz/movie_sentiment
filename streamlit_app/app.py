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
pd.set_option('display.max_columns', None)
from PIL import Image

# In[4]:

st.header('Yours Weekly: Series Sentiment Analysis')
result = pd.read_csv('streamlitdata.csv')
df = pd.read_csv('wordcloud.csv')
image = Image.open('movies.jpg')
image2 = Image.open('logo.jpg')
image3 = Image.open('happy.jpg')
image4 = Image.open('neutral.jpg')
image5 = Image.open('negative.jpg')
image6 = Image.open('twitter.jpg')

st.image(image, caption='Which series are you watching this week?')
st.sidebar.image(image2)

def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]
# In[6]:


movie = list(result['movierater.keyword_new'])
option = st.sidebar.selectbox('Select the series:', movie)
st.sidebar.write('You selected:', option)


# In[ ]:

st.subheader('Twitter Ratings')
st.image(image6,width=200)
top_positive_rotten = result.sort_values(by="positive_percentage",ascending=False).head(3)
fig = px.bar(top_positive_rotten, x='movierater.keyword_new', y='positive_percentage',color="positive_percentage",title= 'Most  postive Rating (Top 3)')
#fig.layout.yaxis.tickformat = ',.0%'


# In[ ]:


top_positive_rotten = result.sort_values(by="negative_percentage",ascending=False).head(3)
fig1 = px.bar(top_positive_rotten, x='movierater.keyword_new', y='negative_percentage',color="negative_percentage",title= 'Most Negative Rating (Top 3)')
#fig1.layout.yaxis.tickformat = ',.0%'


# In[ ]:


col1,col2 =st.beta_columns(2)
with col1:
    
    st.plotly_chart(fig,use_container_width=True)
    st.image(image3,width=100)
with col2:
    st.plotly_chart(fig1,use_container_width=True)
    st.image(image5,width=100,)







# In[ ]:


filtered_data2 =  result[(result['movierater.keyword_new'] == option)]
new = filtered_data2[['movierater.keyword_new', 'neutral_percentage','positive_percentage','negative_percentage']].reset_index(drop=True)
st.header(option+ ' Web-series Rater')
st.table(new)
fig2 = px.pie(new, values= new.mean(), title='Current ratings',names=['neutral_percentage', 'positive_percentage','negative_percentage'])
#st.plotly_chart(fig2)

#filtered_data2

# In[116]:
filtered_data6 =  result[(result['movierater.keyword_new'] == option)]
st.subheader('Count of tweets')
trace = px.bar(filtered_data6, y = 'movierater.keyword_new', x=['rating_negative','rating_positive','rating_neutral'],title= 'Distribution of tweets')
#fig.layout.yaxis.tickformat = ',.0%'


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
positive_top_name = list(positive_top['movierater.keyword_new'])
if st.sidebar.header("Current top positively rated series"):
        st.sidebar.image(image3,width=100)
        st.sidebar.text(positive_top_name)
        st.sidebar.text(positive_top_value)

    
neutral_top = result.sort_values(by="neutral_percentage",ascending=False).head(1)
neutral_top_value = list(neutral_top['neutral_percentage'])
neutral_top_name = list(neutral_top['movierater.keyword_new'])
if st.sidebar.header("Current top neutrally rated series"):
        st.sidebar.image(image4,width=100)
        st.sidebar.text(neutral_top_name)
        st.sidebar.text(neutral_top_value)


negative_top = result.sort_values(by="negative_percentage",ascending=False).head(1)
negative_top_value = list(negative_top['negative_percentage'])
negative_top_name = list(negative_top['movierater.keyword_new'])
if st.sidebar.header("Current top negatively rated series"):
        st.sidebar.image(image5,width=100)
        st.sidebar.text(negative_top_name)
        st.sidebar.text(negative_top_value)


st.header('Top 5 most retweeted tweets for ' + option)
top_tweet = df[(df['movierater.keyword_new'] == option)]
top_tweet=top_tweet.rename(columns={"prep": "Tweets"})
top_tweet = top_tweet.sort_values(by="movierater.retweets",ascending=False).head(5)
top_tweet = top_tweet['Tweets'].reset_index(drop=True)
st.table(top_tweet)




top_location = df[(df['movierater.keyword_new'] == option)]
top_location=top_location['movierater.location'].value_counts().head(3)
figlocation = px.bar(top_location, y = 'movierater.location', color="movierater.location",title= 'Top Location of tweets '+ option)



top_location2=df['movierater.location'].value_counts().head(3)
figlocation2 = px.bar(top_location2, y = 'movierater.location', color="movierater.location",title= 'Top Location of tweets Overall')


col5,col6 =st.beta_columns(2)
with col5:
    
    st.plotly_chart(figlocation2,use_container_width=True)
with col6:
    st.plotly_chart(figlocation,use_container_width=True)


st.header('Top 5 most retweeted tweets Overall')
top_tweet2=df.rename(columns={"prep": "Tweets"})
top_tweet2 = top_tweet2.sort_values(by="movierater.retweets",ascending=False).head(5)
top_tweet2 = top_tweet2['Tweets'].reset_index(drop=True)
st.table(top_tweet2)



# In[121]:
st.header('Most used words in ' + option + ' tweets')
word_cloud =df
word_cloud = word_cloud[['prep', 'movierater.keyword_new']]
#word_cloud['word']=[p.clean(doc) for doc in word_cloud['movierater.tweet']]
word_cloud['adjectives'] = word_cloud['prep'].apply(get_adjectives)
word_cloud['liststring'] = [','.join(map(str, l)) for l in word_cloud['adjectives']]

serie_text = word_cloud[(word_cloud['movierater.keyword_new'] == option)]
text3 = ' '.join(serie_text['liststring'])
wordcloud2 = WordCloud(background_color='black',width=600, height=400,max_words =30).generate(text3)
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.header('Most used words Overall')
serie_text1 = word_cloud
text4 = ' '.join(serie_text1['liststring'])
wordcloud3 = WordCloud(background_color='black',width=600, height=400,max_words =30).generate(text4)
plt.imshow(wordcloud3)
plt.axis("off")
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
