import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import write_post, saved_picture

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route('/post')
def page_post():
    """Страница с формой Добавить пост"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def page_loader_post():
    """Сохранение картинки и комментариев к посту в файл"""
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return "<h1>Ошибка загрузки</h1>"
    if picture.filename.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
        logging.info('Загружаемый файл не картинка')
        return f"<h1>Разрешение {picture.filename.split('.')[-1]} недопустимо</h1>"
    try:
        path = saved_picture(picture)[1:]
        write_post(path, content)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "<h1>File not found</h1>"
    except JSONDecodeError:
        return "<h1>File not open</h1>"
    return render_template('post_uploaded.html', content=content, path=path)

