import os
import shutil

def load_mods(mods_directory, minecraft_mods_directory):
    if not os.path.exists(minecraft_mods_directory):
        os.makedirs(minecraft_mods_directory)
    for mod in os.listdir(mods_directory):
        mod_path = os.path.join(mods_directory, mod)
        if os.path.isfile(mod_path):
            shutil.copy(mod_path, minecraft_mods_directory)
    print("Mods loaded successfully!")

def unload_mods(minecraft_mods_directory):
    for mod in os.listdir(minecraft_mods_directory):
        mod_path = os.path.join(minecraft_mods_directory, mod)
        if os.path.isfile(mod_path):
            os.remove(mod_path)
    print("Mods unloaded successfully!")

if __name__ == "__main__":
    mods_directory = os.path.join(os.getcwd(), "mods")
    minecraft_mods_directory = os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")
    load_mods(mods_directory, minecraft_mods_directory)
