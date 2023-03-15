# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

def run_scraper(search_term, num_terms):

    # Creating list to append tweet data
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_term).get_items()): #declare a username
        if i > num_terms: #number of tweets you want to scrape
            break

        timestamp = datetime.timestamp(tweet.date)

        tweets_list1.append([timestamp,
                             tweet.id,
                             tweet.rawContent,
                             tweet.user.username,
                             tweet.url,
                             tweet.replyCount,
                             tweet.retweetCount,
                             tweet.likeCount,
                             tweet.quoteCount,
                             tweet.conversationId,
                             tweet.lang,
                             tweet.inReplyToTweetId,
                             tweet.inReplyToUser,
                             tweet.mentionedUsers,
                             tweet.place,
                             tweet.hashtags]) #declare the attributes to be returned

    # Creating a dataframe from the tweets list above
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['timestamp',
                                                     'id',
                                                     'text',
                                                     'speaker',
                                                     'meta.url',
                                                     'meta.reply_count',
                                                     'meta.retweet_count',
                                                     'meta.like_count',
                                                     'meta.quote_count',
                                                     'conversation_id',
                                                     'meta.language',
                                                     'reply_to',
                                                     'meta.in_reply_to_speaker',
                                                     'meta.mentioned_speakers',
                                                     'meta.place',
                                                     'meta.hashtags'
                                                     ])

    return tweets_df1
