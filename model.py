import json


class HeroService:
    def __init__(self):
        self.db = load_db()
        self.messages = []

    def get_all_heroes(self,count=None):
        if count:
            return self.db[:count]
        return self.db[1:10]

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
        hero = {'id': len(self.db) + 1, 'name': name,
                'description': '', 'alterEgo': ''}
        self.db.append(hero)
        save_db(self.db)
        self.messages.append(f'Hero with name {name} added')

    def updateHero(self, hero):
        index = 0
        for h in self.db:
            if h['id'] == hero['id']:
                self.db[index] = hero
                save_db(self.db)
                self.messages.append(f"Hero with id {hero['id']} updated")
                return hero
            index = index + 1
        return None

    def remove_hero(self, id):
        index = 0
        for hero in self.db:
            if hero['id'] == id:
                del self.db[index]
                save_db(self.db)
                self.messages.append(f"Hero with id {id} deleted")
                return hero
            index = index + 1


def load_db():
    with open('heroes_db.json', 'r') as f:
        return json.load(f)


def save_db(db):
    with open('heroes_db.json', 'w') as f:
        json.dump(db, f)


# def get_hero(id):
#     for hero in db:
#         if hero['id'] == id:
#             messages.append(f'Hero with id {id} found')
#             return hero
#     return None

# def get_hero_by_name(query):
#     for hero in db:
#         if hero['name'].lower() == query.lower():
#             messages.append(f'Hero with name {query} found')
#             return hero
#     return None

# def addHero(name):
#     hero = {'id': len(db) + 1, 'name': name, 'description': '', 'alterEgo': ''}
#     db.append(hero)
#     save_db(db)
#     messages.append(f'Hero with name {name} added')


# def updateHero(hero):
#     index = 0
#     for h in db:
#         if h['id'] == hero['id']:
#             db[index] = hero
#             save_db(db)
#             messages.append(f"Hero with id {hero['id']} updated")
#             return hero
#         index = index + 1
#     return None


# def remove_hero(id):
#     index = 0
#     for hero in db:
#         if hero['id'] == id:
#             del db[index]
#             save_db(db)
#             messages.append(f"Hero with id {id} deleted")
#             return hero
#         index = index + 1

# db = load_db()

# messages = []