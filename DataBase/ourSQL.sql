CREATE TABLE ipInfo (
    from_IpADD VARCHAR(15) NOT NULL PRIMARY KEY,
    dest_IpADD VARCHAR(15) NOT NULL,
    port INTEGER NOT NULL,
    protocol VARCHAR(100) NOT NULL,
    allow BOOLEAN
);

CREATE TABLE settingsInfo(
    id INTEGER NOT NULL PRIMARY KEY,
    interface INTEGER, 
    notifications VARCHAR(1)
);

CREATE TABLE pastAlerts(
    id VARCHAR NOT NULL PRIMARY KEY,
    sourcePort VARCHAR,
    sourceIP VARCHAR,
    destP VARChAR
);

CREATE TABLE curretnAlertsCount(
    ID INTEGER PRIMARY KEY NOT NULL,
    count INTEGER
);

DROP Table pastAlertsCounter;

INSERT INTO curretnAlertsCount (ID, count) VALUES(1, 0);

UPDATE pastAlertsCounter SET count=5 WHERE ID=1;

UPDATE settingsInfo 
SET interface = 4, 
    notifications = 'T'
WHERE id = 1;
