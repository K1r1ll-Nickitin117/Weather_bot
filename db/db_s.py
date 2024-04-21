import sqlite3


class DB:
    @staticmethod
    def get_stat():
        stat = []
        con = sqlite3.connect('db/weather_bot.db')
        cur = con.cursor()
        result = cur.execute('SELECT * FROM Location')
        for row in result:
            stat.append(row)

        answer_stat = 'Ваши запросы:\n'
        if stat:
            for res in stat:
                answer_stat += f'{res[0]}, широта - {res[1]}, долгота - {res[2]};\n'
        else:
            return 'История поиска пуста. Узнайте погоду.'
        con.commit()
        con.close()
        return answer_stat

    @staticmethod
    def drop_table():
        con = sqlite3.connect('db/weather_bot.db')
        cur = con.cursor()
        cur.execute('UPDATE Location SET city = NULL, lat = NULL, lon = NULL WHERE FALSE;')
        con.commit()
        con.close()

    @staticmethod
    def add_city(city, lat, lon):
        con = sqlite3.connect('db/weather_bot.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO Location VALUES (?, ?, ?)''', (city, lat, lon))
        con.commit()
        con.close()
