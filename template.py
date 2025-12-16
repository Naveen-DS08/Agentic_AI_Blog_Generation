import os 
from pathlib import Path

PROJECT_NAME = "Blog_Generator"

list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/llms/__init__.py",
    f"src/{PROJECT_NAME}/graphs/__init__.py",
    f"src/{PROJECT_NAME}/nodes/__init__.py",
    f"src/{PROJECT_NAME}/tools/__init__.py",
    f"src/{PROJECT_NAME}/state/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "main.py",
    "Dockerfile",
    "app.py"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)

    # create dir 
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        print(f"Creating directory: {file_dir} for the file: {file_name}")
    
    # Create files
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
            print(f"Creating an empty file: {file_name}")
    
    else:
        print(f"{file_name} already exists!")

