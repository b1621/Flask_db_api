import sqlite3
import requests
import random
import json
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


@app.route('/api')
def test_api():
    # response = requests.get("https://randomuser.me/api/")
    response = requests.get(
        "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2019-1010218")
    res = json.loads(response.text)
    return render_template('api_test.html', res=res)
    # return res
@app.route('/api_check', methods=['POST', 'GET'])
def check_api():
    service = ''
    product = ''
    res={}
    if request.method == 'POST':
        service = request.form.get('service')
        product = request.form.get('product')

        response = requests.get(f'https://cve.circl.lu/api/browse/{service}')
        res = response.text
    return render_template("checkapi.html", service=service, product=product, res=res)

@app.route('/api_test', methods=['POST', 'get'])
def api_test():
    part = ''
    vendor = ''
    product = ''
    version = ''
    if request.method == 'POST':
        cpe = 'cpe:2.3:a:ntp:ntp:4.2.8'
        part = request.form.get('part')
        vendor = request.form.get('vendor')
        product = request.form.get('product')
        version = request.form.get('version')
        key_value = request.form.get('key_value')
        keyword = request.form.get('keyword')
        if key_value == 'normal':
            link = f'https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:{part}:{vendor}:{product}:{version}'
        else:
            link = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}'            
        response = requests.get(link)
        res = response.text
        return render_template('testapipost.html',link=link,res=res, key_value=key_value)
    return render_template('testapi.html')



@ app.route("/remove_items", methods=["post"])
def remove_items():
    # "check" is name in the index.html checkbox input tag
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True
    return render_template('index.html', all_items=session["all_items"], shopping_items=session["shopping_items"])


@ app.route("/add_items", methods=['post'])
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


@ app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
