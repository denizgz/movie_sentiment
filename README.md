# Big Data Project: Movies Sentiment Analysis

Sentiment analysis, which also means opinion mining or emotion AI, is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. 

In the past year the Covid-19 pandemic affected people all around the world, forcing people to change their everyday life routines and habits in their working and private life. This problem also affected producers of films and shows since the filming of such films and shows became harder for the industry resulting in delayed premieres for new seasons.

This project aims at analyzing the impact of the Covid-19 pandemic on peoples perception and sentiments towards movies, comparing pre-corona and present, as it is expected that reviews and sentiments will significantly change along the Covid-19 pandemic timeline.

We used reviews from Rotten Tomatoes (before corona) and Twitter (last 7days).

Rotten Tomatoes is the world’s most trusted recommendation resources for quality entertainment, which is the leading online aggregator of movie and TV show reviews from critics, providing fans with a comprehensive guide to what’s Fresh – and what’s Rotten – in theaters and at home. 

Twitter is a microblogging website where people can share their feelings quickly and spontaneously by sending tweets limited by 140 characters. Tweets can be directly addressed to someone by adding the target sign “@” or participate to a topic by adding an hastag “#” to your tweet. Because of the usage of Twitter, it is a perfect source of data to determine the current overall opinion about anything.

Hence, we used the show ratings from rottentomatoes.com as sentiment from before the pandemic, and twitter API to extract the social media data containing tweets that refer to the set of movies to be analyzed, since the twitter data can only be obtained from the last 7 days. 

Using multiple tools and techniques we can extract the subjective information of a dataset and try to classify it according to its polarity such as positive, neutral or negative. 

We used Pig and Hive in order to analyze and process the datasets. This requires to transform data with Pig for further usage and query the data with Hive to gain a first insight into the data set. Next, used pySpark to examine the data and apply natural language processing techniques to identify and label the data with the respective sentiments. 

Used Tableau so that the comparison between the sentiments before and after the pandemic are more easily understandable and a Streamlit application created to function as a prototype for this project and show the final results. 

Finally, used Docker to containerize everything.
