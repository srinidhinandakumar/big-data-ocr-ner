### Measures of How to run some scripts
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
