'''

Performs object detection and image captioning for all the UFO images using Tika
NOTE: Make sure the docker is up and running
'''

import os

directory = "ufo_images_objects"
count = 1
for filename in os.listdir(directory):
    print "Count = " + str(count) + "," + str(filename)
    comm_ = "java -jar tika-1.17/tika-app/target/tika-app-1.17.jar --config=tika-1.17/tika-config-tflow-rest.xml "
    os.remove(file_path)
    file_path = "ufo_images_objects/"+filename
    comm_ = comm_ + file_path
    os.system(comm_)
    count = count + 1
