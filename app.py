from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.store import Store, StoreList
from resources.user import UserRegister
from resources.item import Item, ItemList
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'this really gotta be secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_URS_RULE'] = '/login'
app.config['JWT_AUTH_USERNAME_KEY'] = 'username'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=10800)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
