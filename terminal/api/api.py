from flask import Flask, jsonify, request


app = Flask(__name__)


orders = []


@app.route('/get_orders', methods=['GET'])
def get_orders():
    response = {'type': 'orders', 'data': orders}
    return jsonify(response)


@app.route('/get_quotes', methods=['GET'])
def get_quotes():
    quotes = {'AAPL': 150.25, 'GOOG': 2500.50, 'TSLA': 700.75}
    response = {'type': 'quotes', 'data': quotes}
    return jsonify(response)


@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.get_json()
    new_order = {'symbol': data['symbol'], 'price': data['price'], 'quantity': data['quantity']}
    orders.append(new_order)
    response = {'type': 'order_placed', 'data': new_order}
    return jsonify(response)


@app.route('/cancel_order', methods=['POST'])
def cancel_order():
    data = request.get_json()
    order_id = data['order_id']
    cancelled_order = None
    for order in orders:
        if order['id'] == order_id:
            cancelled_order = order
            orders.remove(order)
            break
    if cancelled_order:
        response = {'type': 'order_cancelled', 'data': cancelled_order}
    else:
        response = {'type': 'order_cancel_failed'}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
