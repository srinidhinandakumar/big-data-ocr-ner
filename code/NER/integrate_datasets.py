__author__ = 'weiweiduan'
import json
import sys

with open(sys.argv[1]) as json_data:
    d = json.load(json_data)


OpenNLP = open(sys.argv[2])
CoreNLP = open(sys.argv[3])
MITIE = open(sys.argv[4])
NLTK = open(sys.argv[5])
Grobid = open(sys.argv[6])

OpenNLP_data = []
CoreNLP_data = []
MITIE_data = []
NLTK_data = []
Grobid_data = []

for line in OpenNLP:
    tmpt = eval(line)
    OpenNLP_data.append(tmpt)

for line in CoreNLP:
    tmpt = eval(line)
    CoreNLP_data.append(tmpt)

for line in MITIE:
    tmpt = eval(line)
    MITIE_data.append(tmpt)

for line in NLTK:
    tmpt = eval(line)
    NLTK_data.append(tmpt)

for line in Grobid:
    tmpt = eval(line)
    Grobid_data.append(tmpt)

for entry in d:
    description = entry['description']
    entry['NER_LOCATION'] = []
    entry['NER_DATE'] = []
    entry['NER_MONEY'] = []
    entry['NER_ORGANIZATION'] = []
    entry['NER_PERCENTAGE'] = []
    entry['NER_TIME'] = []
    entry['NER_PERSON'] = []
    entry['NER_NAMES'] = []
    entry["NER_MEASUREMENTS"] = []
    entry['NER_MEASUREMENT_NUMBERS'] = []
    entry['NER_MEASUREMENT_UNITS'] = []
    entry['NER_NORMALIZED_MEASUREMENTS'] = []
#    entry['NER_LOCATION_CoreNLP'] = []
#    entry['NER_DATE_CoreNLP'] = []
#    entry['NER_MONEY_CoreNLP'] = []
#    entry['NER_ORGANIZATION_CoreNLP'] = []
#    entry['NER_PERCENTAGE_CoreNLP'] = []
#    entry['NER_TIME_CoreNLP'] = []
#    entry['NER_PERSON_CoreNLP'] = []
#    entry['NER_LOCATION_OpenNLP'] = []
#    entry['NER_DATE_OpenNLP'] = []
#    entry['NER_MONEY_OpenNLP'] = []
#    entry['NER_ORGANIZATION_OpenNLP'] = []
#    entry['NER_PERCENTAGE_OpenNLP'] = []
#    entry['NER_TIME_OpenNLP'] = []
#    entry['NER_PERSON_OpenNLP'] = []
#    entry['NER_LOCATION_MITIE'] = []
#    entry['NER_DATE_MITIE'] = []
#    entry['NER_MONEY_MITIE'] = []
#    entry['NER_ORGANIZATION_MITIE'] = []
#    entry['NER_PERCENTAGE_MITIE'] = []
#    entry['NER_TIME_MITIE'] = []
#    entry['NER_PERSON_MITIE'] = []
#    entry['NER_NAMES_NLTK'] = []
#    entry["NER_MEASUREMENTS_Grobid"] = []
#    entry['NER_MEASUREMENT_NUMBERS_Grobid'] = []
#    entry['NER_MEASUREMENT_UNITS_Grobid'] = []
#    entry['NER_NORMALIZED_MEASUREMENTS_Grobid'] = []
    for a in CoreNLP_data:
        if description == a['description']:
            for k in a:
                if k != 'description':
                    print k
                    entry[k+"_CoreNLP"].append(a[k])
    for a in OpenNLP_data:
        if description == a['description']:
            for k in a:
                if k != 'description':
                    entry[k+'_OpenNLP'].append(a[k])
    for a in MITIE_data:
        if description == a['description']:
            for k in a:
                if k != 'description':
                    entry[k+'_MITIE'].append(a[k])
    for a in NLTK_data:
        if description == a['description']:
            for k in a:
                if k != 'description':
                    entry[k+'_NLTK'].append(a[k])
    for a in Grobid_data:
        if description == a['description']:
            for k in a:
                if k != 'description':
                    entry[k+'_Grobid'].append(a[k])

with open(sys.argv[7], 'w') as outfile:
    json.dump(d, outfile)


