from flask import Flask
from order_management import order_manager_blueprint

app = Flask(__name__)

app.register_blueprint(order_manager_blueprint)

@app.route('/')
def hello_world():
    return "Hello, This is home page"

if __name__ == "__main__":
    app.run(debug=True)