import sqlite3
import xml.etree.ElementTree as ET

# init and connect to db
dbConnection = sqlite3.connect('db.sqlite')
dbCursor = dbConnection.cursor()

# insert table Artist
dbCursor.execute("DROP TABLE IF EXISTS Artist")
dbCursor.execute("CREATE TABLE Artist (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")

# insert table Genre
dbCursor.execute("DROP TABLE IF EXISTS Genre")
dbCursor.execute("CREATE TABLE Genre (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")

# insert table Album - FK on Artist
dbCursor.execute("DROP TABLE IF EXISTS Album")
dbCursor.execute("CREATE TABLE Album (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, artist_id INTEGER, title TEXT UNIQUE)")

# insert table Track - FK on Genre and FK on Album
dbCursor.execute("DROP TABLE IF EXISTS Track")
dbCursor.execute("CREATE TABLE Track (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)")

# open XML
xml = ET.parse('Library.xml')
trackDict = xml.getroot()[0][17]
tracks = trackDict.findall('.//dict')

# use escaped \" instead
def cleanString(text):
    #text = text.replace("'", "&#39;")
    #text = text.replace(".", "&#46;")
    return text

for track in tracks:

    trackName = ""
    artistName = ""
    genreName = ""
    albumName = ""
    len = "0"
    rating = "0"
    count = "0"
    currentKey = 0

    for key in track:

        if (key.text == "Name"):
            trackName = cleanString(track[currentKey + 1].text)
        if (key.text == "Artist"):
            artistName = cleanString(track[currentKey + 1].text)
        if (key.text == "Genre"):
            genreName = cleanString(track[currentKey + 1].text)
        if (key.text == "Album"):
            albumName = cleanString(track[currentKey + 1].text)

        if (key.text == "Total Time"):
            len = track[currentKey + 1].text
        if (key.text == "Rating" or key.text == "Album Rating"):
            rating = track[currentKey + 1].text
        if (key.text == "Play Count"):
            count = track[currentKey + 1].text

        currentKey += 1

    # inserts
    dbCursor.execute("INSERT OR IGNORE INTO Artist (name) VALUES (\"" + artistName + "\")")
    dbCursor.execute("INSERT OR IGNORE INTO Genre (name) VALUES (\"" + genreName + "\")")
    dbConnection.commit()

    # select id
    dbCursor.execute("SELECT id FROM Artist WHERE name=\"" + artistName + "\"")
    artistId = str(dbCursor.fetchone()[0])

    dbCursor.execute("SELECT id FROM Genre WHERE name=\"" + genreName + "\"")
    genreId = str(dbCursor.fetchone()[0])

    # insert fks
    dbCursor.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (" + artistId + ",\"" + albumName + "\")")
    dbConnection.commit()
    dbCursor.execute("SELECT id FROM Album WHERE title=\"" + albumName + "\"")
    albumId = str(dbCursor.fetchone()[0])

    # insert fks
    dbCursor.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (\"" + trackName + "\"," + albumId + "," + genreId + "," + len + "," + rating + "," + count + ")")
    dbConnection.commit()

dbCursor.execute("SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3")
results = dbCursor.fetchall()

for result in results:
    print(str(result))

