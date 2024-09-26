import os
import shutil

def backup_to_cloud(source_directory, cloud_directory):
    if not os.path.exists(cloud_directory):
        os.makedirs(cloud_directory)
    for item in os.listdir(source_directory):
        source_path = os.path.join(source_directory, item)
        cloud_path = os.path.join(cloud_directory, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, cloud_path)
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, cloud_path)
    print("Backup to cloud completed successfully!")

def restore_from_cloud(cloud_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    for item in os.listdir(cloud_directory):
        cloud_path = os.path.join(cloud_directory, item)
        destination_path = os.path.join(destination_directory, item)
        if os.path.isfile(cloud_path):
            shutil.copy(cloud_path, destination_path)
        elif os.path.isdir(cloud_path):
            shutil.copytree(cloud_path, destination_path)
    print("Restore from cloud completed successfully!")

if __name__ == "__main__":
    source_directory = os.path.join(os.getenv("APPDATA"), ".minecraft", "saves")
    cloud_directory = os.path.join(os.getcwd(), "cloud_backup")
    backup_to_cloud(source_directory, cloud_directory)
