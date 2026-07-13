import os
import shutil

action = "copy"  # "copy" or "delete"
origin = r"C:\ruta\de\origin"
target = r"C:\ruta\de\target"

def sync_files(origin, target, action):
    files_origin = set(os.listdir(origin))
    files_target = set(os.listdir(target))

    if action == "copy":
        files_to_copy = files_origin - files_target
        for file in files_to_copy:
            origin_path = os.path.join(origin, file)
            target_path = os.path.join(target, file)
            if os.path.isfile(origin_path):
                shutil.copy2(origin_path, target_path)
                print(f"Copied: {file}")

    elif action == "delete":
        files_to_delete = files_target - files_origin
        for file in files_to_delete:
            target_path = os.path.join(target, file)
            if os.path.isfile(target_path):
                os.remove(target_path)
                print(f"Deleted: {file}")

    else:
        print("Invalid action. Use 'copy' or 'delete'.")

sync_files(origin, target, action)
