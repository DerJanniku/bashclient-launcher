
import subprocess
import os
import time

def start_java_backend():
    print("Starting Java Backend...")
    try:
        backend_process = subprocess.Popen(['./gradlew', 'run'], cwd='/home/user/bashclient-launcher/java-backend', stdout=open('/home/user/bashclient-launcher/java_backend.log', 'w'), stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"Failed to start Java Backend: {e}")
    return backend_process
    return backend_process

def start_svelte_frontend():
    print("Starting Svelte Frontend...")
    try:
        frontend_process = subprocess.Popen(['npm', 'run', 'dev'], cwd='/home/user/bashclient-svelte', stdout=open('/home/user/bashclient-launcher/svelte_frontend.log', 'w'), stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"Failed to start Svelte Frontend: {e}")
    return frontend_process

def run_rust_component():
    print("Running Rust Component...")
    try:
        rust_process = subprocess.Popen(['cargo', 'run'], cwd='/home/user/bashclient-rust', stdout=open('/home/user/bashclient-launcher/rust_component.log', 'w'), stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"Failed to run Rust Component: {e}")
    return rust_process

def start_minecraft_client():
    print("Starting Minecraft Client...")
    try:
        client_process = subprocess.Popen(['./gradlew', 'run'], cwd='/home/user/bashclient-launcher/minecraft-client', stdout=open('/home/user/bashclient-launcher/minecraft_client.log', 'w'), stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"Failed to start Minecraft Client: {e}")
    return client_process

if __name__ == "__main__":
    java_backend = start_java_backend()
    time.sleep(5)  # Wait for the backend to start

    svelte_frontend = start_svelte_frontend()
    time.sleep(5)  # Wait for the frontend to start

    rust_component = run_rust_component()
    time.sleep(5)  # Wait for the Rust component to run

    minecraft_client = start_minecraft_client()

    # Wait for all processes to complete
    java_backend.wait()
    svelte_frontend.wait()
    rust_component.wait()
    minecraft_client.wait()
