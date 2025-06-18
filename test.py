# let's NOT put semicolumns
# actionscript > python
# but scratchr2 is written in python so eh

import requests
import json

def loadGroup(id):
    #activityJson = open("group.json")
    response = requests.get("https://www.pixilart.com/api/w/activity/0/" + str(id) + "/group")
    if response:
        print("target acquired")
        print(response)
        print("\n")
    else:
        raise Exception("target failed")
    global activity
    activity = json.loads(response.content)

def getGroupData(data):
    group = [x["group"] for x in activity["activity"]] # why can't I just activity["activity"]["group"]
    print([x[data] for x in group][0]) # for whatever reason it repeats the string 5 times so I put [0]

loadGroup(96434)
getGroupData("url")
getGroupData("name")
print("")
getGroupData("description")