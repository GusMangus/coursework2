import json
post_path = 'data/posts.json'
comments_path = "data/comments.json"


def load_posts() -> list[dict]:
    with open(post_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_comments() -> list[dict]:
    with open(comments_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user: str) -> list[dict]:
    result = []
    for post in load_posts():
        if user.lower() == post['poster_name'].lower():
            result.append(post)

    if len(result) == 0:
        return ValueError and f'У пользователя нет постов'
    return result

def get_comments_by_post_id(post_id):
    result = []
    for post in load_posts():
        if post_id == post['pk']:
            for comment in load_comments():
                if post_id == comment['post_id']:
                    result.append((comment['commenter_name'], comment['comment']))
            if len(result) == 0:
                return ValueError and f'У поста нет комментариев'
            return result    # возвращает список кортежей с парами пользователь, коммент

    return ValueError and f'Такого поста не существует'



def search_for_posts(query) -> list[dict]:
    result = []
    for post in load_posts():
        if query.lower() in post['content'].lower():
            result.append(post)
    if len(result) == 0:
        return ValueError and f'При поиске постов по Вашему запросу результатов не найдено'
    return result
#print(search_for_posts("остров1"))


def get_post_by_pk(pk):
    result = []
    for post in load_posts():
        if pk == post['pk']:
            result.append(post)
    if len(result) == 0:
        return ValueError and f'При поиске постов по Вашему запросу результатов не найдено'
    return result

