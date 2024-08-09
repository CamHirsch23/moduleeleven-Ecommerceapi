# app/tests/test_order.py
import unittest
from app import create_app, db
from app.models.order import Order

class OrderTestCase(unittest.TestCase):
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

    def test_place_order(self):
        response = self.client.post('/orders', json={
            'customer_id': 1,
            'product_ids': [1, 2]
        })
        self.assertEqual(response.status_code, 201)

    def test_get_order(self):
        order = Order(customer_id=1)
        db.session.add(order)
        db.session.commit()
        response = self.client.get(f'/orders/{order.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()