# Applying OCR,Object Detection and NER techniques to Big Datasets

**Objective:** Apply Optical Character Recogntion, Named Entity Detection, Object Detection and Caption Generation on Big datasets


This project is partitioned into three parts:-
- Extracting data from scanned PDF files using OCR techniques
- Crawling and scraping ufostalker.com to get images and data; apply Object detection and captioning techniques to these images
- Apply NER techniques on data/sighting descriptions to extract different named entitites

**Note:** This project is built over the first one [here](https://github.com/srinidhinandakumar/big-data-content-similarity)

The dataset built from the first project is called v1 ufo dataset and the dataset generated from this project is called v2 ufo dataset.

### Tools used
---
  1. ImageMagick (convert scanned pdf to .tiff files)
  2. Ghostscript (convert scanned pdf to .tiff files)
  3. Poppler (to separate a pdf with multiple pages into single page pdfs)
  4. Tesseract (for OCR from .tiff files)
  5. [Tika Dockers](https://github.com/USCDataScience/tika-dockers.git)
  6. [TikaAndVission](https://wiki.apache.org/tika/TikaAndVision)
  7. [Tika Image Captioning](https://wiki.apache.org/tika/ImageCaption)
  8. Selenium (for scrapper/crawler)
  9. OpenNLP
  10. CoreNLP
  11. NLTK
  12. MITIE
  13. Grobid
    
### Measures of How to run some scripts
---
#### OCR
    $> bash separate-pdf.sh /path/to/directory/with/pdf/files
    $> bash pdftotext.ssh /path/to/directory/with/folders/for/pdf/files
    $> bash extract-text.sh inputfile
    $> bash extract_text.sh /path/to/directory/with/pdf/files output-directory language
    $> bash ocr-pipeline.sh /path/to/directory/with/pdf/files
    $> bash extract-ocr-final.py inputfile outputfile
#### Parsing
    $> python3 clean_ocr.py inputfile outputfile 
    $> python3 pythonParser2.py inputfile outputfile #text parser for british ufo and NER
    $> python3 parser3.py inputfile outputfile #text parser for ufostalker and NER
#### Object-detection 
    $> python3 filter-relevant-images.py 
    $> python3 get_images.py <file_containing_image_links> <output_dir>
    $> python objects.py <input_dir>
    $> python scraper.py <output_file>
    $> python3 ufo_stalker_json.py
    $> python3 version2.2-ufo.py objects-input-file data-inputfile outputfile
    $> java ObjectRecognitionParser.java (with Tika)
    $> python check_extensions.py <input_file> <output_file>
#### NER
    $> python CoreNLP.py /path/to/dataset /path/to/ouputs
    $> python OpenNLP.py /path/to/dataset /path/to/ouputs
    $> python MITIE.py /path/to/dataset /path/to/ouputs
    $> nltk-server -v --port 8881
    $> python NLTK.py /path/to/dataset /path/to/ouputs 
    $> mvn -Dmaven.test.skip=true jetty:run-war 
    $> python Grobid.py /path/to/dataset /path/to/ouputs
    $> python integrate_datasets.py /path/to/v1 /path/to/CoreNLP_results /path/to/OpenNLP_results /path/to/NLTK_results /path/to/MITIE_results /path/to/Grobid_results /path/to/outputs
#### Img2Text
    $> python retrain.py --image-dir $dir_of_training_img
#### Merge datasets
    $> python3 merge.py v1withNER-datasetfile britishUFO- datasetfile ufostalker-datasetfile outputfile(v2.json)
    $> python3 jsonToTEV.py inputJSONfile outputTSVfile

### Inferences
---
Refer to [this](https://github.com/srinidhinandakumar/big-data-ocr-ner/blob/master/docs/ENRICHMENT.pdf) document for inferences from this project.
