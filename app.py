"""Урок 12 Домашнее задание"""
import logging
from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint


logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8')

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Отдача загруженных в /uploads файлов"""
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()

