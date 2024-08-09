# app/services/customer_service.py
from ..models.customer import Customer
from .. import db

def create_customer(data):
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def get_customer_by_id(customer_id):
    return Customer.query.get_or_404(customer_id)

def update_customer(customer_id, data):
    customer = Customer.query.get_or_404(customer_id)
    customer.name = data['name']
    customer.email = data['email']
    customer.phone = data['phone']
    db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()