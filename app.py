from crypt import methods
from flask import Flask, render_template, request, abort
from model import db, get_hero, remove_hero, get_hero_by_name, addHero, updateHero

app = Flask(__name__)


@app.route('/')
def index():
    heroes = db[1:5]
    return render_template('index.html', heroes=heroes, messages=["HeroService: fetched heroes"])


@app.route('/heroes')
def heroes():
    return render_template('heroes.html', heroes=db[1:10])


@app.route('/hero/<int:id>')
def hero_detail(id):
    hero = get_hero(id)
    return render_template('detail.html', hero=hero)


@app.route('/hero', methods=['POST'])
def add_hero():
    name = request.form.get('new_hero')
    addHero(name)
    return render_template('heroes.html', heroes=db[1:10])


@app.route('/hero/<int:id>', methods=['POST'])
def update_hero(id):
    hero = get_hero(id)
    hero['name'] = request.form.get('hero_name')
    hero['alterEgo'] = request.form.get('alterEgo')
    hero['description'] = request.form.get('description')

    updateHero(hero)
    return render_template('heroes.html',  heroes=db[1:10])


@app.route('/delete/<int:id>')
def delete_hero(id):
    remove_hero(id)
    return render_template('heroes.html', heroes=db[1:10])


@app.route('/search')
def search():
    hero = get_hero_by_name(request.args.get('query'))
    if hero:
        return render_template('detail.html', hero=hero)
    else:
        abort(404)
