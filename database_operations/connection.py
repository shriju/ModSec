import mysql.connector

class Connection:
    def make_connection(self, db_name=None):
        try:
            conn = mysql.connector.connect(
            host = "localhost",
            user = "thisMe",
            password = "tF0k2h#g",
            database = db_name
            )
        except Exception as e:
            print(type(e).__name__, e)
        else:
            cursor = conn.cursor()
            return (conn, cursor)   # return connection and cursor objects