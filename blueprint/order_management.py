from flask import Blueprint

order_manager_blueprint = Blueprint('order_manager_blueprint', __name__, url_prefix="/order")

@order_manager_blueprint.route('/myorders')
def myorders():
    return "These are your orders."

@order_manager_blueprint.route('placeorder')
def placeorder():
    return "Placing order"