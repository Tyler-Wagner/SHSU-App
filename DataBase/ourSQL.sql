DROP TABLE ipInfo;

CREATE TABLE ipInfo (
    from_IpADD VARCHAR(15) NOT NULL PRIMARY KEY,
    dest_IpADD VARCHAR(15) NOT NULL,
    port INTEGER,
    protocol VARCHAR(100),
    allow BOOLEAN
);
