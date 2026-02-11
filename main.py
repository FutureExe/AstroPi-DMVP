#Initialise -Libraries -Sense HAT -Logs -CSV

from pathlib import Path
from logzero import logger, logfile
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
from sense_hat import SenseHat
import csv

shat = SenseHat()

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def magnetxyz():
    raw = shat.get_compass_raw()
    axis_x = ('{x}'.format(**raw))
    axis_y = ('{y}'.format(**raw))
    axis_z = ('{z}'.format(**raw))

    magx = round(float(axis_x), 2)
    magy = round(float(axis_y), 2)
    magz = round(float(axis_z), 2)

    return magx,magy,magz




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
while (now_time < start_time + timedelta(minutes=1)):
    try:
        #Get Sensor data
        mag = magnetxyz()
        # Save the data to the file
        data = (
            counter,
            datetime.now(),
	    mag[0],
        mag[1],
        mag[2],

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