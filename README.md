# Task 2 Project

This repo is for task 2 of relation extraction problem

## Files in the repo
### review.md
literatury review of the RE (done)

### Notes
notes for concept and coding

### main.py
main entry of code
#### TO RUN
```
python main.py
```
require stanfordcorenlp

## pipeline
1. PDF files from Mendeley database
2. Sentence splitting
3. Tokenizing
4. POS
5. Name entity recognition
6. Parsing
7. Relation extraction
So far, step 1 & 2 are finished by previous project. We apply the stanfordcorenlp api to do step 3-6, and focus on the RE.
We are using rule-based approaches and manually define the rules. we save all sentences from one PDF file in the database for test, namely 'sen_pdf1.txt' in the repo.
Parsing results are transfered as input of step 7 after step 1~6 

## RE
### Negation check
a relation is said to be negated if no node in the candidate relation contains Number.

### Effector-effectee detection
* effector of the relation: the name entity appearing first in the extracted relation, i.e. with the smaller sentence position
* The roles are switched if some form of passive construct is detected

### Enumeration resolution
Noun phrase chunks connected to each other by a and, or, nn, det, or dep dependency form an enumeration. If a noun phrase chunk contains more than one protein name, these are considered to describe alternative agents/targets. 

### Restricting candidate relations to focus domain
The words contained in candidate relations are checked against a set of relation restriction terms.
* focus domain corpora will be generated by:
    * scanning our database and checking noun frequency
    * and check with public corpora in this field
    * we can add a filter in NER

### Rules:
* Negation check
* find triple {NN VB CD} in a relation


## Problem & TODO
1. need more rules 
2. corpora
3. try dependency path
4. train the parser?
