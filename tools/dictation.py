'''
Use for dictation in console
'''

import os
import sqlite3
import time
import sys
import random
from pathlib import Path

def get_letters(word_range):
    '''
    input: word_range
    return: sorted letters
    '''
    letter_set = set()
    for letter in word_range:
        tmp_l = letter.split('-')
        if len(tmp_l) == 1 and len(letter) == 1:
            letter_set.add(letter)
        elif len(tmp_l) == 2 and len(tmp_l[0]) == 1 and len(tmp_l[1]) == 1 and tmp_l[0] < tmp_l[1]:
            for l in range(ord(tmp_l[0]), ord(tmp_l[1]) + 1):
                letter_set.add(chr(l))
        else:
            print("Not right choice. Bye.")
            sys.exit()

    letters = list(letter_set)
    letters.sort()
    return letters

def dictation():
    '''
    Use for dictation in console
    '''
    # open db
    db_file = Path(__file__).parent.parent / 'words.db'
    conn = sqlite3.connect(str(db_file))
    c = conn.cursor()

    choice = input("Please select the first charactors of word." +
                   "e.g. a, b, c OR a-c, OR a, b, c, m-o (like you do in M$ Word print dialog)")

    # parse input to letters range
    word_range = list(map(lambda x: x.strip(' '), choice.split(",")))
    letters = get_letters(word_range)
    word_list = []
    for letter in letters:
        select = "SELECT id, voice, enword FROM words where enword like \"{}%\" \
                  order by id".format(letter)
        c.execute(select)
        for item in c.fetchall():
            word_list.append(item)

    choice = input("Dictation in Order(input O or o) or" +
                   " in Random(input R or r)? Default is in order.")
    if choice in ['r', 'R']:
        random.shuffle(word_list)

    repeat = input("Please choose repeating times (1-5), default is two times.")
    if repeat not in range(1, 6):
        repeat = 2

    # Windows (nt) and other *nix use different command
    if os.name == 'nt':
        command = "mpg123.exe "
    else:
        command = "mpg321 "

    for word in word_list:
        voice = word[1]
        file_path = db_file.parent / voice
        if not os.path.exists(file_path):
            print(voice)
        else:
            for i in range(repeat):
                os.system(command + str(file_path))
                time.sleep(3)

    conn.close()

if __name__ == "__main__":
    dictation()
