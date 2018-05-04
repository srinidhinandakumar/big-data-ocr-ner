import json
import sys
# ufostalker_file = sys.argv[1]
# imageurls_file = sys.argv[2]

ufostalker_file = "ufo_stalker_content.json"
imageurls_file = "imageurls_original_weiwei.txt"
outfile = "ufo_stalker_filtered_content.json"

with open(ufostalker_file) as file1:
    data_total = json.load(file1)  # json file

with open(imageurls_file) as file2:
    data_urls = file2.read().split("\n")  # list of urls

filtered_content = []
for content in data_total:
    if content["url"] in data_urls:
        filtered_content.append(content)
print(len(data_urls))
print(len(filtered_content))
with open(outfile, "w") as file3:
    file3.write(str(filtered_content))
