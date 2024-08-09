# app/routes/customer_routes.py
from flask import Blueprint
from ..controllers import customer_controller
from flask_jwt_extended import jwt_required

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/customers', methods=['POST'])
@jwt_required()
def create_customer():
    return customer_controller.create_customer()

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    return customer_controller.get_customer(customer_id)

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    return customer_controller.update_customer(customer_id)

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id):
    return customer_controller.delete_customer(customer_id)