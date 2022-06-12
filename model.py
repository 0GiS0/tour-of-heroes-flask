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


db = load_db()
