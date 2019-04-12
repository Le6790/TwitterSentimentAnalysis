import GetOldTweets3 as got 
import csv
import sys




def retrieveData(query, getTop=False):
    name = query.replace(" ", "_")
    with open("{}.csv".format(name), 'a', encoding="utf8") as fOut:
        csvWriter = csv.writer(fOut, delimiter=",", lineterminator='\n', quotechar='"')
        
        for i in range(1,30):
            print("Currently on day: 2019-03-{:02d}".format(i))
            tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince("2019-03-{:02d}".format(i)).setUntil("2019-03-{:02d}".format(i+1)).setMaxTweets(500).setTopTweets(getTop)
            tweet = got.manager.TweetManager.getTweets(tweetCriteria)

            for twit in tweet:
                csvWriter.writerow([twit.date, twit.favorites, twit.retweets, twit.text])


def main():
    query = sys.argv[1]
    getTop = sys.argv[2]
    if getTop == "True":
        topBool = True 
    else:
        topBool = False
        
    retrieveData(query, topBool)

if __name__ == "__main__":
    main()