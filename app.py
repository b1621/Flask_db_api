import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"


@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["shopping_items"] = get_db()
    # return "<h1>This is My Starter App !!</h1>"
    # return str(data)
    # return data[0]
    return render_template('index.html', all_items=session["all_items"], shopping_items=session["shopping_items"])


@app.route("/remove_items", methods=["post"])
def remove_items():
    # "check" is name in the index.html checkbox input tag
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True
    return render_template('index.html', all_items=session["all_items"], shopping_items=session["shopping_items"])


@app.route("/add_items", methods=['post'])
def add_items():
    session["shopping_items"].append(request.form["my_selection"])
    session.modified = True
    # return request.form["my_selection"]
    return render_template('index.html', all_items=session["all_items"], shopping_items=session["shopping_items"])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute("select * from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[1]) for val in all_data]

        shopping_items = all_data.copy()
        random.shuffle(shopping_items)
        shopping_items = shopping_items[:6]
    return all_data, shopping_items


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
