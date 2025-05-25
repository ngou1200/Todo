import sys
import os

# Print current information
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")
print(f"User: ngou1200")
print(f"Current time: 2025-05-25 05:27:04")

# Try importing the module
try:
    from gui.dialogs.task_dialog import TaskDialog
    print("\nSuccessfully imported TaskDialog")
except ImportError as e:
    print(f"\nImport error: {e}")