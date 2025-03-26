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
        diet = data['diet'] if 'diet' in data else True
        snack = Snack(name=name, description=description, diet=diet)
        db.session.add(snack)
        db.session.commit()
        return jsonify({'message': 'Dieta cadastrada com sucesso!'}), 201
    
    return jsonify({'message': 'Credenciais inválidas'}), 400

@app.route('/diet/<int:id_diet>', methods=['PUT'])
def update_diet(id_diet):
    data = request.json
    snack = Snack.query.get(id_diet)

    if not snack:
        return jsonify({'message': 'Dieta não encontrada!'}), 404

    for field in ['name', 'description', 'diet']:
        if field in data:
            setattr(snack, field, data[field])

    db.session.commit()
    return jsonify({'message': f'A Dieta {id_diet} foi atualizada com secesso!'})
    
@app.route('/diet/<int:id_diet>', methods=['DELETE'])
def delete_diet(id_diet):
    snack = Snack.query.get(id_diet)

    if snack and id_diet:
        db.session.delete(snack)
        db.session.commit()
        return jsonify({'message': f'Dieta {id_diet} removido com sucesso!'})
    return jsonify({'message': f'Dieta não encontrada!'}),404

@app.route('/diets', methods=['GET'])
def get_all():
    snacks = Snack.query.all()

    result = []
    for snack in snacks:
        result.append({
            'id': snack.id,
            'name': snack.name,
            'description': snack.description,
            'date': snack.date.isoformat(),
            'diet': snack.diet
        })
    return jsonify(result)

@app.route('/diet/<int:id_diet>', methods=['GET'])
def get_id(id_diet):
    snack = Snack.query.get(id_diet)

    if snack:
        return {
                'id': snack.id,
                'name': snack.name, 
                'description': snack.description,
                'diet': snack.diet,
                'date': snack.date.isoformat()
                }
    return jsonify({'message': 'Dieta não encontrada!'}), 404

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Snack': Snack}

if __name__ == '__main__':
    app.run(debug=True)
