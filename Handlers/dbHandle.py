import sqlite3
import os

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')

#COUNTER DB

def clearCounterDB():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
   
    cursor.execute("UPDATE packetCounters SET packetNumber = 0")
   
    conn.commit()
    cursor.close()
    conn.close()

def setPacketCounter(packetName, packetCount):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
   
    cursor.execute("UPDATE packetCounters SET packetNumber=? WHERE packetName=?", (packetCount, packetName,))
   
    conn.commit()
    cursor.close()
    conn.close()
    
def getPacketCounter(packetName):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
   
    cursor.execute("SELECT packetNumber FROM packetCounters WHERE packetName=?", (packetName,))
   
    row = cursor.fetchone()
    if row:
        packet_number = row[0]
        return packet_number
    else:
        print(f"No packet found with name {packetName}")
   
    conn.commit()
    cursor.close()
    conn.close()

#USER SETTINGS DB INFO

#GETS USER SETTINGS ON START OF PROGRAM
def importUserSettings(info):
    conn = sqlite3.connect(path)
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

#UPDATES THE USERS SETTINGS ON A CHANGE
def updateUserSettings(column, value):
    conn = sqlite3.connect(path)
    cursor = conn.cursor() 
    
    cmd = f'UPDATE settingsInfo SET {column}=? WHERE id=1'  # Prevents SQL Injections
    cursor.execute(cmd, (value,))
    
    conn.commit()
    cursor.close()
    conn.close()

# PAST ALERTS DB INFO 

#UPDATES THE PAST ALERTS DB WITH NEW PAST ALERT
def updatePastAlerts(date, sourceIP, sourceP, destP):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO pastAlerts (date, sourcePort, sourceIP, destP) VALUES (?,?,?,?)", (date, sourceP, sourceIP, destP,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
#GETS ALL PAST ALERTS FROM DB    
def importPastAlerts():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pastAlerts")
    
    rows = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return rows

#GETS THE PAST ALERTS COUNT
def importPastAlertsCount():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM pastAlerts")
    
    row = cursor.fetchone()  # Retrieve the first (and only) row
    
    count = row[0] if row else None  # Extract the count value
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return count
    
#UPDATES THE CURRENT ALERTS COUNT    
def updateCurrentAlertsCount(value):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE curretnAlertsCount SET count=? WHERE ID=1", (value,))  
    
    conn.commit()
    cursor.close()
    conn.close()  