# app/utils/jwt_utils.py
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta

def generate_token(identity):
    return create_access_token(identity=identity, expires_delta=timedelta(hours=1))

@jwt_required()
def get_current_user():
    return get_jwt_identity()