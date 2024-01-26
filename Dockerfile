#FROM jupyter/minimal-notebook:python-3.8.13
FROM jupyter/minimal-notebook
USER root

ADD ./code /home/jovyan/mt/code
ADD ./data /home/jovyan/mt/data
ADD ./scripts /home/jovyan/mt/scripts
ADD ./plots /home/jovyan/mt/plots

# required for writing files into the folders
RUN sudo find data/ -type d -exec chmod 777 {} \;

RUN sudo find plots/ -type d -exec chmod 777 {} \;

RUN apt-get update && apt-get install -y vim

RUN sudo vim -c "%s///g | wq" /home/jovyan/mt/scripts/research_question_4/install_gervader.sh

RUN sudo bash /home/jovyan/mt/scripts/research_question_4/install_gervader.sh

# GerVADER only seems to work inside the container if the path is absolute, therefore the path to outputmap.txt is replaced inside the code of the GerVADER library
RUN sudo vim -c "%s/outputmap.txt/\/home\/jovyan\/mt\/code\/research_question_4\/GerVADER\/outputmap.txt/g | wq" /home/jovyan/mt/code/research_question_4/GerVADER/vaderSentimentGER.py

RUN pip install pandas textblob-de numpy scikit-learn transformers cleantext wordcloud matplotlib pandarallel num2words cologne_phonetics
