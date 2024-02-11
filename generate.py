import random
import array
from tkinter import *
from tkinter import ttk

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
LOWER_CASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
UPPER_CASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '~', '>',  
           '*', '(', ')', '<']

COMBINED_LIST = DIGITS + UPPER_CASE_CHARACTERS + LOWER_CASE_CHARACTERS + SYMBOLS

def generate():
    rand_digit = random.choice(DIGITS) 
    rand_upper = random.choice(UPPER_CASE_CHARACTERS) 
    rand_lower = random.choice(LOWER_CASE_CHARACTERS) 
    rand_symbol = random.choice(SYMBOLS) 

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

    for x in range(MAX_LEN - 4): 
        temp_pass = temp_pass + random.choice(COMBINED_LIST) 
        temp_pass_list = array.array('u', temp_pass) 
        random.shuffle(temp_pass_list) 

    password = "" 
    for x in temp_pass_list: 
            password = password + x 
            
    final_password.set(password)
    copy_confirmation.set('')
    
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(final_password.get())
    copy_confirmation.set('Copied!')

root = Tk()
root.title("Ephemera")

mainframe = ttk.Frame(root, padding="20 20 20 20", borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0, sticky=N)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

final_password = StringVar()
copy_confirmation = StringVar()
password_return = ttk.Label(mainframe, textvariable=final_password).grid(column=2, row=1, sticky=N)

ttk.Button(mainframe,text="Generate PW", command=generate).grid(column=2, row=2, sticky=N)
ttk.Button(mainframe,text="Copy to Clipboard", command=copy_to_clipboard).grid(column=2, row=3, sticky=N)
copy_success_label = ttk.Label(mainframe, textvariable=copy_confirmation).grid(column=2, row=4, sticky=N)


for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

root.bind("<Return>, generate")

root.mainloop()