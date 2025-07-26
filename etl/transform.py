import pandas as pd
import logging

#taking df as a arg from main function of extract_data return df.
def transform_data(df):
    logging.info("Printing first five rows of data before transformation!..") 
    print(df.head(5))

    #converting the post_time from string datatype into date_time datatype.
    df['post_time'] = pd.to_datetime(df['post_time'],errors = 'coerce') #Handle errors like invalid/missing datetime strings (using errors='coerce' will convert those to NaT)

    #splitting post_time into post_date and post_timing.
    df['post_date'] = df['post_time'].dt.date
    df['post_timing'] = df['post_time'].dt.time

    #dropping the post_time col.
    df = df.drop('post_time',axis = 1)

    #dropping the sentiment col.
    df = df.drop('sentiment_score',axis = 1)

    #reordering the columns.
    df = df[['post_id', 'platform', 'post_type', 'post_date', 'post_day','post_timing',
             'likes', 'comments', 'shares']]

    #creating transformed csv file and removing indexs.
    df.to_csv('transformed.csv',index=False)

    logging.info("Tansformed data successfully!.")
    logging.info("Printing top 5 rows after the data transformation.")
    print(df.head(5))