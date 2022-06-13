import requests
import os

class HeroService:
    def __init__(self):
        self.messages = []
        # self.apiUrl = 'http://192.168.0.53:8080/api/hero'
        self.apiUrl = os.environ['API_URL']

    def get_all_heroes(self):
        heroes = requests.get(self.apiUrl)
        self.messages.append('Heroes loaded from API')
        return heroes.json()

    def get_hero(self, id):
        hero = requests.get(f'{self.apiUrl}/{id}')
        self.messages.append(f'Hero with id {id} found')
        return hero.json()

    def get_hero_by_name(self, query):
        for hero in self.db:
            if hero['name'].lower() == query.lower():
                self.messages.append(f'Hero with name {query} found')
                return hero
        return None

    def addHero(self, name):
        requests.post(self.apiUrl, json={"name": name, "description": "", "alterEgo": ""})
        self.messages.append(f'Hero with name {name} added')

    def updateHero(self, hero):
        id = hero['id']
        hero = requests.put(f'{self.apiUrl}/{hero["id"]}', json=hero)
        self.messages.append(f"Hero with id {id} updated")
       

    def remove_hero(self, id):
        requests.delete(f'{self.apiUrl}/{id}')
        self.messages.append(f"Hero with id {id} deleted")