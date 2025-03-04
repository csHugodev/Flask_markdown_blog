from config import Config
import os

def get_posts_list():
    file_names = os.listdir(Config.POSTS_FOLDER)
    posts_names = {}
    for name in file_names:
        post_path = os.path.join(Config.POSTS_FOLDER, name)
        with open(post_path, "r", encoding="utf-8") as file:
            title = file.readline()
        posts_names[name] = title.rstrip('\n')
    return posts_names

