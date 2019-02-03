# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys


app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    alist = []
    for article in articles:
        title = article[1]
        url = "/article/"+article[0]
        alist.append({"title":title, "url":url})

    return render_template('articles.html', articles = alist)


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    current_article = topic + "/" + filename 
    rec = recommended(article, articles, 5)

    for i in articles:
    	if i[0] == current_article:
            current_article = i
    		break 
    return render_template('article.html', rec_articles=rec, article = current_article)



# initialization
i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]


"""
gloves: a dictionary mapping a word to its 300d vector. 
articles: a list of list, contains the fully-qualified file name, the article title,
the text without the title, and the word vector computed from the text
without the title
"""
gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)
