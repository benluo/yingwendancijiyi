import sqlite3
import csv
from bs4 import BeautifulSoup as bs
import requests
import time
import re

# 序号, 单词, 音标, 词性, 意思
conn = sqlite3.connect('words.db')
c = conn.cursor()
with open('niujin.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        word = row[1].strip()
        c.execute('SELECT enword FROM words WHERE enword=?', (word,))
        if word == c.fetchone():
            continue
        page = requests.get("http://www.dict.cn/" + word)
        b = bs(page.text, "html.parser").find('div', class_="phonetic")
        if b and b.span.bdo:
            pheno = re.sub("\[(.*?)\]", '\\1', b.span.bdo.text)
        else:
            pheno = ""
        print(pheno)
        c.execute(
            'insert into words values ({0},"{1}","""{2}""","{3}","{4}","");'.format(int(row[0]),
                                                                                    word, pheno, row[3],
                                                                                    row[4]))
        conn.commit()
        time.sleep(3)

conn.close()
