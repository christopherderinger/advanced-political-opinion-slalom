FROM jupyter/minimal-notebook
USER root

ADD ./code /home/jovyan/mt/code
ADD ./data /home/jovyan/mt/data
ADD ./scripts /home/jovyan/mt/scripts

# curl is needed if the embeddings are not existing yet
RUN apt-get update && apt-get install -y curl unzip

RUN /home/jovyan/mt/scripts/hyperbole_detection/install_gervader.sh

# Download the GloVe embeddings and the Word2Vec embeddings if they are not existing yet
RUN /home/jovyan/mt/scripts/hyperbole_detection/check_glove.sh 
RUN /home/jovyan/mt/scripts/hyperbole_detection/check_word2vec.sh 

RUN pip install pandas cologne-phonetics beautifulsoup4 textblob-de numpy scikit-learn
