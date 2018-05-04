import json
import string
import re
import pprint
import sys

read_file = sys.argv[1]
# read_file = "split-british-ufo-files/output.json"
with open(read_file) as file:
    data = json.load(file)

content = dict()
for i in data:
    im = data[i]["im"]
    gs = data[i]["gs"]

    # remove unicode \n
    printable = set(string.printable)
    im = ''.join(filter(lambda x: x in printable, im))
    gs = ''.join(filter(lambda x: x in printable, gs))

    replace_unicode = str.maketrans("\n", ' ')
    im = im.translate(replace_unicode)
    gs = gs.translate(replace_unicode)
    print(im)
    print(gs)

    # remove double and single quotes
    im = re.sub('"', ' ', im)
    im = im.replace('\'', ' ')
    gs = re.sub('"', ' ', gs)
    gs = gs.replace('\'', ' ')
    print(im)
    print(gs)
    # a = sys.argv[1]
    # # remove special characters
    # im = im.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    # gs = gs.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    # replace punctuation with space
    replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    im = im.translate(replace_punctuation)
    gs = gs.translate(replace_punctuation)

    # remove multiple spaces
    im = re.sub(' +', ' ', im)
    gs = re.sub(' +', ' ', gs)

    content[i] = dict()
    content[i]["im"] = im
    content[i]["gs"] = gs

pprint.pprint(content, indent=4)
write_file = sys.argv[2]
# write_file = "cleaned-ocr-output.json"
with open(write_file, "w") as file:
    file.write(str(content))
