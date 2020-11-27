from tkinter import Tk, Text, Button, END, re, ttk, Frame

class Interface(ttk.Frame): 
    def __init__(self, window):
        self.window = window
        self.window.title("Delivery")
        #text field 
        self.textline = Text(window, state="disabled",width= 40, height = 3, foreground="white")
        #put the screen in the main window 
        self.textline.grid(row = 0, column = 0, columnspan=4, padx=5, pady=5)
        #init the order to ""
        self.order="What do you want to order?"
        #we create a button
        button1 = self.createButton("OK")
        button2 = self.createButton("CANCEL")

        #we put the buttons in a list to place them in the correct place 
        buttons = [button1, button2]
        buttons[0].grid(row = 2, column = 0)
        buttons[1].grid(row = 2, column = 1)

        #creates a combobox to select the order 
        combo = ttk.Combobox(window)
        combo.place(x=50, y=50)
        combo.grid(row=1, column =0)
        options = ["hamburger", "fries", "hotdog", "steak", "salad", "soup", "cake", "shake"]
        combo['values'] = options

    def createButton(self, value, width = 9, height = 1):
        return Button(self.window, text = value, width = width, height = height, command = lambda:self.click(value))

    def showInScreen(self, value): 
        self.textline.configure(state="normal")
        self.textline.insert(END, value)
        self.textline.configure(state="disabled")

    def click(self, text): 
        self.order+= str(text)
        self.showInScreen(text)

    def obtainInfo(self): 
        #complete the method 
        print("complete the method ")
        
#class Controller: 
    #controller class, MVC model 

main_window =Tk()
delivery = Interface(main_window)
main_window.mainloop()
