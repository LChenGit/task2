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