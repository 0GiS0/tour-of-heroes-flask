import json


def load_db():
    with open('heroes_db.json', 'r') as f:
        return json.load(f)


def save_db(db):
    with open('heroes_db.json', 'w') as f:
        json.dump(db, f)


def get_hero(id):
    for hero in db:
        if hero['id'] == id:
            return hero
    return None

def get_hero_by_name(query):
    for hero in db:
        if hero['name'].lower() == query.lower():
            return hero
    return None

def addHero(name):
    hero = {'id': len(db) + 1, 'name': name}
    db.append(hero)
    save_db(db)

def remove_hero(id):
    index = 0
    for hero in db:
        if hero['id'] == id:
            del db[index]
            save_db(db)
            return hero
        index = index + 1

db = load_db()
