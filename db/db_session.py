import sqlite3


class DBSession:
    def add_location(self, lat, lon, location_now):
        con = sqlite3.connect('.db')
        cur = con.cursor()
        cur.execute(f'INSERT INTO location (id, name, surname, birthdate) VALUES ({location_now}, {lat}, {lon})')
        con.commit()
        con.close()

    def get_location(self):
        pass
