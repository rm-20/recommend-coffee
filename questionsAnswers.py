# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute("""CREATE TABLE questionAnswer (id integer primary key not null,
#          question text, group1 text, group2 text, group3 text, group4 text)""")
#c.execute("""INSERT INTO questionAnswer VALUES(1,'Whats your favorite season','Fall','Winter','Spring','Summer')""")
question_list = ['Pick your favorite show','Pick your favorite genre','Pick your favorite character','Pick your favorite past time']
group1_list = ['Wizards of Waverly Place','Horror','Hermione Granger','Reading']
group2_list = ['One Tree Hill','Drama','Bella Swan','Exercising']
group3_list = ['The Office','Comedy','Kelly Kapoor','Cooking']
group4_list = ['Avatar:The Last Airbender','Adventure','Toph Beifong','Exploring']
conn.commit()

#row = 1
#for item in question_list:
 #    row += 1
  #   c.execute("INSERT INTO questionAnswer(question) VALUES(?)",(item,))
#conn.commit()

#row = 1
#for item in group1_list:
#    row += 1
#    c.execute("UPDATE questionAnswer SET group1 = ? WHERE id = ?",(item,row))
#conn.commit()

#row = 1
#for item in group2_list:
#    row += 1
#    c.execute("UPDATE questionAnswer SET group2 = ? WHERE id = ?",(item,row))
#conn.commit()

#row = 1
#for item in group3_list:
#    row += 1
#    c.execute("UPDATE questionAnswer SET group3 = ? WHERE id = ?",(item,row))
#conn.commit()

row = 1
#for item in group4_list:
 #   row += 1
  #  c.execute("UPDATE questionAnswer SET group4 = ? WHERE id = ?",(item,row))
#conn.commit()

for row in c.execute("SELECT * FROM questionAnswer"):
    print(row)

