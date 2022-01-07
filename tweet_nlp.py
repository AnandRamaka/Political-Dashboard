import tweepy as tw
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# import flair


def get_tweets(api, person, num):



    search_words = "#" + person
    date_since = "2021-12-01"

    tweets = tw.Cursor(api.search_tweets,
                q=search_words,
                lang="en"
                ).items(num)

    avg_polarity = 0
    tweets_text = []
    analyzer = SentimentIntensityAnalyzer()

    first = True 
    for tweet in tweets:
        if first:
            # print(tweet)
            first = False
        tweets_text.append(tweet.text)
        avg_polarity += analyzer.polarity_scores(tweet.text)['compound']
    

    avg_polarity = avg_polarity / len(tweets_text) if len(tweets_text) > 0 else avg_polarity

    return (tweets_text, avg_polarity)


def tweet_list(people):
    auth = tw.OAuthHandler("hrbuhyDqN8ZyJFV26z8tn8dA5", "BWRQoqIwCV3WnFpGNzGehQRxDwb4zpn80hE260rOtjFLXPYOox")
    # Create API object
    api = tw.API(auth)
    # Create a tweet
    # api.update_status("Hello Tweepy")

    try:
        redirect_url = auth.get_authorization_url()
        print(redirect_url)
    except tw.TweepError:
        print('Error! Failed to get request token.')
    
    data_list = []
    for p in people:
        data_list.append( get_tweets(api, p, 25) )

    return data_list
# Authenticate to Twitter


# text, pol = get_tweets("pypl", 10)




#s = flair.data.Sentence(tweet.text)
# output = flair_sentiment.predict(s)
# print(output)



