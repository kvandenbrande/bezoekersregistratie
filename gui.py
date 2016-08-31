#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GUI:

    def __init__(self, master):
        
        master.title('Bezoekersregistratie')
        master.resizable(False, False)
        master.minsize(width=800, height=480)
        master.configure(background = '#FA9D00')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#FA9D00')
        self.style.configure('TButton', background = '#ADD8E6')
        self.style.configure('TLabel', background = '#FA9D00', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'kvkaw.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 5)
        ttk.Label(self.frame_header, wraplength = 600, text = 'Welkom bij Voka-Kamer van Koophandel Antwerpen-Waasland', style = 'Header.TLabel').grid(row = 1, column = 1)
        
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        
        ttk.Button(self.frame_content, text = 'BEZOEK / MEETING',
                   command = self.submit).grid(row = 4, column = 0, rowspan=2, padx = 5, pady = 5, sticky=W+E+N+S)
        ttk.Button(self.frame_content, text = 'OPLEIDING / EVENT',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        #messagebox.showinfo(title = 'Safety Feedback', message = 'Thank you for making you voice heard!')
    
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
         
def main():            
    
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    
if __name__ == "__main__": main()
