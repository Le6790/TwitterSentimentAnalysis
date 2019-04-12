import sys
import os
import csv
from nltk import word_tokenize 
#import the graph that I forgot the name of
import textblob 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#updating the lexicon
newSentiment = {"madness": 0}

vader = SentimentIntensityAnalyzer()
vader.lexicon.update(newSentiment)




#Clean up the tweets




def main():
    #parameter 1: filename of csv to analyze
    filename = sys.argv[1]

    with open(filename, "r", encoding="utf8") as csvIn:

        csvReader = csv.reader(csvIn) 
        

        csvData = {}
        for i in range(1,30):
            csvData["2019-03-{:02d}".format(i)] = []


        for row in csvReader:
            csvData[row[0][0:10]].append(row[3])
            

        print(len(csvData["2019-03-01"]))
        print(csvData["2019-03-01"])
            





if __name__ == "__main__":
    main()


