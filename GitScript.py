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
        subprocess.Popen(['Git-2.42.0.2-64-bit.exe'])
        time.sleep(5) # Installer to start wait time

        # UAC (User Account Control) promt
        pyautogui.press('enter')

        # Git Setup Wizard setup
        time.sleep(2) # Wait for setup window to appear
        pyautogui.press('enter') # Accept GNU General Public License
        pyautogui.press('tab') # Move to Select Destination Location
        pyautogui.write('C:\\Program Files\\Git') # Set destination location
        pyautogui.press('enter')
        pyautogui.press('enter') # Accept default components
        pyautogui.press('enter') # Accept default Start Menu folder
        pyautogui.press('enter') # Use default editor
        pyautogui.press('enter') # Let Git decide initial branch
        pyautogui.press('enter') # Use Git from command line and thired-party software
        pyautogui.press('enter') # Use bundled OpenSSH
        pyautogui.press('enter') # Use OpenSSL library for HTTPS
        pyautogui.press('enter') # Configure line ending conversions
        pyautogui.press('enter') # Configure terminal emulator
        pyautogui.press('enter') # Choose default 'git pull' behavior
        pyautogui.press('enter') # Choose Git Credential Manager Core
        pyautogui.press('enter') # Enable file system caching
        pyautogui.press('enter') # Configure experimental options
        pyautogui.press('enter') # Complete Git Setup Wizard

        # Installation finish wait time
        while "Completing Git Setup Wizard" not in subprocess.check_output(['tasklist']).decode('utf-8'):
            time.sleep(2)

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
