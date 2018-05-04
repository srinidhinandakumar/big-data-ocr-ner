import sys
import json
import pprint

inputfile1 = sys.argv[1]  # dataset1 v1 + NER
inputfile2 = sys.argv[2]  # dataset3 British UFO files + NER
inputfile3 = sys.argv[3]  # dataset3 UFO stalker images and data + NER
outfile = sys.argv[4] # output of final merged v2 dataset
# inputfile1 = "../../data/Results/final/v1-withNER.json"  # dataset1 v1 + NER
# inputfile2 = "../../data/Results/final/british-ufo-withNER.json"   # dataset3 British UFO files + NER
# inputfile3 = "../../data/Results/final/ufo_stalker_withNER.json"   # dataset3 UFO stalker images and data + NER
# outputfile = "../../data/Results/final/v2.json"

with open(inputfile1) as i1:
    data1 = json.load(i1)

with open(inputfile2) as i2:
    data2 = json.load(i2)

with open(inputfile3) as i3:
    data3 = json.load(i3)
c = dict()

c["cancer_incidence_counts_allraces"] = ""
c["county"] = ""
c["SO2 Mean"] = ""
c["description"] = ""
c["O3 Mean"] = ""
c["reported_at"] = ""
c["cancer_incidence_counts_white"] = ""
c["airport_name"] = ""
c["longitude"] = ""
c["cancer_incidence_counts_hispanic"] = ""
c["duration"] = ""
c["shape"] = ""
c["location"] = ""
c["death rate"] = ""
c["latitude"] = ""
c["airport_distance"] = ""
c["sighted_at"] = ""
c["CO Mean"] = ""
c["population"] = ""
c["zipcode"] = ""
c["image-objects"] = ""
c["image-url"] = ""
c["image-captions"] = ""
c["NER_LOCATION"] = []
c["NER_DATE"] = []
c["NER_NAMES"] = []
c["NER_NORMALIZED_MEASUREMENTS"] =[]
c["NER_MONEY"] = []
c["NER_ORGANIZATION"] = []
c["NER_PERCENTAGE"] = []
c["NER_TIME"] = []
c["NER_PERSON"] = []
c["NER_MEASUREMENTS"] = []
c["NER_MEASUREMENT_UNITS"] = []
c["NER_MEASUREMENT_NUMBERS"] = []
keys = c.keys()
list_keys = ["image-objects", "image-captions", "NER_NAMES", "NER_NORMALIZED_MEASUREMENTS", "NER_LOCATION", "NER_DATE", "NER_MONEY", "NER_ORGANIZATION", "NER_PERCENTAGE", "NER_TIME", "NER_PERSON", "NER_MEASUREMENTS", "NER_MEASUREMENT_UNITS", "NER_MEASUREMENT_NUMBERS"]
for d in data1:
    for k in keys:
        if k not in d:
            if k in list_keys:
                d[k] = []
            else:
                d[k] = ""

for d in data2:
    for k in keys:
        if k not in d:
            if k in list_keys:
                d[k] = []
            else:
                d[k] = ""

for d in data3:
    for k in keys:
        if k not in d:
            if k in list_keys:
                d[k] = []
            else:
                d[k] = ""

data4 = []
data4 += data1+data2+data3
print(len(data1))
print(len(data2))
print(len(data3))
print(len(data4))

with open(outputfile, 'w') as i4:
    json.dump(data4, i4, indent=4)

