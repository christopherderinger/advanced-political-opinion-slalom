#!/bin/bash

FILE_PATH=/home/jovyan/mt/data/hyperbole_detection/word2vec/word2vec_vectors.txt

if [ -f "$FILE_PATH" ]; then
		echo "Word2Vec file exists, no download is necessary."
else
		echo "Word2Vec  file does not exist, download is necessary."
		curl "https://int-emb-word2vec-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt" > $FILE_PATH
fi
