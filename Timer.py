
import os
import time
from queue import Queue
from threading import Thread, Event


try:
    # print("trying to import Qt4 @ analoggaugewidget.py")
    from PyQt4.QtGui import QMainWindow

    from PyQt4.QtGui import QWidget
    from PyQt4.QtGui import QApplication
    from PyQt4.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont
    from PyQt4.QtGui import QPainter, QFontMetrics, QConicalGradient
    # QtGui -> QPolygon, QPolygonF, QColor, QPen, QFont,
    #       -> QWidget
    #       -> QApplication

    from PyQt4.QtCore import Qt, QTime, QTimer, QPoint, QPointF, SIGNAL, QRect, QSize
    from PyQt4.QtCore import QObject, pyqtSignal
    # QtCore -> Qt.NoPen, QTime, QTimer, QPoint, QPointF, QRect, QSize


    used_Qt_Version = 4
    # print("end trying to import Qt4 @ analoggaugewidget.py")
    # # Antialysing may be problem with Qt4
    # print("ToDo: Fix error output QPainter.Antialiasing")

except:
    try:
        # print("Try5: analoggaugewidget.py")
        from PyQt5.QtWidgets import QMainWindow, QInputDialog, QPushButton

        from PyQt5.QtWidgets import QWidget
        from PyQt5.QtWidgets import QApplication
        # QtWidgets -> QWidget
        # QtWidgets -> QApplication

        from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont
        from PyQt5.QtGui import QPainter, QFontMetrics, QConicalGradient
        # QtGui -> QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient

        from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize
        from PyQt5.QtCore import QObject, pyqtSignal
        # QtCore -> Qt.NoPen ,QTime, QTimer, QPoint, QPointF, QRect, QSize

        used_Qt_Version = 5
        # print("end trying to import Qt5 @ analoggaugewidget.py")
    except:
        print("Error Import Qt 4 & 5 @ analoggaugewidget.py")
        exit()

from Timer_Window import Ui_MainWindow
from Timer_thread import Stoppuhr_thread as sut
import sys
import os  # Used in Testing Script

class mainclass(QMainWindow):
    global app
    def __init__(self, parent=None, autoupdate=Event()):
        QWidget.__init__(self, parent)


        # self.app = QApplication(sys.argv)
        # window = QMainWindow()
        self.my_gauge = Ui_MainWindow()
        self.my_gauge.setupUi(self)

        self.my_gauge.widget.enable_barGraph = True

        self.my_gauge.widget.value_needle_snapzone = 1

        # self.my_gauge.widget.value_min = 0
        # self.my_gauge.widget.value_max = 30
        # self.my_gauge.widget.scala_main_count = 30
        self.my_gauge.widget.set_scale_polygon_colors([[.0, Qt.green],
                                       [.1, Qt.green],
                                       [.35, Qt.yellow],
                                       [.65, Qt.red],
                                       [.95, Qt.red]])
        # self.my_gauge.ActualSlider.setMaximum(self.my_gauge.widget.value_max)
        # self.my_gauge.ActualSlider.setMinimum(self.my_gauge.widget.value_min)
        # self.my_gauge.AussenRadiusSlider.setValue(self.my_gauge.widget.gauge_color_outer_radius_factor * 1000)
        # self.my_gauge.InnenRadiusSlider.setValue(self.my_gauge.widget.gauge_color_inner_radius_factor * 1000)
        # self.my_gauge.GaugeStartSlider.setValue(self.my_gauge.widget.scale_angle_start_value)
        # self.my_gauge.GaugeSizeSlider.setValue(self.my_gauge.widget.scale_angle_size)

        self.my_gauge.pushButton.clicked.connect(self.start_timer)

        self.autoupdate = autoupdate
        self.starten = Event()
        self.stoppen = Event()
        self.new_data = Queue()
        self.reset = Event()
        self.my_queue = Queue()

        button_x_size = 50
        button_y_size = 50
        x_pos = 50
        y_pos = 50
        self.button_ring =(QPushButton(str("I"), self))
        self.button_ring.setGeometry(100, 100, button_x_size, button_y_size)
        self.button_ring.clicked.connect(self.set_timer_seconds)

        self.button_ring.move(x_pos - button_x_size / 2, y_pos)  # + button_y_size / 2)
        self.button_ring.show()


        self.running = sut(self.starten, self.stoppen, self.reset, self.my_queue, self.new_data)
        self.running.start()

        self.set_time(30)
        time.sleep(0.1)
        # self.starten.set()

        self.state_dict = {"init": "start",
                           "reset": "start",
                           "start": "stop",
                           "stop": "reset"}

        self.actual_state = "init"
        print(self.actual_state)
        # print(self.state_dict[self.actual_state])
        QTimer.singleShot(10, self.check_new_data)

    def set_timer_seconds(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")
        if ok:
            print("new value ", str(num))
            self.set_time(num)

    def set_time(self, value):
        self.timer_value = value * 10 # sec * 10
        self.my_gauge.widget.value_max = int(self.timer_value / 10)

        self.my_gauge.widget.scala_main_count = int(self.timer_value / 10)
        if self.timer_value > 300:
            self.my_gauge.widget.scala_main_count = int((self.timer_value / 100))

        elif self.timer_value > 3000:
            self.my_gauge.widget.scala_main_count = int(self.timer_value / 1000)
        self.my_gauge.widget.update_value(self.timer_value)
        self.running.set_countdouwn_value(self.timer_value)

    def next_state(self):
        self.actual_state = self.state_dict[self.actual_state]
        return self.actual_state

    def start_timer(self):
        # self.starten.set()
        print(self.next_state())
        self.MatchTimeStart = time.time()




    def stop_thread(self):
        print("stop_thread")
        self.starten.clear()
        self.stoppen.set()
        self.running.join()

    def stop_app(self):
        print("stop_app")
        self.stop_thread()
        sys.exit(0)

    def check_new_data(self):
        if not self.new_data.empty():
            data = self.new_data.get()/10
            print("new data", data)
            self.my_gauge.widget.update_value(data)
            # self.new_data.clear()
        else:
            # print("GUI idle")
            pass

        if self.actual_state == "start":
            # print("start_timer")
            if not self.starten.is_set():
                self.starten.set()
                self.my_gauge.pushButton.setText("Stop")
            else:
                if self.my_gauge.widget.value <=0:
                    self.MatchTimeStartnew = time.time()
                    self.time_delta = self.MatchTimeStartnew - self.MatchTimeStart
                    print(self.time_delta)
                    self.my_gauge.pushButton.setText("Reset")
                    self.starten.clear()
                    self.next_state()
        elif self.actual_state == "stop":
            self.starten.clear()
            self.my_gauge.pushButton.setText("Reset")
        elif self.actual_state == "reset":
            self.reset.set()
            self.my_gauge.pushButton.setText("Start")
            self.MatchTimeStart = time.time()

        elif self.actual_state == "init":
            pass

        QTimer.singleShot(1, self.check_new_data)