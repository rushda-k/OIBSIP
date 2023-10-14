import tkinter as tk
from tkinter import messagebox
import webbrowser

user_data = {
    "user1": "password1",
    "user2": "password2"
}

def register():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username in user_data:
        messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        user_data[new_username] = new_password
        messagebox.showinfo("Registration Successful", "You can now log in.")

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username in user_data and user_data[entered_username] == entered_password:
        messagebox.showinfo("Login Successful", f"Welcome, {entered_username}!")
        open_website()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_website():
    url = "https://oasisinfobyte.com"
    webbrowser.open(url)

# main window
window = tk.Tk()
window.title("Login Page")
window.geometry("1800x900")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.configure(bg ="teal")

new_username_label = tk.Label(window, text="New Username:",font=("helvetica", 45),bg="coral")
new_username_label.pack()
new_username_entry = tk.Entry(window,width=40,bd=20,bg="white")
new_username_entry.pack()

new_password_label = tk.Label(window, text="New Password:",font=("helvetica", 45),bg="coral")
new_password_label.pack()
new_password_entry = tk.Entry(window, show="*",width=40,bd=20,bg="white")
new_password_entry.pack()

register_button = tk.Button(window, text="Register", command=register,pady=0,font=("helvetica", 30),width=10,bd=5,bg="mediumseagreen")
register_button.pack()

separator = tk.Frame(height=2, bd=1, relief="ridge")
separator.pack(fill="x", padx=5, pady=5)

username_label = tk.Label(window, text="Username:",font=("helvetica", 45),bg="coral")
username_label.pack()
username_entry = tk.Entry(window,width=40,bd=20,bg="white")
username_entry.pack()

password_label = tk.Label(window, text="Password:",font=("helvetica", 45),bg="coral")
password_label.pack()
password_entry = tk.Entry(window, show="*",width=40,bd=20,bg="white")
password_entry.pack()

login_button = tk.Button(window, text="Login", command=login,pady=0,font=("helvetica", 30),width=10,bd=5,bg="mediumseagreen")
login_button.pack()

# main loop
window.mainloop()
