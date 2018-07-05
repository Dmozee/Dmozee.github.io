from flask import Flask, render_template, abort
import yaml, os

app = Flask(__name__)
PROBLEMS_DIR = "problemsets/"
EXT = ".yml"


def get_problemset(slug):
    with open(os.path.join(PROBLEMS_DIR, slug)) as f:
        task = yaml.load(f.read())
        task["slug"] = slug.split(".")[0]
        return task


def get_problemsets():
    tasks = []
    for slug in os.listdir(PROBLEMS_DIR):
        tasks.append(get_problemset(slug))
    tasks.sort(key = lambda task: task["position"])
    return tasks

def indexate(lst):
    return [ (chr(ord('A') + i), lst[i]) for i in range(len(lst)) ]

@app.route("/")
def main():
    return render_template("index.html", problemsets=get_problemsets())


@app.route("/problems/<file>/")
def problemset(file):
    if "." in file:
        abort(403)
    if not os.path.exists(os.path.join(PROBLEMS_DIR, file + EXT)):
        abort(404)

    return render_template(
        "problemset.html",
        problemset=get_problemset(file + EXT,
        problems=indexate(get_problemset(file + EXT).problems),
        problemsets=get_problemsets(),
        current=file
    )
