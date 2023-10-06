import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

def check_local_repository():
    try:
        # Run a Git command to check for local repository
        subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def configure_git():
    # Check if local repository already exists
    if check_local_repository():
        messagebox.showinfo("Git Configuration", "Local Git repository already exists.")
    else:
        # Create Tkinter window
        window = tk.Tk()
        window.title("Git Configuration")

        # Create labels and entry fields for username and email
        name_label = tk.Label(window, text="Enter your name (first and last name): ")
        name_label.pack(padx=10, pady=5)
        name_entry = tk.Entry(window)
        name_entry.pack(padx=10, pady=5)

        email_label = tk.Label(window, text="Enter your email (GitHub account email): ")
        email_label.pack(padx=10, pady=5)
        email_entry = tk.Entry(window)
        email_entry.pack(padx=10, pady=5)

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

if __name__ == "__main__":
    configure_git()