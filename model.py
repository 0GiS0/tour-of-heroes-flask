import json

class HeroService:
    def __init__(self):
        self.messages = []
        with open('heroes_db.json') as f:
            self.db = json.load(f)

    def get_all_heroes(self):
        self.messages.append('Heroes loaded from local JSON file')
        return self.db

    def get_hero(self, id):
        for hero in self.db:
            if hero['id'] == id:
                self.messages.append(f'Hero with id {id} found')
                return hero
        return None

    def get_hero_by_name(self, query):
        for hero in self.db:
            if hero['name'].lower() == query.lower():
                self.messages.append(f'Hero with name {query} found')
                return hero
        return None

    def addHero(self, name):
        new_hero = {"id": len(self.db) + 1, "name": name, "description": "", "alterEgo": ""}
        self.db.append(new_hero)
        self.messages.append(f'Hero with name {name} added')

    def updateHero(self, hero):
        for i, h in enumerate(self.db):
            if h['id'] == hero['id']:
                self.db[i] = hero
                self.messages.append(f"Hero with id {hero['id']} updated")
                break
