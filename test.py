import hashlib, random, time, functools, requests

API_KEY = "a99cd12c8e721865e884d05d587a2e5eb3fed38e"
API_SECRET = "e191279c026eaf33cb7ed30d42ac1a0a7d3e139f"

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
	for i in range(len(req)):
		hashString += req[i][0] + "=" + req[i][1]
		if i != len(req)-1:
			hashString += "&"

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
	for i in range(len(originalReq)):
		ADDRESS += originalReq[i][0] + "=" + originalReq[i][1] + "&"
	ADDRESS += "apiSig=" + str(randNum) + str(hashedString)
	print(ADDRESS)
	data = requests.get(ADDRESS)
	return data.content

# Testing Data
# getResponse("user.rating", [("handle", "21171_somesh")])
