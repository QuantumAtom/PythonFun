import requests
import os

api = os.getenv("AV_API_KEY") 
equityrequest = input("\nWhat equity do you want to research? ")

avnews = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=" + str(equityrequest) + "&apikey=" + str(api)
avnewsstr = str(avnews)
urlnews=avnewsstr

avequity = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + str(equityrequest) + "&apikey=" + str(api)
avequitystr = str(avequity)
urlequity = avequitystr


req = requests.get(urlequity)
rnws = requests.get(urlnews)

equitydata = req.json()
newsdata = rnws.json()

print(equitydata)
print(newsdata)


