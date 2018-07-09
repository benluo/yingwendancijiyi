import os
import sqlite3
import time
import string
import sys
import random

conn = sqlite3.connect('../words.db')
c = conn.cursor()
repeatTime = 2

print("Please select the first charactors of word. \
e.g. a, b, c, or a-c, or a, b, c, m-o (like you do in M$ Word print dialog)")
choice = input()

# parse input to letters range
wordRange = list(map(lambda x: x.strip(' '), choice.split(",")))
letters = []
for letter in wordRange:
    tmpLetters = letter.split('-')
    if len(tmpLetters) == 1 and len(letter) == 1:
        letters.append(letter)
    elif len(tmpLetters) == 2 and len(tmpLetters[0]) == 1 and len(tmpLetters[1]) == 1 and tmpLetters[0] < tmpLetters[1]:
        for l in range(ord(tmpLetters[0]), ord(tmpLetters[1]) + 1):
            letters.append(chr(l))
    else:
        print("Not right choice. Bye.")
        sys.exit()

letters = list(set(letters))
letters.sort()

wordList = []
for letter in letters:
    select = "SELECT id, voice, enword FROM words where enword like \"{}%\" \
                order by id".format(letter)
    c.execute(select)
    for item in c.fetchall():
        wordList.append(item)

choice = input("Dictation in Order(input O) or in Random(input R)? Default is in order.")
if choice in ['r', 'R']:
    random.shuffle(wordList)

repeat = input("Please choose repeating times (1-5), default is two times.")
if repeat not in range(1, 6):
    repeat = 2

for word in wordList:
    voice = word[1]
    filePath = "../" + voice
    if not os.path.exists(filePath):
        print(voice)
    else:
        for i in range(repeatTime):
            os.system("mpg321 " + filePath)
            time.sleep(3)

conn.close()
