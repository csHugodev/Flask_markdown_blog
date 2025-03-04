from flask import Blueprint, render_template
from ..helpers import markdownConverter, postsList

global_scope = Blueprint("views", __name__)

@global_scope.route('/')
def home():
    """LANDING PAGE ROUTE"""

    return render_template("index.html")

@global_scope.route('/posts')
def posts():
    """POSTS PAGE ROUTE"""
    posts_list = postsList.get_posts_list()
    print(posts_list)
    return render_template("posts.html", posts=posts_list)

@global_scope.route('/posts/<post>')
def read_post(post):
    """POST READ ROUTE"""
    print(post)
    content, title, autor, fecha = markdownConverter.convert_md_to_html(post)

    return render_template("post_read.html", mdContent=content, title=title, autor=autor, fecha=fecha)