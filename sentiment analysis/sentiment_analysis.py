import pandas as pd
import numpy as np
from textblob import TextBlob
from wordcloud import WordCloud
import spacy

nlp = spacy.load('en_core_web_sm')

# Function to preprocess data. It removes stopwords,punctuation and spaces and convert to spacy doc
def preprocess(text):
     doc = nlp(text)
     return ' '.join([token.lemma_.lower().strip() for token in doc if not token.is_stop and not token.is_punct and token.is_alpha])

# Function to convert preprocessed text to a SpaCy doc (which inherently contains a vector)
def get_nlp(text):
     return nlp(text)

# Function to analyse sentiment 
def analyse_sentiment_column(df) :

    # Function to determine polarity
    def analyze_polarity (token) :
       blob = TextBlob(str(token))
       polarity_found = blob.sentiment.polarity
       return polarity_found
    
    # Function to determine sentiment based on polarity
    def analyze_sentiment(polarity_found):
      if polarity_found > 0 :
          sentiment = 'positive'
      elif polarity_found < 0 :
          sentiment = 'negative'
      else :
         sentiment = 'neutral'
      return sentiment
    
    # df with 'polarity' column added
    pd.set_option('mode.chained_assignment',None)
    df['polarity'] = df['nlp_list'].apply(analyze_polarity)

    # df with 'sentiment' column added
    pd.set_option('mode.chained_assignment',None)
    df['sentiment'] = df['polarity'].apply(analyze_sentiment)
    return df
  
# read file from csv file and dataframe df created.
df = pd.read_csv('amazon_product_reviews.csv',delimiter = ',',low_memory =False)
print()
print('Sample of amazon_product_reviews.csv :')
print(df.head())
print()

'''
# sample of df is taken for faster processing and testing the program
df = df.sample(500, random_state=42)
print()
print('sampling done')
print()
'''

# shape of df is assessed
print()
print(f'Shape of dataframe is {df.shape}')
print()

# Nan values of each column is assessed
print()
print('Nan values in each column:')
print(df.isnull().sum() )
# only 1 row has null value in reviews.text
print()

# null values in reviews.text removed
df_without_null = df.dropna(subset = ['reviews.text'])

# required columns selected from df for data processing
df_without_null_required_columns = df_without_null[['name','reviews.text']]
print()
print('Dataframe with required columns for data analysis:')
print(df_without_null_required_columns.head())
print()

# stop words,punctuation etc removed
pd.set_option('mode.chained_assignment',None)
df_without_null_required_columns['processed_reviews'] = df_without_null_required_columns['reviews.text'].apply(preprocess)
print()
print('Dataframe after preprocessing of processed_reviews column :')
print(df_without_null_required_columns.head())
print()
pd.set_option('mode.chained_assignment',None)
df_without_null_required_columns['nlp_list'] = df_without_null_required_columns['processed_reviews'].apply(get_nlp)
print()

df_sample = df_without_null_required_columns.copy()

print('Dataframe when reviews.text processed column content converted to nlp tokens :')
print(df_without_null_required_columns.head())
print()

# sentiment analysis of reviews done
analyse_sentiment_column(df_without_null_required_columns)
print()
print('Sample of dataframe with polarity and sentiment columns added :')
print(df_without_null_required_columns.head())

# removed unwanted coulumns used for data analysis and printing final dataframe with sentiment
print()
print (' Result with sentiment analysis :')
df_without_null_required_columns = df_without_null_required_columns.drop(['processed_reviews','nlp_list','polarity'], axis =1)
print(df_without_null_required_columns.head())
print()


# Checking the sentiment analysis function output with sample reviews :

print('SAMPLES OF SENTIMENT ANALYSIS')
print('------------------------------')
print()
name_1 = df_sample['name'].iloc[101]
review_1 = df_sample['reviews.text'].iloc[101]
print(f'Product : {name_1}')
print(f'Review:  {review_1}')
df_3 = df_sample.iloc[101:102]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

name_2 = df_sample['name'].iloc[1000]
review_2 = df_sample['reviews.text'].iloc[1000]
print(f'Product : {name_2}')
print(f'Review:  {review_2}')
df_3 = df_sample.iloc[1000:1001]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

name_3 = df_sample['name'].iloc[1801]
review_3 = df_sample['reviews.text'].iloc[1801]
print(f'Product :{name_3} ')
print(f'Review:  {review_3}')
df_3 = df_sample.iloc[1801:1802]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

name_4 = df_sample['name'].iloc[1898]
review_4 = df_sample['reviews.text'].iloc[1898]
print(f'Product : {name_4}')
print(f'Review:  {review_4}')
df_3 = df_sample.iloc[1898:1899]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

name_5 = df_sample['name'].iloc[131]
review_5 = df_sample['reviews.text'].iloc[131]
print(f'Product : {name_5}')
print(f'Review:  {review_5}')
df_3 = df_sample.iloc[131:132]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

name_6 = df_sample['name'].iloc[399]
review_6 = df_sample['reviews.text'].iloc[399]
print(f'Product : {name_6}')
print(f'Review:  {review_6}')
df_3 = df_sample.iloc[399:400]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
print()

review_7 = df_sample['reviews.text'].iloc[10302]
print(f'Product : {df_sample['name'].iloc[10302]}')
print(f'Review:  {review_7}')
df_3 = df_sample.iloc[10302:10303]
print('Sentiment:')
analyse_sentiment_column(df_3)
print(df_3['sentiment'])
# Comparing similarities between reviews :

print('Similarity between reviews: ')
print('----------------------------')
nlp = spacy.load('en_core_web_md')

review_1 = df_sample['reviews.text'].iloc[1103]
review_2 = df_sample['reviews.text'].iloc[1104]
print(f'Review 1 {review_1}')
print(f'Review 2 {review_2}')
rev_1 = nlp(review_1)
rev_2 = nlp(review_2)
print(f'Similarity between review 1 and review 2 :  {rev_1.similarity(rev_2)}')
print()

review_1 = df_sample['reviews.text'].iloc[2500]
review_2 = df_sample['reviews.text'].iloc[2997]
print(f'Review 1 {review_1}')
print(f'Review 2 {review_2}')
rev_1 = nlp(review_1)
rev_2 = nlp(review_2)
print(f'Similarity between review 1 and review 2:  {rev_1.similarity(rev_2)}')
print()

review_1 = df_sample['reviews.text'].iloc[3100]
review_2 = df_sample['reviews.text'].iloc[3103]
print(f'Review 1 {review_1}')
print(f'Review 2 {review_2}')
rev_1 = nlp(review_1)
rev_2 = nlp(review_2)
print(f'Similarity between review 1 and review 2 :  {rev_1.similarity(rev_2)}')
print()

review_1 = df_sample['reviews.text'].iloc[1100]
review_2 = df_sample['reviews.text'].iloc[1496]
print(f'Review 1 {review_1}')
print(f'Review 2 {review_2}')
rev_1 = nlp(review_1)
rev_2 = nlp(review_2)
print(f'Similarity between review 1 and review 2 :  {rev_1.similarity(rev_2)}')
print()
