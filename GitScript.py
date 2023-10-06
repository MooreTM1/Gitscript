"""

This is a script that will install
Git on a computer if Git is not
installed already and check if
Git is installed and what version.

"""

import os
import subprocess
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
from pywinauto import Application

def is_git_installed():
    try:
        subprocess.check_output(['git', '--version'])
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
    
def install_git():
    # Check if Git is installed
    if is_git_installed():
        print("Git is already installed.")
        latest_version = subprocess.check_output(['git', '--version']).decode('utf-8').strip()
        pyautogui.alert(f"Git is on the latest version:\n{latest_version}", "Git Installation")
    else:
        # Git is not installed, continue with installion
        print("Installing Git...")
        
        # Run Git installer
        installer_path = 'Git-2.42.0.2-64-bit.exe'
        app = Application(backend="uia").start(installer_path)

        # Git Setup Wizard to appear
        dlg = app['Git Setup Wizard']
        dlg.wait('visible', timeout=60)
        
        # Installation automated steps
        dlg.type_keys('{ENTER}') # Accept GNU General Public License
        dlg.type_keys('{TAB}') # Move to Select Destination Location
        dlg.type_keys('C:\\Program Files\\Git') # Set destination location
        dlg.type_keys('{ENTER}')
        dlg.type_keys('{ENTER}') # Accept default components
        dlg.type_keys('{ENTER}') # Accept default Start Menu folder
        dlg.type_keys('{ENTER}') # Use default editor
        dlg.type_keys('{ENTER}') # Let Git decide initial branch
        dlg.type_keys('{ENTER}') # Use Git from command line and thired-party software
        dlg.type_keys('{ENTER}') # Use bundled OpenSSH
        dlg.type_keys('{ENTER}') # Use OpenSSL library for HTTPS
        dlg.type_keys('{ENTER}') # Configure line ending conversions
        dlg.type_keys('{ENTER}') # Configure terminal emulator
        dlg.type_keys('{ENTER}') # Choose default 'git pull' behavior
        dlg.type_keys('{ENTER}') # Choose Git Credential Manager Core
        dlg.type_keys('{ENTER}') # Enable file system caching
        dlg.type_keys('{ENTER}') # Configure experimental options
        dlg.type_keys('{ENTER}') # Complete Git Setup Wizard

        # Installation finish wait time
        app.wait_not('visible', timeout=600)
        
        # Completion message
        pyautogui.alert("Git has successfully installed!", "Git Installation")

def install_button_clicked():
    # Check if Git is installed before installing
    if is_git_installed():
        messagebox.showinfo("Git Installtion", "Git is already installed")
    else:
        install_git()
        messagebox.showinfo("Git Installation", "Git installion has started.")

if __name__ == "__main__":
    # Create Tkinter window
    window = tk.Tk()
    window.title("Git Installer")

    window.geometry("800x500")

    # Create label
    label = tk.Label(window, text="Git Installer")
    label.pack(pady=40)

    # Create install button
    install_button = tk.Button(window, text="Install Git", command=install_button_clicked)
    install_button.pack()

    # Run Tkinter event loop
    window.mainloop()
