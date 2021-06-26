logs = LOAD '/user/hive/warehouse/topserie/to_hive_aftercorona.csv' USING PigStorage(',') AS (index:int,user_id:chararray, tweet:chararray,retweets:chararray,location:chararray,created:chararray,followes:chararray,keyword:chararray,language:chararray); 



--only take the unique values
 remove_duplicates = DISTINCT logs;

--put the text column into lowecase
replace_data = FOREACH logs GENERATE (index,user_id,tweet,retweets,location,created,followes,keyword,language),LOWER(tweet); 

--remove # from the keyword column
replace_data1 = FOREACH replace_data  GENERATE (index,user_id,tweet,retweets,location,created,followes,keyword,language),REPLACE(keyword,'#',','); 

-- store it in the hive table
dump replace_data1
STORE replace_data1 INTO '/user/nitish_acharya/pig_update4/' USING PigStorage (',');