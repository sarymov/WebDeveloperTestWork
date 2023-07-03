from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/moex')
def moex():
    # Подключение к базе данных
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()

    # Получение данных из таблицы акций
    c.execute('SELECT * FROM stocks')
    data = c.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    return render_template('moex/moex.html', data=data)


if __name__ == '__main__':
    app.run(port=8000)
