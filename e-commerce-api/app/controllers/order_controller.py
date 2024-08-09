# app/controllers/order_controller.py
from flask import request, jsonify
from ..models.order import Order, OrderProduct
from .. import db

def place_order():
    data = request.get_json()
    new_order = Order(customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    for product_id in data['product_ids']:
        order_product = OrderProduct(order_id=new_order.id, product_id=product_id)
        db.session.add(order_product)
    
    db.session.commit()
    return jsonify({'message': 'Order placed successfully'}), 201

def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    products = [{'id': op.product.id, 'name': op.product.name, 'price': op.product.price} for op in order.products]
    return jsonify({'order_date': order.order_date, 'customer_id': order.customer_id, 'products': products})