import pytest
import json
from flask.testing import FlaskClient


def test_get_orders(client):
    response = client.get('/get_orders')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['type'] == 'orders'


def test_get_quotes(client):
    response = client.get('/get_quotes')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['type'] == 'quotes'


def test_place_order(client):
    order = {'symbol': 'AAPL', 'price': 150.25, 'quantity': 10}
    response = client.post('/place_order', json=order)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['type'] == 'order_placed'


def test_cancel_order(client):
    order = {'order_id': 1}
    response = client.post('/cancel_order', json=order)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['type'] == 'order_cancelled' or data['type'] == 'order_cancel_failed'