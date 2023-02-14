import sqlite3

connection = sqlite3.connect("osint.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS cve")
cursor.execute('''
    CREATE TABLE cve  ( id text PRIMARY KEY,
                                published_date bigint default 0,
                                last_modified bigint default 0,
                                sourceidentifier text default '',
                                description text default '',
                                part text default '',
                                vendor text default '',
                                product text default '',
                                basescore init default 0
                                 )

''')



connection.commit()
connection.close()
