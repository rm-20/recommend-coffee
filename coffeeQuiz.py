# -*- coding: utf-8 -*-
"""
Spyder Editor

coffee related app, take a short quiz,outputs coffee recommendation
"""
import tkinter as tk
from tkinter import *
import random

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
        title.grid(column = 0, row = 1, sticky = W, pady = 2)
        self.group1 = 0
        self.group2 = 0
        self.group3 = 0
        self.group4 = 0
        
        q1 = Label(self.newWindow, text = "What's your favorite season?")
        q1.grid(column = 0, row = 2,sticky = W, pady = 2)
        
        self.fall = Button(self.newWindow, text = "Fall", command = self.storeFall)
        self.fall.grid(column = 0, row = 3, sticky = W, pady = 2)
        
        self.spring = Button(self.newWindow, text = "Spring", command = self.storeSpring)
        self.spring.grid(column = 0, row = 4, sticky = W, pady = 2)
        
        self.summer = Button(self.newWindow, text = "Summer", command = self.storeSummer)
        self.summer.grid(column = 0, row = 5, sticky = W, pady = 2)
        
        self.winter = Button(self.newWindow, text = "Winter", command = self.storeWinter)
        self.winter.grid(column = 0, row = 6, sticky = W, pady = 2)
        
        q2 = Label(self.newWindow, text = "What's your favorite show?")
        q2.grid(column = 0, row = 8, sticky = W, pady = 2)
        
        self.show1 = Button(self.newWindow, text = "Avatar: The Last Airbender", command = self.storeShow1)
        self.show1.grid(column = 0, row = 9, sticky = W, pady = 2)
        
        self.show2 = Button(self.newWindow, text = "The Office", command = self.storeShow2)
        self.show2.grid(column = 0, row = 10, sticky = W, pady = 2)
        
        self.show3 = Button(self.newWindow, text = "One Tree Hill", command = self.storeShow3)
        self.show3.grid(column = 0, row = 11, sticky = W, pady = 2)
        
        self.show4 = Button(self.newWindow, text = "Wizards of Waverly Place", command = self.storeShow4)
        self.show4.grid(column = 0, row = 12, sticky = W, pady = 2)
        
        q3 = Label(self.newWindow, text = "What's your favorite book genre?")   
        q3.grid(column = 0, row = 14, sticky = W, pady = 2)
       
        self.g1 = Button(self.newWindow, text = "horror", command = self.storeG1)
        self.g1.grid(column = 0, row = 15, sticky = W, pady = 2)
        
        self.g2 = Button(self.newWindow, text = "comedy", command = self.storeG2)
        self.g2.grid(column = 0, row = 16, sticky = W, pady = 2)
        
        self.g3 = Button(self.newWindow, text = "mystery", command = self.storeG3)
        self.g3.grid(column = 0, row = 17, sticky = W, pady = 2)
        
        self.g4 = Button(self.newWindow, text = "romance", command = self.storeG4)
        self.g4.grid(column = 0, row = 18, sticky = W, pady = 2)      
       
        self.submit = Button(self.newWindow, text = "Done!", command = self.quizResult)
        self.submit.grid(column = 0, row = 20, sticky = W, pady = 2)
    
    def storeFall(self):
        self.group1 += 1
        print(self.group1)

    def storeSpring(self):
        self.group3 += 1
        print(self.group3)
    
    def storeSummer(self):
        self.group4 += 1
        print(self.group4)
    
    def storeWinter(self):
        self.group2 += 1
        print(self.group2)
        
    def storeShow1(self):
        self.group4 += 1
        print(self.group4)
    
    def storeShow2(self):
        self.group3 += 1
        print(self.group3)
    
    def storeShow3(self):
        self.group2 += 1
        print(self.group2)
    
    def storeShow4(self):
        self.group1 += 1
        print(self.group1)
        
    def storeG1(self):
        self.group1 += 1
        print(self.group1)    
        
    def storeG2(self):
        self.group2 += 1
        print(self.group2)    
        
    def storeG3(self):
        self.group3 += 1
        print(self.group3)
        
    def storeG4(self):
        self.group4 += 1
        print(self.group4)
    
    def quizResult(self):
        if self.group1 >= 2:
            group_1 = ['Pumpkin Spice Latte','Cinnamon Maple Latte','Caramel Macchiato','Chestnut Praline Latte','Cafe Mocha']
            rec = Label(self.newWindow, text = random.choice(group_1))
            rec.grid(column = 2, row = 1, sticky = W, pady = 2)
            thank_you = Button(self.newWindow, text = "Thank you!", command = self.newWindow.destroy)
            thank_you.grid(column = 2, row = 2, sticky = W, pady = 2)
            try_again = Button(self.window, text = "Try again", command = self.newPage)
            try_again.grid(column = 0, row = 2, sticky = W, pady = 2)
            good_bye = Button(self.window, text = "Goodbye", command = self.window.destroy)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
            
            
        elif self.group2 >= 2:
            group_2 = ['Peppermint Mocha','Gingerbread Latte','Winter Spiced Coffee','Cappuccino']
            rec = Label(self.newWindow, text = random.choice(group_2))
            rec.grid(column = 2, row = 1, sticky = W, pady = 2)
            thank_you = Button(self.newWindow, text = "Thank you!", command = self.newWindow.destroy)
            thank_you.grid(column = 2, row = 2, sticky = W, pady = 2)
            try_again = Button(self.window, text = "Try again", command = self.newPage)
            try_again.grid(column = 0, row = 2, sticky = W, pady = 2)
            good_bye = Button(self.window, text = "Goodbye", command = self.window.destroy)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
            
        elif self.group3 >= 2:
            group_3 = ['Thai Iced Coffee','Cafe Con Miel', 'Rose Coffee','Iced Vietnamese Latte']
            rec = Label(self.newWindow, text = random.choice(group_3))
            rec.grid(column = 2, row = 1, sticky = W, pady = 2)
            thank_you = Button(self.newWindow, text = "Thank you!", command = self.newWindow.destroy)
            thank_you.grid(column = 2, row = 2, sticky = W, pady = 2)
            try_again = Button(self.window, text = "Try again", command = self.newPage)
            try_again.grid(column = 0, row = 2, sticky = W, pady = 2)
            good_bye = Button(self.window, text = "Goodbye", command = self.window.destroy)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
                      
        elif self.group4 >= 2:
            group_4 = ['Vanilla Iced Coffee','Nutella Iced Coffee','Colf Brew Coffee', 'Cafe Au Lait']
            rec = Label(self.newWindow, text = random.choice(group_4))
            rec.grid(column = 2, row = 1, sticky = W, pady = 2)
            thank_you = Button(self.newWindow, text = "Thank you!", command = self.newWindow.destroy)
            thank_you.grid(column = 2, row = 2, sticky = W, pady = 2)
            try_again = Button(self.window, text = "Try again", command = self.newPage)
            try_again.grid(column = 0, row = 2, sticky = W, pady = 2)
            good_bye = Button(self.window, text = "Goodbye", command = self.window.destroy)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
                       
        else:
            generic_coffees = ['Flat White', 'Espresso','Espresso Machiatto', 'Cold Brew Coffee', 'Cafe Au Lait', 'Iced Latte', 'Turkish Coffee', 'Americano', 'Black Coffee']
            rec = Label(self.newWindow, text = random.choice(generic_coffees))
            rec.grid(column = 2, row = 1, sticky = W, pady = 2)
            thank_you = Button(self.newWindow, text = "Thank you!", command = self.newWindow.destroy)
            thank_you.grid(column = 2, row = 2, sticky = W, pady = 2)
            try_again = Button(self.window, text = "Try again", command = self.newPage)
            try_again.grid(column = 0, row = 2, sticky = W, pady = 2)
            good_bye = Button(self.window, text = "Goodbye", command = self.window.destroy)
            good_bye.grid(column = 0, row = 3, sticky = W, pady = 2)
        
app = NewApp
app()
