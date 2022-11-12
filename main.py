# import time
# from superheroapicom import SuperHeroApiCom
from superheroapi import SuperHeroApi
# import urllib.parse as UP

if __name__ == '__main__':
    heroes_list = ['Hulk', 'Captain america', 'Thanos']
    hero_dict = {}
    for hero in heroes_list:
        hero_dict.update({hero.lower().replace(" ", "_"): SuperHeroApi(hero)})

    # Вариант 1
    print(SuperHeroApi.megamind['name'])

    # Вариант 2
    def megamind(hero_dict):
        intelligence = []
        for hero, data in hero_dict.items():
            intelligence.append(data.intelligence)
        intelligence.sort()
        megamind = intelligence.pop()

        for hero, data in hero_dict.items():
            if megamind == data.intelligence:
                print(data.name)

    megamind(hero_dict)

