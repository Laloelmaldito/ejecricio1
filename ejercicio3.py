import requests
import json

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consultita = json.loads(response.text)
    dic = {'comentario' : consultita[n]['body']}
    return dic

print(comment(4))
