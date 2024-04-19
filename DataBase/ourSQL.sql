CREATE TABLE settingsInfo(
    id INTEGER NOT NULL,
    interface INTEGER, 
    notifications VARCHAR(5)
);

CREATE TABLE pastAlerts(
    date VARCHAR NOT NULL,
    sourcePort VARCHAR,
    sourceIP VARCHAR,
    destP VARChAR
);

CREATE TABLE packetCounters(
    packetName VARCHAR NOT NULL,
    packetNumber INTEGER
);

CREATE TABLE firstRun(
    ans INTEGER
);

CREATE TABLE dateCheck(
    date VARCHAR
);

CREATE TABLE curretnAlertsCount(
    ID INTEGER PRIMARY KEY NOT NULL,
    count INTEGER
);

CREATE TABLE apiCounter(
    apiCount INTEGER
);

-- DELETE FROM settingsInfo;
-- DELETE FROM pastAlerts;
-- DELETE FROM packetCounters;
-- DELETE FROM firstRun;
-- DELETE FROM dateCheck;
-- DELETE FROM currentAlertsCount;
-- DELETE FROM apiCounter;

-- INSERT INTO pastAlerts (date, sourcePort, sourceIP, destP) 
-- VALUES 
-- ('2024-04-04/14:50:12', '22', '1234556789', '22'),
-- ('2024-04-04/14:50:12', '22', '1234556789', '22'),
-- ('2024-04-15/10:18:21', '22', '1234556789', '22'),
-- ('2024-04-15/10:19:37', '22', '1234556789', '22'),
-- ('2024-04-15/10:20:24', '22', '1234556789', '22'),
-- ('2024-04-15/10:20:24', '22', '1234556789', '22'),
-- ('2024-04-15/17:04:37', '22', '123456789', '22'),
-- ('2024-04-15/17:15:39', '22', '123456789', '22'),
-- ('2024-04-15/17:23:06', '22', '123456789', '22'),
-- ('2024-04-15/17:33:38', '22', '123456789', '22'),
-- ('2024-04-15/17:35:31', '22', '123456789', '22'),
-- ('2024-04-15/17:36:20', '22', '123456789', '22'),
-- ('2024-04-15/17:36:20', '22', '123456789', '22'),
-- ('2024-04-15/17:53:33', '22', '123456789', '22'),
-- ('2024-04-15/17:53:33', '22', '123456789', '22'),
-- ('2024-04-17/12:33:36', '22', '123456789', '22'),
-- ('2024-04-17/16:07:53', '22', '123456789', '22'),
-- ('2024-04-18/16:45:56', '22', '104.250.49.205', '22');

