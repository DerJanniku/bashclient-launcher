
import subprocess
import os
import time
import logging

# Configure logging
logging.basicConfig(filename='/home/user/bashclient-launcher/launcher.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_java_backend():
    logging.info("Starting Java Backend...")
    try:
        backend_process = subprocess.Popen(['./gradlew', 'run'], cwd='/home/user/bashclient-launcher/java-backend', stdout=open('/home/user/bashclient-launcher/java_backend.log', 'w'), stderr=subprocess.STDOUT)
        logging.info("Java Backend started successfully.")
    except Exception as e:
        logging.error(f"Failed to start Java Backend: {e}")
        return None
    return backend_process
    return backend_process

def start_svelte_frontend():
    logging.info("Starting Svelte Frontend...")
    try:
        frontend_process = subprocess.Popen(['npm', 'run', 'dev'], cwd='/home/user/bashclient-svelte', stdout=open('/home/user/bashclient-launcher/svelte_frontend.log', 'w'), stderr=subprocess.STDOUT)
        logging.info("Svelte Frontend started successfully.")
    except Exception as e:
        logging.error(f"Failed to start Svelte Frontend: {e}")
        return None
    return frontend_process

def run_rust_component():
    logging.info("Running Rust Component...")
    try:
        rust_process = subprocess.Popen(['cargo', 'run'], cwd='/home/user/bashclient-rust', stdout=open('/home/user/bashclient-launcher/rust_component.log', 'w'), stderr=subprocess.STDOUT)
        logging.info("Rust Component running successfully.")
    except Exception as e:
        logging.error(f"Failed to run Rust Component: {e}")
        return None
    return rust_process

def start_minecraft_client():
    logging.info("Starting Minecraft Client...")
    try:
        client_process = subprocess.Popen(['./gradlew', 'run'], cwd='/home/user/bashclient-launcher/minecraft-client', stdout=open('/home/user/bashclient-launcher/minecraft_client.log', 'w'), stderr=subprocess.STDOUT)
        logging.info("Minecraft Client started successfully.")
    except Exception as e:
        logging.error(f"Failed to start Minecraft Client: {e}")
        return None
    return client_process

if __name__ == "__main__":
    java_backend = start_java_backend()
    if java_backend:
        time.sleep(5)  # Wait for the backend to start

        svelte_frontend = start_svelte_frontend()
        if svelte_frontend:
            time.sleep(5)  # Wait for the frontend to start

            rust_component = run_rust_component()
            if rust_component:
                time.sleep(5)  # Wait for the Rust component to run

                minecraft_client = start_minecraft_client()
                if minecraft_client:
                    # Wait for all processes to complete
                    java_backend.wait()
                    svelte_frontend.wait()
                    rust_component.wait()
                    minecraft_client.wait()
                else:
                    logging.error("Minecraft Client failed to start.")
            else:
                logging.error("Rust Component failed to run.")
        else:
            logging.error("Svelte Frontend failed to start.")
    else:
        logging.error("Java Backend failed to start.")
