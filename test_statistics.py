import sys
import os

# Print current information
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")
print(f"User: ngou1200")
print(f"Current time: 2025-05-25 05:39:40")

try:
    from gui.widgets.statistics_widget import StatisticsWidget
    print("\nSuccessfully imported StatisticsWidget")
except ImportError as e:
    print(f"\nImport error: {e}")