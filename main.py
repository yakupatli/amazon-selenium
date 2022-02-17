from Siniflar import CheckGoogle
from tkinter import *
import tkinter as tk

def butonBas():
    Asin = e1.get()
    liste.grid(row=1, column=1)
    liste1.grid(row=9, column=1)
    liste2.grid(row=17, column=1)
    labelTr.grid(row=1,column=0)
    labelUsa.grid(row=9, column=0)
    labelNl.grid(row=17, column=0)
 #########################################################################################################
    test = CheckGoogle("https://www.amazon.com.tr", "C:/Users/ev/chromedriver.exe", Asin)
    data = test.RunR()
    ubil = test.urunBilgi(data)
    ubag = test.check_url(data)
    ubas = test.check_title(data)
    liste.insert(tk.END, ubil + "-------------")
    liste.insert(tk.END, ubag + "-------------")
    liste.insert(tk.END, ubas + "--------------")
    test.PageQuit(data)
 #######################################################################################################
    test1 = CheckGoogle("https://www.amazon.com", "C:/Users/ev/chromedriver.exe", Asin)
    data1 = test1.RunR()
    ubil = test.urunBilgi(data1)
    ubag = test.check_url(data1)
    ubas = test.check_title(data1)
    liste1.insert(tk.END, ubil + "-------------")
    liste1.insert(tk.END, ubag + "-------------")
    liste1.insert(tk.END, ubas + "--------------")
    test.PageQuit(data)
#############################################################################################################
    test = CheckGoogle("https://www.amazon.nl", "C:/Users/ev/chromedriver.exe", Asin)
    data = test.RunR()
    ubil = test.urunBilgi(data)
    ubag = test.check_url(data)
    ubas = test.check_title(data)
    liste2.insert(tk.END, ubil + "-------------")
    liste2.insert(tk.END, ubag + "-------------")
    liste2.insert(tk.END, ubas + "--------------")
    test.PageQuit(data)
 ########################################################################################################
    pencere.mainloop()

pencere=tk.Tk()
pencere.geometry("1366x768")
pencere.maxsize(width=1366,height=768)
e1 = tk.Entry(width=36)
e1.grid(row=0,column=1)
b1 = tk.Button(text="ARA", bg="black", fg="white", font="Arial 20 bold",command=butonBas)
b1.grid(row=0,column=2)
liste = tk.Text(pencere, height=8, width=140)
liste1 = tk.Text(pencere, height=8, width=140)
liste2 = tk.Text(pencere, height=8, width=140)
labelTr=tk.Label(pencere,text="TÜRKİYE")
labelUsa=tk.Label(pencere,text="AMERİKA")
labelNl=tk.Label(pencere,text="HOLLANDA")
pencere.mainloop()




#test.CookieOk(data)
#print(test.urunBilgi(data))
#print(test.check_url(data))
#print(test.check_title(data))



