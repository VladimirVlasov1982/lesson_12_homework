import json

POST_PATH = "posts.json"


def load_json() -> list[dict]:
    """Загрузка файла JSON"""
    with open(POST_PATH, encoding="utf-8") as file:
        return json.load(file)


def search_posts(search) -> list[dict]:
    """Возвращает найденные посты"""
    content = load_json()
    result = []
    for item in content:
        if search.lower() in item['content'].lower():
            result.append(item)
    return result


def write_post(path, content):
    """Записывает данные добавленных постов в файл JSON"""
    dct = {'pic': path, 'content': content}
    file = load_json()
    file.append(dct)
    with open('posts.json', 'w', encoding='utf-8') as text:
        json.dump(file, text, ensure_ascii=False, indent=4)


def saved_picture(picture) -> str:
    """Сохраняет картинку в папку /uploads/images. Возвращает путь к файлу"""
    name_picture = picture.filename
    path = f'./uploads/images/{name_picture}'
    picture.save(path)
    return path
