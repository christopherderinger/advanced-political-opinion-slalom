# Political Opinion Analysis and Figure of Speech detection

This document aims to be the readme file of this masterthesis. It contains a section on the general folder structure, the setup which can be performed to run everything in a Docker container, a small description of all the notebooks and their purpose and a section that contains the citations.

## Folder structure

There are three important folders that are reachable from the main directory:

* \\code
* \\data
* \\plots

The **code** folder and the **data** folder have five subfolders each:

* \\protocol_obtainment
* \\research_question_1
* \\research_question_2
* \\research_question_3
* \\research_question_4

The **plots** subfolder only has four subfolders, one per research question:

* \\research_question_1
* \\research_question_2
* \\research_question_3
* \\research_question_4

The protocol_obtainment folders contain everything that is related to the protocol parser, the download of the protocols, the data itself once the download is completed and the procedure that is used to parse all the protocols. The **plots** folder and all the subfolders are created while the docker container is created, as it is not possible to save empty folders in github.

## Setup

On Unix-based systems only Docker is required, on Windows machines Git Bash should be installed as well so that Bash can be used.

As there are a lot of big datasets a separate folder was created containing all of these datasets. The urls to the datasets are contained in the notebooks. All of the datasets should be stored in a folder called **big_datasets**, this folder is then used as a volume for Docker, so that the files are not included in the container itself. There are also some additional files that were too big for github, they belong into the **data** folder and can be gathered by contacting me.

The **start_docker.sh** file contains the scripts that are executed for creating a container based on the image and for running the docker container with the mounted volume. There is a variable called **PATH_TO_BIG_DATASETS_FOLDER**, normally it should be possible to leave it as is, but if there are problems with mounting the **big_datasets** folder, or if it is located in another location, this variable needs to be adjusted.

If Docker is activated and configured in a way so that it can be used in the command line, the Docker container can be created and executed by calling the **start_docker.sh** script like the following:

```
bash start_docker.sh
```

This will create a Jupyter Lab environment which is hosted on localhost:8887, it contains all the notebooks and datasets.

## Programs

### Protocol Obtainment

One has to consider that all the protocols are downloaded from the web, therefore it is always possible that some changes occur. In case this happens the dataset which has been used throughout the thesis has been included as well, it has the name **political_statements_thesis.csv** and is located in the **data\\protocol_obtainment** folder. The **political_statements_thesis.csv** dataset should also be used if one tries to reproduce the results described in the thesis, therefore it is always the default dataset in each notebook where the political statements dataset is used. It contains additional information like the POS-tagged version of each statement, which were created using the RF-Tagger by Schmid and Laws [1].

The protocol obtainment can be separated into two parts. In the first part the protocols are being downloaded from the internet and stored as html files in the **data\\protocol_obtainment\\download** folder. 

For this the list of urls, which is stored in the file **data\\protocol_obtainment\\protocol_urls.txt** is used as an input. The procedure is stored in the **code\\protocol_obtainment\\scrape_and_convert_protocol.ipynb** notebook.

To parse the protocols, which are stored in a html format, a tiny library has been written, it is stored in the **code\\protocol_obtainment\\parser_lib** folder. This library is utilized in the **code\\protocol_obtainment\\protocol_parsing.ipynb** notebook, which implements the procedure where the parser is called on each html file that was previously downloaded.

The parsed html files are then moved into the done folder (**data\\protocol_obtainment\\done**) and the extracted data is stored into separate .csv files in the **data\\protocol_obtainment\\parsed** folder. These .csv files are then combined into one .csv file inside the previously mentioned procedure.

One additional tiny file is stored in the **data\\protocol_obtainment** folder, namely **collect_urls.js**, this tiny script has been used to gather all the urls that are stored in the **protocol_urls.txt** file. This script was written for an old version of the website which listed all the protocols of the national council, I think it would need to be updated if one wants to gather all the urls of the currently available protocols.

## Research Question 1

The code for the first research question is located in the **code\\research_question_1** folder. There are three notebooks:

* preparation_rq1.ipynb
* experiment_rq1.ipynb
* evaluation_rq1.ipynb

In addition there are two tiny packages:

* \\inverted_index
* \\wikipedia_wordclouds

The first one of the two tiny packages implements the logic for the inverted index, which is used to store the political statements. The second one implements the logic which is used to retrieve the article from Wikipedia using the Wikipedia API.

### Preparation

The **preparation_rq1.ipynb** notebook contains the preprocessing of the DeWaC German corpus and the preparation of the political statement dataset. In the end a simple example of the corpus-based approach is shown.

Two datasets are used at the beginning of the notebook. The first one is the **political_statements_thesis.csv** which was explained in the section on protocol obtainment. This dataset is used here as it is the original dataset that was used for the thesis, containing the statements that were extracted from the protocols and further fields. It is included as it is possible to create a new dataset as well, which could lead to different results.

The second dataset is the **speaker_party_unique.csv** which contains all the speakers that were found in the **political_statements_thesis.csv** with the party that they belong to and a unique name for each speaker. The unique name is used as a few speakers are appearing with slightly different styles of writing (for example sometimes a title is missing in one version).

In addition the **preprocessed_frequency_list.csv**, which is a shorter version of the DeWaC German corpus [2,3], was created using a few simple rules:

* Each word should contain letters only
* The word length has to be greater than 3
* The amount of unique characters per word has to be greater than 2 (to remove words like "aaaabbbb")
* Words with a count of less than 11 are removed, as some of them are still faulty cases


### Experiment

The **experiment_rq1.ipynb** notebook contains the code that was used to search the inverted index for the articles which contain the topic-related terms that were extracted from the Wikipedia article on the topic.

