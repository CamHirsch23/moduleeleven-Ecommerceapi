# app/services/customer_account_service.py
from ..models.customer_account import CustomerAccount
from .. import db

def create_customer_account(data):
    new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
    db.session.add(new_account)
    db.session.commit()
    return new_account

def get_customer_account_by_id(account_id):
    return CustomerAccount.query.get_or_404(account_id)

def update_customer_account(account_id, data):
    account = CustomerAccount.query.get_or_404(account_id)
    account.username = data['username']
    account.password = data['password']
    db.session.commit()
    return account

def delete_customer_account(account_id):
    account = CustomerAccount.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()