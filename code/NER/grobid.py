__author__ = 'weiweiduan'

import json
import subprocess

OFile = open(sys.argv[2], 'w')
with open(sys.argv[1]) as data_file:
    data = json.loads(data_file.read())
count = 0
for i in data:
    outputfile = open('description_tmpt.txt', 'w')
    text = i['description']
    outputfile.writelines(text)
    cmd = 'java -Dner.impl.class=org.apache.tika.parser.ner.grobid.GrobidNERecogniser\
     -classpath /Users/weiweiduan/GrobidQuantitiesRest-resources:/Users/weiweiduan/Downloads/tika-1.13/tika-app/target/tika-app-1.13.jar org.apache.tika.cli.TikaCLI\
      --config=/Users/weiweiduan/GrobidQuantitiesRest-resources/tika-config.xml\
       -m  /Users/weiweiduan/GrobidQuantitiesRest-resources/599_HW2/description_tmpt.txt '
    p = subprocess.Popen(cmd, shell=True,stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out,err = p.communicate()
    res = out.split('\n')
    dictionary = {}
    for i in range(len(res)):
        if "NER_MEASUREMENTS" in res[i] or "NER_MEASUREMENT_NUMBERS" in res[i] or "NER_MEASUREMENT_UNITS" in res[i] or "NER_NORMALIZED_MEASUREMENTS" in res[i] or "NER_ORGANIZATION" in res[i]\
            or "NER_PERCENTAGE" in res[i] or "NER_time" in res[i] or "NER_PERSON" in res[i]:
            tmpt = res[i].strip().split(":")
            dictionary['description'] = text
            dictionary[tmpt[0]] = tmpt[1]
            print count, tmpt[1]
    if dictionary != {}:
        OFile.writelines(str(dictionary)+'\n')
    count += 1

