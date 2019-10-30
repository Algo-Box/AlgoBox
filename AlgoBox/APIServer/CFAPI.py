import hashlib, random, time, functools, requests, os

from config import *
API_KEY = os.environ.get("CodeForcesAPIKey")
API_SECRET = os.environ.get("CodeForcesAPISecret")

def customCmp(A, B):
	if(A[0] == B[0]):
		if A[1] < B[1]:
			return -1
		return 1
	elif A[0] < B[0]:
		return -1
	return 1

def getHash(randNum, method, req):
	hashString = str(randNum) + "/" + method + "?"
	for params in req:
		hashString += str(params[0]) + "=" + str(params[1])
		hashString += "&"
	hashString = hashString[:-1]
	hashString += "#" + API_SECRET
	hashFunc = hashlib.sha512(hashString.encode())
	return hashFunc.hexdigest()

def getResponse(method, req):
	baseAddress = "http://www.codeforces.com/api/"
	currTime = round(time.time())
	randNum = random.randint(100000, 1000000)

	req.append(("apiKey", API_KEY))
	req.append(("time", str(currTime)))
	originalReq = req

	req.sort(key=functools.cmp_to_key(customCmp))

	hashedString = getHash(randNum, method, req)
	ADDRESS = baseAddress + method + "?"
	for params in originalReq:
		ADDRESS += params[0] + "=" + params[1] + "&"
	ADDRESS += "apiSig=" + str(randNum) + str(hashedString)
	data = requests.get(ADDRESS)
	return data.content

# Testing Data
# getResponse("contest.list", [])