#!/bin/bash

COMMIT_SHA=edb89a2416b9f49a08735311207f116e381e0b19
URL="https://github.com/KarstenAMF/GerVADER/archive/${COMMIT_SHA}.zip"
FILE_PATH=/home/jovyan/mt/code/research_question_4

cd $FILE_PATH
curl -L -O $URL
unzip edb89a2416b9f49a08735311207f116e381e0b19.zip 
rm edb89a2416b9f49a08735311207f116e381e0b19.zip
mv GerVADER-edb89a2416b9f49a08735311207f116e381e0b19/ GerVADER/
touch GerVADER/__init__.py
# vader won't run if this permission is not set, as it is not allowed to write to this file
sudo chmod a+w GerVADER/outputmap.txt
