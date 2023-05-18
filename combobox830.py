#Import from the class libry.
import tkinter as tk
from tkinter import ttk

#Creating the function for event.
def on_select(event):

    #Create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
     
#Create root window.
root=tk.Tk()
root.title("Cristina is cool")

#Create an arrey item
items = ["Item1","Item 2","Item 3","Item4","Item5",]

#Create a combo box objects,put the objects in the root window and populate value. 
combo_box = ttk.Combobox(root, value=items)

#The bind function will tie the selected item to the on_selected function. 
combo_box.bind("<<ComboboxSelected>>",on_select)

#Pack the objects to the screen with the Geometry manager.
combo_box.pack()

#Mainloop keeps the root patent window visible.
root.mainloop()