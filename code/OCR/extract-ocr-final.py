import json
import sys
#import enchant

# def clean_data(text):
outputfile = sys.argv[2]
# outputfile = "../data/split-british-ufo-files/output.json"
# f = open(outputfile, "a")


def fetch_data(filename):
    fp = open(filename, "r")
    data = fp.read()
    lines = data.split("\n")
    result = dict()
    i = 0
    # d = enchant.Dict("en_US")

    while i<len(lines):
        gs_file = lines[i]
        im_file = lines[i+1]

        fq = open(gs_file)
        fr = open(im_file)
        gs_text = fq.read().strip()
        im_text = fr.read().strip()
        filename = gs_file.rstrip("_gs.txt")
        filename = filename+".pdf"
        result[filename] = dict()
        result[filename]["gs"] = gs_text
        result[filename]["im"] = im_text
        fq.close()
        fr.close()
        i = i+2

    with open(outputfile, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    # return 


file = sys.argv[1]
fetch_data(file)
