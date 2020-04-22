#!/usr/bin/env python3

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
sys.path.append(os.path.dirname(__file__))

print(os.path.dirname(__file__))

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

def compile_my_GUI():
    if used_Qt_Version == 4:
        print("Compile QUI for Qt Version: " + str(used_Qt_Version))
        os.system("pyuic4 -o Timer_Window.py Timer_Window.ui")
    elif used_Qt_Version == 5:
        print("Compile QUI for Qt Version: " + str(used_Qt_Version))
        os.system("pyuic5 -o Timer_Window.py Timer_Window.ui")

# compile_my_GUI()

from Timer import mainclass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')

    autoupdate = Event()
    my_gauge = mainclass(None, autoupdate)
    my_gauge.setWindowTitle("Timer")
    icon_name = "icon.png"
    icon_path = os.path.dirname(__file__) + os.path.sep + icon_name
    app_icon = QIcon()
    app_icon.addFile(icon_path)
    my_gauge.setWindowIcon(app_icon)

    # my_gauge.se
    my_gauge.show()

    autoupdate.set()

    sys.exit(app.exec_())
    pass
