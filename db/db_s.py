import sqlite3


class DB:
    def __init__(self, database_file='db/weather_bot.db'):
        self.connection = None
        self.database_file = database_file

    def connect(self):
        self.connection = sqlite3.connect(self.database_file)

    def execute(self, query, params=None):
        """Выполнение запроса к базе данных."""
        if not self.connection:
            raise Exception('Надо подключиться к бд')
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor

    def commit(self):
        """Фиксация транзакции."""
        if not self.connection:
            raise Exception('Надо подключиться к бд')
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def fetchall(self, cursor):
        """Возвращает все строки результата запроса."""
        return cursor.fetchall()

    def get_stat(self):
        db = DB()
        db.connect()
        stat = []
        try:
            result = db.execute('SELECT  *  FROM location')
            for row in db.fetchall(result):
                stat.append(row)
        finally:
            db.close()
        answer_stat = 'Ваши запросы:\n'
        if stat:
            for res in stat:
                answer_stat += f'{res[1]}, широта - {res[2]}, долгота - {res[3]};\n'
        return answer_stat

    def drop_table(self):
        db = DB()
        db.connect()
        db.execute('''''DROP TABLE location') 
        db.execute('CREATE TABLE location (
    id   INTEGER PRIMARY KEY,
    city TEXT,
    lat  REAL,
    lon  REAL)''')

    def add_city(self, city, lat, lon):
        db = DB()
        db.connect()
        db.execute(f'INSERT INTO location (city, lat, lon) VALUES (?, ?, ?)',
                   (f'{city}', {lat}, {lon}))
