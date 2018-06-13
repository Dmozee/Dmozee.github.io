from flask import Flask, render_template
import yaml, os

app = Flask(__name__)
PROBLEMS_DIR = "problemsets/"


def get_problemsets():
    tasks = []
    for task_slug in os.listdir(PROBLEMS_DIR):
        with open(os.path.join(PROBLEMS_DIR, task_slug)) as f:
            task = yaml.load(f.read())
            task["slug"] = task_slug.split(".")[0]
            tasks.append(task)
    return tasks

    
@app.route("/")
def main():
    return render_template("index.html", problemsets=get_problemsets())
