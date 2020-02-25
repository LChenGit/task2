relation extraction are sentence-based ensuring that larger block of texts like abstracts, whole documents, etc. are split into single sentences which are further split into tokens which serves as inputs used in the subsequent steps.
NER is complicated:
* each biomedical entity such as gene or protein might have several names and abbreviations.
* the same name can refer to different entities depending on the context.
* biomedical entities may have multi-word names which cause overlap of candidate names.

Current the state-of-the-art NER systems for biomedical texts in terms of F-scores varies from 78% to 90%.

Some common NER tools for biomedical text:
* BANNE
* Lingpipe
* GENIA Tagger
* ACELA

Techniques used in relation extraction systems can be divided into four groups:
* co-occurrence approaches.
* pattern-based approaches.
* rule-based approaches.
* machine learning-based approaches.

# NLP Pipeline
## Sentence splitting
Sentence splitting is the process of determining sentence boundaries. It splits input text such as abstracts and paragraphs into single sentences and is a prerequisite step for subsequent processes.

## Lexical processing
### Tokenization
Tokenization is the process of splitting the input sentence into a sequence of tokens. The tokenization process encounters many problems such as:
* abbreviation， in which words are not always separated from other tokens by white space; 
* the use of hyphenation： Cdc2-depedent VS DNA-binding
* additional challenges due to domain-specific terminology, nonstandard punctuation, and orthographic patterns: e.g., 12.0 +/- 1.6%, and alpha-galactosyl-1,4-beta-galactosyl-1,4-glucosyl.
Currently, tokenization tools for biomedical text achieve an accuracy of 95%.


### Stemming
Stemming (morphological analysis) is the process of mapping various syntactic forms of a word into its canonical base form. Stemming is a standard technique which is commonly used to create the bags-of-words (BOW) features in many relation extraction systems.

## Syntactic processing
Syntactic processing reveals structural relationship between groups of words at the sentence level.

### POS tagging
POS tagging is the first step of syntactic analysis and is essential to cope with the various lexico-syntactic ambiguity forms of words. Here is an Alphabetical list of part-of-speech tags used in the Penn Treebank Project:https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html. The POS tagger receives input as a sequence of words of a sentence, and assigns POS tags to the words of that sentence. For example, the sentence "water boils at 100 Celsius" returns the POS result:
```
water: NN (Noun, singular or mass )
boils: VBZ (Verb, 3rd person singular present )
at: IN (Preposition or subordinating conjunction )
100: CD (Cardinal number )
Celsius: NNP (Proper noun, singular )
```
This step identifies the grammatical form of a word based on the word itself and its surrounding context. However, we need to re-train the POS taggers on our topic corpora in order to achieve a good accuracy level. Some biomedical text mining corpora can be found at https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwjZ26eV-K_oAhXXVc0KHYqpA8gQygQwAXoECAcQCA&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBiomedical_text_mining%23Corpora&usg=AOvVaw2VA__9KdXshcQlJwVft1Bh.

#### Shallow parsing
Shallow parsing is the process of combining sequences of words into syntactic groups such as noun and verb phrases using both lexical and POS sequence information. 

### Full parsing
Full parsing is the process of analyzing syntactic structure of a sentence with the most elaborated details. It accumulates the output of all previous steps such as POS tags, phrases (chunks) and adds more information about structural dependencies between phrases. The full parsing output of a given sentence is a parse tree which reveals the relationship of subject-predicate-object of that sentence.


## Commonly used toolbox for above topic
* Sentence splitter
    * Lingpipe 
    * Enju
* Tokenization
    * OpenNLP
    * Stanford
    * Lingpipe
* POS tagger
    * Enju
    * OpenNLP
    * Stanford
    * Lingpipe
* Shallow parser
    * OpenNLP
    * Illinois Chunker
    * Lingpipe
* Full parser
    * Stanford
    * Charniak–Lease reranking
    * OpenNLP
    * Enju