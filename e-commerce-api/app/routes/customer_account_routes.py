# app/routes/customer_account_routes.py
from flask import Blueprint
from ..controllers import customer_account_controller
from flask_jwt_extended import jwt_required

customer_account_bp = Blueprint('customer_account_bp', __name__)

@customer_account_bp.route('/customer_accounts', methods=['POST'])
@jwt_required()
def create_customer_account():
    return customer_account_controller.create_customer_account()

@customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['GET'])
@jwt_required()
def get_customer_account(account_id):
    return customer_account_controller.get_customer_account(account_id)

@customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['PUT'])
@jwt_required()
def update_customer_account(account_id):
    return customer_account_controller.update_customer_account(account_id)

@customer_account_bp.route('/customer_accounts/<int:account_id>', methods=['DELETE'])
@jwt_required()
def delete_customer_account(account_id):
    return customer_account_controller.delete_customer_account(account_id)