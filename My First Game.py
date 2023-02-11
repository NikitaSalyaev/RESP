from tkinter import *
import random 
score, max_score = 0, 20
size_x, size_y = 1280, 800
def put():
    global button
    button = Button(root, text = 'НАЖМИ', width = 13, height= 3, bg= 'red', fg = 'blue', activebackground = 'lime', command = click)
    button.place(x = random.randint(50, size_x-50), y = random.randint(25, size_y-25))
def click():
    global score
    button.destroy()
    score += 1
    if  score < max_score:
        put()
    else:
        Label(root, text = 'Ты выиграл, \n красавчик!!!').place(relx=0.5,rely=0.5)
    
root = Tk()
root.title('Моя первая игруха')
root.geometry(f'{size_x}x{size_y}')
root.resizable(False, False)
put()
root.mainloop()