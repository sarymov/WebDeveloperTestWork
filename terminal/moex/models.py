from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading.db'
db = SQLAlchemy(app)


# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    purchases = db.relationship('Purchase', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


# Модель покупки акций
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Purchase %r>' % self.ticker


# Регистрация пользователя
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})


# Покупка акций
@app.route('/buy', methods=['POST'])
def buy():
    username = request.json['username']
    ticker = request.json['ticker']
    quantity = request.json['quantity']

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'})

    purchase = Purchase(user=user, ticker=ticker, quantity=quantity)
    db.session.add(purchase)
    db.session.commit()

    return jsonify({'message': 'Stock purchased successfully'})


# Просмотр списка покупок пользователя
@app.route('/purchases/<username>')
def get_purchases(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'})

    purchases = Purchase.query.filter_by(user=user).all()

    result = []
    for purchase in purchases:
        result.append({
            'ticker': purchase.ticker,
            'quantity': purchase.quantity
        })

    return jsonify({'purchases': result})


if __name__ == '__main__':
    db.create_all()
    app.run()