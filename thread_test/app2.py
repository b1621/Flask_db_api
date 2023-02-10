from flask import Flask, jsonify
from flask_restful import Resource, Api
import time
import threading


app = Flask(__name__)
app.secret_key = 'secret'

starttime = time.time()


def back_work():
    while True:
        print("tick")
        # print(60.0 - ((time.time() - starttime) % 60.0))
        # time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        time.sleep(10)

@app.route('/')
def index():
    threading.Thread(target=back_work).start()
    # back_work()
    return 'hello'

@app.route('/json')
def json_test():
    data = jsonify(
                    {"message": "some string", "severity": "danger"}
                )
    return data

if __name__ == '__main__':
    app.run(debug=True)    