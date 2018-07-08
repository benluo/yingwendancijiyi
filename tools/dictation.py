import os
import sqlite3
import time
import string

conn = sqlite3.connect('../words.db')
c = conn.cursor()
repeatTime = 2

for letter in string.ascii_lowercase:
    select = "SELECT id, voice,enword FROM words where enword like \"{}%\" order by id".format(letter)
    c.execute(select)
    for item in c.fetchall():
        voice = item[1]
        filePath = "../"+voice
        if not os.path.exists(filePath):
            print(voice)
        else:
            for i in range(repeatTime):
                os.system("mpg321 "+filePath)
                time.sleep(3)

    nextLetter = input("Next letter? y(for yes) or n(for no)")
    if nextLetter == 'n':
        break
    else:
        continue

conn.close()
