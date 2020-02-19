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
    * Part-of-Speech (POS) tagging
    * Named entity recognition
    * Parsing
* Relation extraction
* Transformations
