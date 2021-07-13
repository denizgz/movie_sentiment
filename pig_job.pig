logs = LOAD '/user/hive/warehouse/topserie/to_hive_aftercorona.csv' USING PigStorage(',') 
AS (index:int,user_id:chararray, tweet:chararray,retweets:chararray,location:chararray,created:chararray,followes:chararray,keyword:chararray,language:chararray); 

--only take the unique values
 remove_duplicates = DISTINCT logs;

--put the text column into lowercase
replace_data = FOREACH logs GENERATE (index,user_id,tweet,retweets,location,created,followes,keyword,language),LOWER(tweet);

--Returns a copy of a string with only trailing white space removed
replace_data = FOREACH logs GENERATE (index,user_id,tweet,retweets,location,created,followes,keyword,language),RTRIM(tweet); 

--replace # from the keyword column
replace_data1 = FOREACH replace_data  GENERATE (index,user_id,tweet,retweets,location,created,followes,keyword,language),REPLACE(keyword,'#',''); 

--replace special characters with regex
replace_data1 = FOREACH replace_data GENERATE REPLACE (tweet)(line,'([^a-zA-Z\\s]+)','');

--tokenize tweet column
replace_data2 = FOREACH logs GENERATE(index,user_id,tweet,retweets,location,created,followes,keyword,language),TOKENITE(tweet); 

-- store it in the hive table
dump replace_data1
STORE replace_data1 INTO '/user/nitish_acharya/pig_update4/' USING PigStorage (',');

