import urllib.request as urlRequest
import urllib.parse as urlParse
import sys
import os
import json
#TODO: do NOT open missing beatmap pages in browser
#Script requires you to run it when you are in a multi (Stable) or anywhere in cutting-edge.
idColl=sys.argv[1]
i=0
fatColl=[]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
def GatherTwoHundred(pathname):
	req = urlRequest.Request(pathname, headers = headers)
	a=json.loads(urlRequest.urlopen(req).read().decode("utf-8"))
	listOfIDS=[]
	for p in a:
		listOfIDS.append(p["beatmap"]["beatmapSetId"])
	return(listOfIDS)
def remove_dupes(x):
  return list(dict.fromkeys(x))

while(1>0):
	if urlRequest.urlopen(urlRequest.Request("https://osustats.ppy.sh/apiv2/collection/"+str(idColl)+"/beatmaps?offset="+str(i), headers = headers)).read().decode("utf-8")=="[]":
		break #GetOutOnEmptyResponse
	else:
		fatColl.append(GatherTwoHundred("https://osustats.ppy.sh/apiv2/collection/"+str(idColl)+"/beatmaps?offset="+str(i)))
	i=i+200
pureList=[]
for item in fatColl:
	for embedItem in item:
		pureList.append(embedItem)
pureList=remove_dupes(pureList) #Remove duplicates
for item in pureList:
	os.system("start osu://dl/"+str(item)) #Flood osu!