import feedparser
from flask import Flask
from flask import render_template

app=Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition.rss',
'fox': 'http://feeds.foxnews.com/foxnews/latest',
'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route('/')
@app.route('/<publication>')
def bbc(publication="bbc"):
    if publication:
        #return get_news(publication)
        #return get_news1(publication)
        return get_news2(publication)

    else:
        return "this is test"

def get_news(publication):
    feed=feedparser.parse(RSS_FEEDS[publication])
    first_article=feed['entries'][0]
    return render_template("home.html",
        title=first_article.get("title"),
        published=first_article.get("published"),
        summary=first_article.get("summary"))
def get_news1(publication):
    feed=feedparser.parse(RSS_FEEDS[publication])
    first_article=feed['entries'][0]
    return render_template("home1.html", article=first_article)

def get_news2(publication):
    feed=feedparser.parse(RSS_FEEDS[publication])
    articles=feed['entries']
    return render_template("home2.html", articles=articles)


if __name__=='__main__':
    app.run(port=5000,debug=True)