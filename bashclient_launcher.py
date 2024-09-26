
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

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

if __name__ == "__main__":
    app = BashClientLauncher()
    app.mainloop()
