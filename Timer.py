
import os
import time
from queue import Queue
from threading import Thread, Event
from os.path import isfile


try:
    # print("trying to import Qt4 @ analoggaugewidget.py")
    from PyQt4.QtGui import QMainWindow

    from PyQt4.QtGui import QWidget
    from PyQt4.QtGui import QApplication
    from PyQt4.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPixmap
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
        from PyQt5.QtWidgets import QMainWindow, QInputDialog, QPushButton, QSizePolicy, QFileDialog

        from PyQt5.QtWidgets import QWidget
        from PyQt5.QtWidgets import QApplication
        # QtWidgets -> QWidget
        # QtWidgets -> QApplication

        from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPixmap
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
        self.my_gauge.widget.set_scale_polygon_colors([[.0, Qt.green],
                                       [.1, Qt.green],
                                       [.25, Qt.yellow],
                                       [.55, Qt.blue],
                                       [.95, Qt.darkBlue]])
        # self.my_gauge.ActualSlider.setMaximum(self.my_gauge.widget.value_max)
        # self.my_gauge.ActualSlider.setMinimum(self.my_gauge.widget.value_min)
        # self.my_gauge.AussenRadiusSlider.setValue(self.my_gauge.widget.gauge_color_outer_radius_factor * 1000)
        # self.my_gauge.InnenRadiusSlider.setValue(self.my_gauge.widget.gauge_color_inner_radius_factor * 1000)
        # self.my_gauge.GaugeStartSlider.setValue(self.my_gauge.widget.scale_angle_start_value)
        # self.my_gauge.GaugeSizeSlider.setValue(self.my_gauge.widget.scale_angle_size)

        self.my_gauge.pushButton.clicked.connect(self.start_timer)
        self.my_gauge.pushButton_openfile.clicked.connect(self.openfile_read_list)
        self.my_gauge.pushButton_clear.clicked.connect(self.clear_name_list_widget)



        # self.my_gauge.widge
        self.my_gauge.widget.set_enable_ScaleText(False)

        self.autoupdate = autoupdate
        self.starten = Event()
        self.stoppen = Event()
        self.new_data = Queue()
        self.reset = Event()
        self.my_queue = Queue()

        button_x_size = 30
        button_y_size = 30
        x_pos = 20
        y_pos = 0

        self.button_ring =(QPushButton(str("sec"), self))
        self.button_ring.setGeometry(x_pos, y_pos, button_x_size, button_y_size)
        self.button_ring.clicked.connect(self.set_timer_seconds)
        self.button_ring.move(x_pos - button_x_size / 2, y_pos)  # + button_y_size / 2)
        self.button_ring.show()

        self.button_panel =(QPushButton(str(">"), self))
        self.button_panel.setGeometry(x_pos+button_x_size, y_pos, button_x_size, button_y_size)
        self.button_panel.clicked.connect(self.toggle_panel)
        self.button_panel.move((x_pos - button_x_size / 2) + button_x_size, y_pos)  # + button_y_size / 2)
        self.button_panel.show()
        self.panel_show = True

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

        # add banner image
        self.pixmap = QPixmap('banner.png')
        # self.pixmap = self.pixmap.scaledToWidth(300)
        self.my_gauge.label.setPixmap(self.pixmap)
        self.my_gauge.label.setScaledContents(True)

        self.my_gauge.widget.initial_value_fontsize = 50

        QTimer.singleShot(10, self.check_new_data)
        self.update()


    # # Todo emit event
    # def paintEvent(self, event):
    #     qp = QPainter()
    #     search_pixmap = QPixmap('banner.png')
    #     posX = 30
    #     posY = 50
    #     width = 250
    #     height = 50
    #     qp.drawPixmap(posX, posY, width, height,
    #                   search_pixmap.scaled(width, height, transformMode=Qt.SmoothTransformation))


    def set_timer_seconds(self):
        min = 5
        max = 10000
        num, ok = QInputDialog.getInt(self, "Change Time", "enter {} - {} seconds ".format(min, max), value = 30, min = min, max = max)
        if ok:
            print("new value ", str(num))
            self.set_time(num)

    def toggle_panel(self, force_show = True):
        # show/hide sidebar
        if self.panel_show:
            self.my_gauge.groupBox.setDisabled(True)
            self.my_gauge.groupBox.hide()
            self.panel_show=False
        else:
            self.my_gauge.groupBox.show()
            self.my_gauge.groupBox.setDisabled(False)
            self.panel_show=True

        if force_show:
            self.my_gauge.groupBox.show()
            self.my_gauge.groupBox.setDisabled(False)
            self.panel_show=True

    def set_time(self, value):
        self.timer_value = value * 10 # sec * 10
        self.my_gauge.widget.value_max = int(self.timer_value / 10)

        self.my_gauge.widget.scala_main_count = int(self.timer_value / self.timer_value*10)
        self.my_gauge.widget.update_value(self.timer_value)
        self.running.set_countdouwn_value(self.timer_value)

    def next_state(self):
        self.actual_state = self.state_dict[self.actual_state]

        # if self.my_gauge.name_list.c
        # print(self.my_gauge.name_list.selectedItems())
        if self.actual_state == "stop":
            # print("actual_state =", self.actual_state)
            # print("Current Row: ", self.my_gauge.name_list.row(self.my_gauge.name_list.currentItem()))
            if (self.my_gauge.name_list.count() > 0) and (
                    self.my_gauge.name_list.row(self.my_gauge.name_list.currentItem()) < self.my_gauge.name_list.count()-1):
                # print("set state: ", self.my_gauge.name_list.row(self.my_gauge.name_list.currentItem())+1)
                self.my_gauge.name_list.setCurrentRow(
                            self.my_gauge.name_list.row(
                            self.my_gauge.name_list.currentItem())+1)
                # print("Selected name = ", self.my_gauge.name_list.currentItem().text())
                # print( self.my_gauge.name_list.row(self.my_gauge.name_list.currentItem()))

        return self.actual_state

    def start_timer(self):
        # self.starten.set()
        print(self.next_state())
        self.MatchTimeStart = time.time()



    def closeEvent(self, event):
        self.stop_app()

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
            # print("new data", data)
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

    def openfile_read_list(self):
        self.name_list = self.openFileNameDialog()
        print(self.name_list)

        # fill list widget here
        self.my_gauge.name_list.clear()
        self.my_gauge.name_list.addItems(self.name_list)
        if self.my_gauge.name_list.count() > 0:
            self.my_gauge.name_list.setCurrentRow(0)
            # print("Select row 0 ")
            # print("Selected row ", self.my_gauge.name_list.row(self.my_gauge.name_list.currentItem()))
            # print("Row lenght ", self.my_gauge.name_list.count())

    def clear_name_list_widget(self):
        self.my_gauge.name_list.clear()


    def openFileNameDialog(self):
        # https://pythonspot.com/pyqt5-file-dialog/
        name_list = []
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select name list", "","Text File (*.txt)", options=options)
        if fileName:
            print(fileName)
            name_list = self.read_name_list(fileName)
        return name_list

    def read_name_list(self, filename):
        # Using readlines()
        myfile = open(filename, 'r')
        Lines = myfile.readlines()
        name_list = []
        # Strips the newline character
        for line in Lines:
            name_list.append(line.strip())
        myfile.close()
        name_list.append("Stop")
        return name_list

    def get_value_from_list_by_index(mylist, myindex):
        list_lenght = len(mylist)
        if myindex >= list_lenght:
            return "Ende"
        else:
            #         print(list_lenght, mylist[myindex])
            return mylist[myindex]