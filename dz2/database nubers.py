import sqlite3

con = sqlite3.connect("Phone book.db")
curs = con.cursor()

curs.execute("""CREATE TABLE PPL
                (id INTEGER PRIMARY KEY,
                Name TEXT,
                Surname TEXT,
                Second_Name TEXT,
                FOREIGN KEY (Surname) REFERENCES Number(Phone_number),
                FOREIGN KEY (Surname) REFERENCES Comment(Comment))""")

curs.execute("""CREATE TABLE Number
                (id INTEGER PRIMARY KEY,
                Phone_number INTEGER,
                FOREIGN KEY (Phone_number) REFERENCES Comment(Comment))""")

curs.execute("""CREATE TABLE Comment
                (id INTEGER PRIMARY KEY,
                Comment TEXT)""")

con.commit()

curs.close()
con.close()