import tkinter

window = tkinter.Tk()

window.title("My First Gui Program")
window.minsize(width= 500, height=500)
window.config(padx=20,pady=20)

#Label

my_label = tkinter.Label(text= "This is a label")

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Button2

button = tkinter.Button(text="Click Me Harder", command=button_clicked)
button.grid(column=2,row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)









window.mainloop()