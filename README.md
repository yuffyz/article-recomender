# Simple Article Recommendation Engine


## Introduction

This program is a simple article recommendation engine that recommend the top 5 most relevant articles given an article you're reading. The algorithm makes use of word vector (GloVe, BERT) and euclidean distances. 


## Dataset 

The [BBC Dataset](http://mlg.ucd.ie/datasets/bbc.html) contains 2225 documents from the BBC news website corresponding to stories in five topical areas from 2004-2005. By default, the full filename will be `bbc/topic/filename.txt` (this format is coded into doc2vec.py). 


## How the program works

The similarity and relationships between articles are modeled based on word vector. I tested with both the 300 dimension Stanford [GloVe](https://nlp.stanford.edu/projects/glove/) trained on 2014 Wikipedia and the 12-layer Google [BERT](https://github.com/google-research/bert) model (needs to be tuned on +12GB RAM GPU). 

For GloVe, each word is represented as a vector of 300-floating point mumbers. This vector captures the meaning of the word regarding other words within its pretrained corpus (the 2014 Wikipedia corpus), and is learned from a neural network that captures the word-word co-occurrence probabilities among the 300-d space. 

For each document, I calculate the centroid of this document's cloud of word vectors by dividing the sum of the vectors by the number of words in the article. This is equivalent to normalize the document based on the pretrained word2vec. The distance between two article is measured by the euclidean distance between their centroid. Then, I sorted the distances to return the top 5 articles.  

I built a web server with Flask to display the result. Clicking on any articles page will redirect you to an article page that shows the text of the article, and a list of five recommended articles. 


## How to run the program 

The program reads in a database of word vectors and a corpus of text articles, then organize them into a table (list of lists) for processing.

To run the program, download [BBC Dataset](http://mlg.ucd.ie/datasets/bbc.html) to the data folder, then download the pretrained 300-d [GloVe](https://nlp.stanford.edu/projects/glove/) to the word2vec folder. 

File structure will look like this: 
```
├── doc2vec.py
├── server.py
└── data
    └── bbc/
└── word2vec
    └── glove.6B.300d.txt
└── templates
    ├── article.html
    └── articles.html
```

Then in your terminal, run: 

```bash
$ python server.py word2vec/glove.6B.300d.txt data/bbc
```

Next, go to `http://localhost:5000/`, you will see the web server on your local host. 

To launch this server on AWS, install [gunicorn](https://gunicorn.org/).  


## Reference

[BERT FineTuning with Cloud TPUs](https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb)


## Credit 

This project is built with the guidance of [MSDS692 Data Acquisition](https://github.com/parrt/msds692) course. Thanks Prof. Parr for sharing the materials. 
