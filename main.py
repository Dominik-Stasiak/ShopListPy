import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "training"

@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["furniture_items"] = get_db()
    return render_template("index.html", all_items=session["all_items"],
                                         furniture_items=session["furniture_items"])


@app.route("/add_items", methods=["post"])
def add_items():
    session["furniture_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items=session["all_items"],
                                         furniture_items=session["furniture_items"])

@app.route("/remove_items", methods=["post"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["furniture_items"]:
            idx = session["furniture_items"].index(item)
            session["furniture_items"].pop(idx)
            session.modified = True
    return render_template("index.html", all_items=session["all_items"],
                                         furniture_items=session["furniture_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('furniture_list.db')
        cursor = db.cursor()
        cursor.execute("select name from furniture")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        furniture_items = all_data.copy()
        random.shuffle(furniture_items)
        furniture_items = furniture_items[:5]
    return all_data, furniture_items

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()