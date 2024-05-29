import tkinter as tk
from tkinter import messagebox
import os
import getpass

def display_welcome_message():
    print("WITAJ ZALOGUJ SIE I KONTYNUJ")
    print("============================")
    print("=======HASŁO DO ADMINA======")
    print("=========WPISZ HASŁO========")
    print("========hasło to admin =====")
    print("============================")

def log_activity(user_input):
    with open("log.txt", "a") as log_file:
        log_file.write(user_input + "\n")

def login(username, password):
    # Tutaj można dodać logikę weryfikacji hasła
    if username == "admin" and password == "admin":
        log_activity(f"Login successful for user: {username}")
        return True
    else:
        log_activity("Login failed")
        return False

def add_account():
    username = input("Enter new username: ")
    password = getpass.getpass("Enter new password: ")

    with open("accounts.txt", "a") as accounts_file:
        accounts_file.write(f"{username}:{password}\n")
    print("Account created successfully.")

def explore_files():
    files = os.listdir()
    print("Files in current directory:")
    for file in files:
        print(file)

def reset_system():
    print("Resetting the system...")
    # You can add reset logic here
    print("System reset complete.")

def run_command(command, is_logged_in):
    if is_logged_in:
        if command == "exit":
            print("Exiting Simple OS. Goodbye!")
            exit()
        elif command == "hello":
            print("Hello! Welcome to Simple OS.")
        elif command == "date":
            os.system("date")
        elif command == "time":
            os.system("time")
        elif command == "help" or command == "pomoc":
            print("Available commands:")
            print("hello - Display a greeting")
            print("date - Display the current date")
            print("time - Display the current time")
            print("help - Display this help message")
            print("exit - Logout and exit the system")
            print("add_account - Add a new account")
            print("explore_files - Explore files in the current directory")
            print("calc - karkurator")
            print("reset_system - Reset the system")
        elif command == "add_account":
            add_account()
        elif command == "explore_files":
            explore_files()
        elif command == "reset":
            reset_system()
        elif command == "calc":
            print("Calculator is not implemented yet.")
        else:
            print(f"Command '{command}' not recognized.")

        log_activity(command)
    else:
        print("Please login to access other commands.")

def on_login_button_click():
    username = username_entry.get()
    password = password_entry.get()
    if login(username, password):
        messagebox.showinfo("Login Successful", "Welcome to Simple OS!")
        login_window.destroy()
        show_command_window()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def show_command_window():
    def on_command_submit():
        command = command_entry.get()
        run_command(command, True)

    command_window = tk.Tk()
    command_window.title("Simple OS Command Interface")

    tk.Label(command_window, text="Enter Command:").pack()
    command_entry = tk.Entry(command_window)
    command_entry.pack()
    tk.Button(command_window, text="Submit", command=on_command_submit).pack()

    command_window.mainloop()

# Create login window
login_window = tk.Tk()
login_window.title("Simple OS Login")

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=on_login_button_click).pack()

login_window.mainloop()
