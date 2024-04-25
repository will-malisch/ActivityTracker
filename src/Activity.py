from sense_hat import SenseHat
import time
import csv
from pathlib import Path

class Activity:
    def __init__(self, sense):
        self.sense = sense
        self.running = False

    def record(self):
        try:
            self.running = True

            timestamp = int(time.time())
            output_file_path = Path(f"outputs/{timestamp}.csv").resolve()

            print("Activity started.")
            with open(output_file_path, 'a') as file:
                
                writer = csv.writer(file)
                
                while self.running:
                    # Read data from the IMU
                    imu_data = self.sense.get_accelerometer_raw()
                    acceleration = imu_data['x'], imu_data['y'], imu_data['z']

                    rounded_acceleration = [round(value, 2) for value in acceleration]
                    writer.writerow(rounded_acceleration)

                    joy_stick = self.sense.stick.get_events()
                    for event in joy_stick:
                        if(event.action == "pressed" and event.direction == "middle"):
                            self.running = not self.running

            return True

        except Exception as e:
            print(e, "An error was encountered when recording your activity. Please try again.")
            return False
