# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

def run_search_scraper(search_term, num_terms):

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


def get_conversations(tweets_df):
    """
    Returns conversations dataframe for a tweets dataframe
    """

    # get a list of unique conversation ids
    conversation_ids = tweets_df['conversation_id'].unique()

    tweet_dfs = []

    for tweet_id in conversation_ids:  #treating convo id as a tweet id (top level tweet)
        tweet_id = str(tweet_id)[:19]
        mode = sntwitter.TwitterTweetScraperMode
        snscraper_reply = sntwitter.TwitterTweetScraper(tweetId=tweet_id, mode=mode.RECURSE)
        try:
            replies = list(snscraper_reply.get_items())

            tweets_list1 = []
            for tweet in replies:
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

            tweet_dfs.append(tweets_df1)
        except Exception as e:
            print(e)


    final_tweet_df = pd.concat(tweet_dfs,
                               ignore_index=True).drop_duplicates(subset=["id"],
                                                                  ignore_index=True)
    return final_tweet_df




