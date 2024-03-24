CREATE TABLE ipInfo (
    from_IpADD VARCHAR(15) NOT NULL PRIMARY KEY,
    dest_IpADD VARCHAR(15) NOT NULL,
    port INTEGER NOT NULL,
    protocol VARCHAR(100) NOT NULL,
    allow BOOLEAN
);
-- DROP TABLE ipInfo;
CREATE TABLE settingsInfo(
    id INTEGER NOT NULL PRIMARY KEY,
    interface INTEGER, 
    notifications VARCHAR(1)
);
-- DROP TABLE settingsInfo;
CREATE TABLE pastAlerts(
    id INTEGER NOT NULL PRIMARY KEY,
    sourcePort VARCHAR(15),
    sourceIP VARCHAR(15),
    destP INTEGER
);
-- DROP TABLE pastAlerts;


-- Here I have made the DEFAULT settings entery for each user.

INSERT INTO settingsInfo(id, interface, notifications) VALUES (1, 2, 'T');

-- DELETE FROM settingsInfo WHERE id=1;

-- SELECT * FROM settingsInfo;