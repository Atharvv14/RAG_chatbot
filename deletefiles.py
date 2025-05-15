import os

folder = r"C:\Python312\Scripts"

files_to_delete = ["huggingface-cli.exe"]
extensions_to_delete = [".deleteme"]

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if filename in files_to_delete or any(filename.endswith(ext) for ext in extensions_to_delete):
        try:
            os.remove(filepath)
            print(f"Deleted: {filepath}")
        except Exception as e:
            print(f"Failed to delete {filepath}: {e}")
