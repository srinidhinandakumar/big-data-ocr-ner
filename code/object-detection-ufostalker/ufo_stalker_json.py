#!/usr/bin/env python                                                                                                                                                                                                                    
# -*- coding: utf-8 -*-  

import requests
import json
import pprint
from time import sleep

def writeLinks(lks):
    with open('ufo_stalker_urls.csv', 'a') as usu:
        for l in lks:
            usu.write(l+"\n")

def writeContent(content):
    with open('ufo_stalker_content.json', 'a') as usc:
        json.dump(content, usc)


print("0\n")

url = "http://ufostalker.com:8080/eventsByTag"
totalPages = 0
totalElements = 0

params = dict(
   page='1',
   size='25',
   tag='photo'
)
print("1st\n")
resp = requests.get(url=url, params=params)
data = resp.json()
print("2nd\n")

totalPages = data["totalPages"]
totalElements = data["totalElements"]
print("3rd\n")

print("Total Pages: ["+str(totalPages)+"] Total Elements: ["+str(totalElements)+"]")
print("Processing page 1 of "+str(totalPages))

print(data.keys())
print(data['content'][0].keys())
# pprint.pprint(data['content'], indent=4r)
count = 0
content = []
for obj in data["content"]:
    if obj["urls"]!=None and len(obj["urls"]) > 0:
        l = len(obj["urls"])
        for i in range(l):
            c = dict()
            c["cancer_incidence_counts_allraces"] = ""
            c["county"] = obj["county"]
            c["SO2 Mean"] = ""
            c["description"] = obj["detailedDescription"]
            c["O3 Mean"] = ""
            c["reported_at"] = ""
            c["cancer_incidence_counts_white"] = ""
            c["airport_name"] = ""
            c["longitude"] = obj["longitude"]
            c["cancer_incidence_counts_hispanic"] = ""
            c["duration"] = obj["duration"]
            c["shape"] = obj["shape"]
            c["location"] = obj["locationName"]
            c["death rate"] = ""
            c["latitude"] = obj["latitude"]
            c["airport_distance"] = ""
            c["sighted_at"] = obj["occurred"]
            c["CO Mean"] = ""
            c["population"] = ""
            c["zipcode"] = obj["zipcode"]
            c["url"] = obj["urls"][i]
            content.append(c)


# for d in data["content"]:
#     if d["urls"]!=None and len(d["urls"]) > 0:
#         writeLinks(d["urls"])

for i in range(2, totalPages):
    print("Processing page "+str(i)+" of "+str(totalPages))
    
    params = dict(
      page=str(i),
      size='25',
      tag='photo'
    )                           
                           
    resp = requests.get(url=url, params=params)
    data = resp.json()
    
    for obj in data["content"]:
        if obj["urls"] != None and len(obj["urls"]) > 0:
            # writeLinks(d["urls"])
            l = len(obj["urls"])
            for i in range(l):
                c = dict()
                c["cancer_incidence_counts_allraces"] = ""
                c["county"] = obj["county"]
                c["SO2 Mean"] = ""
                c["description"] = obj["detailedDescription"]
                c["O3 Mean"] = ""
                c["reported_at"] = ""
                c["cancer_incidence_counts_white"] = ""
                c["airport_name"] = ""
                c["longitude"] = obj["longitude"]
                c["cancer_incidence_counts_hispanic"] = ""
                c["duration"] = obj["duration"]
                c["shape"] = obj["shape"]
                c["location"] = obj["locationName"]
                c["death rate"] = ""
                c["latitude"] = obj["latitude"]
                c["airport_distance"] = ""
                c["sighted_at"] = obj["occurred"]
                c["CO Mean"] = ""
                c["population"] = ""
                c["zipcode"] = obj["zipcode"]
                c["url"] = obj["urls"][i]
                content.append(c)

    sleep(2)

writeContent(content)
