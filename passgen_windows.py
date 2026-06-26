import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import os
import sys


def generate_password():

    length = length_var.get()

    if length < 8 or length > 16:
        messagebox.showerror(
            "Error",
            "Password length must be between 8 and 16."
        )
        return

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!$@.%#&*"

    all_chars = letters + numbers + symbols

    password = ""

    for _ in range(length):
        password += random.choice(all_chars)

    password_var.set(password)

    status_var.set("Password generated.")


def copy_password():

    password = password_var.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    status_var.set("Password copied.")


def open_passwords():

    if not os.path.exists("passwords.txt"):

        messagebox.showinfo(
            "Info",
            "No passwords saved yet."
        )

        return

    if sys.platform.startswith("win"):

        os.startfile("passwords.txt")

    elif sys.platform.startswith("linux"):

        os.system("xdg-open passwords.txt")

    elif sys.platform == "darwin":

        os.system("open passwords.txt")


def save_password():

    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_var.get()

    if website == "":
        messagebox.showwarning(
            "Warning",
            "Enter website/account name."
        )
        return

    if username == "":
        messagebox.showwarning(
            "Warning",
            "Enter username/email."
        )
        return

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    try:

        if not os.path.exists("passwords.txt"):

            with open("passwords.txt", "w", encoding="utf-8") as file:

                file.write(
                    "Platform            Username/Email                 Password\n"
                )

                file.write(
                    "-" * 80 + "\n"
                )

        with open("passwords.txt", "a", encoding="utf-8") as file:

            file.write(
                f"{website:<20} {username:<30} {password}\n"
            )

        status_var.set("Password saved.")

        messagebox.showinfo(
            "Success",
            "Password saved to passwords.txt"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# MAIN WINDOW

root = tk.Tk()

root.title("PassGen Windows v1.0")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#121212")

# TITLE

title_label = tk.Label(
    root,
    text="PASSGEN WINDOWS",
    font=("Segoe UI", 20, "bold"),
    bg="#121212",
    fg="#ccff00"
)

title_label.pack(pady=10)

# WEBSITE

website_label = tk.Label(
    root,
    text="Website / Account:",
    bg="#121212",
    fg="white",
    font=("Segoe UI", 10)
)

website_label.pack()

website_entry = tk.Entry(
    root,
    width=50,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 10)
)

website_entry.pack(pady=5)

# USERNAME

username_label = tk.Label(
    root,
    text="Username / Email:" ,
    bg="#121212",
    fg="white",
    font=("Segoe UI", 10)
)

username_label.pack()

username_entry = tk.Entry(
    root,
    width=50,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 10)
)

username_entry.pack(pady=5)

# PASSWORD LENGTH

length_label = tk.Label(
    root,
    text="Password Length (8-16):" ,
    bg="#121212",
    fg="white",
    font=("Segoe UI", 10)
)

length_label.pack()

length_var = tk.IntVar(value=16)

length_spinbox = tk.Spinbox(
    root,
    from_=8,
    to=16,
    textvariable=length_var,
    width=10,
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 10)
)

length_spinbox.pack(pady=5)

# PASSWORD

password_label = tk.Label(
    root,
    text="Generated Password:" ,
    bg="#121212",
    fg="white",
    font=("Segoe UI", 10)

)

password_label.pack()

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=50,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 10),
    justify="center"
)

password_entry.pack(pady=10)

# BUTTONS

generate_button = tk.Button(
    root,
    text="Generate Password",
    width=25,
    bg="#ccff00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    command=generate_password
)

generate_button.pack(pady=5)

copy_button = tk.Button(
    root,
    text="Copy Password",
    width=25,
    bg="#ccff00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    command=copy_password
)

copy_button.pack(pady=5)

save_button = tk.Button(
    root,
    text="Save Password",
    width=25,
    bg="#ccff00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    command=save_password
)

save_button.pack(pady=5)

my_passwords_button = tk.Button(
    root,
    text="My Passwords",
    width=25,
    bg="#ccff00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    command=open_passwords
)

my_passwords_button.pack(pady=5)

# STATUS

status_var = tk.StringVar()
status_var.set("Ready")

status_label = tk.Label(
    root,
    textvariable=status_var,
    bg="#121212",
    fg="#ccff00",
    font=("Segoe UI", 10, "bold")
)

status_label.pack(pady=15)

root.mainloop()