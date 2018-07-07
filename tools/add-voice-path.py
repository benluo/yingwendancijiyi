import sqlite3
import re

# id, enword, phonetic, class, cnword, voice
conn = sqlite3.connect('../words.db')
c = conn.cursor()

c.execute('SELECT enword FROM words')
words = []
for item in c.fetchall():
    word = item[0]
    word = word.replace(" ", "-")
    testPath = "../voices/" + word + ".mp3"
    try:
        handle = open(testPath)
    except FileNotFoundError:
        print(word)
        continue
    path = "voices/" + word + ".mp3"
    c.execute('update words set voice=(?) where enword=(?)', (path, word))

conn.commit()
conn.close()
