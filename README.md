# advanced-political-opinion-slalom

## Introduction

This is a first version of the repository for my master thesis about the topic advanced political opinion slalom.

The code can be executed using docker and the start.sh script as described below.

## Prerequesits

Docker needs to be installed on the system

## Step 1

Go inside the directory which is created by cloning the repository and run the start.sh script like:

```bash start.sh```

This has been tested on macOS. It should work on Linux machines as well. On Windows machines it should be possible to manually execute the commands from the start.sh file like:

```
docker build -t test-mt .
docker run --user root -p 8887:8888 -it test-mt
```

## Step 2

A JupyterLab Server is started and can be accessed using the following link:

```localhost:8887```

A token will be required to log into the JupyterLab. This token can be found in the command line window where the docker commands have been exexuted.

The message will look like the following:

```
Jupyter Server 1.18.1 is running at:
http://44ddfe5fa174:8888/lab?token=bbb7a73fe4a339c9ee17e7a7c7f99d782ec951d8c48c5cb0
 or http://127.0.0.1:8888/lab?token=bbb7a73fe4a339c9ee17e7a7c7f99d782ec951d8c48c5cb0
```

The token is found at the end, in this example it would be ```bbb7a73fe4a339c9ee17e7a7c7f99d782ec951d8c48c5cb0```

## Step 3

The JupyterLab should allow the navigation to the ```mt``` folder. It should be listed on the left side, right above the ```work``` folder.

From there it is possible to navigate to the ```mt/code/alliteration_detection``` folder, where the current notebooks can be found.
