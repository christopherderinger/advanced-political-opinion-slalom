# advanced-political-opinion-slalom

## Introduction

This is a first version of the repository for my master thesis about the topic advanced political opinion slalom.

The code can be executed using docker and the start.sh script as described below.

Building the docker container **takes around 1600 seconds** on my system. One reason for this is the download of the GloVe embeddings and the Word2Vec embeddings. Alternatively they can be downloaded locally on the system and then inserted as described below.

**General source:** https://www.deepset.ai/german-word-embeddings

**GloVe source:** https://int-emb-glove-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt

**Word2Vec source:** https://int-emb-word2vec-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt

One way to download the files is using curl (Linux and MacOS)

```
curl "https://int-emb-glove-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt" > glove_vectors.txt
curl "https://int-emb-word2vec-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt" > word2vec_vectors.txt
```

**GloVe target path:** /data/hyperbole_detection/glove/glove_vectors.txt

**Word2Vec target path:** /data/hyperbole_detection/word2vec/word2vec_vectors.txt

## Prerequesits

Docker needs to be installed on the system

## Step 1

Go inside the directory which is created by cloning the repository and run the start.sh script like:

```bash start.sh```

This has been tested on macOS. It should work on Linux machines as well. On Windows machines it should be possible to manually execute the commands from the start.sh file like:

```
docker build -t test-mt .
docker run --user root -p 8887:8888 -it test-mt start.sh jupyter lab --LabApp.token=''
```

## Step 2

A JupyterLab Server is started and can be accessed using the following link:

```localhost:8887```

## Step 3

The JupyterLab should allow the navigation to the ```mt``` folder. It should be listed on the left side, right above the ```work``` folder.

From there it is possible to navigate to the ```mt/code/alliteration_detection``` folder and to the ```mt/code/hyperbole_detection``` folder, where the current notebooks can be found.
