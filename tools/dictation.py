import os
import sqlite3
import time
import string
import sys

conn = sqlite3.connect('../words.db')
c = conn.cursor()
repeatTime = 2

choice = input("Dictation in Order(input O) or in Random(input R)?")
if choice in ['o','O']:
    choice = input("Please select ")
elif choice in ['r','R']:
    choice = input("Please input how many words you want to dictation. Please input one number in range of 1 to 627.")
else:
    print ("Not right choice. Bye.")
    sys.exit()

for letter in string.ascii_lowercase:
    select = "SELECT id, voice,enword FROM words where enword like \"{}%\" order by id".format(letter)
    c.execute(select)
    for item in c.fetchall():
        voice = item[1]
        filePath = "../"+voice
        if not os.path.exists(filePath):
            print(voice)
        else:
            print(item[2])
#  for i in range(repeatTime):
#      os.system("mpg321 "+filePath)
#      time.sleep(3)
#
    nextLetter = input("Next letter? y(for yes) or n(for no)")
    if nextLetter == 'n':
        break
    else:
        continue

conn.close()
