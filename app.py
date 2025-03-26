from flask import Flask, jsonify, request

from database import db
from models.snack import Snack

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@127.0.0.1:3306/dayly_diet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Rotas
@app.route('/diet', methods=['POST'])
def create_diet():
    data = request.json
    name = data.get("name")
    description = data.get("description")

    if name and description:
        snack = Snack(name=name, description=description, diet=True)
        db.session.add(snack)
        db.session.commit()
        return jsonify({'message': 'Dieta cadastrada com sucesso!'}), 201
    
    return jsonify({'message': 'Credenciais inválidas'}), 400

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Snack': Snack}

if __name__ == '__main__':
    app.run(debug=True)
