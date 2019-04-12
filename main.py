import sys
import os
import csv
import re
from nltk import word_tokenize 
#import the graph that I forgot the name of
import matplotlib
import textblob 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#updating the lexicon
newSentiment = {"madness": 0}

vader = SentimentIntensityAnalyzer()
#vader.lexicon.update(newSentiment)



def vaderSentimentAnalysis(csvData, filename):

    csvFile = "{}_vader.csv".format(filename)
    with open(csvFile, 'w') as fOut:
        csvWriter = csv.writer(fOut, delimiter=",", lineterminator='\n', quotechar='"')
        for i in (csvData):
            tweetList = csvData[i]
            totalSentVal = 0
            for tweet in tweetList:
                vader_dict = vader.polarity_scores(tweet)
                totalSentVal = totalSentVal + float(vader_dict['compound'])
            totalSentVal = (totalSentVal/len(tweetList))*10

            csvWriter.writerow([i,totalSentVal])



#Clean up the tweets
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 





def main():
    #parameter 1: filename of csv to analyze
    filename = sys.argv[1]

    with open(filename, "r", encoding="utf8") as csvIn:

        csvReader = csv.reader(csvIn) 
        

        csvData = {}
        for i in range(1,30):
            csvData["2019-03-{:02d}".format(i)] = []


        for row in csvReader:
            csvData[row[0][0:10]].append(clean_tweet(row[3]))
            

        # print(len(csvData["2019-03-01"]))
        print(csvData["2019-03-01"])

        print(vaderSentimentAnalysis(csvData, filename[:-4]))
            





if __name__ == "__main__":
    main()


