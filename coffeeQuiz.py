# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import random
import sqlite3
class NewApp:
    def __init__(self): 
       self.window = tk.Tk()
       self.window.geometry("500x500")
       welcome_btn = Button(self.window, text = "Welcome", command = self.newPage)
       welcome_btn.grid(row = 0, column = 0, sticky = W, pady = 2)
       self.window.mainloop()      
    def newPage(self):
        self.newWindow = Toplevel(self.window)
        self.newWindow.geometry("500x500")
        title = Label(self.newWindow,text = "Please answer the questions below")
        title.grid(column = 0, row = 0, sticky = W, pady = 2)
        self.create_DB()
        self.group1 = 0
        self.group2 = 0
        self.group3 = 0
        self.group4 = 0
        self.result = []     
    def create_DB(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        #c.execute("""CREATE TABLE questionAnswer (id integer primary key not null,
         #         question text, group1 text, group2 text, group3 text, group4 text)""")
        question_list = ['Pick your favorite show','Pick your favorite genre','Pick your favorite character','Pick your favorite past time']
        group1_list = ['Wizards of Waverly Place','Horror','Hermione Granger','Reading']
        group2_list = ['One Tree Hill','Drama','Bella Swan','Exercising']
        group3_list = ['The Office','Comedy','Kelly Kapoor','Cooking']
        group4_list = ['Avatar:The Last Airbender','Adventure','Toph Beifong','Exploring']
        conn.commit()
        ##First row 
        #c.execute("""INSERT INTO questionAnswer VALUES(1,'Whats your favorite season','Fall','Winter','Spring','Summer')""")
        #Starting column 2 at row 2
        #row = 1
        #for item in question_list:
        #     row += 1
        #     c.execute("INSERT INTO questionAnswer(question) VALUES(?)",(item,))
        #conn.commit()
        ##Col 3
        #row = 1
        #for item in group1_list:
        #    row += 1
        #    c.execute("UPDATE questionAnswer SET group1 = ? WHERE id = ?",(item,row))
        #conn.commit()
        ##Col 4
        #row = 1
        #for item in group2_list:
        #   row += 1
        #   c.execute("UPDATE questionAnswer SET group2 = ? WHERE id = ?",(item,row))
        #conn.commit()
        ##Col 5
        #row = 1
        #for item in group3_list:
        #    row += 1
        #    c.execute("UPDATE questionAnswer SET group3 = ? WHERE id = ?",(item,row))
        #conn.commit()
        ##Col 6
        #row = 1
        #for item in group4_list:
        #    row += 1
        #    c.execute("UPDATE questionAnswer SET group4 = ? WHERE id = ?",(item,row))
        #conn.commit()
        #for row in c.execute("SELECT * FROM questionAnswer"):
        #    print(row)              
        rw = 0
        col = 0
        x = 0
        for row in c.execute("SELECT id,question FROM questionAnswer"):
            col+= 1 
            rw += 1
            x += 1
            q_label = Label(self.newWindow, text = row)
            q_label.grid(column = 0, row = rw, sticky = W, pady = 2)
        new_rw = 0
        for row in c.execute("SELECT group1 FROM questionAnswer"):
            new_rw += 1
            self.g1btn = Button(self.newWindow, text = row, command = self.g1Counter)
            self.g1btn.grid(column = 1, row = new_rw,sticky = W, pady = 2)
        new_rw = 0
        for row in c.execute("SELECT group2 FROM questionAnswer"):
            new_rw += 1
            self.g2btn = Button(self.newWindow, text = row, command = self.g2Counter)
            self.g2btn.grid(column = 2, row = new_rw,sticky = W, pady = 2)
        new_rw = 0
        for row in c.execute("SELECT group3 FROM questionAnswer"):
            new_rw += 1
            self.g3btn = Button(self.newWindow, text = row, command = self.g3Counter)
            self.g3btn.grid(column = 3, row = new_rw,sticky = W, pady = 2)
        new_rw = 0
        for row in c.execute("SELECT group4 FROM questionAnswer"):
            new_rw += 1
            self.g4btn = Button(self.newWindow, text = row, command = self.g3Counter)
            self.g4btn.grid(column = 4, row = new_rw,sticky = W, pady = 2)
        submit = Button(self.newWindow, text = "Submit", command = self.submit)
        submit.grid(column = 0, row = 7, sticky = W, pady = 2)
        self.g1 = ['Caramel Machiatto', 'Pumpkin Spice Latte','Chestnut Praline Latte','Capuccino with Cinnamon']
        self.g2 = ['Gingerbread Latte', 'Peppermint Mocha','Cafe Mocha','Spiced Vanilla Latte']
        self.g3 = ['Rose Coffee','Iced Vietnamese Latte','Vanilla Iced Latte','Cafe Con Miel']
        self.g4 = ['Cold Coffee','Turkish Coffee','Iced Thai Latte','Nutella Iced Coffee']
        self.rand_coffees = ['Flat White','Black Coffee','Espresso','Plain Latte','Plain Cappuccino','Cafe Au Lait','Americano']
        list_array = [self.g1, self.g2,self.g3,self.g4,self.rand_coffees]
    def g1Counter(self):
        self.group1 += 1
        if self.group1 >= 3:
            self.result = self.g1
    def g2Counter(self):
        self.group2 += 1
        if self.group2 >= 3:
            self.result = self.g2
    def g3Counter(self):
        self.group3 += 1
        if self.group3 >= 3:
            self.result = self.g3
    def g4Counter(self):
        self.group4 += 1
        if self.group4 >= 3:
            self.result = self.g4
    def submit(self):
        if self.group1 < 3:
            if self.group2 < 3:
                if self.group3 < 3:
                    if self.group4 < 3:
                        self.result = self.rand_coffees
        elif self.group2 < 3:
            if self.group1 < 3:
                if self.group3 < 3:
                    if self.group4 < 3:
                        self.result = self.rand_coffees
        
        elif self.group3 < 3:
            if self.group2 < 3:
                if self.group1 < 3:
                    if self.group4 < 3:
                        self.result = self.rand_coffees
        elif self.group4 < 4:
            if self.group2 < 3:
                if self.group3 < 3:
                    if self.group1 < 3:
                        self.result = self.rand_coffees
        sgn = Label(self.newWindow,text = random.choice(self.result))
        sgn.grid(column = 0, row = 8, sticky = W, pady = 2)
        try_again = Button(self.newWindow, text = "Try again", command = self.newPage)
        try_again.grid(column = 0, row = 9, sticky = W, pady = 2)
        good_bye = Button(self.newWindow, text = "Goodbye", command = self.newWindow.destroy)
        good_bye.grid(column = 0, row = 10, sticky = W, pady = 2)
        good_bye2 = Button(self.window, text = "Goodbye",command = self.window.destroy)
        good_bye2.grid(column = 0, row = 1, sticky = W, pady = 2)
app = NewApp
app()

