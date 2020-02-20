Notes for task 2
# Task
* Current code can successfully extract sentences from papers and classify whether a sentence is about experiments or not. So we need the next step, which is extracting numbers and their fields sentences.
* from "water boils at 100 Celsius", we want to extract that water's boiling point is 100 celsius
* rule-based relation extraction
- highly template languages -> manually crafted rules might be enough


# Acronyms
* Automatic content extraction (ACE) 
* Knowledge Base Population (KBP):  Knowledge Base Population is the task of taking an incomplete knowledge base (e.g., Freebase, or the structured information in Wikipedia infoboxes), and a large corpus of text (e.g., Wikipedia), and completing the incomplete elements of the knowledge base. That is, the computer has to "read" the text and get information out of it. Stanford has focused on two aspects of this task: 1.Slotfilling; 2. Entity Linking  
* Relation Extraction (RE): defined as the task of recognizing semantic relations between  pairs  of  terms  in  text,  has  received  renewed  interest in the "Web of Data" era,
* Resource Description Framework (RDF): a standard model for data interchange on the Web
* Name entity recognition (NER)

# Characteristics of Relations 
* Relations appear in a wide range of forms:   
    * Embedded constructs (one argument contains the other)   
        * within a single noun group: John’s wife     
        * linked by a preposition   
    * Formulaic constructs
        * Tarragona, Spain
        * Walter Cronkite, CBS News, New York
    * Longer-­‐range (‘predicate-­‐linked’) constructs
        * Fred lived in New York
        * Fred and Mary got married

# Workflow
* Generate sentences from current code.
    * tokeniznation
        * problem: abbreviation; the use of hyphenation;
        * Tools: Stanford; 
    * Part-of-Speech (POS) tagging
    * Named entity recognition
    * Parsing
* Relation extraction
* Transformations


# Library
* How to use Stanford CoreNLP API in NLTK
```
$ cd /home/lc/Git/stanford-corenlp-full-2018-10-05
$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
-preload tokenize,ssplit,pos,lemma,ner,parse,depparse \
-status_port 9000 -port 9000 -timeout 15000 & 
```
    Then in Python:

```
>>> from nltk.parse import CoreNLPParser
>>> parser = CoreNLPParser(url='http://localhost:9000')
# Parse tokenized text.
>>> list(parser.parse('What is the airspeed of an unladen swallow ?'.split()))
[Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

# Parse raw string.
>>> list(parser.raw_parse('What is the airspeed of an unladen swallow ?'))
[Tree('ROOT', [Tree('SBARQ', [Tree('WHNP', [Tree('WP', ['What'])]), Tree('SQ', [Tree('VBZ', ['is']), Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('NN', ['airspeed'])]), Tree('PP', [Tree('IN', ['of']), Tree('NP', [Tree('DT', ['an']), Tree('JJ', ['unladen'])])]), Tree('S', [Tree('VP', [Tree('VB', ['swallow'])])])])]), Tree('.', ['?'])])])]

# Neural Dependency Parser
>>> from nltk.parse.corenlp import CoreNLPDependencyParser
>>> dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
>>> parses = dep_parser.parse('What is the airspeed of an unladen swallow ?'.split())
>>> [[(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]
[[(('What', 'WP'), 'cop', ('is', 'VBZ')), (('What', 'WP'), 'nsubj', ('airspeed', 'NN')), (('airspeed', 'NN'), 'det', ('the', 'DT')), (('airspeed', 'NN'), 'nmod', ('swallow', 'VB')), (('swallow', 'VB'), 'case', ('of', 'IN')), (('swallow', 'VB'), 'det', ('an', 'DT')), (('swallow', 'VB'), 'amod', ('unladen', 'JJ')), (('What', 'WP'), 'punct', ('?', '.'))]]


# Tokenizer
>>> parser = CoreNLPParser(url='http://localhost:9000')
>>> list(parser.tokenize('What is the airspeed of an unladen swallow?'))
['What', 'is', 'the', 'airspeed', 'of', 'an', 'unladen', 'swallow', '?']

# POS Tagger
>>> pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
>>> list(pos_tagger.tag('What is the airspeed of an unladen swallow ?'.split()))
[('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'), ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]

# NER Tagger
>>> ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner').
>>> list(ner_tagger.tag(('Rami Eid is studying at Stony Brook University in NY'.split())))
[('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'STATE_OR_PROVINCE')]
```