A small class called TechnicalTermsFinder is defined which contains the logic required to extract the topic-related terms (technical terms) from a text.

The WikiCorpusCreator from the tiny wikipedia_wordclouds package is used to get the article from Wikipedia. The topic-related terms are stored in .csv files.

After that the inverted index is initialized and the statements are retrieved based on the topic-related terms.

### Evaluation

The **evaluation_rq1.ipynb** notebook is used for creating the plots for the data analysis of research question 1. The notebook is configured in a way so that only the plots for one topic are created per execution. The plots are stored in the pdf format. 

The topic can be configured by changing the PATH_CHOSEN, TOPIC_CHOSEN, TERMS_CHOSEN and 
PDF_FOLDER_CHOSEN variables. 

This is possible by renaming the tuple that is assigned to these variables, per default ALL_CLIMATE is assigned, but it can be changed to ALL_FEMINISM and ALL_ASYL. The plots are stored in the **plots/research_question_1** folder in the respective subfolder.

## Research Question 2

The code for the second research question is located in the **code\\research_question_2** folder. There are three notebooks:

* experiments_rq2.ipynb
* evaluation_rq2.ipynb
* rftagger_runs.ipynb

The **rftagger_runs.ipynb** notebook contains the code that was used for applying the RFTagger to the dataset containing the political statements. It needs a bit of manual work as it was not possible to run it at all statements at once, so the batches need to be reconfigured after every run. The idea is to create batch files (in csv format), they are concatenated at the end. The RFTagger by Schmid and Laws [4] is executed in a subprocess according to the method described in this stackoverflow article by the user Sören Etler[5]. 

The **experiments_rq2.ipynb** notebook contains all the experiments that were performed in the context of the second research question. Again, the datasets from the real thesis are used if needed. Three different approaches for detecting comparative opinions and superlative opinions were implemented and compared. Two approaches for detecting opinions (without superlative and comparative) were compared.

The **evaluation_rq2.ipynb** notebook contains the code that was used to generate the plots regarding the data analysis that was performed on the results of the experiments and the annotations. All the plots are stored in the **plots\\research_question_2** folder in pdf format.

## Research Question 3

The code for the third research question is located in the **code\\research_question_3** folder. There are two notebooks:

* experiments_rq3.ipynb
* evaluation_rq3.ipynb

The **experiments_rq3.ipynb** notebook contains the algorithm that was implemented and tested for alliteration detection on two different datasets. The experiments themself are also included in this notebook.

The **evaluation_rq3.ipynb** notebook contains the code that was used for creating the plots for the data analysis of the results of the third research question.

The alliteration dataset, which was downloaded from Ulrich Mehners website [6] in January 2023 is contained in the **data\\research_question_3\\thesis** folder, as well as the manually annotated samples.

## Research Question 4

The code for the fourth research question is located in the **code\\research_question_4** folder. There are four notebooks:

* hyperbole_detection.ipynb
* hyperbole_feature_engineering.ipynb
* hyperbole_experiment_political.ipynb
* evaluation_rq4.ipynb

The **hyperbole_feature_engineering.ipynb** notebook contains the code that was used to compute the semantic features that were used by Troiano et al. [7], they are imageability, subjectivity, polarity, unexpectedness and emotional intensity. The notebook requires two additional downloads, which are directly started when executing the notebook. The first one is the PyTorch package, which is downloaded and installed in the first block. This package is included here as it led to problems if it was installed during the creation of the docker container. The second download is the mdebertav3-subjectivity-german model from huggingface.co, which is used to compute the subjectivity.

The **hyperbole_detection.ipynb** notebook contains the experiments that were conducted on the three different datasets (400 manually translated hyperboles, 400 machine translated hyperboles, all machine translated hyperboles) - The hyperboles were taken from the English HYPO-L dataset by Zhang et al. [8] and translated using Google Translate or manually. The datasets can be found in the **data\\research_question_4\\thesis** folder.

The **hyperbole_experiment_political.ipynb** notebook contains the experiment that was conducted on statements from a single protocol of the Austrian national council. The statements which were classified as being hyperbolic where then manually evaluated.

The **evaluation_rq4.ipynb** notebook contains the code that was used to generate the plots for the evaluation of the fourth research question.

## Citation

[1] Helmut Schmid and Florian Laws: Estimation of Conditional Probabilities with Decision Trees and an Application to Fine-Grained POS Tagging, _COLING 2008_, Manchester, Great Britain.

[2] Faaß, Gertrud, and Kerstin Eckart. "Sdewac–a corpus of parsable sentences from the web." _Language Processing and Knowledge in the Web: 25th International Conference, GSCL 2013, Darmstadt, Germany, September 25-27, 2013. Proceedings_. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013.

[3] Baroni, Marco, et al. "The WaCky wide web: a collection of very large linguistically processed web-crawled corpora." _Language resources and evaluation_ 43 (2009): 209-226.

[4] Schmid, Helmut, and Florian Laws. "Estimation of conditional probabilities with decision trees and an application to fine-grained POS tagging." _Proceedings of the 22nd International Conference on Computational Linguistics (Coling 2008)_. 2008.

[5] https://stackoverflow.com/questions/51295141/run-rftagger-in-python

[6]  https://www.mehner.info/html/alliteration.html

[7] Troiano, Enrica, et al. "A computational exploration of exaggeration." Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing. 2018.

[8] Zhang, Yunxiang, and Xiaojun Wan. "MOVER: Mask, over-generate and rank for hyperbole generation." arXiv preprint arXiv:2109.07726 (2021).


