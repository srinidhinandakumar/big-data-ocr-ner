import sys
import json
import pprint
import csv

inputfile = sys.argv[1]  # dataset1 v2.json
outputfile = sys.argv[2] # output v2.tsv

# inputfile = "../../data/Results/final/v2.json"   # dataset3 UFO stalker images and data + NER
# outputfile = "../../data/Results/final/v2.tsv"

with open(inputfile) as input_file:
    data = json.load(input_file)

with open(outputfile, 'w') as output_file:
    dw = csv.DictWriter(output_file, data[0].keys(), delimiter='\t')
    dw.writeheader()
    dw.writerows(data)


# filename = "../../data/Results/final/v2.json"
#
# f1 = "1.txt"
# f2 = "2.txt"
#
# with open(filename) as f:
#     x = json.load(f)
#
# print(sorted(x[0].keys()))
# # pprint.pprint(x[69000])
