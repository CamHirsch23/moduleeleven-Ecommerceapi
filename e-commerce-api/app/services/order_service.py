# app/services/order_service.py
from ..models.order import Order, OrderProduct
from .. import db

def place_order(data):
    new_order = Order(customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    for product_id in data['product_ids']:
        order_product = OrderProduct(order_id=new_order.id, product_id=product_id)
        db.session.add(order_product)
    
    db.session.commit()
    return new_order

def get_order_by_id(order_id):
    return Order.query.get_or_404(order_id)