#task 1
#To Do list
from tkinter import *
from tkinter import ttk
import os
project=os.getcwd()
print(project)
root=Tk()
#add title and geometry
root.title("To-Do List application")
root.geometry("950x900")
root.resizable("false","false")
root.config(background="#79443B")
to_do_list=[]


#add label
label_1=Label(root,text="To-Do List application",font=('Castellar', 20),width=24, height=1, background="#ACE1AF")
label_1.pack(side="top")
label_2=Label(root,text="Add new task",font=('Castellar', 20),width=14, height=1, background="#ACE1AF")
label_2.pack(side="left")
label_2.place(x=40,y=140)
#get the new task from user
task= StringVar()
task.set("")
task_input =Entry(root,textvariable=task,width=60,font=("Arial",16),bd=0 )
task_input.pack()
task_input.place(x=40,y=180)
task_input.focus()
def addtask():
    global to_do_list
    task=task_input.get()
    task_input.delete(0,END)
    if task:
        with open("tasks.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        to_do_list.append(task)
        list_box.insert(END,task)
def deletetask ():
    global to_do_list
    task=str(list_box.get(ANCHOR))
    if task in to_do_list:
        to_do_list.remove(task)
        with open("tasks.txt",'w') as taskfile:
            for task in to_do_list:
                taskfile.write(task+"\n")
        list_box.delete(ANCHOR)

def openfile():
    try:
        global to_do_list
        with open("tasks.txt","r") as taskfile :
            tasks =taskfile.readlines()

        for task in tasks:
            if task!="\n":
                to_do_list.append(task)
                list_box.insert(END,task)
    except:
        file=open("tasks.txt","w")
        file.close()

#add button
add_btn=Button(root,text="Add",font=('Castellar', 20),background="#ACE1AF",width=4,height=1,bd=0,command=addtask)
add_btn.place(x=800,y=160)
#listbox
fram=Frame(root,bd=3,width=700,height=500,bg="#DAC8AE")
fram.pack(pady=(160,0))
fram.place(x=40,y=220)
list_box=Listbox(fram,font=("Arial",16),fg="black",width=40,height=20,bg="#DAC8AE",cursor="hand2")
list_box.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(fram)
scrollbar.pack(side=RIGHT,fill=BOTH)
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)
#delete_button
delete_btn=Button(root,text="Delete",bd=0,font=('Castellar', 20),background="dark red",fg="white",width=6,height=1,command=deletetask)
delete_btn.place(x=500,y=740)
#delete_btn.pack(pady=13)


root.mainloop()