from pymongo import MongoClient
from elasticsearch import Elasticsearch
import pprint

client = MongoClient()
db = client.wp
post = db.posts.find_one()

es = Elasticsearch()

search_result = es.search(index="wp-posts", body= {
    "query" : {
        "match_all": {}
    }
})


text = 'ra'
suggDoc = {
           "entity-suggest" : {
                'text' : post['content'],
                "completion" : {
                    "field" : "content"
                }
            }
        }

#result = es.suggest(body=suggDoc, index="wp-posts", params=None)

result = es.suggest(index="wp-posts", body={"my_suggestion": {"text": post['content'], "term": {"field":"content" }}})

pp = pprint.PrettyPrinter(indent=4)
suggestions = result['my_suggestion']

pp.pprint(search_result)

#for suggestion in suggestions:
#    print suggestion['text']

