# app/tests/test_product.py
import unittest
from app import create_app, db
from app.models.product import Product

class ProductTestCase(unittest.TestCase):
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

    def test_create_product(self):
        response = self.client.post('/products', json={
            'name': 'Product 1',
            'price': 10.0
        })
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        product = Product(name='Product 1', price=10.0)
        db.session.add(product)
        db.session.commit()
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()