#!/usr/bin/env python

import logging
import threading
import time

# Set up a logger to output to
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s (T:%(thread)d):- %(message)s")

class MessagePrinter(threading.Thread):
    """
    A simple class to print messages to the log a a given interval.
    """
    
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        self._args = args
        self._kwargs = kwargs

    def run(self):
        for message in self._args:
            logging.info(message)
            time.sleep(self._kwargs.get("delay", 1.0))


# Set up two message printer obejcts
mp1 = MessagePrinter("Hello", "Good day!")
mp2 = MessagePrinter("A", "B", "C", delay=3)

# Start each of them on their own thread
mp1.start()
mp2.start()

# Wait for those threads to exit before exiting the main thread
mp1.join()
mp2.join()
