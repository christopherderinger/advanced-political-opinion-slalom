from bs4 import BeautifulSoup
import re
import cleantext
import os.path
import pandas as pd

class ProtocolParser:
    def __init__(self, path):
        self.res = None
        self.soup = None
        if self._is_path_valid(path):
                with open(path) as f:
                    self.soup = BeautifulSoup(f,'html.parser')
                    self.soup = BeautifulSoup(self.soup.prettify())
        else:
            print("Please provide a path to a valid html")
    
    def parse(self):
        if self.soup == None:
            print("Please reinitialize the parser using a valid path")
            return
        else:
            word_sections = self._get_word_sections()

            indices_speeches = self._get_indices_of_speeches(word_sections)

            speeches = [word_sections[index] for index in indices_speeches]

            self._drop_i_tags_from_speeches(speeches)
            self._unwrap_sub_tags_in_speeches(speeches)

            self.res = self._get_dict_speakers_speeches(speeches)
    
    def export(self, path):

        if self.res == None:
            print("Please run parse() first")
            return 

        if not path.endswith(".csv"):
            print("Only .csv files are supported")
        else:
            csv_rows = []

            if len(self.res.keys()) > 0:

                for key in self.res.keys():
                    entry_list = self.res[key]

                    for entry in entry_list:
                        csv_rows.append((key,entry))

            
            else:
                print("There are not values to export")
                return

            df = pd.DataFrame(csv_rows, columns=["speaker", "speech"])

            df.to_csv(path, index=False)

    def _is_path_valid(self, path):
        return path is not None and path.endswith(".html") and os.path.isfile(path)

    def _get_word_sections(self):
        return self.soup.select('div[class^=WordSection]')
    
    def _get_indices_of_speeches(self, word_sections):
    
        index = 0
        indices = []
    
        while index < len(word_sections):
        
            if(self._contains_speech(word_sections[index])):
                indices.append(index)
        
            index += 1
    
        return indices
    
    # RB might stand for begin of speech (Redebeginn)
    def _contains_standardRB(self, word_section):
        return word_section.find("p",class_="StandardRB") != None

    # RE might stand for end of speech (Redeende)
    def _contains_standardRE(self, word_section):
        return word_section.find("p",class_="StandardRE") != None

    def _contains_speech(self, word_section):
        return self._contains_standardRB(word_section) and self._contains_standardRE(word_section)

    def _get_speech(self, word_section):
        if(self._contains_speech(word_section)):
            return word_section.get_text()
        else:
            return None
    
    # these seem to contain Zwischenrufe etc. only
    def _drop_i_tags_from_speeches(self, speeches):
        for speech in speeches:
            i_tags = speech.find_all("i")
            
            for i_tag in i_tags:
                i_tag.decompose()

    # is used in CO2 for example (subscript text)
    def _unwrap_sub_tags_in_speeches(self, speeches):
        for speech in speeches:
            sub_tags = speech.find_all("sub")
            
            for sub_tag in sub_tags:
                sub_tag.unwrap()
    # has a problem with numbers, they alway have this form: '2000texts' instead of 
    # '2000 texts' the space is missing
    def _clean_text(self, text):
        text_clean = self._clean_text_with_certain_options(text)
    
        # replace some patterns that might be in the text. The first pattern is used to
        # 'save' the word CO2. This is harder to get because the 2 is placed between <sub> tags
        text_clean = text_clean.replace("\n \n 2\n \n ","2").replace("\n \n "," ").replace("\n \n\n","")

        # a few more replacements of patterns that show up frequently
        text_clean = text_clean.replace("\xa0"," ").replace("\xad","").replace("\n"," ").replace("–","")

        text_clean = self._clean_text_with_certain_options(text_clean)

        return text_clean
    
    def _clean_text_with_certain_options(self, text):
        return cleantext.clean(text,clean_all=False, extra_spaces=True, stemming=False,
                           stopwords=False, lowercase=False, numbers=False, punct=False)
    
    def _get_dict_speakers_speeches(self, speeches):
    
        res = {}

        for speech in speeches:
            speaker = self._find_speaker(speech)
            
            if speaker not in res.keys():
                res[speaker] = []
            
            contents = self._get_contents(speech)
            
            res[speaker].extend(contents)
        
        return res

    def _find_speaker(self, speech):
        speaker_unclean = self._find_speaker_unclean(speech)
    
        return self._clean_text(speaker_unclean)
    
    def _find_speaker_unclean(self, speech):
        try:
            pattern_1 = speech.find_all("p",{"class": "StandardRB"})[0].find_all("span")[1].get_text()

            length_check = pattern_1.replace(" ","")
            
            if pattern_1 != "\n\n" and len(length_check) > 10:
                return pattern_1
        except:
            print("pattern 1 did not work")

        return speech.find_all("p",{"class": "StandardRB"})[0].find("a").get_text()
    
    def _get_contents(self, speech):
        # remove the first and last paragraph as they always contain numbers
        rb_tags = speech.find_all("p",{"class":"RB"})
        re_tags = speech.find_all("p",{"class":"RE"})
        
        for tag in rb_tags:
            tag.decompose()
        
        for tag in re_tags:
            tag.decompose()
        
        contents = []
        
        for tag in speech.find_all("p"):
            text = tag.get_text()
            if len(text) > 10:
                contents.append(self._clean_text(text))
        
        # remove speaker from first paragraph
        if ":" in contents[0][:-150 or None]:
            contents[0] = contents[0].split(":",1)[1][1:]
        
        return contents

