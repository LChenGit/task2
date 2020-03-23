#%%
import sys
import os
from stanfordcorenlp import StanfordCoreNLP
from nltk.parse.stanford import StanfordParser
import logging
import json
from collections import defaultdict

#%%
class StanfordNLP:
    '''defines api from stanfold nlp
    '''
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

#%%
def sen_process(text):
    '''process just on sentence
    ---
    Return 
    Parsing result
    '''
    sNLP = StanfordNLP()
    print ("Annotate:", sNLP.annotate(text))
    print ("POS:", sNLP.pos(text))
    print ("Tokens:", sNLP.word_tokenize(text))
    print ("NER:", sNLP.ner(text))
    print ("Parse:", sNLP.parse(text))
    print ("Dep Parse:", sNLP.dependency_parse(text))
    return sNLP.parse(text)

#%%
def sen_reader(txt_file):
    with open(txt_file) as f:
        line = f.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line=f.readline()
            cnt +=1
        f.close()
#%%
def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1
#%%
def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

#%%
def main():
    filepath = "sen_pdf1.txt"
    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
    bag_of_words = {}
    with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
    sorted_words = order_bag_of_words(bag_of_words, desc=True)
    print("Most frequent 10 words {}".format(sorted_words[:10]))
#%%
def test1():
    filepath = "sen_pdf1.txt"
    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
    bag_of_words = {}
    with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
    sorted_words = order_bag_of_words(bag_of_words, desc=True)
    print("Most frequent 10 words {}".format(sorted_words[:10]))



def check_triple():
    pass
#%%
if __name__ == "__main__":
    # main()
    sen = "After testing 1000 times, we found water boils at 100 degree"
    # dependencyParse = sen_process(sen)
    # print(type(dependencyParse))
    # for (i, begin, end) in dependencyParse:
    #     print (i, '-'.join([str(begin), token[begin-1]]), '-'.join([str(end),token[end-1]]))
    sNLP = StanfordNLP()
    pos = sNLP.pos(sen)
    candidate_relation=[]
    for i in range(len(pos)):
        if ('CD' in pos[i]):
            candidate_relation.append(i)


