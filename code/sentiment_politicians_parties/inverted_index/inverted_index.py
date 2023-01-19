import pandas as pd
from collections import Counter
import os.path

class InvertedIndex:
    def __init__(self, csv_file, text_column):
        self.csv_file = csv_file
        self.text_column = text_column
        self.document_list = []
        self.storage = dict()
        
        if self.csv_file.endswith(".csv") and os.path.isfile(self.csv_file):
            self.doc_corpus = pd.read_csv(self.csv_file)
        else:
            raise Exception("The provided csv path is incorrect, the file does not exist")
    
    def create(self):
        
        self.doc_corpus.apply(lambda row: self.document_list.append(Document(row.name, 
                                row[self.text_column])),axis=1)
        
        for document in self.document_list:
            self.add_document(document)
    
    def get_document(self, doc_id):
        return self.doc_corpus.iloc[doc_id]
        
    def search(self, word):
        if len(self.storage) > 0:
            if word in self.storage.keys():
                return list(Counter(self.storage[word]).items())
        else:
            print("Please create an index first")
    
    def add_document(self, document):
        
        tokens = self.get_tokens(document)
        
        for token in tokens:
            if token not in self.storage:
                self.storage[token] = []
            self.storage[token].append((document.get_id()))
    
    def get_tokens(self, document):
        return document.get_text().split(" ")

class Document:
    def __init__(self, doc_id, text):
        self.doc_id = doc_id
        self.text = text
    
    def get_text(self):
        return self.text
    
    def get_id(self):
        return self.doc_id