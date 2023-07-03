import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('stocks.db')
c = conn.cursor()

# Создание таблицы акций
c.execute('''
    CREATE TABLE IF NOT EXISTS stocks (
        ticker TEXT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
''')

# Заполнение таблицы акций примерами данных
data = [
    ('AAPL', 'Apple Inc.', 150.25, 100),
    ('GOOGL', 'Alphabet Inc.', 2550.75, 50),
    ('MSFT', 'Microsoft Corporation', 300.50, 75)
]
c.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?)', data)

# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
