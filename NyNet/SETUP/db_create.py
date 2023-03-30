import hashlib, sqlite3

connection = sqlite3.connect("database.db")
cur = connection.cursor()

cur.execute("""
CREATE TABLE IS NOT EXIST database.db (
    id  INTERGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255), NOT NULL
)""")

username1, password1 = "root",hashlib.sha256("root".encode()).hexdigest() #CHANGE
username2, password2 = "test",hashlib.sha256("test".encode()).hexdigest() #Remove

cur.execute("INSERT INTO database (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO database (username, password) VALUES (?, ?)", (username2, password2))

