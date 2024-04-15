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

UPDATE settingsInfo 
SET interface = 4, 
    notifications = 'T'
WHERE id = 1;
