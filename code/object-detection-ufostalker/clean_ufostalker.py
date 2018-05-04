import sys
import pprint
import json

# object_file = sys.argv[1]
# caption_file = sys.argv[2]

object_file = "../data/ufo-stalker/objects.txt"
caption_file = "../data/ufo-stalker/caption.txt"
imageurl_file = "../data/ufo-stalker/imageurls_original_weiwei.txt"
objects = open(object_file, 'r').read().split("\n")
captions = open(caption_file, 'r').read().split("\n")
imageurls = open(imageurl_file, 'r').read().split("\n")
obj = dict()
cap = dict()

for o in objects:
    pos1 = o.find('.')
    pos2 = o.find('[')
    image_id = o[4:pos1]
    if image_id == '':
        continue
    image_id = int(image_id)
    #print(image_id)
    #a = input("enter: ")
    object_list = o[pos2+1:].strip(']')

    obj[image_id] = object_list.split(",")
    #print(obj)

for c in captions:
    pos1 = c.find('.')
    pos2 = c.find('[')
    image_id = c[4:pos1]
    if image_id == '':
        continue
    image_id = int(image_id)
    caption_list = c[pos2+1:].strip(']')
    # print(caption_list)
    cap[image_id] = caption_list.split(",")

# pprint.pprint(obj)
# print("\n\n\n")
# pprint.pprint(cap)

sorted_obj = sorted(obj)
sorted_captions = sorted(cap)

final_content = dict()
count = 0
for key in sorted_captions:
    if key == "":
        continue
    else:
        newkey = "img_"+str(key)+".jpeg"
        print(key, cap[key], obj[key])
        final_content[imageurls[count]] = dict()
        final_content[imageurls[count]]["objects"] = obj[key]
        final_content[imageurls[count]]["captions"] = cap[key]
        final_content[imageurls[count]]["image-name"] = "s"+newkey
        # final_content[imageurls[count]]["url"] = imageurls[count]
        count += 1
# pprint.pprint(final_content)
json.dump(final_content, open("cleaned_ufostalker_content_urlsaskeys-2.json", 'w'), indent=4)

ufo_version_twopointtwo = list

