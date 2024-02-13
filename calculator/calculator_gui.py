from tkinter import *

class GUICalculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("320x520")
        self.root.resizable(0, 0)
        self.root.title("Calculator GUI")
        self.root.iconbitmap(r"E:\Aditya\development\Programming\python_work\Internship Projects\calculator\calculator-icon.ico")
        self.expr = ""

    def buttonClicked(self, newExpr):
        self.expr = self.expr + str(newExpr)
        self.input_text.set(self.expr)

    def clearInputFrame(self):
        self.expr = "" 
        self.input_text.set("")

    def evaluateEquation(self):
        try:
            result = str(eval(self.expr))
            self.expr = result
        except ZeroDivisionError:
            result = "Cannot Divide by Zero"
        self.input_text.set(result)

    def removeLastExpr(self):
        self.expr = self.expr[:-1]
        self.input_text.set(self.expr)

    def negateExpr(self):
        self.expr = str((-1)*eval(self.expr))
        self.input_text.set(self.expr)

    def run(self):
        self.input_text = StringVar()
        inputFrame = Frame(self.root, width=310, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        inputFrame.place(x=5, y=20)

        input_field = Entry(inputFrame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=22, bg="#eee", bd=0, justify=RIGHT)
        input_field.grid(row=0, column=0)
        input_field.place(x=5, y=9)
        
        btns_frame = Frame(self.root, width=310, height=300, bg="grey")
        btns_frame.place(x=5, y=85)

        clear = Button(btns_frame, text = "C", fg = "black", width = 21, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.clearInputFrame()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
        delete = Button(btns_frame, text = "<x", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.removeLastExpr()).grid(row = 0, column = 2, columnspan = 1, padx = 1, pady = 1)
        divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.buttonClicked("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

        seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
        eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
        nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(9)).grid(row = 1, column = 2, padx = 1, pady = 1)    
        multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.buttonClicked("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
         
        four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
        five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
        six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
        minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.buttonClicked("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
        one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
        two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
        three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
        plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.buttonClicked("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
        negate = Button(btns_frame, text = "+/-", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.negateExpr()).grid(row = 4, column = 0, columnspan = 1, padx = 1, pady = 1)
        zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: self.buttonClicked(0)).grid(row = 4, column = 1, columnspan = 1, padx = 1, pady = 1)
        point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.buttonClicked(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: self.evaluateEquation()).grid(row = 4, column = 3, padx = 1, pady = 1)

        self.root.mainloop()

if __name__ == "__main__":
    calculator = GUICalculator()
    calculator.run()


