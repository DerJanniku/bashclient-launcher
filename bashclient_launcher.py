
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from mod_manager import ModManager
from installer import Installer
from marketplace import Marketplace

class BashClientLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BashClient Launcher")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Welcome to BashClient!")
        self.label.pack(pady=10)
        
        self.launch_button = tk.Button(self, text="Launch BashClient", command=self.launch_bashclient)
        self.launch_button.pack(pady=10)
        
        self.mods_button = tk.Button(self, text="Install Mods", command=self.install_mods)
        self.mods_button.pack(pady=10)
        
        self.custom_mods_button = tk.Button(self, text="Load Custom Mods", command=self.load_custom_mods)
        self.custom_mods_button.pack(pady=10)
        
        self.mod_manager_button = tk.Button(self, text="Open Mod Manager", command=self.open_mod_manager)
        self.mod_manager_button.pack(pady=10)
        
        self.installer_button = tk.Button(self, text="Open Installer", command=self.open_installer)
        self.installer_button.pack(pady=10)
        
        self.marketplace_button = tk.Button(self, text="Open Marketplace", command=self.open_marketplace)
        self.marketplace_button.pack(pady=10)
        
    def launch_bashclient(self):
        try:
            bashclient_path = os.path.join(os.getcwd(), "BashClient", "bashclient.exe")
            subprocess.Popen([bashclient_path])
            messagebox.showinfo("Success", "BashClient launched successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch BashClient: {e}")
    
    def install_mods(self):
        try:
            mods_path = os.path.join(os.getcwd(), "mods")
            minecraft_mods_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")
            if not os.path.exists(minecraft_mods_path):
                os.makedirs(minecraft_mods_path)
            for mod in os.listdir(mods_path):
                mod_path = os.path.join(mods_path, mod)
                if os.path.isfile(mod_path):
                    subprocess.run(["copy", mod_path, minecraft_mods_path], shell=True)
            messagebox.showinfo("Success", "Mods installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install mods: {e}")
    
    def load_custom_mods(self):
        try:
            custom_mods_path = os.path.join(os.getcwd(), "custom_mods")
            for mod in os.listdir(custom_mods_path):
                mod_path = os.path.join(custom_mods_path, mod)
                if os.path.isfile(mod_path) and mod_path.endswith('.py'):
                    subprocess.Popen(["python", mod_path])
            messagebox.showinfo("Success", "Custom mods loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load custom mods: {e}")
    
    def open_mod_manager(self):
        try:
            mod_manager = ModManager()
            mod_manager.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Mod Manager: {e}")
    
    def open_installer(self):
        try:
            installer = Installer()
            installer.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Installer: {e}")
    
    def open_marketplace(self):
        try:
            marketplace = Marketplace()
            marketplace.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Marketplace: {e}")

if __name__ == "__main__":
    app = BashClientLauncher()
    app.mainloop()
