import requests

from pymongo import MongoClient
client = MongoClient()
db = client.wp

url = 'https://public-api.wordpress.com/rest/v1.1/sites/73194874/posts'

params = {'number': 100}
offset = 0

while True:
    response = requests.get(url, params=params).json()
    found = response['found']
    posts = response['posts']       
    
    db.posts.insert_many(posts)
    
    print('Inserted {number} posts'.format(number=len(posts)))
    offset += 100
    if offset >= found:
        break
    
    print('We have {left} posts left to go'.format(left=found-offset))     
    params['offset'] = offset
