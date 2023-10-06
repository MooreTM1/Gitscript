import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

def check_local_repository():
    try:
        # Run a Git command to check for local repository
        subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def create_local_repository(directory):
    # Initialize a new Git repository in specified directory
    subprocess.run(['git', 'init', directory])

def configure_git():
    if check_local_repository():
        # Git repository already extist
        create_new_repo = messagebox.askyesno("Git Configuration", "A Git repository already exists. Would you like to create another one?")

        if not create_new_repo:
            return
    # Choose location for Git repository directory
    directory = simpledialog.askstring("Git Configuration", "Enter path to directory for Git repository: ")

    if not directory:
        return
    
    # Create new local Git repository
    create_local_repository(directory)

    # Create Tkinter window
    window = tk.Tk()
    window.title("Git Configuration")

    # Create labels and entry fields for username and email
    name_label = tk.Label(window, text="Enter your name (first and last name): ")
    name_label.pack(padx=30, pady=15)
    name_entry = tk.Entry(window)
    name_entry.pack(padx=30, pady=15)

    email_label = tk.Label(window, text="Enter your email (GitHub account email): ")
    email_label.pack(padx=30, pady=15)
    email_entry = tk.Entry(window)
    email_entry.pack(padx=30, pady=15)

    # Git configurations set and display success message
    def set_git_configurations():
        name = name_entry.get()
        email = email_entry.get()

        # Set Git username and email
        subprocess.run(['git', 'config', '--global', 'user.name', name])
        subprocess.run(['git', 'config', '--global', 'user.email', email])

        # Set default branch to main
        subprocess.run(['git', 'config', '--global', 'init.defaultBranch', 'main'])

        # Close Tkinter window
        window.destroy()

        # Display success message
        messagebox.showinfo("Git Configuration", "Local Git repository has been made.")

    # Create "Configure Git" button
    configure_button = tk.Button(window, text="Cofigure Git", command=set_git_configurations)
    configure_button.pack(pady=10)

    # Run Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    configure_git()