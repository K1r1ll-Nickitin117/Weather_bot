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
        pass

    def drop_table(self):
        # db.execute('DROP TABLE')
        pass

    def start_db_ses(self):
        pass
