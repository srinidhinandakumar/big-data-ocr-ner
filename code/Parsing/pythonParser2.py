from pynlp import StanfordCoreNLP
import sys
import json

def initJsonObject():
    c = {}
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
    c["image-objects"] = ""
    c["image-url"] = ""
    c["image-captions"] = ""
    c["NER_LOCATION"] = []
    c["NER_DATE"] = []
    c["NER_MONEY"] = []
    c["NER_ORGANIZATION"] = []
    c["NER_PERCENTAGE"] = []
    c["NER_TIME"] = []
    c["NER_PERSON"] = []
    c["NER_MEASUREMENTS"] = []
    c["NER_MEASUREMENT_UNITS"] = []
    c["NER_MEASUREMENT_NUMBERS"] = []
    return c

def populateJSONEntry(json_entry, entity, description):
    json_entry["description"] = description
    if entity.type == "CITY":
        json_entry["county"] = entity.__str__()
        json_entry["airport_name"] = entity.__str__()

    elif entity.type == "DATE":
        json_entry["sighted_at"] = entity.__str__()
        json_entry["reported_at"] = entity.__str__()
        json_entry["NER_DATE"].append(entity.__str__())

    elif entity.type == "TIME":
        json_entry["duration"] = entity.__str__()
        json_entry["NER_TIME"].append(entity.__str__())

    elif entity.type == "LOCATION" or entity.type == "STATE_OR_PROVINCE" or entity.type == "COUNTRY":
        json_entry["location"] = entity.__str__()
        json_entry["NER_LOCATION"].append(entity.__str__())

    elif entity.type == "NUMBER":
        json_entry["airport_distance"] = entity.__str__()
        json_entry["population"] = entity.__str__()

    elif entity.type == "MONEY":
        json_entry["NER_MONEY"].append(entity.__str__())

    elif entity.type == "ORGANIZATION":
        json_entry["NER_ORGANIZATION"].append(entity.__str__())

    elif entity.type == "PERSON":
        json_entry["NER_PERSON"].append(entity.__str__())

annotators = 'tokenize, ssplit, pos, lemma, ner'
options = {'openie.resolve_coref': 'true'}

nlp = StanfordCoreNLP(annotators=annotators, options=options)

data = {}

with open(sys.argv[1]) as data_file:
    json_data = data_file.read()
    try:
        data = json.loads(json_data)
    except ValueError:
        print("\n ERROR : File not in JSON format")

text = ''
json_result = []
entitySet = set()
#sys.stdout = open('out_trial.txt', 'w')

for key in data:
    #print("\n Entry " + key +  " :\n")
    text = '\n' + data[key]['im'] + '\n' + data[key]['gs']

    current_json_entry = initJsonObject()
    try:
        document = nlp(text)
        for sentence in document:
            for entity in sentence.entities:
                entitySet.add(entity.type)
                if entity.type == "DATE":
                    if len(str(entity)) > 10 or str(entity).replace(" ","").isdigit():
                        continue
                #print(entity, '({})'.format(entity.type))
                populateJSONEntry(current_json_entry, entity, data[key]['gs'])
    except:
        pass
    json_result.append(current_json_entry)

with open('out_trial.txt', 'w') as data_file:
    json.dump(json_result, data_file, indent=4)

sys.stdout = open('entity.txt', 'w')
print(entitySet)
