'''
Downloads the images to a directory from the list of links given through a file

'''

import requests
import os
import shutil


def make_dir(dirname):
    current_path = os.getcwd()
    path = os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

def save_image_to_file(image, dirname, suffix, exten):
    with open('{dirname}/img_{suffix}.{exten}'.format(dirname=dirname, suffix=suffix, exten=exten), 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)

count = 1
dir_name = "ufo_images"

make_dir(dir_name)

file = open("imageurls.txt", "r")
failed_links = []
for line in file:
    line = line.rstrip()
    response = requests.get(line, stream=True)
    if response.status_code != 200:
        failed_links.append(line)
        continue
    exten = line.split(".")[-1]
    exten = exten.lower()
    if exten == "jpg":
        exten = "jpeg"

    save_image_to_file(response, dir_name, count, exten)
    print count
    count = count + 1
print failed_links