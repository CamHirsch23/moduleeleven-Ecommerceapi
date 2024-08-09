# app/tests/test_customer.py
import unittest
from app import create_app, db
from app.models.customer import Customer

class CustomerTestCase(unittest.TestCase):
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

    def test_create_customer(self):
        response = self.client.post('/customers', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_customer(self):
        customer = Customer(name='John Doe', email='john@example.com', phone='1234567890')
        db.session.add(customer)
        db.session.commit()
        response = self.client.get(f'/customers/{customer.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()