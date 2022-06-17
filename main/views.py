import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import search_posts

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """Главная страница"""
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    """Поиск постов"""
    logging.info("Поиск постов")
    query = request.args.get('s')
    try:
        posts = search_posts(query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "<h1>File not found</h1>"
    except JSONDecodeError:
        return "<h1>File not open</h1>"
    return render_template('post_list.html', query=query, posts=posts)