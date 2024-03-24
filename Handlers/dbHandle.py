import sqlite3

def import_data_from_db(cmd):
    conn = sqlite3.connect('ourDB.db')
    cursor = conn.cursor()
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
