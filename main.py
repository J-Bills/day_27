import tkinter

window = tkinter.Tk()

window.title("My First Gui Program")
window.minsize(width= 500, height=500)


#label

my_label = tkinter.Label(text= "This is a label")
my_label.pack()

#advanced arguments

#There are default arguments for some functions that could be changed specifically but if not already hold a value
#multipy(a=5,b=4,c=6)


#unlimited positional arguments(**args)
#multiply(*args)

def add(*args):
    result = 0
    for num in args:
        result+=num
        print(result)

add(1,4,8,0,456,3)
add(1,2,3)

#arguments get entered as a tuple object

#unlimited keyword arguments(**kwargs)

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
        
    n += kwargs["add"]
    n *= kwargs["multiply"]
    
calculate(5, add=1, multiply=6)
#arguments get entered as a dictionary

class Car:
    def __init__(self,**kwargs) -> None:
        #using get allows us to have a default None val if no argument passed
        self.make = kwargs.get('make')
        self.model = kwargs.get("model")
        
my_car = Car(make="Nissan")
print(my_car)































window.mainloop()