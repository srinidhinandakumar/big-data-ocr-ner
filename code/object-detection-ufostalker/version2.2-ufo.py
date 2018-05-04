import sys
import pprint
import json
import random

ufostalker_objects = sys.argv[1]
ufostalker_data = sys.argv[2]

# ufostalker_objects = "cleaned_ufostalker_content_urlsaskeys-2.json"
# ufostalker_data = "ufo_stalker_content.json"

with open(ufostalker_objects) as ufoObj:
    ufo_obj = json.load(ufoObj)
with open(ufostalker_data) as ufoData:
    ufo_data = json.load(ufoData)

# pprint.pprint(ufo_obj)
final_content = []
visited_urls = []
for row in ufo_data:
    if row == '':
        continue
    if row['url'] in ufo_obj:
        visited_urls.append(row['url'])
        content = row
        content["image-objects"] = ufo_obj[row['url']]['objects']
        content["image-captions"] = ufo_obj[row['url']]['captions']
        content["description"] = content["description"].replace('\n', " ")
        content["url"] = "data/ufo-stalker/images/"+ufo_obj[row['url']]['image-name']
        content["image-url"] = content.pop("url")
        content["NER_LOCATION"] = []
        content["NER_DATE"] = []
        content["NER_MONEY"] = []
        content["NER_ORGANIZATION"] = []
        content["NER_PERCENTAGE"] = []
        content["NER_TIME"] = []
        content["NER_PERSON"] = []
        content["NER_MEASUREMENTS"] = []
        content["NER_MEASUREMENT_UNITS"] = []
        content["NER_MEASUREMENT_NUMBERS"] = []
        final_content.append(content)
print(len(final_content))

# adding common content from other
for row in ufo_data:
    # print(row)
    if ('url' in row and row['url'] not in visited_urls) or ('image-url' in row and row['image-url'] not in visited_urls):
        # visited_urls.append(row['url'])
        content = row
        url = random.sample(list(ufo_obj), 1)
        content["image-objects"] = ufo_obj[url[0]]['objects']
        content["image-captions"] = ufo_obj[url[0]]['captions']
        content["description"] = content["description"].replace('\n', " ")
        # content["url"] = url[0]
        content["url"] = "data/ufo-stalker/images/"+ufo_obj[url[0]]['image-name']
        content["image-url"] = content.pop("url")
        content["NER_LOCATION"] = []
        content["NER_DATE"] = []
        content["NER_MONEY"] = []
        content["NER_ORGANIZATION"] = []
        content["NER_PERCENTAGE"] = []
        content["NER_TIME"] = []
        content["NER_PERSON"] = []
        content["NER_MEASUREMENTS"] = []
        content["NER_MEASUREMENT_UNITS"] = []
        content["NER_MEASUREMENT_NUMBERS"] = []
        # pprint.pprint(content)
        final_content.append(content)
        #a = input()

print(len(final_content))
# pprint.pprint(final_content)

# with open("ufo-stalker-only-content.json", 'w') as u:
#     json.dump(final_content, u, indent=4)
outputfile = sys.argv[3]
# outputfile = "ufostalker-final.json"
with open(outputfile, 'w') as u:
    json.dump(final_content, u, indent=4)
