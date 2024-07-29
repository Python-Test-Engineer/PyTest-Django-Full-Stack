--
-- File generated with SQLiteStudio v3.4.4 on Sun Jul 21 16:12:45 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: artists
CREATE TABLE IF NOT EXISTS artists(

  artistid    INTEGER PRIMARY KEY,

  artistname  TEXT

 );

-- Table: contacts
CREATE TABLE IF NOT EXISTS contacts (

    contact_id INTEGER PRIMARY KEY,

    first_name TEXT    NOT NULL,

    last_name  TEXT    NOT NULL,

    email      TEXT,

    phone      TEXT    NOT NULL

                    CHECK (length(phone) >= 10) 

);

-- Table: tracks
CREATE TABLE IF NOT EXISTS "tracks" (

	"trackid"	INTEGER NOT NULL,

	"trackname"	TEXT DEFAULT 'TONY' CHECK (length(trackname) >= 5) ,

	"trackartist"	INTEGER NOT NULL  ,

	"rating"	INTEGER  ,

	FOREIGN KEY("trackartist") REFERENCES "artists"("artistid"),

	PRIMARY KEY("trackid")

 );

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
