'''Conver a json file into SQLite database 
    3 Steps: sqlits3.connect ->  con.cursor -> cur.execute '''

import sqlite3
import json

# get a connection, create / connect to the db file
conn = sqlite3.connect('people.db')

# open the database 
cur = conn.cursor()
# cur.execute('''DROP TABLE people''') # so that to create a new one from scratch

# use doc string for multiple line of command
cur.execute('''CREATE TABLE people (
    name text,
    phone text,
    email text,
    postal text, 
    country text
)''')

# open json file and read it 
filehandler = open('data.json')
# decode json
people_list = json.load(filehandler)

# write each item in the list to the database
for p in people_list:
    name = p['name']
    phone = p['phone']
    email = p['email']
    postal = p['postalZip']
    country = p['country']
    cur.execute('INSERT INTO people VALUES (?,?,?,?,?)', (name, phone, email, postal, country))


# TASKS:
# 



# commit the changes
conn.commit()
conn.close()
    

