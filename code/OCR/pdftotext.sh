#!/bin/bash
INPUTPATH=$1

for path in $( ls $INPUTPATH ); do
	echo "PATH:"$path
	# cd $path
	ls $INPUTPATH/$path
	echo " "

	for FILENAME in $( ls $INPUTPATH/$path ); do
		filename_no_path=$(basename "$FILENAME")
		# if [ "$filename_no_path" -eq "outtxt" ] || [ "$filename_no_path" -eq "tiff" ];then
		# 	continue
		# fi
		extension="${filename_no_path##*.}"
		filename_no_extension="${filename_no_path%.*}"
		echo "**************"
		echo "Processing $INPUTPATH$path/$FILENAME with extension $extension: filename without extension: $filename_no_extension"
		
		the_file=$(basename $FILENAME)
	    the_file_ext="${the_file##*.}"
	    the_file_noext="${the_file%.*}"
	    file_gs="${the_file_noext}_gs"
	    file_im="${the_file_noext}_im"
	    echo " "
	    # read textname
	    echo "Creating tiff file using ImageMagick for $FILENAME"
	    if convert -density 300 $INPUTPATH$path/$FILENAME -depth 8 -alpha off -background white $INPUTPATH$path/tiff/$file_im.tiff; then
	    	echo "Successfull ImageMagick for $filename_no_extension/$the_file ">>log.txt
	    else
	    	echo ""
	    	echo "Failure!!! ImageMagick for $filename_no_extension/$the_file"
	    	echo ""
	    	echo "Failure!!! ImageMagick for $filename_no_extension/$the_file ">>log.txt
	    fi
	    # read textname
	    echo "OCR for file using tesseract for ImageMagick of $FILENAME"
	    if tesseract $INPUTPATH$path/tiff/$file_im.tiff $INPUTPATH$path/outtxt/$file_im; then
	    	echo "Successfull ImageMagick OCR for $filename_no_extension/$the_file ">>log.txt
	    else
	    	echo ""
	    	echo "Failure!!! ImageMagick OCR for $filename_no_extension/$the_file"
	    	echo ""
	    	echo "Failure!!! ImageMagick OCR for $filename_no_extension/$the_file ">>log.txt
	    fi
	    echo " "
	    # read textname
	    echo "Creating tiff file using GhostScript for $FILENAME"
	    if gs -q -dNOPAUSE -sDEVICE=tiffg4 -sOutputFile=$INPUTPATH$path/tiff/$file_gs.tiff $INPUTPATH$path/$FILENAME -c quit; then
	    	echo "Successfull GhostScript for $filename_no_extension/$the_file ">>log.txt
	    else
	    	echo ""
	    	echo "Failure!!! GhostScript for $filename_no_extension/$the_file"
	    	echo ""
	    	echo "Failure!!! GhostScript for $filename_no_extension/$the_file ">>log.txt
	    fi
	    # read textname
	    echo "OCR for file using tesseract for IM of $FILENAME"
	    if tesseract $INPUTPATH$path/tiff/$file_gs.tiff $INPUTPATH$path/outtxt/$file_gs; then
	    	echo "Successfull GhostScript OCR for $filename_no_extension/$the_file ">>log.txt
	    else
	    	echo ""
	    	echo "Failure!!! GhostScript OCR for $filename_no_extension/$the_file"
	    	echo ""
	    	echo "Failure!!! GhostScript OCR for $filename_no_extension/$the_file ">>log.txt
	    #cat " ">>log.txt
		fi
	
	done
done