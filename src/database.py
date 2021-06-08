import mysql.connector

class Database():
    def __init__(self, host, port, username, password):
        self.db = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password
        )

    def fetch(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()