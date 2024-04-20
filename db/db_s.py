import sqlite3


class DB:
    @staticmethod
    def get_stat():
        con = sqlite3.connect('weather_bot.db')
        cur = con.cursor()
        stat = []

        result = cur.execute('SELECT * FROM location')
        for row in cur.fetchall(result):
            stat.append(row)

        answer_stat = 'Ваши запросы:\n'
        if stat:
            for res in stat:
                answer_stat += f'{res[1]}, широта - {res[2]}, долгота - {res[3]};\n'
        con.commit()
        con.close()
        return answer_stat

    @staticmethod
    def drop_table():
        con = sqlite3.connect('weather_bot.db')
        cur = con.cursor()
        cur.execute('''''DROP TABLE location') 
        db.execute('CREATE TABLE location (
    id   INTEGER PRIMARY KEY,
    city TEXT,
    lat  REAL,
    lon  REAL)''')
        con.commit()
        con.close()

    @staticmethod
    def add_city(city, lat, lon):
        con = sqlite3.connect('weather_bot.db')
        cur = con.cursor()
        cur.execute(f'INSERT INTO location (city, lat, lon) VALUES (?, ?, ?)',
                    (f'{city}', {lat}, {lon}))
        con.commit()
        con.close()
