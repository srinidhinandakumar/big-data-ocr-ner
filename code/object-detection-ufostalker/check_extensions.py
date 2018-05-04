'''

Cleans the URLs received from UFO site. Only png, jpeg and gif are considered.

'''

file = open("imageurls.txt", "r")

type_dict = {}

for line in file:
    line  = line.strip('\n')
    exten = line.split(".")[-1].lower()
    if exten not in type_dict:
        type_dict[exten] = []

    type_dict[exten].append(line)

import json
with open('imageurls_exten.txt', 'w') as outfile:
    json.dump(type_dict, outfile, indent=4)