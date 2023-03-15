# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

def run_scraper(search_term, num_terms):

    # Creating list to append tweet data
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_term).get_items()): #declare a username
        if i>num_terms: #number of tweets you want to scrape
            break

        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned

    # Creating a dataframe from the tweets list above
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    return tweets_df1
