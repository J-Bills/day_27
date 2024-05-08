import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=200, height=400)


#Entry - button
miles_input = tkinter.Entry()
miles_input.grid(row=0,column=1)

#Labels
label1 = tkinter.Label(text="Miles")
label1.grid(row=0, column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1, column=0)

km_label = tkinter.Label(text="0")
km_label.grid(row=1, column=1)

label3 = tkinter.Label(text="Km")
label3.grid(row=1, column=2)

#Button
def button_click():
    miles = miles_input.get()
    result = 1.61*int(miles)
    km_label.config(text=result)

calc_button = tkinter.Button(text="Calculate", command=button_click)
calc_button.grid(row=2,column=1)




window.mainloop()