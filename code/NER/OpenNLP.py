__author__ = 'weiweiduan'
import json
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.tokenize import RegexpTokenizer


OFile = open(sys.argv[2], 'w')
with open(sys.argv[1]) as data_file:
    data = json.loads(data_file.read())
count = 0
# nltk.download()
for i in data:
    outputfile = open('description_tmpt.txt', 'w')
    text = i['description']
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    word_tokens = tokenizer.tokenize(text)
    # word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_text = " ".join(filtered_sentence)
    # print text
    # print filtered_text
    # print "***************"
    outputfile.writelines(text)
    cmd = 'java -classpath /Users/weiweiduan/Documents/tika/tika-ner-resources:/Users/weiweiduan/Downloads/tika-1.12/tika-app/target/tika-app-1.12.jar  org.apache.tika.cli.TikaCLI --config=tika-config.xml -m /Users/weiweiduan/Documents/tika/tika-ner-resources/HW2/description_tmpt.txt'
    p = subprocess.Popen(cmd, shell=True,stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out,err = p.communicate()
    res = out.split('\n')
    dictionary = {}
    for i in range(len(res)):
        if "NER_LOCATION" in res[i] or "NER_DATE" in res[i] or "NER_LOCATION" in res[i] or "NER_MONEY" in res[i] or "NER_ORGANIZATION" in res[i]\
            or "NER_PERCENTAGE" in res[i] or "NER_time" in res[i] or "NER_PERSON" in res[i]:
            tmpt = res[i].strip().split(":")
            dictionary['description'] = text
            dictionary[tmpt[0]] = tmpt[1]
            print count, tmpt[1]
    if dictionary != {}:
        OFile.writelines(str(dictionary)+'\n')
    count += 1