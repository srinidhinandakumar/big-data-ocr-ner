#!/bin/bash
mkdir -p $filename_no_extension
     mkdir -p $filename_no_extension/tiff
     mkdir -p $filename_no_extension/outtxt
     pdfseparate "$FILENAME" "$filename_no_extension"/%d.pdf
