import sqlite3
import os

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')

def importUserSettings(info):
    parent_dir = os.path.dirname(__file__)
    db_path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cmd = f'SELECT {info} FROM settingsInfo' 
    cursor.execute(cmd)
    row = cursor.fetchone()
    if row:
        value = row[0]
        if(value=="T"):
            value = True
        elif(value=="F"):
            value = False
    else:
        print("No data found")
        value = None
    cursor.close()
    conn.close()
    return value

def updateUserSettings(column, value):
    db_path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor() 
    cmd = f'UPDATE settingsInfo SET {column}=? WHERE id=1'  # Prevents SQL Injections
    cursor.execute(cmd, (value,))
    conn.commit()
    cursor.close()
    conn.close()

def updatePastAlerts(date, sourceIP, sourceP, destP):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO pastAlerts (date, sourcePort, sourceIP, destP) VALUES (?,?,?,?)", (date, sourceP, sourceIP, destP,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
def importPastAlerts():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pastAlerts")
    
    rows = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return rows
