# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE IF NOT EXISTS test(test text)''')
#c.execute("""CREATE TABLE questions (question text, answer1, answer2, answer3, answer4)""")

# Insert a row of data
#c.execute("INSERT INTO test VALUES ('one')")
c.execute("""INSERT INTO questions VALUES('Whats your favorite season','Fall','Winter','Spring','Summer')""")

question_list = ['Pick your favorite show','Pick your favorite genre','Pick your favorite character','Pick your favorite past time']
answer1_list = ['Wizards of Waverly Place','Horror','Hermione Granger','Reading']
answer2_list = ['One Tree Hill','Drama','Bella Swan','Exercising']
answer3_list = ['The Office','Comedy','Kelly Kapoor','Cooking']
answer4_list = ['Avatar:The Last Airbender','Adventure','Toph Beifong','Exploring']

for item in question_list:
    c.execute("""INSERT INTO questions(question) VALUES(%s)"""(item))
# Save (commit) the changes
conn.commit()

for row in c.execute('SELECT * FROM questions'):
        print(row)
conn.close()

