import logging
import threading
import time

class MessagePrinter(threading.Thread):
    """
    A simple class to print messages to the log a a given interval.
    """
    
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        self._args = args
        self._kwargs = kwargs
        self._lock = kwargs.get("lock", None)

    def run(self):
        for message in self._args:
            # If we have a lock object then try to acquire the lock first
            if self._lock:
                self._lock.acquire()
                
            print message

            # If we have a lock object then now release it
            if self._lock:
                self._lock.release()
                
            time.sleep(self._kwargs.get("delay", 1.0))

# Set up a lock to synchronize the print statements
lock = None #threading.Lock()

# Set up two message printer objects
mp1 = MessagePrinter("Hello", "Good day!", lock=lock)
mp2 = MessagePrinter("A", "B", "C", delay=3, lock=lock)

# Start each of them on their own thread
mp1.start()
mp2.start()

# Wait for those threads to exit before exiting the main thread
mp1.join()
mp2.join()
