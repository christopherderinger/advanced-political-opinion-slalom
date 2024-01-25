#!/bin/bash

FILE_PATH=/home/jovyan/mt/data/hyperbole_detection/glove/glove_vectors.txt

if [ -f "$FILE_PATH" ]; then
		echo "GloVe file exists, no download is necessary."
else
		echo "GloVe file does not exist, download is necessary."
		curl "https://int-emb-glove-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt" > $FILE_PATH
fi
