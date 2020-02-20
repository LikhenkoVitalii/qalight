import sqlite3

con = sqlite3.connect("Clients.db")
curs = con.cursor()

curs.execute("""CREATE TABLE clients  
                  (id INTEGER PRIMARY KEY, 
                  company TEXT,
                  country TEXT, 
                  FOREIGN KEY (country) REFERENCES adress(country),
                  FOREIGN KEY (company) REFERENCES product(name))""")

curs.execute("""CREATE TABLE product
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  country TEXT,
                  amount INTEGER,
                  type_amount INTEGER)
                  """)

curs.execute("""CREATE TABLE adress 
                  (id INTEGER PRIMARY KEY,
                  country TEXT,
                  street TEXT,
                  home INTEGER)
                  """)

curs.execute('INSERT INTO cliets (company, country) VALUES ("McDonals", "Germany")')
curs.execute('INSERT INTO cliets (company, country) VALUES ("McDonals", "USA")')
curs.execute('INSERT INTO cliets (company, country) VALUES ("McDonals", "France")')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "Germany", 400, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "Germany", 200, 1)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "France", 500, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "France", 100, 1)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "USA", 200, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Meat", "USA", 500, 1)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "France", 700, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "France", 800, 1)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "USA", 1000, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "USA", 600, 1)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "Germany", 600, 2)')
curs.execute('INSERT INTO product (name, country, amount, type) VALUES ("Potato", "France", 900, 1)')
curs.execute('INSERT INTO adress (country, street, home) VALUES ("USA", "Vas", 5)')
curs.execute('INSERT INTO adress (country, street, home) VALUES ("USA", "DEFF", 24)')
curs.execute('INSERT INTO adress (country, street, home) VALUES ("France", "sdsd", 19)')
curs.execute('INSERT INTO adress (country, street, home) VALUES ("Germany", "wwee", 67)')


con.commit()

curs.close()
con.close()