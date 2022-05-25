import requests
import json


def georeference(n):
    response= requests.get('https://jsonplaceholder.typicode.com/users')
    consulta = json.loads(response.text)
    resultadito=[]
    resultadito.append(consulta[n]['name'])
    resultadito.append(consulta[n]['address']['geo']['lat'])
    resultadito.append(consulta[n]['address']['geo']['lng'])
    return resultadito

print(georeference(1))

