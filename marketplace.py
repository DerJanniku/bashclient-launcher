
import os
import tkinter as tk
import shutil
from tkinter import messagebox, filedialog

class Marketplace(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BashClient Marketplace")
        self.geometry("600x400")
        
        self.label = tk.Label(self, text="Welcome to BashClient Marketplace!")
        self.label.pack(pady=10)
        
        self.mod_listbox = tk.Listbox(self, height=15, width=50)
        self.mod_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.install_button = tk.Button(self, text="Install Selected Mod", command=self.install_mod)
        self.install_button.pack(pady=10)
        
        self.refresh_mod_list()
    
    def refresh_mod_list(self):
        self.mod_listbox.delete(0, tk.END)
        # Dummy list of mods (replace with actual mod repository)
        mods = ["Mod1", "Mod2", "Mod3"]
        for mod in mods:
            self.mod_listbox.insert(tk.END, mod)
    
    def install_mod(self):
        selected_mod = self.mod_listbox.get(tk.ACTIVE)
        if selected_mod:
            mod_file = filedialog.askopenfilename(title="Select Mod File", filetypes=[("Mod Files", "*.jar")])
            if mod_file:
                minecraft_mods_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")
                if not os.path.exists(minecraft_mods_path):
                    os.makedirs(minecraft_mods_path)
                shutil.copy(mod_file, minecraft_mods_path)
                messagebox.showinfo("Success", f"{selected_mod} installed successfully!")
        else:
            messagebox.showerror("Error", "No mod selected!")

if __name__ == "__main__":
    app = Marketplace()
    app.mainloop()
