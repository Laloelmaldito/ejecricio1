import requests
import json


def show():
    response= requests.get('https://randomuser.me/api')
    consulta = json.loads(response.text)
    if (consulta['results'][0]['gender'])=="female ":
        print("Datos del usuario (hombre)")
        print(consulta['results'][0]['name']['first'],"",consulta['results'][0]['name']['last'])
        print("Usuario: ",consulta['results'][0]['login']['username'])
        print("Contraseña: ",consulta['results'][0]['login']['password'])
    else:
        print("Datos del usuario (mujer)")
        print(consulta['results'][0]['name']['first'],"",consulta['results'][0]['name']['last'])
        print("Direccion: ",consulta['results'][0]['location']['street']['name'],", ", consulta['results'][0]['location']['street']['number'])
        print("Ciudad: ",consulta['results'][0]['location']['city'])

show()
