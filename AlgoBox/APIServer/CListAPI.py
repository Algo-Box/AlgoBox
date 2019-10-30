import requests, json, os
from datetime import date, datetime, timezone
from APIServer.config import *
from APIServer.models import contest

def getContestList(jsonValue = True):

	currentTime = str(datetime.now(timezone.utc).strftime("%Y-%m-%d"))
	API_UNAME = str(os.environ.get("CListUserName"))
	API_KEY = str(os.environ.get("CListAPIKey"))

	baseAddress = "https://clist.by/api/v1/contest/?format=json&username=" + API_UNAME + "&api_key=" + API_KEY + "&order_by=start"
	baseAddress += "&end__gte="
	baseAddress += currentTime

	contestList = {"objects":[]}
	sites = {
		0:"codeforces.com", 
		1:"topcoder.com", 
		2:"codechef.com", 
		3:"facebook.com/hackercup", 
		4:"codingcompetitions.withgoogle.com", 
		5:"codeforces.com/gyms", 
		6:"hackerearth.com", 
		7:"hackerrank.com", 
		8:"open.kattis.com", 
		9:"csacademy.com", 
		10:"leetcode.com", 
		11:"kaggle.com", 
		12:"atcoder.jp"
	}
	limits = {0:3, 1:3, 2:4, 3:2, 4:2, 5:2, 6:10, 7:3, 8:3, 9:2, 10:3, 11:4, 12:4}

	for siteNum in sites:
		address = baseAddress + "&resource__name=" + sites[siteNum] + "&limit=" + str(limits[siteNum])
		data = requests.get(address)
		contestList["objects"] += json.loads(data.content)["objects"]
	contestList = contestList["objects"]

	if jsonValue == False:
		return contestList
	jsonObject = json.dumps(contestList)
	return jsonObject

def saveModel():
	dictObj = getContestList(jsonValue=False)
	print (dictObj) 
	listOfContest = contest.objects.all()
	for obj in dictObj:
		if not listOfContest.filter(event=obj["event"]).exists():
			con = contest (
				event = obj["event"], 
				start = obj["start"], 
				end = obj["end"], 
				duration = obj["duration"], 
				href = obj["href"], 
				domain = obj["resource"]["name"]
			)
			con.save()
