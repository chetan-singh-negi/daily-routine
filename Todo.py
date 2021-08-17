from tkinter import *
tasklist=[]
counter=1
def click(event):
    global counter
    text=event.widget.cget("text")
    if(text=="submit"):
        value=scr.get()+"\n"
        tasklist.append(value)
        print(tasklist)
        T.insert(END,"["+str(counter)+"]"+value)
        counter=counter+1
        e1.update(scr.set(""))
    elif text=="delete":
        number=scr1.get()
        number=int(number)
        tasklist.pop(number-1)
        T.delete(1.0,END)
        counter=counter-1
        e2.update(scr1.set(""))
        for i in range(0,len(tasklist)):
            T.insert(END,"["+str(i+1)+"]"+tasklist[i])

        pass
    else:
        root.destroy()

root=Tk()
root.geometry("400x500")
root.title("ToDo app")
scr=StringVar()
scr.set("")
scr1=StringVar()
scr1.set("")
l1=Label(root,text="enter your task",fg="black",bg="yellow")
l1.pack()
e1=Entry(root,textvariable=scr)
e1.pack()
b1=Button(root,text="submit",fg="black",bg="red")
b1.pack()
b1.bind("<Button>",click)
T=Text(root,height=10,width=20)
T.pack()
l2=Label(root,text="delete task number",fg="black",bg="yellow")
l2.pack()
e2=Entry(root,textvariable=scr1)
e2.pack()
b2=Button(root,text="delete",fg="black",bg="red")
b2.pack()
b2.bind("<Button>",click)
b3=Button(root,text="Exit",fg="black",bg="red")
b3.pack()
b3.bind("<Button>",click)
root.mainloop()