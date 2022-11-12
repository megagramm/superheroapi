import requests


class SuperHeroApi:
    url = 'https://akabab.github.io/superhero-api/api/'
    all_heroes = {}
    megamind = {'name': "", 'value': 0}  # Самый умный супер герой

    def __init__(self, name: str):
        self.name = name
        if len(SuperHeroApi.all_heroes) == 0:
            SuperHeroApi.all_heroes = self.get_all_heroes()
        self.id = self.get_id_by_name(name)
        self.intelligence = self.get_intelligence_by_id(self.id)
        if SuperHeroApi.megamind['value'] < self.intelligence:
            SuperHeroApi.megamind['name'] = self.name
            SuperHeroApi.megamind['value'] = self.intelligence

    def get_intelligence_by_id(self, id):
        for hero in self.all_heroes:
            if id == hero['id']:
                return hero['powerstats']['intelligence']

    def get_id_by_name(self, name: str):
        for hero in self.all_heroes:
            if name.lower() == hero['name'].lower():
                return hero['id']

    def get_all_heroes(self):
        method = 'all.json'
        api_url = f"{self.url}{method}"
        responce = requests.get(api_url).json()
        return responce


if __name__ == '__main__':
    ...
