#FROM jupyter/minimal-notebook:python-3.8.13
FROM jupyter/minimal-notebook
USER root

ADD ./code /home/jovyan/mt/code
ADD ./data /home/jovyan/mt/data
ADD ./scripts /home/jovyan/mt/scripts
ADD ./plots /home/jovyan/mt/plots

# required for writing files into the folders
RUN sudo find /home/jovyan/mt/data/ -type d -exec chmod 777 {} \;

RUN sudo find /home/jovyan/mt/plots/ -type d -exec chmod 777 {} \;

RUN apt-get update && apt-get install -y vim

# download and setup GerVADER
ARG COMMIT_SHA=edb89a2416b9f49a08735311207f116e381e0b19
ADD https://github.com/KarstenAMF/GerVADER/archive/$COMMIT_SHA.zip /home/jovyan/mt/code/research_question_4/GerVADER.zip
RUN sudo unzip /home/jovyan/mt/code/research_question_4/GerVADER.zip -d /home/jovyan/mt/code/research_question_4
RUN sudo mv /home/jovyan/mt/code/research_question_4/GerVADER-$COMMIT_SHA /home/jovyan/mt/code/research_question_4/GerVADER
RUN sudo touch /home/jovyan/mt/code/research_question_4/GerVADER/__init__.py
RUN sudo rm /home/jovyan/mt/code/research_question_4/GerVADER.zip
RUN sudo chmod a+w /home/jovyan/mt/code/research_question_4/GerVADER/outputmap.txt

# GerVADER only seems to work inside the container if the path is absolute, therefore the path to outputmap.txt is replaced inside the code of the GerVADER library
RUN sudo vim -c "%s/outputmap.txt/\/home\/jovyan\/mt\/code\/research_question_4\/GerVADER\/outputmap.txt/g | wq" /home/jovyan/mt/code/research_question_4/GerVADER/vaderSentimentGER.py

RUN pip install pandas textblob-de numpy scikit-learn transformers cleantext wordcloud matplotlib pandarallel num2words cologne_phonetics
