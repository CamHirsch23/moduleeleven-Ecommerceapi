# app/controllers/customer_account_controller.py
from flask import request, jsonify
from ..models.customer_account import CustomerAccount
from .. import db

def create_customer_account():
    data = request.get_json()
    new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'Customer account created successfully'}), 201

def get_customer_account(account_id):
    account = CustomerAccount.query.get_or_404(account_id)
    return jsonify({'username': account.username, 'customer_id': account.customer_id})

def update_customer_account(account_id):
    data = request.get_json()
    account = CustomerAccount.query.get_or_404(account_id)
    account.username = data['username']
    account.password = data['password']
    db.session.commit()
    return jsonify({'message': 'Customer account updated successfully'})

def delete_customer_account(account_id):
    account = CustomerAccount.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({'message': 'Customer account deleted successfully'})