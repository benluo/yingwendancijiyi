import os
import sqlite3
import time

conn = sqlite3.connect('../words.db')
c = conn.cursor()

c.execute('SELECT id, voice FROM words order by id')

for item in c.fetchall():
    voice = item[1]
    filePath = "../"+voice
    print(filePath)
    try:
        handle = open(filePath)
    except FileNotFoundError:
        print(voice)
        continue
    for i in range(2):
        os.system("mpg321 "+filePath)
        time.sleep(3)

conn.close()
