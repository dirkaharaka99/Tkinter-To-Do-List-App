from tkinter import *
from tkinter import font
from tkinter.font import Font


root = Tk()
root.title("Dirqa todo list")
root.iconbitmap()
root.geometry("500x500")

#define our font
my_font = Font(
    family= "Brush Script MT",
    size= 30,
    weight= "bold",
)

#create frame
my_frame = Frame(root)
my_frame.pack(pady = 10)

my_list = Listbox(my_frame,
    font= my_font,
    width= 25,
    height = 5,
    bg= "#FFFA4D", 
    bd = 0,
    fg= "purple",
    highlightthickness=0,
    selectbackground="orange",
    activestyle="none",
    
)
my_list.pack(side=LEFT, fill=BOTH)

#create dumy list
stuff = ["Learn Coding", "Go to work", "Play games", "Learn Python", "football", "Drink", "Watching film"]

#add dummy list to listbox
for item in stuff:
    my_list.insert(END, item)

#create scroolbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview) 

#create entry box
my_entry = Entry(root, font= ("Helvetica", 24))
my_entry.pack(pady=20)

#create button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#FUNCTION
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    pass

def uncross_item():
    pass

#add some button
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx = 10)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx = 10)

root.mainloop()