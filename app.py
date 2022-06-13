from flask import Flask, render_template, request, abort
from model import HeroService

app = Flask(__name__)
heroService = HeroService()


@app.route('/')
def index():
    return render_template('index.html', heroes=heroService.get_all_heroes()[1:5], messages=heroService.messages)


@app.route('/heroes')
def heroes():
    return render_template('heroes.html', heroes=heroService.get_all_heroes(), messages=heroService.messages)


@app.route('/hero/<int:id>')
def hero_detail(id):
    return render_template('detail.html', hero=heroService.get_hero(id), messages=heroService.messages)


@app.route('/hero', methods=['POST'])
def add_hero():
    name = request.form.get('new_hero')
    heroService.addHero(name)
    return render_template('heroes.html', heroes=heroService.get_all_heroes(), messages=heroService.messages)


@app.route('/hero/<int:id>', methods=['POST'])
def update_hero(id):
    hero = heroService.get_hero(id)
    hero['name'] = request.form.get('hero_name')
    hero['alterEgo'] = request.form.get('alterEgo')
    hero['description'] = request.form.get('description')

    heroService.updateHero(hero)
    return render_template('heroes.html',  heroes=heroService.get_all_heroes(), messages=heroService.messages)


@app.route('/delete/<int:id>')
def delete_hero(id):
    heroService.remove_hero(id)
    return render_template('heroes.html', heroes=heroService.get_all_heroes(), messages=heroService.messages)


@app.route('/search')
def search():
    hero = heroService.get_hero_by_name(request.args.get('query'))
    if hero:
        return render_template('detail.html', hero=hero, messages=heroService.messages)
    else:
        abort(404)

@app.route('/clear_messages')
def clear_messages():
    heroService.messages.clear()
    return render_template('heroes.html', heroes=heroService.get_all_heroes(), messages=heroService.messages)