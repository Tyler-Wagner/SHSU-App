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

CREATE TRIGGER prevent_delete
BEFORE DELETE ON pastAlerts
FOR EACH ROW
WHEN OLD.id = 1
BEGIN
    SELECT RAISE(ABORT, 'Deletion is not allowed for this row');
END;
-- DROP TABLE ipInfo;
-- DROP TABLE settingsInfo;
-- DROP TABLE pastAlerts;

INSERT INTO settingsInfo (id, interface, notifications) VALUES (1, 4,'T'); 


-- ############## DEMO ############## --
UPDATE settingsInfo SET interface=7;
-- UPDATE settingsInfo SET notifications='T';
-- SELECT * FROM settingsInfo;
-- ##############      ############## --

-- Here I have made the DEFAULT settings entery for each user.

-- INSERT INTO settingsInfo(id, interface, notifications) VALUES (1, 2, 'T');

-- DELETE FROM settingsInfo; --clear table
--  SELECT * FROM settingsInfo;