#Import tkinter  from the class library 
import tkinter as tk 

#Create function for button click 
def button_click():
    print("Button clicked!")
#Create root window 
root = tk.Tk()
root.title("Button Example")

#Create the button object
button =  tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#Create a main loop
root.mainloop()