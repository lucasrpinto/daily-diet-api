from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@127.0.0.1:3306/dayly_diet'

db.init_app(app)

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
