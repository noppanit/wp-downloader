from pymongo import MongoClient
from elasticsearch import Elasticsearch

client = MongoClient()
db = client.wp

posts = db.posts.find({})

es = Elasticsearch()
es.indices.delete(index='wp-posts', ignore=[400, 404])
es.indices.create(
    index='wp-posts',
    body={
        'settings': {
            # just one shard, no replicas for testing
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'mappings': {
                'post': {
                    'properties': {
                        'content': {
                            'type' :'string',
                            "index" : "analyzed"
                        }
                    }
                }
            },
            'analysis': {
                'analyzer': {
                    "standard": { 
                        "type": "standard", 
                        "stopwords": "_english_"
                    },
                    'wordpress_content': {
                        'type': 'custom',
                        'tokenizer': 'standard',
                        'filter': ['standard', 'lowercase', 'html_strip']
                        }
                    }
                }
            }
        },
    # Will ignore 400 errors, remove to ensure you're prompted
    ignore=400
)

for post in posts:
    es.index(index='wp-posts', doc_type='post', id=post['ID'], body={
        'content': post['content']
    })
