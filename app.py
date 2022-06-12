from flask import Flask, render_template,request,abort
from model import db, get_hero, remove_hero,get_hero_by_name

app = Flask(__name__)


@app.route('/')
def index():
    heroes = db[1:5]
    return render_template('index.html', heroes=heroes)


@app.route('/heroes')
def heroes():
    return render_template('heroes.html', heroes=db[1:10])


@app.route('/hero/<int:id>')
def hero_detail(id):
    hero = get_hero(id)
    return render_template('detail.html', hero=hero)


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