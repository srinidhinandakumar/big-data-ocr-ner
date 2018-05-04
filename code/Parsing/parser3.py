from pynlp import StanfordCoreNLP
import sys
import json


inputfile = sys.argv[1]
outfile = sys.argv[2]
p
def populateJSONEntry(json_entry, entity):
    if entity.type == "DATE":
        json_entry["NER_DATE"].append(entity.__str__())

    elif entity.type == "TIME":
        json_entry["NER_TIME"].append(entity.__str__())

    elif entity.type == "LOCATION" or entity.type == "STATE_OR_PROVINCE" or entity.type == "COUNTRY":
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

with open(inputfile) as data_file:
    json_data = data_file.read()
    try:
        data = json.loads(json_data)
    except ValueError:
        print("\n ERROR : File not in JSON format")

entitySet = set()
i = 0
for item in data:
    print(i)
    i+=1
    text = item["description"]
    try:
        document = nlp(text)
        for sentence in document:
            for entity in sentence.entities:
                entitySet.add(entity.type)
                populateJSONEntry(item, entity)
    except:
        pass

# outfile = 'ufo_stalker_output.txt'
with open(outfile, 'w') as data_file:
    json.dump(data, data_file, indent=4)

sys.stdout = open('entity.txt', 'w')
print(entitySet)
