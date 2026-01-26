from pathlib import Path
from logzero import logger, logfile
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time", "Latitude", "Longitude")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)



base_folder = Path(__file__).parent.resolve()

logfile(base_folder/"events.log")

# Initialise the CSV file
data_file = base_folder/"data.csv"
create_csv_file(data_file)

# Initialise the counter
counter = 1
# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()
# Run a loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=0.3)):
    try:

        # Save the data to the file
        data = (
            counter,
            datetime.now(),
	    "bla1",
	    "bla2",

        )

        add_csv_data(data_file, data)
        logger.info(f"Loop number {counter} started")
        counter += 1
	# 2 Sekunden Pause
        sleep(2)
        # Update the current time
        now_time = datetime.now()


    except Exception as e:
        now_time = datetime.now()
        logger.error(f'{e.__class__.__name__}: {e}')
        sleep(5)