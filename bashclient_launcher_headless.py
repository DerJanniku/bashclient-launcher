
import os
import subprocess

def launch_bashclient():
    try:
        bashclient_path = os.path.join(os.getcwd(), "bashclient-launcher", "BashClient", "bashclient.py")
        subprocess.Popen(["python3", bashclient_path])
        print("BashClient launched successfully!")
    except Exception as e:
        print(f"Failed to launch BashClient: {e}")

def install_mods():
    try:
        mods_path = os.path.join(os.getcwd(), "bashclient-launcher", "mods")
        minecraft_mods_path = os.path.join(os.getcwd(), "test_minecraft_mods")
        if not os.path.exists(minecraft_mods_path):
            os.makedirs(minecraft_mods_path)
        for mod in os.listdir(mods_path):
            mod_path = os.path.join(mods_path, mod)
            if os.path.isfile(mod_path):
                print(f"Copying {mod_path} to {os.path.join(minecraft_mods_path, os.path.basename(mod_path))}")
                shutil.copy(mod_path, os.path.join(minecraft_mods_path, os.path.basename(mod_path)))
        print("Mods installed successfully!")
    except Exception as e:
        print(f"Failed to install mods: {e}")

def run_translator():
    try:
        translator_path = os.path.join(os.getcwd(), "translations", "run_translator.py")
        subprocess.Popen(["python3", translator_path])
        print("Auto-Translator started successfully!")
    except Exception as e:
        print(f"Failed to start Auto-Translator: {e}")

if __name__ == "__main__":
    print("Testing BashClient Launcher Functions")
    launch_bashclient()
    install_mods()
    run_translator()
