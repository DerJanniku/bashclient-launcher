
import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

class Installer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BashClient Installer")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Welcome to BashClient Installer!")
        self.label.pack(pady=10)
        
        self.install_button = tk.Button(self, text="Install BashClient", command=self.install_bashclient)
        self.install_button.pack(pady=10)
        
        self.backup_button = tk.Button(self, text="Backup Settings and Worlds", command=self.backup_data)
        self.backup_button.pack(pady=10)
        
    def install_bashclient(self):
        try:
            # Assuming the BashClient files are in the 'BashClient' directory
            bashclient_path = os.path.join(os.getcwd(), "BashClient")
            install_path = filedialog.askdirectory(title="Select Installation Directory")
            if install_path:
                shutil.copytree(bashclient_path, os.path.join(install_path, "BashClient"))
                messagebox.showinfo("Success", "BashClient installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install BashClient: {e}")
    
    def backup_data(self):
        try:
            backup_path = filedialog.askdirectory(title="Select Backup Directory")
            if backup_path:
                minecraft_path = os.path.join(os.getenv("APPDATA"), ".minecraft")
                backup_minecraft_path = os.path.join(backup_path, ".minecraft_backup")
                shutil.copytree(minecraft_path, backup_minecraft_path)
                messagebox.showinfo("Success", "Settings and worlds backed up successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to backup data: {e}")

if __name__ == "__main__":
    app = Installer()
    app.mainloop()
