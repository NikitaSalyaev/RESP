from tkinter import *
list = ['C', 'DEL', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '(', '0', ')', 'X^2']
def set_value(formula):
    if formula == '':
        label['text'] = '0'
    else:
        label['text']= str(eval(formula))
def logic(operator):
    if operator == 'C':
        set_value('')
    elif operator == 'DEL':
        label['text'] = label['text'][0:-1]
        if label['text'] == '':
            label['text'] == '0'
    elif operator == 'X^2':
        set_value(str((eval(label['text']))**2))
    elif operator == '=':
        set_value(label['text'])
    else:
        if label['text'] == '0':
            label['text'] = ''
        label['text']=label['text']+operator

root = Tk()
root['bg'] = 'green'
root.title('Сложный калькулятор!!!')
root.geometry('495x560')
root.resizable(False, False)
label = Label(root, text = '0', font= ('Consolas', 21, 'bold'), bg = 'green', fg = 'white')
label.place(x=10,y=50)
x=10
y=140
for lis in list:
    com = lambda x = lis: logic(x)
    Button(text=lis, bg='white',activebackground= 'red',font= ('Consolas', 15), command= com).place(x=x,y=y, width=115, height=80)
    x+=117
    if x > 400:
        x=10
        y+=82
root.mainloop()