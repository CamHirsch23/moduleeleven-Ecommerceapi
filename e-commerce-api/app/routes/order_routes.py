# app/routes/order_routes.py
from flask import Blueprint
from ..controllers import order_controller
from flask_jwt_extended import jwt_required

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def place_order():
    return order_controller.place_order()

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    return order_controller.get_order(order_id)