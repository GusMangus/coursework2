from flask import Flask, request, render_template, send_from_directory

from loader.views_loader import loader_blueprint
from main.views_main import main_blueprint

from utils import get_posts_by_user

post_path = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


print (get_posts_by_user())
app.run()