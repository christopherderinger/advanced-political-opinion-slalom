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
docker run --user root -p 8887:8888 -it test-mt start.sh jupyter lab --LabApp.token=''
```

## Step 2

A JupyterLab Server is started and can be accessed using the following link:

```localhost:8887```

## Step 3

The JupyterLab should allow the navigation to the ```mt``` folder. It should be listed on the left side, right above the ```work``` folder.

From there it is possible to navigate to the ```mt/code/alliteration_detection``` folder, where the current notebooks can be found.
