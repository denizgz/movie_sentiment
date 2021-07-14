# Big Data Project: Movies Sentiment Analysis

Sentiment analysis, which also means opinion mining or emotion AI, is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. 

This project aims to analyze and portray differences of sentiment between different shows such as ‘The Walking Dead’, ‘Money Heist’ and ‘Game of Thrones’. The team wants to use this project to investigate this unsupervised problem of having unstructured text data that holds useful information to derive sentiments across the social media platform.   

The team uses the Twitter API to extract the social media data containing the tweets that involve and refer to the set of shows that should be analyzed by using the shows titles as keyword. Since data can only be obtained from the last 7 days, it is not possible to gain a full overview of the users sentiments throughout a whole time and therefore displays more a snapshot of the last the weeks that can then be used for examining. The raw data for each keyword was obtained as .json file and was merged via python as a .csv file. Afterwards, the merged data should then be stored in the Hadoop distributed file system for further use.

Twitter is a microblogging website where people can share their feelings quickly and spontaneously by sending tweets limited by 140 characters. Tweets can be directly addressed to someone by adding the target sign “@” or participate to a topic by adding an hastag “#” to your tweet. Because of the usage of Twitter, it is a perfect source of data to determine the current overall opinion about anything.

Using multiple tools and techniques we can extract the subjective information of a dataset and try to classify it according to its polarity such as positive, neutral or negative. 

We used Pig and Hive in order to analyze and process the datasets. This requires to transform data with Pig for further usage and query the data with Hive to gain a first insight into the data set. Next, used pySpark to examine the data and apply natural language processing techniques to identify and label the data with the respective sentiments. 

Finally, used Docker to containerize everything.


# Content Description

Archiv : All the files that were used during the project which is not directly related to final output

Data: Data from hive table, rotton tomatoes and others

data_top10_series: Json files from the twitter data and raw csv twitter file

streamlit_app: The folder with all the requirements for streamlit app and the docker 

0_Twitter_API: The python file used to read twitter data through tweepy and export to raw csv file

1_hive: Pre processed in python so that its easy to read in hive

data_analysis: EDA of twitter data 

hive_job: command lines to create hive table

pig_job: pre processing command lines in pig

sentiment_eval : Evaluation of sentiment analysis

sentiment_analysis_streamlit: Final python file to save different dataframes for creating streamlit app

streamlit_app.tar: For deployment in caprover

vader_compound: Accuracy check of vader
