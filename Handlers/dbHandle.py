import sqlite3
import os

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(parent_dir, '..', 'DataBase', 'ourDB.db')

#DETERMINE IF FIRSTRUN FOR SETUP WIZ
def getFirstRun():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT ans FROM firstRun")
    
    row = cursor.fetchone()
    
    if row:
        ans = int(row[0])
    else:
        ans = None

    cursor.close()
    conn.close()
    return ans

def setFirstRun(): #SET THE VALUE TO TRUE IF THERE IS NONE IN THE DB
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO firstRun (ans) VALUES (1)")
    
    conn.commit()
    cursor.close()
    conn.close()
    
def updateFirstRun():#SET VALUE TO FALSE AFTER FIRST RUN
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE firstRun SET ans=0")
    
    conn.commit()
    cursor.close()
    conn.close()


#API COUNTER AND DATE
def setDate(date):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO dateCheck VALUES (?)", (str(date),))
    
    conn.commit()
    cursor.close()
    conn.close()  
    
def checkCount():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT apiCount FROM apiCounter")
    
    row = cursor.fetchone()
    
    if row:
        number = row[0]
    else: 
        number = None
        
    cursor.close()
    conn.close()
    return int(number)

def updateCount(number):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE apiCounter SET apiCount=?", (number,))
    
    conn.commit()
    cursor.close()
    conn.close()   
    
def checkDate():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT date FROM dateCheck")
    
    row = cursor.fetchone()
    if row:
        date = row[0]
    else:
        date = None
        
    cursor.close()
    conn.close()
    return str(date)
    

def updateDate(date):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE dateCheck SET date=?", (date,))
    
    conn.commit()
    cursor.close()
    conn.close()
    

#PACKET COUNTER DB
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
        # print("No data found")
        value = None
    
    cursor.close()
    conn.close()
    return value

#UPDATES THE USERS SETTINGS ON A CHANGE
def updateUserSettings(column, value):
    conn = sqlite3.connect(path)
    cursor = conn.cursor() 
    
    if importUserSettings(column)==None:
        cmd = f'INSERT INTO settingsInfo (id, {column}) VALUES (1, ?)'  
    else:
        cmd = f'UPDATE settingsInfo SET {column}=? WHERE id=1'  
    
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
    
    cursor.close()
    conn.close()
    
    if rows:
        return rows
    else:
        return None

#GETS THE PAST ALERTS COUNT
def importPastAlertsCount():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM pastAlerts ORDER BY date")
    
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
    
    cursor.execute("SELECT count(*) FROM currentAlertsCount")
    result = cursor.fetchone()
    if result[0] > 0: 
        cursor.execute("UPDATE currentAlertsCount SET count=? WHERE ID=1", (value,))
        conn.commit()
    else:
        cursor.execute("INSERT INTO currentAlertsCount (ID, count) VALUES (1, 0)")  # Corrected typo
        conn.commit()
    
    cursor.close()
    conn.close()


#INITIATE THE DB SO THAT THERE ARE TABLES IN THE DB AND THE USER HAS A CLEAN SLATE ON FIRST RUN
class initiation:
    def initiateDB():
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        
        initiation.createTables(cursor=cursor)
        initiation.deleteData(cursor=cursor)
        
        cursor.execute("INSERT OR IGNORE INTO apiCounter (apiCount) VALUES (999)")
        cursor.execute("INSERT OR IGNORE INTO settingsInfo (id, interface, notifications) VALUES (1, 0, 'F')")
        cursor.execute("INSERT OR IGNORE INTO currentAlertsCount (ID, count) VALUES (1, 0)")
        
        initial_values = [
            ("UDP", 0),
            ("TCP", 0),
            ("ICMP", 0),
            ("ARP", 0)
        ]
        cursor.executemany("INSERT OR IGNORE INTO packetCounters (packetName, packetNumber) VALUES (?, ?)", initial_values)

        conn.commit()
        cursor.close()
        conn.close()


    def deleteData(cursor):
        table_names = [
                "settingsInfo",
                "pastAlerts",
                "packetCounters",
                "dateCheck",
                "currentAlertsCount",
                "apiCounter"
            ]

        # Delete all data from each table for a clean start
        for table_name in table_names:
            cursor.execute(f"DELETE FROM {table_name}")

    def createTables(cursor):
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS settingsInfo (
                            id INTEGER NOT NULL,
                            interface INTEGER,
                            notifications VARCHAR(5)
                            )''')

        # Create pastAlerts table
        cursor.execute('''CREATE TABLE IF NOT EXISTS pastAlerts (
                            date VARCHAR NOT NULL,
                            sourcePort VARCHAR,
                            sourceIP VARCHAR,
                            destP VARCHAR
                            )''')

        # Create packetCounters table
        cursor.execute('''CREATE TABLE IF NOT EXISTS packetCounters (
                            packetName VARCHAR NOT NULL,
                            packetNumber INTEGER
                            )''')
        # Create dateCheck table
        cursor.execute('''CREATE TABLE IF NOT EXISTS dateCheck (
                            date VARCHAR
                            )''')

        # Create currentAlertsCount table
        cursor.execute('''CREATE TABLE IF NOT EXISTS currentAlertsCount (
                            ID INTEGER PRIMARY KEY NOT NULL,
                            count INTEGER
                            )''')

        # Create apiCounter table
        cursor.execute('''CREATE TABLE IF NOT EXISTS apiCounter (
                            apiCount INTEGER
                            )''')
  