# app/tests/test_customer_account.py
import unittest
from app import create_app, db
from app.models.customer_account import CustomerAccount

class CustomerAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_customer_account(self):
        response = self.client.post('/customer_accounts', json={
            'username': 'johndoe',
            'password': 'password123',
            'customer_id': 1
        })
        self.assertEqual(response.status_code, 201)

    def test_get_customer_account(self):
        account = CustomerAccount(username='johndoe', password='password123', customer_id=1)
        db.session.add(account)
        db.session.commit()
        response = self.client.get(f'/customer_accounts/{account.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()