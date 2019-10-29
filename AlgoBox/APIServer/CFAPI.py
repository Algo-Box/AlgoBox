import hashlib, random, time, functools, requests, os

from config import *
API_KEY = os.environ.get("CodeForcesAPIKey")
API_SECRET = os.environ.get("CodeForcesAPISecret")

def customCmp(A, B):
	if (A[0] - B[0] == 0):
		return A[1] - B[1]
	else:
		return A[0] - B[0]

def getHash(randNum, method, req):
	hashString = str(randNum) + "/" + method + "?"
	for i in range(len(req)):
		hashString += str(req[i][0]) + "=" + str(req[i][1])
		if i != len(req)-1:
			hashString += "&"

	hashString += "#" + API_SECRET
	hashFunc = hashlib.sha512(hashString.encode())
	return hashFunc.hexdigest()

def getResponse(method, req):
	baseAddress = "http://www.codeforces.com/api/"
	currTime = round(time.time())
	# print(API_KEY)
	randNum = random.randint(100000, 1000000)

	req.append(("apiKey", API_KEY))
	req.append(("time", str(currTime)))
	originalReq = req

	req.sort(key=functools.cmp_to_key(customCmp))

	hashedString = getHash(randNum, method, req)
	ADDRESS = baseAddress + method + "?"
	for i in range(len(originalReq)):
		ADDRESS += originalReq[i][0] + "=" + originalReq[i][1] + "&"
	ADDRESS += "apiSig=" + str(randNum) + str(hashedString)
	print(ADDRESS)
	data = requests.get(ADDRESS)
	# print(data.content)
	return data.content

# Testing Data
getResponse("contest.list", [])
