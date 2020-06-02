import sqlite3

# init and connect to db
dbConnection = sqlite3.connect('db.sqlite')
dbCursor = dbConnection.cursor()

# insert table
dbCursor.execute("DROP TABLE IF EXISTS Counts")
dbCursor.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

textFile = input("Enter file name: ")
fileHandler = open(textFile)
query = ""

# parse through and count each email per organization
for line in fileHandler:
    if line.startswith("From:"):
        lineBuffer = line.split(" ")
        email = lineBuffer[1]
        organization = email.split("@")[1]
        organization = organization.replace("\n", "")

        query = "SELECT * FROM Counts WHERE org = '" + organization + "'"
        #print(query)

        # check db for entry - execute then fetch
        dbCursor.execute(query)
        exists = dbCursor.fetchall()

        if len(exists) == 0:
            query = "INSERT INTO Counts VALUES ('" + organization + "', 1)"
            #print(query)
            dbCursor.execute(query)

        else:
            query = "UPDATE Counts SET count = count + 1 WHERE org = '" + organization + "'"
            #print(query)
            dbCursor.execute(query)

        # execute and commit transaction
        dbConnection.commit()

# get final counts
query = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
#print(query)
dbCursor.execute(query)
selectQry = dbCursor.fetchall()

# destructuring
for (organization, counts) in selectQry:
    print(str(organization), str(counts))

# close connection to avoid memory leaks
dbCursor.close()
dbConnection.close()