from flask import Flask, render_template
import yaml, os

app = Flask(__name__)
PROBLEMS_DIR = "problemsets/"


def get_problemset(slug):
    with open(os.path.join(PROBLEMS_DIR, slug)) as f:
        task = yaml.load(f.read())
        task["slug"] = slug.split(".")[0]
        return task


def get_problemsets():
    tasks = []
    for task_slug in os.listdir(PROBLEMS_DIR):
        tasks.append(get_problemset(slug))
    return tasks

    
@app.route("/")
def main():
    return render_template("index.html", problemsets=get_problemsets())
