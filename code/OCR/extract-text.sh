#!/bin/bash
INPUTPATH=$1
# outfile=$INPUTPATH"output.json"
files_list=$INPUTPATH"files_list.txt"
# echo $outfile
# echo "{" >> $outfile
for path in $( ls $INPUTPATH ); edo
	echo "PATH:"$path
	# cd $path
	# ls $INPUTPATH/$path
	echo " "

	for FILENAME in $( ls $INPUTPATH/$path ); do
		filename_no_path=$(basename "$FILENAME")
		# if [ "$filename_no_path" -eq "outtxt" ] || [ "$filename_no_path" -eq "tiff" ];then
		# 	continue
		# fi
		extension="${filename_no_path##*.}"
		filename_no_extension="${filename_no_path%.*}"
		echo ""
		echo "**************"
		echo "Processing $INPUTPATH$path/$FILENAME with extension $extension: filename without extension: $filename_no_extension"
		
		the_file=$(basename $FILENAME)
	    the_file_ext="${the_file##*.}"
	    the_file_noext="${the_file%.*}"
	    file_gs="${the_file_noext}_gs"
	    file_im="${the_file_noext}_im"
	    
	    gs_text="`cat "$INPUTPATH$path/outtxt/$file_gs.txt"`"
	    im_text="`cat "$INPUTPATH$path/outtxt/$file_im.txt"`"
	    echo $INPUTPATH$path/outtxt/$file_gs.txt>>$files_list
	    echo $INPUTPATH$path/outtxt/$file_im.txt>>$files_list
		# echo $gs_text
		# echo $gs_text=${gs_text//\"/_}
		# echo $gs_text
		# echo $im_text
		# printf '"%s":{"im-content":"%s","gs-content":"%s"}\n' "$INPUTPATH$path/$FILENAME" "$im_text" "$gs_text">>$outfile
		# printf ",\n">>$outfile
		# echo {"file-path": "$INPUTPATH$path/$FILENAME", "im-content": $im_text, "gs-content": $gs_text }
		# read var
	done
done
# printf "}">>$outfile