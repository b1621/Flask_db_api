# import sqlite3

# connect = sqlite3.connect('data.db')

# connect.execute('DROP TABLE IF EXISTS CUSTOMER')
# connect.execute('''
# CREATE TABLE CUSTOMER
# (ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# AGE INT NOT NULL);''')

# connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1,'Tomi', 21)")
# connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (5,'Nf', 25)")

# all_data = connect.execute('''SELECT * FROM CUSTOMER''')
# for row in all_data:
#     print(row)
# connect.close()

# ----------------------------------------------------

# url = https://api.tomitokko.repl.co/

import requests
import json

# response = requests.get("https://api.tomitokko.repl.co/")
# response = requests.get(    "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2019-1010218")
response = requests.get("https://anapioficeandfire.com/api/houses/1")

print(response.status_code)
res = json.loads(response.text)
# print(res)
# for data in res:
#     print(data)
