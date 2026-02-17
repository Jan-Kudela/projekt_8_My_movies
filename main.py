from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("My movies")
window.geometry("430x320")
window.resizable(False, False)

def add_text():
    list_box.insert(END, user_input.get()+ "\n")
    user_input.delete(0,END)

def remove_movie():
    """odstraní jeden film ze seznamu"""
    list_box.delete(ANCHOR)

def clear_list():
    """odstraní všechny položky ze seznamu"""
    list_box.delete(0, END)

def save_movie():
    """uloží film do textového souboru"""
    with open("filmy.txt", "w",) as file:
        my_tasks = list_box.get(0, END)
        for task in my_tasks:
            if task.endswith("\n"):
              file.write(f"{task}")  
            else:
                file.write(f"{task}\n")

def open_movies():
    try:
        with open("filmy.txt", "r") as file:
            for line in file:
                list_box.insert(END, line)
    
    except:
        print("Chyba při otevírání souboru filmy.txt.")

# framy
input_fr = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
buttons_frame = customtkinter.CTkFrame(window)
input_fr.pack()
text_frame.pack()
buttons_frame.pack()

#prvni frame
user_input = customtkinter.CTkEntry(
    input_fr, width=250,placeholder_text="Název filmu"
    )
user_input.grid(row=0, column=0, padx=5, pady=5)
button_input = customtkinter.CTkButton(
    input_fr, text="Přidat",width=50, command=add_text
    )
button_input.grid(row=0, column=1, padx=5, pady=5,)

#scrollbar - sticky - podle světových stran
list_box = Listbox(
    text_frame, height=12, width=45,bg="#4E4E4E",
    fg="white", font=("Helvetica", 12)
    )
list_box.grid(row=0, column=0, padx=0, pady=5)

scrollbar_txt = customtkinter.CTkScrollbar(text_frame,command=list_box.yview)
scrollbar_txt.grid(row=0, column=1)

list_box.config(yscrollcommand=scrollbar_txt.set)
#propojení scrollbaru s listboxem

#buttonframe
remove_button = customtkinter.CTkButton(
    buttons_frame, text="Odstranit film", width= 75, command=remove_movie)
clear_button = customtkinter.CTkButton(
    buttons_frame, text="Smazat seznam",width= 75, command=clear_list)
save_button = customtkinter.CTkButton(
    buttons_frame, text="Uložit",width=55, command=save_movie)
quit_button = customtkinter.CTkButton(
    buttons_frame, text="Zavřít", width=55, command=window.destroy)

remove_button.grid(row=0, column=0, padx=5, pady=5)
clear_button.grid(row=0, column=1, padx=5, pady=5)
save_button.grid(row=0, column=2,padx=5, pady=5)
quit_button.grid(row=0, column=3,padx=5, pady=5)

open_movies()

window.mainloop()