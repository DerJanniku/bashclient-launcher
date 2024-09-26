
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

class ModManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BashClient Mod Manager")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Mod Manager")
        self.label.pack(pady=10)
        
        self.mod_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.mod_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.load_mods_button = tk.Button(self, text="Load Selected Mods", command=self.load_selected_mods)
        self.load_mods_button.pack(pady=10)
        
        self.refresh_mod_list()
    
    def refresh_mod_list(self):
        self.mod_listbox.delete(0, tk.END)
        mods_path = os.path.join(os.getcwd(), "mods")
        for mod in os.listdir(mods_path):
            if mod.endswith(".jar"):
                self.mod_listbox.insert(tk.END, mod)
    
    def load_selected_mods(self):
        selected_mods = [self.mod_listbox.get(i) for i in self.mod_listbox.curselection()]
        minecraft_mods_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")
        if not os.path.exists(minecraft_mods_path):
            os.makedirs(minecraft_mods_path)
        for mod in selected_mods:
            mod_path = os.path.join(os.getcwd(), "mods", mod)
            subprocess.run(["copy", mod_path, minecraft_mods_path], shell=True)
        messagebox.showinfo("Success", "Selected mods loaded successfully!")

if __name__ == "__main__":
    app = ModManager()
    app.mainloop()
