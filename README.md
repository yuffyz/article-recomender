# Simple Article Recommendation Engine


## Introduction

This program is a simple article recommendation engine that recommend the top 5 most relevant articles given an article you're reading. 

The program makes use of word vector and euclidean distances. 


## Dataset 

The [BBC News](http://mlg.ucd.ie/datasets/bbc.html) dataset contains 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. 


## How the program works

The similarity and relationships between articles are modeled based on word vector. I tested with both the 300 dimension Stanford [GloVe](https://nlp.stanford.edu/projects/glove/) trained on 2014 Wikipedia and the a context free model [BERT](https://github.com/google-research/bert). 

For GloVe, each word is represented as a vector of 300-floating point mumbers. This vector captures the meaning of the word regarding other words within its pretrained corpus (the 2014 Wikipedia corpus), and is learned from a neural network that captures the word-word co-occurrence probabilities among the 300-d space. 

For each document, we calculate the centroid of the document's cloud of word vectors by dividing the sum of the vectors by the number of words in the article. The distances between each articles are measured by the euclidean distance between their centroid. 


## How to run the program 

The program reads in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

The web server displays a list of BBC articles for URL http://localhost:5000 (testing) and the IP xxx hosted on AWS. Clicking on any articles of this page will redirect you to an article page that shows the text of the article as well as a list of five recommended articles. 

## Source 

This project is built with the guidance of the [MSDS692 Data Acquisition](https://github.com/parrt/msds692) course of University of San Francisco

