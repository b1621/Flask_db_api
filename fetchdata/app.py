import sqlite3
import requests
from datetime import datetime , timedelta
import random
import json
import xmltodict
from flask import Flask, jsonify,session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"


    # insert_cve(12,'01-02-2012','05-06-2013','description','a','apache','apache',7.6,'mitre')
    # return get_db()
@app.route('/')
def redirect_page():
    return render_template('home.html')

all_data = []
@app.route('/first_test')
def home():
    start_date = '2020-10-02'
    end_date = '2020-12-02'
    url = 'https://services.nvd.nist.gov/rest/json/cves/2.0/?'
    params = {
        "pubStartDate": start_date + "T00:00:00.000",
        "pubEndDate": end_date + "T23:59:59.999",
        
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return "error fetching data from nvd api"
    
@app.route("/second_test")
def second():
    start_date = '2020-10-02'
    end_date = '2020-12-02'
    url = 'https://services.nvd.nist.gov/rest/json/cves/2.0/?'
    params = {
        "pubStartDate": start_date + "T00:00:00.000",
        "pubEndDate": end_date + "T23:59:59.999",
        "resultsPerPage": 2000
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        total_results = data['totalResults']
        results = data['vulnerabilities']
        page_number = 1
        while len(results) < total_results:
            page_number += 1
            params['startIndex'] = (page_number - 1) * params['resultsPerPage']
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                results.extend(data['vulnerabilities'])
            else:
                print("Error fetching data from NVD API")
                break

        for item in results:
            print(item['cve']['id'])
        return results 
    else:
        print("Error fetching data from NVD API")

    return 'd'
        


def insert_cve(id, published_date, last_modified, description, part, vendor, product,basescore,sourceidentifier):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database =sqlite3.connect('osint.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO cve(id,published_date,last_modified,description,part,vendor,product,sourceidentifier,basescore) VALUES (?,?,?,?,?,?,?,?,?) ",(id,published_date,last_modified,description,part,vendor,product,sourceidentifier,basescore))
    return 

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('osint.db')
        cursor = db.cursor()
        cursor.execute("select * from cve")
        all_data = cursor.fetchall()
        
    return all_data


@ app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)