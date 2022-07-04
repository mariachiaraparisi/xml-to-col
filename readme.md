# xml-to-col
This repository contains a Python script, called `xml-to-col`, that converts lemmatised XML files to TSV files compliant with the Computational Natural Language Learning format (CoNLL). 

## Source corpora 
I have used this script to convert two high-quality lemmatised corpora: 

1. Celano, G. Lemmatized Ancient Greek Texts 1.2.5: https://github.com/gcelano/LemmatizedAncientGreekXML

This corpus has been built from the following repositories: 
- https://github.com/PerseusDL/canonical-greekLit/releases/tag/0.0.236
- https://github.com/OpenGreekAndLatin/First1KGreek/releases/tag/1.1.1802 

2. Clérice, T. (2021). Corpus Latin antiquité et antiquité tardive lemmatisé (0.1.3) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.4337145 : https://github.com/lascivaroma/latin-lemmatized-texts 

This corpus has been built from the following repositories: 
- https://github.com/PerseusDL/canonical-latinLit 0.0.843
- https://github.com/OpenGreekAndLatin/csel-dev 1.0.211
- https://github.com/OpenGreekAndLatin/Latin 1.10.0
- https://github.com/lascivaroma/digiliblt 0.0.64
- https://github.com/lascivaroma/priapeia 1.1.18
- https://github.com/lascivaroma/additional-texts 1.0.192

## How it works 
This script is designed to parse the XML files contained in the lemmatised corpora, and to organise them into columns. The columns report information in the following order: 
- word form, 
- lemma, 
- PoS tag,
- the remaining morphological information provided in the lemmatised file (e.g. case, declinations, etc.),
- lemma ID number (ifted from a list of lemmas used to disambiguate lemmas during the lemmatisation process).

The lemmatised corpora do not share the same XML structure (i.e. the so-called element tree). Thus the script first recognises the structure of the input file (coming from either from lemmatised corpus 1 or 2 above), then the script extracts the relevant information, creating the TSV files and writing them to an output folder. 

## Why
`xml-to-col` creates TSV files, parsing the information of the lemmatised Ancient Greek and Latin corpus, to be further converted into a specific XML-based format for linguistic annotations, namely FoLiA (https://github.com/proycon/folia/). This format includes annotations of corpora at a token level by specifying e.g. word form, lemma and PoS. The FoLia XML files can be then uploaded in AutoSearch (https://portal.clarin.nl/node/4222), developed by Clarin NL), an environment that allows users to upload and search their corpora. 

## Example
A sample from a TSV file created by the script is below, which is a excerpt from the parsed lemmatised file of Aristotle’s *Prior Analytics*.

```
ΑΝΑΛΥΤΙΚΩΝ			n	-s---mv-	533057
ΠΡΟΤΕΡΩΝ			n	-s---mv-	533058
Α			-	-------	213596
.		.	u	--------	
Πρῶτον	Πρῶτος		n	-s---ma-	207925
εἰπεῖν	λέγω	εἶπον	v	--ana---	8447
περὶ		περί	r	--------	
τί	τίς		p	-s---na-	7761
καὶ	καί		d	--------	13
τίνος			p	-s---mg-	40877
ἐστὶν	εἰμί		v	3spia---	4883
ἡ		ὁ	l	-s---fn-	1317
σκέψις	σκέψις		n	-s---fn-	64262
,		,	u	--------	
ὅτι	ὅτι2	ὅτι	c	--------	15113
περὶ		περί	r	--------	
ἀπόδειξιν	ἀπόδειξις		n	-s---fa-	19397
```

E.g. on the last line, the information is parsed into CoNLL format: word form (ἀπόδειξιν, meaning *demonstration*), lemma (ἀπόδειξις), part of speech (*n*, noun), other morphological information (*s*, singular; *f*, feminine; *a*, accusative), and lemma ID (*19397*). The ‘-’ indicates information which is not applicable to the word form, e.g. information of  verbs such as tense and mood cannot be applied to a noun.
