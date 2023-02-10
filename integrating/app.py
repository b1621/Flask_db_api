from flask import Flask, request, render_template, jsonify
import time
import requests
import threading
from datetime import datetime

app = Flask(__name__)

# app.register_blueprint()
data = [ "apache", "windows_10", "oracle" ]

@app.before_first_request
def before_first_request():
    print('the first program to execute')
    # send_req()
    t = threading.Thread(target=send_req)
    t.start()


@app.route('/')
def hello_world():
    return "Hello, This is home page"

@app.route('/about')
def about():
    return "about page"

# @app.route()

def send_req():   
    while True:
        print('****************** start for all **********************')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        for keyword in data:
            link = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}'
            print('-------------------- starting single session -------------------')

            response = requests.get(link)
            if response.status_code == 200:
                cve_data = response.json()
                # print(jsonify(cve_data))
                # print(cve_data)
                print('-------------------end for single session---------------------------')
        print('****************************end all session************************')
        time.sleep(100)    

if __name__ == "__main__":
    app.run(debug=True)
    