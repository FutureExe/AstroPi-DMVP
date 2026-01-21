from pathlib import Path
from datetime import datetime, timedelta 
from time import sleep
import csv

base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"
for i in range(10):
    with open(data_file, "w", buffering=1) as f:
        writer = csv.writer(f)
        writer.writerow("test")