
import os
import shutil
import sys

def copy_files(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                copy_files(item_path, destination_dir)
            else:
                file_extension = os.path.splitext(item)[1]
                target_dir = os.path.join(destination_dir, file_extension[1:])
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(item_path, target_dir)
        print(f"Files copied from {source_dir} to {destination_dir} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def main():
    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py source_directory destination_directory")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    # If destination directory is not provided, use 'dist'
    if not destination_dir:
        destination_dir = 'dist'

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()