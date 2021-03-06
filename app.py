from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel
from resources.user import Users, User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    base.create_all()

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<string:hotel_id>')
api.add_resource(Users, '/users')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from sql_alchemy import base
    base.init_app(app)
    app.run(debug = True)