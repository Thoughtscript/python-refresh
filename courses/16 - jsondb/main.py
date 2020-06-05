import sqlite3
import json
import re

# init and connect to db
dbConnection = sqlite3.connect('db.sqlite')
dbCursor = dbConnection.cursor()

# insert table User
dbCursor.execute("DROP TABLE IF EXISTS User ")
dbCursor.execute("CREATE TABLE User (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")

# insert table Course
dbCursor.execute("DROP TABLE IF EXISTS Course")
dbCursor.execute("CREATE TABLE Course (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE)")

# insert table Member
dbCursor.execute("DROP TABLE IF EXISTS Member")
dbCursor.execute("CREATE TABLE Member (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, user_id INTEGER, course_id INTEGER, role TEXT)")

# open data
jsonAsString = ""
handle = open("roster_data.json")
for line in handle:
    jsonAsString += line
entries = json.loads(jsonAsString)

for entry in entries:
    student = str(entry[0])
    course = str(entry[1])
    role = str(entry[2])

    print(student + " " + course + " " + role)

    # inserts
    dbCursor.execute("INSERT OR IGNORE INTO User (name) VALUES (\"" + student + "\")")
    dbCursor.execute("INSERT OR IGNORE INTO Course (title) VALUES (\"" + course + "\")")
    dbConnection.commit()

    # selects
    dbCursor.execute("SELECT id FROM User WHERE name=\"" + student + "\"")
    studentId = str(dbCursor.fetchone()[0])
    dbCursor.execute("SELECT id FROM Course WHERE title=\"" + course + "\"")
    courseId = str(dbCursor.fetchone()[0])

    # insert fks
    dbCursor.execute("INSERT OR IGNORE INTO Member (role, user_id, course_id) VALUES (\"" + role + "\"," + studentId + "," + courseId + ")")
    dbConnection.commit()

dbCursor.execute("SELECT hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X")
results = dbCursor.fetchall()

for result in results:
    print(str(result))

