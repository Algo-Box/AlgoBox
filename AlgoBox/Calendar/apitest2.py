import requests, json, os
from datetime import date, datetime, timezone
from config import *
today = str(datetime.now(timezone.utc).strftime("%Y-%m-%d"))
API_UNAME = str(os.environ.get("username"))
API_KEY = str(os.environ.get("apikey"))
baseaddress = "https://clist.by/api/v1/contest/?format=json&username="+API_UNAME+"&api_key="+API_KEY+"&order_by=start"
baseaddress += "&end__gte="
baseaddress += today
baseaddress += "&resource__name__in=codeforces.com,"
dict = {"objects":[]}
sites = {0:"codeforces.com", 1:"topcoder.com", 7:"hackerrank.com", 3:" facebook.com/hackercup", 4:"codingcompetitions.withgoogle.com", 5:"codeforces.com/gyms", 6:"hackerearth.com", 2:"codechef.com", 8:"open.kattis.com", 9:"csacademy.com", 10:"leetcode.com", 11:"kaggle.com", 12:"atcoder.jp"}
for i in range(1, len(sites)) :
	baseaddress += ","
	baseaddress += sites[i]
baseaddress += "&order_by=start"
data = requests.get(baseaddress)
pymap = json.loads(data.content)
for i in range(len(pymap["objects"])) :
    dict["objects"].append(pymap["objects"][i])
jsonobject = json.dumps(dict)
print(jsonobject)
