
import tkinter as tk
from tkinter import filedialog

def open_mod_manager():
    # Erstellt das Hauptfenster für den Mod-Manager
    mod_manager_window = tk.Tk()
    mod_manager_window.title("Mod Manager")
    mod_manager_window.geometry("500x400")
    
    # Labels und Buttons für die Mod-Verwaltung
    label = tk.Label(mod_manager_window, text="Verfügbare Mods:", font=("Arial", 12))
    label.pack(pady=10)
    
    mod_listbox = tk.Listbox(mod_manager_window, height=10, width=50)
    mod_listbox.pack(pady=10)
    
    # Dummy-Mods (diese kannst du durch eine dynamische Liste von Mods ersetzen)
    mods = ["Mod1", "Mod2", "Mod3"]
    for mod in mods:
        mod_listbox.insert(tk.END, mod)
    
    def add_mod():
        mod_file = filedialog.askopenfilename(title="Mod-Datei auswählen", filetypes=[("Mod-Dateien", "*.jar")])
        if mod_file:
            mod_listbox.insert(tk.END, mod_file.split('/')[-1])
    
    def remove_mod():
        selected_mod = mod_listbox.curselection()
        if selected_mod:
            mod_listbox.delete(selected_mod)
    
    add_button = tk.Button(mod_manager_window, text="Mod hinzufügen", command=add_mod)
    add_button.pack(pady=5)

    remove_button = tk.Button(mod_manager_window, text="Mod entfernen", command=remove_mod)
    remove_button.pack(pady=5)
    
    # Startet das Tkinter-Fenster
    mod_manager_window.mainloop()
