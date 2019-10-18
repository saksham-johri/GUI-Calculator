from tkinter import *
import parser
 
root = Tk()
root.title('Calculator')
 
#get the user input and place it in the textfield
i = 0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
 
def clear_all():
    display.delete(0,END)
 
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)


#adding the input field
display = Entry(root,font=('arial',35,'bold'), bd=20, insertwidth = 3, bg = "#bce4eb", justify = 'right')
display.grid(row=1,columnspan=6)

 
#adding buttons to the calculator
 
Button(root,text="1",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(1)).grid(row=2,column=0)
Button(root,text="2",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(2)).grid(row=2,column=1)
Button(root,text="3",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(3)).grid(row=2,column=2)
 
Button(root,text="4",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(4)).grid(row=3,column=0)
Button(root,text="5",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(5)).grid(row=3,column=1)
Button(root,text="6",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(6)).grid(row=3,column=2)
 
Button(root,text="7",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(7)).grid(row=4,column=0)
Button(root,text="8",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(8)).grid(row=4,column=1)
Button(root,text="9",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(9)).grid(row=4,column=2)
 
#adding other buttons to the calculator
Button(root,text="AC",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command=clear_all).grid(row=5,column=0)
Button(root,text="0",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command = lambda :get_variables(0)).grid(row=5,column=1)
Button(root,text="=",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command=lambda :calculate()).grid(row=5,column=2)
 
 
Button(root,text="+",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("+")).grid(row=2,column=3)
Button(root,text="-",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("-")).grid(row=3,column=3)
Button(root,text="*",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("*")).grid(row=4,column=3)
Button(root,text="/",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("/")).grid(row=5,column=3)
 
# adding new operations
Button(root,text="pi",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("*3.14")).grid(row=2,column=4)
Button(root,text="%",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("%")).grid(row=3,column=4)
Button(root,text="(",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("(")).grid(row=4,column=4)
Button(root,text="^x",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("**")).grid(row=5,column=4)
 
Button(root,text="<-",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :undo()).grid(row=2,column=5)
Button(root,text="x!",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold')).grid(row=3,column=5)
Button(root,text=")",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation(")")).grid(row=4,column=5)
Button(root,text="^2",padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),command= lambda :get_operation("**2")).grid(row=5,column=5)
 
 
root.mainloop()
