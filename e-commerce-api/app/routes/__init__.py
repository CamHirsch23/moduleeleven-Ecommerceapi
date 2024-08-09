# app/routes/__init__.py
from .customer_routes import customer_bp
from .customer_account_routes import customer_account_bp
from .product_routes import product_bp
from .order_routes import order_bp

def register_routes(app):
    app.register_blueprint(customer_bp)
    app.register_blueprint(customer_account_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)