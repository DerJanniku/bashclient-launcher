
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

class BashClientLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BashClient Launcher")
        self.geometry("400x300")
        
        self.label = tk.Label(self, text="Welcome to BashClient!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.launch_button = tk.Button(self, text="Launch BashClient", command=self.launch_bashclient)
        self.launch_button.pack(pady=10)
        
        self.mods_button = tk.Button(self, text="Install Mods", command=self.install_mods)
        self.mods_button.pack(pady=10)
        
        self.translator_button = tk.Button(self, text="Run Auto-Translator", command=self.run_translator)
        self.translator_button.pack(pady=10)
        
        self.mod_manager_button = tk.Button(self, text="Open Mod Manager", command=self.open_mod_manager)
        self.mod_manager_button.pack(pady=10)
        
        self.fabric_button = tk.Button(self, text="Launch Minecraft with Fabric", command=self.launch_minecraft_with_fabric)
        self.fabric_button.pack(pady=10)
        
        self.update_button = tk.Button(self, text="Start Dynamic Update System", command=self.start_dynamic_update_system)
        self.update_button.pack(pady=10)
        
        self.pvp_tools_button = tk.Button(self, text="Start PvP Tools", command=self.start_pvp_tools)
        self.pvp_tools_button.pack(pady=10)
        
        self.performance_monitor_button = tk.Button(self, text="Start Performance Monitor", command=self.start_performance_monitor)
        self.performance_monitor_button.pack(pady=10)
        
        self.ui_customization_button = tk.Button(self, text="Start UI Customization", command=self.start_ui_customization)
        self.ui_customization_button.pack(pady=10)
        
        self.load_mods_button = tk.Button(self, text="Load Mods", command=self.load_mods)
        self.load_mods_button.pack(pady=10)
        
        self.unload_mods_button = tk.Button(self, text="Unload Mods", command=self.unload_mods)
        self.unload_mods_button.pack(pady=10)
        
        self.blender_button = tk.Button(self, text="Start Blender", command=self.start_blender)
        self.blender_button.pack(pady=10)
        
        self.backup_button = tk.Button(self, text="Backup to Cloud", command=self.backup_to_cloud)
        self.backup_button.pack(pady=10)
        
        self.restore_button = tk.Button(self, text="Restore from Cloud", command=self.restore_from_cloud)
        self.restore_button.pack(pady=10)
        
        self.social_features_button = tk.Button(self, text="Start Social Features", command=self.start_social_features)
        self.social_features_button.pack(pady=10)
        
    def launch_bashclient(self):
        try:
            bashclient_path = os.path.join(os.getcwd(), "BashClient", "bashclient.exe")
            subprocess.Popen([bashclient_path], shell=True)
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
                    shutil.copy(mod_path, minecraft_mods_path)
            messagebox.showinfo("Success", "Mods installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install mods: {e}")
    
    def open_mod_manager(self):
        try:
            mod_manager_path = os.path.join(os.getcwd(), "open_mod_manager.py")
            subprocess.Popen(["python", mod_manager_path])
            messagebox.showinfo("Success", "Mod Manager opened successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Mod Manager: {e}")

    def launch_minecraft_with_fabric(self):
        try:
            fabric_loader_path = os.path.join(os.getcwd(), "BashClient", "fabric", "versions", "fabric-loader-0.16.5-1.21.1", "fabric-loader-0.16.5-1.21.1.jar")
            minecraft_path = os.path.join(os.getenv("APPDATA"), ".minecraft")
            subprocess.Popen(["java", "-jar", fabric_loader_path, "--gameDir", minecraft_path])
            messagebox.showinfo("Success", "Minecraft launched with Fabric successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Minecraft with Fabric: {e}")

    def start_dynamic_update_system(self):
        try:
            dynamic_update_path = os.path.join(os.getcwd(), "dynamic_update.py")
            subprocess.Popen(["python", dynamic_update_path])
            messagebox.showinfo("Success", "Dynamic Update System started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Dynamic Update System: {e}")

    def start_pvp_tools(self):
        try:
            pvp_tools_path = os.path.join(os.getcwd(), "pvp_tools.py")
            subprocess.Popen(["python", pvp_tools_path])
            messagebox.showinfo("Success", "PvP Tools started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start PvP Tools: {e}")

    def start_performance_monitor(self):
        try:
            performance_monitor_path = os.path.join(os.getcwd(), "performance_monitor.py")
            subprocess.Popen(["python", performance_monitor_path])
            messagebox.showinfo("Success", "Performance Monitor started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Performance Monitor: {e}")

    def start_ui_customization(self):
        try:
            ui_customization_path = os.path.join(os.getcwd(), "ui_customization.py")
            subprocess.Popen(["python", ui_customization_path])
            messagebox.showinfo("Success", "UI Customization started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start UI Customization: {e}")

    def load_mods(self):
        try:
            mod_loader_path = os.path.join(os.getcwd(), "mod_loader.py")
            subprocess.Popen(["python", mod_loader_path])
            messagebox.showinfo("Success", "Mods loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load mods: {e}")

    def unload_mods(self):
        try:
            mod_loader_path = os.path.join(os.getcwd(), "mod_loader.py")
            subprocess.Popen(["python", mod_loader_path, "unload"])
            messagebox.showinfo("Success", "Mods unloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to unload mods: {e}")

    def start_blender(self):
        try:
            blender_integration_path = os.path.join(os.getcwd(), "blender_integration.py")
            subprocess.Popen(["python", blender_integration_path])
            messagebox.showinfo("Success", "Blender started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Blender: {e}")

    def backup_to_cloud(self):
        try:
            cloud_backup_path = os.path.join(os.getcwd(), "cloud_backup.py")
            subprocess.Popen(["python", cloud_backup_path])
            messagebox.showinfo("Success", "Backup to cloud completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to back up to cloud: {e}")

    def restore_from_cloud(self):
        try:
            cloud_backup_path = os.path.join(os.getcwd(), "cloud_backup.py")
            subprocess.Popen(["python", cloud_backup_path, "restore"])
            messagebox.showinfo("Success", "Restore from cloud completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restore from cloud: {e}")

    def start_social_features(self):
        try:
            social_features_path = os.path.join(os.getcwd(), "social_features.py")
            subprocess.Popen(["python", social_features_path])
            messagebox.showinfo("Success", "Social Features started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Social Features: {e}")

    def run_translator(self):
        try:
            translator_path = os.path.join(os.getcwd(), "translations", "run_translator.py")
            subprocess.Popen(["python", translator_path])
            messagebox.showinfo("Success", "Auto-Translator started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Auto-Translator: {e}")

if __name__ == "__main__":
    app = BashClientLauncher()
    app.mainloop()
