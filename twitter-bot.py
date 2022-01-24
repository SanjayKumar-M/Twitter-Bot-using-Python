from asyncio import sleep
from curses import window
import email
from click import command
from flask import session
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from tkinter import * 
import pyautogui as py

class twitter_bot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot.webdriver.Brave()
    
    def login(self):
        bot=self.bot 
        bot.get("https://twitter.com/")
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.RETURN)
        time.sleep(10)

    def tweet(self,entry3):
        bot=self.bot
        bot.get('https://twitter.com/search?q='+str(entry3)+'&src=typed_query')
        while True:
            py.click(py.locateCenterOnScreen('like.png'))
            time.sleep(3)
            bot.execute.script('root.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)


#creating function for execute
def execute():
    log = twitter_bot(str(entry1.get()),str(entry2.get()))
    log.login()
    log.tweet(entry3.get())

#creating gui using tkinter

root = Tk()
root.geometry('700x600')

#creating gui for entering email
email = Label(root,text="Enter email id",font="times 24 bold")
email.grid(row=0,column=0)
entry1 = Entry(root)
entry1.grid(row=0,column=6)

#creating gui for entering password
password = Label(root,text="Enter password id",font="times 24 bold")
password.grid(row=2,column=0)
entry2 = Entry(root)
entry2.grid(row=2,column=6)

#creating gui for entering hashtag
hashtag = Label(root,text="Enter hashtag id",font="times 24 bold")
hashtag.grid(row=3,column=0)
entry3 = Entry(root)
entry3.grid(row=3,column=6)

#now creating button to execute

b1 = Button(root,text="Click Here!",command = execute, width=12 ,bg="red")
b1.grid(row=7,column=4)
root.mainloop()






    