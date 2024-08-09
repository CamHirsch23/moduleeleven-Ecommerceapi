# app/services/product_service.py
from ..models.product import Product
from .. import db

def create_product(data):
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_product_by_id(product_id):
    return Product.query.get_or_404(product_id)

def update_product(product_id, data):
    product = Product.query.get_or_404(product_id)
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return product

def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

def list_products():
    return Product.query.all()