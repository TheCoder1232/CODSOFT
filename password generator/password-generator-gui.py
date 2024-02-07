from tkinter import *
from tkinter import messagebox
import random

class PasswordGeneratorGUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x100")
        self.root.title("Password Generator")
        self.root.iconbitmap(r"E:\Aditya\development\Programming\python_work\Internship Projects\password generator\show-password.ico")
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                          'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                          'U', 'V', 'W', 'X', 'Y', 'Z']
        self.symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '=']

    def generatePassword(self):
        length = self.password_length_entry.get()
        if length.isdigit() and int(length)>0:
            password = ""
            combined = self.numbers + self.lowercase + self.uppercase + self.symbols
            for _ in range(int(length)):
                password += str(random.choice(combined))
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, password)
        else:
            messagebox.showerror("Error", "Enter a valid password length.")
    
    def copy_password(self):
        self.root.clipboard_append(self.password_entry.get())
    
    def run(self):
        length_label = Label(self.root, text="Enter length of password:")
        length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.password_length_entry = Entry(self.root)
        self.password_length_entry.grid(row=0, column=1, padx=10, pady=5)

        generate_button = Button(self.root, text="Generate", command=self.generatePassword)
        generate_button.grid(row=0, column=2, padx=10, pady=5)

        self.password_entry = Entry(self.root)
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        copy_button = Button(self.root, text="Copy", command=self.copy_password)
        copy_button.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        self.root.mainloop()
    
if __name__ == "__main__":
    pg = PasswordGeneratorGUI()
    pg.run()
