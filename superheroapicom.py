"""
Модуль не работает. Либо проблемы сервера, либо ограничения сервера
"""
import requests
import urllib.parse as UP


class SuperHeroApiCom:
    url = 'https://superheroapi.com/api'
    super_hero_list = []
    with open('token.txt') as tk:
        token = tk.readline()

    def __init__(self, name):
        self.name = name
        self.id = self.get_superhero_id(name)
        # self.super_hero_list.append(self.get_superhero(name))

    def get_token(self):
        with open('token.txt') as tk:
            return tk.readline()

    def get_superhero_id(self, name: str):
        method = 'search'
        api_url = f"{self.url}/{self.token}/{method}/{UP.quote(name)}"
        print(api_url)
        responce = requests.get(api_url)
        for res in responce.json()['results']:
            if res['name'].lower() == name.lower():
                return res['id']
        return 1 #responce.json()['results']