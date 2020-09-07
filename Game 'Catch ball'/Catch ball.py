from tkinter import *
from random import randint as rnd, choice
import time
root = Tk()
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
n = 0
v = StringVar()
Label(root, textvariable=v).pack()


def tick():
    global x, y, R, v, n, ball_id, mx, my
    x += mx
    y += my
    if x + R > 800 or x - R < 0:
        mx *= -1
    if y + R > 600 or y - R < 0:
        my *= -1
    canv.move(ball_id, mx, my)
    root.after(10, tick)



    

def click(event):
    global x, y, R, n
    if event.x in range(x - R, x + R) and event.y in  range(y - R, y + R):
        n+=1
    else:
        n=0
    return n
    
    

def main():
    global x, y, R, root, v, n, ball_id, mx, my
    v.set("Score : "+ str(n))
    canv.delete(ALL)
    R = rnd(20, 50)
    x = rnd(100, 700)
    y = rnd(100, 500)
    mx, my = 1, 1
    colors = ['red','orange','yellow','green','blue']
    b1 = canv.bind('<Button-1>', click)
    ball_id = canv.create_oval(x-R, y-R, x+R, y+R, fill = choice(colors), width = 0)
    tick()
    root.mainloop()

main()

