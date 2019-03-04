

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
import psycopg2
from sqlalchemy.sql.expression import func


from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base



from textblob import TextBlob

import reddit.collection_app.schema as sc
from reddit.collection_app.insert_pgdb import insert_pgdb
from reddit.collection_app.cfg import meta, db


Session = sessionmaker(bind = db)


session = Session()
# search2 = session.query(Content).filter_by(reviewid = 16).first()

def sentiment(table):
    
    if not table in meta.tables:
        sc.create_table_nlp(table)



    # for instance in session.query(sc.RedditHot).filter(func.length(sc.RedditHot.body) > 7000):

    for instance in session.query(sc.RedditHot):
        if instance.title:
            body_blob = TextBlob(instance.title)
            data ={
                "post_id" : instance.post_id,
                "sentiment_polarity": body_blob.sentiment.polarity,
                "sentiment_subjectivity": body_blob.sentiment.subjectivity,
                "title": instance.title
            }
            print(body_blob.sentiment.polarity)
            try:
                insert_pgdb('django1', table, data)
            except:
                print('repeated value')

    # search2 = session.query(sc.RedditHot).filter(func.length(sc.RedditHot.body) > 1000).first()

    # print(search2)
    # search_blob = TextBlob(search2.body)
    # print("raw version sentiment %s" % str(search_blob.sentiment))


# def spacy_sentiment(table):
#     if not table in meta.tables:
#         sc.create_table_nlp(table)
