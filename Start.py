#!/usr/bin/env python

###
# Author: Stefan Holstein
# Timer for the Virtual PythonBarCamp Cologne 2020
#
# Sorry for mixing english & german notes
#
# Todo: print() in logging() ausgabe aendern
###



import sys
import os
from threading import Thread, Event

try:
    from PyQt5.QtWidgets import QApplication, QFrame
    from PyQt5.QtGui import QIcon
    used_Qt_Version = 5
except:
    try:
        from PyQt4.QtGui import QApplication
        used_Qt_Version = 4
    except:
        exit()
        pass

if used_Qt_Version == 4:
    print("Compile QUI for Qt Version: " + str(used_Qt_Version))
    os.system("pyuic4 -o Timer_Window.py Timer_Window.ui")
elif used_Qt_Version == 5:
    print("Compile QUI for Qt Version: " + str(used_Qt_Version))
    os.system("pyuic5 -o Timer_Window.py Timer_Window.ui")

from Timer import mainclass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')

    autoupdate = Event()
    my_gauge = mainclass(None, autoupdate)
    my_gauge.setWindowTitle("Timer")
    my_gauge.setWindowIcon(QIcon("icon.png"))
    # my_gauge.se
    my_gauge.show()

    autoupdate.set()

    sys.exit(app.exec_())
    pass
