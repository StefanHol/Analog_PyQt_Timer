#python3
from time import sleep
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
        # from PyQt4 import QtGui
        # from PyQt4 import QtCore
        used_Qt_Version = 4
    except:
        exit()
        pass
from Timer import mainclass



if used_Qt_Version == 4:
    print("Compile QUI for Qt Version: " + str(used_Qt_Version))
    os.system("pyuic4 -o Timer_Window.py Timer_Window.ui")
elif used_Qt_Version == 5:
    print("Compile QUI for Qt Version: " + str(used_Qt_Version))
    os.system("pyuic5 -o Timer_Window.py Timer_Window.ui")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')

    autoupdate = Event()
    my_gauge = mainclass(None, autoupdate)
    my_gauge.setWindowTitle("Timer")

    my_gauge.show()

    autoupdate.set()

    sys.exit(app.exec_())
    pass
