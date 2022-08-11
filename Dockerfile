FROM jupyter/minimal-notebook
USER root
ADD ./code /home/jovyan/mt/code
ADD ./data /home/jovyan/mt/data
RUN pip install pandas cologne-phonetics
