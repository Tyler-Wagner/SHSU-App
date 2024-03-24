import sqlite3
import os

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.abspath(__file__))

def importUserSettings():
    db_path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cmd = f'SELECT * FROM settingsInfo'
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print("User 1 Data Info")
        print(row)
    cursor.close()
    conn.close()

def updateUserSettings(column, value):
    db_path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor() 
    cmd = f'UPDATE settingsInfo SET {column}=? WHERE id=1'  # Prevents SQL Injections
    cursor.execute(cmd, (value,))
    conn.commit()
    cursor.close()
    conn.close()

# Testing
# def main():
#     updateUserSettings('interface', '2')
#     importUserSettings()
    
# if __name__ == "__main__":
#     main()