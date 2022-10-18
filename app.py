# Kevin Hayden
# CS361

# Code Adapted/Based/Copied from the following:
# https://pythonguides.com/python-tkinter-table-tutorial/
# https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import *
from  tkinter import ttk

# UI colors from darkest to lightest
# #080808 Vampire Black
# #676767 Granite Gray
# #808080 Gray
# #A9A9A9 X11 Dark Gray
# #BEBEBE X11 Gray

ws  = Tk()
ws.title('Leet Gains')
ws.geometry('1280x720')
ws['bg'] = '#676767'

app_dirs = "Add, edit or delete your workouts."

# Create label
l = Label(ws, text = "Leet Gains")
l.config(font =("Magneto", 14))
l.pack(pady=10)

dirs = Label(ws, text = "Add, Edit or Delete Exercises")
dirs.config(font = ("Arial", 11))
dirs.pack(pady=10)

app_frame = Frame(ws)
app_frame.pack(pady=10)

my_app = ttk.Treeview(app_frame)

my_app.pack()

#define our column
my_app['columns'] = ('Exercise', 'Reps', 'Weight')

# format our column
my_app.column("#0", width=0, stretch=NO)
my_app.column("Exercise",anchor=CENTER, width=160)
my_app.column("Reps",anchor=CENTER,width=160)
my_app.column("Weight",anchor=CENTER,width=160)

#Create Headings 
my_app.heading("#0",text="",anchor=CENTER)
my_app.heading("Exercise",text="Exercise",anchor=CENTER)
my_app.heading("Reps",text="Reps",anchor=CENTER)
my_app.heading("Weight",text="Weight",anchor=CENTER)

#add data 
my_app.insert(parent='',index='end',iid=0,text='',
values=('Bench','10','250'))
my_app.insert(parent='',index='end',iid=1,text='',
values=('Squat','10','250'))
my_app.insert(parent='',index='end',iid=2,text='',
values=('Deadlift','10','400'))
my_app.insert(parent='',index='end',iid=3,text='',
values=('Butterflies','10','100'))

my_app.pack()

frame = Frame(ws)
frame.pack(pady=20)

#labels
exercise= Label(frame,text = "Exercise")
exercise.grid(row=0,column=0 )

reps = Label(frame,text="Reps")
reps.grid(row=0,column=1)

weight = Label(frame,text="Weight")
weight.grid(row=0,column=2)

#Entry boxes
exercise_entry= Entry(frame)
exercise_entry.grid(row= 1, column=0)

rep_entry = Entry(frame)
rep_entry.grid(row=1,column=1)

weight_entry = Entry(frame)
weight_entry.grid(row=1,column=2)

#Select Record
def select_record():
    #clear entry boxes
    exercise_entry.delete(0,END)
    rep_entry.delete(0,END)
    weight_entry.delete(0,END)
    
    #grab record
    selected=my_app.focus()
    #grab record values
    values = my_app.item(selected,'values')
    #temp_label.config(text=selected)

    #output to entry boxes
    exercise_entry.insert(0,values[0])
    rep_entry.insert(0,values[1])
    weight_entry.insert(0,values[2])

#save Record
def update_exercise():
    selected=my_app.focus()
    #save new data 
    my_app.item(selected,text="",values=(exercise_entry.get(),rep_entry.get(),weight_entry.get()))
    
   #clear entry boxes
    exercise_entry.delete(0,END)
    rep_entry.delete(0,END)
    weight_entry.delete(0,END)

#Buttons
select_button = Button(ws,text="Select Exercise", command=select_record)
select_button.pack(pady =10)

add_button = Button(ws, text="Add")
add_button.pack(pady = 10)

edit_button = Button(ws,text="Edit",command=update_exercise)
edit_button.pack(pady = 10)

delete_button = Button(ws, text="Delete")
delete_button.pack(pady = 10)

ws.mainloop()
