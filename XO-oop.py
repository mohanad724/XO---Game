import tkinter as tk
from tkinter import *
import numpy as np
import tkinter.font as font 

window = tk.Tk()
window.title("xo game")
window.geometry("500x500")
myFont = font.Font(family='Courier', size=15, weight='bold', slant="roman" )

m = ""

state = ['0','1','2','3','4','5','6','7','8']
newarr = np.array(state)
arr =  newarr.reshape(3, 3)

class button:
    def __init__(self,i,j):
        self.i = i,j
        

        btn = tk.Button(text = "", height=4 , width=8 ,bg='#0052cc', fg='#ffffff',command= lambda: self.btn_txt(btn))
        btn.grid(row=i,  column= j)

    def btn_txt(self,btn):
        
        if btn['text'] == "":
            m = next_value()
            btn['text'] =  m 
            arr[self.i] = m
            Winner(arr)
            
           
def next_value():
        global m 
        
        if m == "X" :
            m = "O"
            turn['text'] = "Now Turn Is X "
        else :
            m = "X"
            turn['text'] = "Now Turn Is O"
        return m


def buttons(arr):
    for i in range(0,arr.shape[0]):
        for j in range(0,arr.shape[1]):
            button(i,j)

def Winner(arr):
    print(arr)
    for i in range(3):
		
        A = arr[i,:]
        B = arr[:,i]
        C = arr[0,0] == arr[1,1] == arr[2,2] == "X"
        D = arr[0,2] == arr[1,1] == arr[2,0] == "X"
        E = arr[0,0] == arr[1,1] == arr[2,2] == "O"
        F = arr[0,2] == arr[1,1] == arr[2,0] == "O"

        if np.all(A =='X') or np.all(B == 'X') or C or D : 
            leb_win['text'] = ['X  is win!!!!']

        elif np.all(A == "O") or np.all(B =="O") or E or F :
            leb_win['text'] = ['O  is win!!!!']
	
turn = tk.Label(window, text = "Now Turn Is X ", bg='#12125c',fg="Red", font=("Helvetica", 18))
turn.grid(row=0,column=6)
leb_win = tk.Label(window, text = "start", bg='#000000',fg="Red", font=("Helvetica", 18))


leb_win['font'] = myFont
leb_win.grid(row= 1, column=6)
    
buttons(arr)


window.mainloop()

