# app/controllers/customer_controller.py
from flask import request, jsonify
from ..models.customer import Customer
from .. import db

def create_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully'}), 201

def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({'name': customer.name, 'email': customer.email, 'phone': customer.phone})

def update_customer(customer_id):
    data = request.get_json()
    customer = Customer.query.get_or_404(customer_id)
    customer.name = data['name']
    customer.email = data['email']
    customer.phone = data['phone']
    db.session.commit()
    return jsonify({'message': 'Customer updated successfully'})

def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'})