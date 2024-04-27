# Controller.py

from src.activity import Activity
from src.logger import Logger
from sense_hat import SenseHat
import time

class Controller:
    def __init__(self):
        self.sense = SenseHat()
        self.logger = Logger(self.sense)
        self.activity = Activity(self.sense)

    def run(self):
        try:
            while True:
                for event in self.sense.stick.get_events():
                    if event.action == "pressed":
                        if event.direction == "middle":
                            self.logger.print_start()
                            status = self.activity.record()
                            print(status)
                            self.logger.print_end()

                # Use a short sleep statement to help save battery. Calls to the SenseHat are battery intensive, this slightly reduces the number of calls
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("Exiting...")
            self.sense.clear()