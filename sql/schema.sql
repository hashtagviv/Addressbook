CREATE TABLE Addresses(
    addressid INTEGER PRIMARY KEY AUTOINCREMENT,
    lastname varchar(20),
    firstname varchar(20),
    Company varchar(40),
    Email varchar(20),
    Category varchar(20)
);

CREATE TABLE contactinfo(
    addressid INTEGER PRIMARY KEY,
    workphone varchar(20),
    homephone varchar(20),
    mobile varchar(20),
    urllink varchar(20)
);

CREATE TABLE addressinfo(
    addressid INTEGER PRIMARY KEY,
    address_ varchar(20),
    city varchar(20),
    country varchar(20),
    state_ varchar(20),
    zip varchar(20)
);