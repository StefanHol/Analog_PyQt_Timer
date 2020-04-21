#!/usr/bin/env python

###
# Author: Stefan Holstein
# Timer for the Virtual PythonBarCamp Cologne 2020
#
# Sorry for mixing english & german notes
#
# Todo: print() in logging() ausgabe aendern
###

from threading import Thread, Event
# from overwatch import overwatch
import time

# import json_helper
from queue import Queue
from threading import Thread, Event

class Stoppuhr_thread(Thread):
    def __init__(self, start_event, stop_event, reset_event, queue_data, new_data):
        Thread.__init__(self)
        self.starten = start_event
        self.reset = reset_event
        self.stop = stop_event
        self.queue_data = queue_data
        self.new_data = new_data
        self.MatchTimeStart = time.time()
        self.set_countdouwn_value(30)
        self.counter = 0

    def set_countdouwn_value(self, value):
        self.countdouwn_value = value
        self.actual_countdouwn_value = self.countdouwn_value


    def run(self):
        print("Start run")
        while_loop = True

        self.start_init = False
        while while_loop:
            # print("loop")
            time.sleep(0.01)
            # endless loop until while_loop = False
            if self.stop.isSet():
                print("StopEvent")
                while_loop = False
                break

            if self.reset.isSet():
                self.actual_countdouwn_value = self.countdouwn_value
                self.reset.clear()
                # time.sleep(0.5)
                self.new_data.put(self.actual_countdouwn_value)
                self.start_init = False

            if self.starten.isSet():
                # time.sleep(0.001)
                if self.start_init == False:
                    # print("started")
                    self.TimerStart = time.time()
                    self.start_init = True
                    self.counter = 0

                self.MatchTimeStartnew = time.time()
                self.time_delta = self.MatchTimeStartnew - self.TimerStart


                if self.time_delta >= 0.1 * self.counter:

                    print(self.counter, self.time_delta)
                    # print("start ist set")
                    self.actual_countdouwn_value -= 1
                    self.new_data.put(self.actual_countdouwn_value)
                    self.counter += 1

                if self.actual_countdouwn_value <= 0 or self.counter >= self.countdouwn_value:
                    # print("clear starten event")
                    self.starten.clear()
                    self.start_init = False
                        # self.reset.set()


            try:
                for i in range(self.queue_data.qsize()):
                    if not self.queue_data.empty():
                        my_stuff = self.queue_data.get()
                        print(my_stuff)
                    else:
                        # time.sleep(0.05)
                        print("nothing in queue")
            except Exception as e:
                print("Error fallback_overwrite_", e)
            # time.sleep(0.01)

def main():
    starten = Event()
    stoppen = Event()
    reset = Event()
    my_queue = Queue()
    new_data = Queue()

    running = Stoppuhr_thread(starten, stoppen, reset, my_queue, new_data)

    print("send start")
    running.start()
    time.sleep(0.1)
    starten.set()

    time.sleep(3)
    my_queue.put("Stuff 1")
    my_queue.put("Stuff 2")
    my_queue.put("Stuff 3")

    time.sleep(3)
    my_queue.put("Stuff 4")
    my_queue.put("Stuff 5")
    my_queue.put("Stuff 6")

    time.sleep(3)
    print("send clear")
    starten.clear()
    print("send stop")
    stoppen.set()
    running.join()

if __name__ == "__main__":
    main()
