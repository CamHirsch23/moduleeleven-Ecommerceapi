# app/routes/product_routes.py
from flask import Blueprint
from ..controllers import product_controller
from flask_jwt_extended import jwt_required

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    return product_controller.create_product()

@product_bp.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product(product_id):
    return product_controller.get_product(product_id)

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    return product_controller.update_product(product_id)

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    return product_controller.delete_product(product_id)

@product_bp.route('/products', methods=['GET'])
@jwt_required()
def list_products():
    return product_controller.list_products()