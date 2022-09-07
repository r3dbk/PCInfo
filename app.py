import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from cpuinfo import get_cpu_info
from gpiozero import CPUTemperature

import res_rc
import GPUtil
import psutil
import datetime
import time
import matplotlib

gpus = GPUtil.getGPUs()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        app.focusChanged.connect(self.on_focusChanged)
        self.setWindowTitle("PCInfo")

        self.setFixedSize(QSize(1000, 700))

        self.initUI()

    def initUI(self):
        self.menu_vert_frame = QWidget(self)
        self.menu_vert_frame.setGeometry(QRect(0, 0, 1000, 110))
        self.menu_vert_frame.setStyleSheet(
            u"border-bottom: 1px solid gray;"
            u"background-color: rgb(66, 140, 223);")
        self.menu_horiz_frame = QWidget(self)
        self.menu_horiz_frame.setGeometry(QRect(0, 110, 150, 590))
        self.menu_horiz_frame.setStyleSheet(
            u"border-right: 1px solid gray")
        self.name_frame = QWidget(self)
        self.name_frame.setGeometry(QRect(150, 110, 850, 60))
        self.name_frame.setStyleSheet(
            u"border-bottom: 1px solid gray")
        self.name_frame_gpu = QWidget(self)
        self.name_frame_gpu.setGeometry(QRect(150, 110, 850, 60))
        self.name_frame_gpu.setStyleSheet(
            u"border-bottom: 1px solid gray")
        self.pc_frame = QWidget(self)
        self.pc_frame.setGeometry(QRect())
        self.btn1_mv = QPushButton()
        self.btn1_mv.setStyleSheet(u"background-image:url(resources/home_house_icon-icons.com_49851.png);"
                                   u"border: none;")
        self.btn1_mv.clicked.connect(self.show_cont1)
        self.btn1_mv.setFixedSize(64, 64)

        layout = QGridLayout()
        layout.addWidget(self.btn1_mv, 0, 0)
        self.menu_vert_frame.setLayout(layout)
        self.frame_1 = QFrame(self)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(150, 170, 850, 530))
        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(150, 170, 850, 530))

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(170, 120, 118, 23))
        self.progressBar.setValue(int(psutil.cpu_percent(interval=1)))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 10, 49, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 50, 49, 16))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 70, 49, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 50, 131, 16))
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 70, 131, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 120, 61, 16))
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 170, 61, 16))
        self.progressBar_2 = QProgressBar(self.frame_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(170, 170, 118, 23))
        self.progressBar_2.setValue(int(gpus[0].load * 100))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 230, 81, 16))
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(80, 270, 81, 16))
        self.lcdNumber = QLCDNumber(self.frame_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(170, 230, 64, 23))
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("intValue", 10)
        self.lcdNumber_2 = QLCDNumber(self.frame_2)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(170, 270, 64, 23))
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setMidLineWidth(0)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", gpus[0].temperature)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(350, 40, 121, 20))
        self.label_55 = QLabel(self.frame_2)
        self.label_55.setObjectName(u"label_15")
        self.label_55.setGeometry(QRect(350, 70, 121, 20))
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(350, 210, 101, 16))
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(350, 230, 91, 16))
        self.label_22.setStyleSheet(u"text-align: center;")
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(350, 270, 101, 16))
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(350, 250, 111, 16))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PC info:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", str(get_cpu_info()['brand_raw']), None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", gpus[0].name, None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU Load:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GPU Load:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU Temp* (\u00b0C):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GPU Temp (\u00b0C):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"GPU tot. memory: ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", str(gpus[0].memoryTotal) + " Mb", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", str(gpus[0].memoryUsed) + " Mb", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"GPU used memory:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total RAM:", None))
        self.virt_mem = round(int(dict(psutil.virtual_memory()._asdict())['total']) / 1024 / 1024 / 1024, 2)
        self.label_55.setText(
            QCoreApplication.translate("MainWindow", str(self.virt_mem) + u" GB", None))

        self.label_name = QLabel(self.name_frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(70, 10, 300, 40))
        self.label_name.setStyleSheet(u"font-size: 25px;")
        self.label_name.setText(QCoreApplication.translate("MainWindow", str(get_cpu_info()['brand_raw']), None))
        self.label_name_g = QLabel(self.name_frame_gpu)
        self.label_name_g.setObjectName(u"label_name_g")
        self.label_name_g.setGeometry(QRect(70, 10, 500, 40))
        self.label_name_g.setStyleSheet(u"font-size: 25px;")
        self.label_name_g.setText(QCoreApplication.translate("MainWindow", gpus[0].name, None))

        self.btn2_mv = QPushButton()
        self.btn2_mv.setStyleSheet(
            u"background-image:url(resources/976599-all-in-one-appliances-desktop-display-electronics-pc-screen_106534.png);"
            u"border: none;")
        self.btn2_mv.clicked.connect(self.show_cont1)
        self.btn2_mv.setFixedSize(64, 64)
        layout.addWidget(self.btn2_mv, 0, 1)
        self.btn3_mv = QPushButton()
        self.btn3_mv.setStyleSheet(u"background-image:url(resources/1492790841-18time_84210.png);"
                                   u"border: none;")
        self.btn3_mv.clicked.connect(self.show_cont1)
        self.btn3_mv.setFixedSize(64, 64)
        layout.addWidget(self.btn3_mv, 0, 2)
        self.btn4_mv = QPushButton()
        self.btn4_mv.setStyleSheet(
            u"background-image:url(resources/976605-appliances-console-controller-dualshock-gamepad-games-videogame_106553.png);"
            u"border: none;")
        self.btn4_mv.clicked.connect(self.show_cont1)
        self.btn4_mv.setFixedSize(64, 64)
        layout.addWidget(self.btn4_mv, 0, 3)
        self.btn5_mv = QPushButton()
        self.btn5_mv.setStyleSheet(
            u"background-image:url(resources/1491254488-chartflexibledatestatstatistics_82950.png);"
            u"border: none;")
        self.btn5_mv.clicked.connect(self.show_cont1)
        self.btn5_mv.setFixedSize(64, 64)
        self.label_cpu = QLabel(self.name_frame)
        self.label_cpu.setObjectName(u"label_cpu")
        self.label_cpu.setFixedSize(48, 48)
        self.label_cpu.setGeometry(QRect(11, 6, 59, 54))
        self.label_cpu.setStyleSheet(
            u"background-image:url(resources/cpu_icon_160215.png);")
        self.label_gpu = QLabel(self.name_frame_gpu)
        self.label_gpu.setStyleSheet(
            u"background-image:url(resources/976602-appliances-computer-display-pc-screen-tv_106537.png);")
        self.label_gpu.setObjectName(u"label_gpu")
        self.label_gpu.setFixedSize(48, 48)
        self.label_gpu.setGeometry(QRect(11, 6, 59, 54))
        self.label1_mh = QLabel(self.menu_horiz_frame)
        self.label1_mh.setGeometry(QRect(10, 5, 145, 30))
        self.label1_mh.setText(QCoreApplication.translate("MainWindow", u"Equipment:", None))
        self.label1_mh.setStyleSheet(u"font-size: 17px;")
        self.btn1_mh = QPushButton(self.menu_horiz_frame)
        self.btn1_mh.setGeometry(QRect(12, 40, 145, 55))
        self.btn1_mh.setText(QCoreApplication.translate("MainWindow", u"Central Processing Unit", None))
        # self.btn1_mh.setStyleSheet(u"font-size: 12px;"
        #                            u"background: none;"
        #                            u"color: black;"
        #                            u"border: none;"
        #                            u"cursor: pointer;"
        #                            u"outline: none;")
        self.btn1_mh.setFixedSize(133, 15)
        self.btn1_mh.clicked.connect(self.cpu_btn)
        self.btn2_mh = QPushButton(self.menu_horiz_frame)
        self.btn2_mh.setGeometry(QRect(12, 65, 145, 80))
        self.btn2_mh.setText(QCoreApplication.translate("MainWindow", u"Graphic Processing Unit", None))
        # self.btn2_mh.setStyleSheet(u"font-size: 12px;"
        #                            u"background: none;"
        #                            u"color: black;"
        #                            u"border: none;"
        #                            u"cursor: pointer;"
        #                            u"outline: none;")
        self.btn2_mh.clicked.connect(self.gpu_btn)
        self.btn2_mh.setFixedSize(133, 15)

        self.label_111 = QLabel(self.frame_1)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(60, 50, 120, 20))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"GPU name:", None))
        self.label_gpu1 = QLabel(self.frame_1)
        self.label_gpu1.setObjectName(u"label_gpu1")
        self.label_gpu1.setGeometry(QRect(140, 50, 200, 20))
        self.label_gpu1.setText(QCoreApplication.translate("MainWindow", str(gpus[0].name), None))
        self.label_gpu2 = QLabel(self.frame_1)
        self.label_gpu2.setObjectName(u"label_gpu2")
        self.label_gpu2.setGeometry(QRect(60, 75, 160, 20))
        self.label_gpu2.setText(u"GPU Total memory: ")
        self.label_gpu3 = QLabel(self.frame_1)
        self.label_gpu3.setObjectName(u"label_gpu3")
        self.label_gpu3.setGeometry(QRect(180, 75, 240, 20))
        self.label_gpu3.setText(QCoreApplication.translate("MainWindow", str(gpus[0].memoryTotal) + " Mb", None))
        self.label_gpu4 = QLabel(self.frame_1)
        self.label_gpu4.setObjectName(u"label_gpu4")
        self.label_gpu4.setGeometry(QRect(60, 100, 160, 20))
        self.label_gpu4.setText(u"GPU Used memory: ")
        self.label_gpu5 = QLabel(self.frame_1)
        self.label_gpu5.setObjectName(u"label_gpu5")
        self.label_gpu5.setGeometry(QRect(180, 100, 240, 20))
        self.label_gpu5.setText(
            QCoreApplication.translate("MainWindow", str(gpus[0].memoryUsed) + " Mb (" + str(
                round(gpus[0].memoryUsed / (gpus[0].memoryTotal / 100), 2)) + "%)",
                                       None))
        self.label_gpu2 = QLabel(self.frame_1)
        self.label_gpu2.setObjectName(u"label_gpu2")
        self.label_gpu2.setGeometry(QRect(60, 125, 160, 20))
        self.label_gpu2.setText(u"GPU Temperature (C): ")
        self.label_gpu3 = QLabel(self.frame_1)
        self.label_gpu3.setObjectName(u"label_gpu3")
        self.label_gpu3.setGeometry(QRect(180, 125, 240, 20))
        self.label_gpu3.setText(QCoreApplication.translate("MainWindow", str(gpus[0].temperature) + "°", None))

        # self.btn1_mh = QPushButton()
        # self.btn1_mh.setStyleSheet(
        #     u"Qbtn1_mh:hover { background-color: black; }")
        # self.btn1_mh.clicked.connect(self.show_cont1)
        # self.btn1_mh.setFixedSize(64, 64)
        layout.addWidget(self.btn5_mv, 0, 4)
        self.menu_vert_frame.setLayout(layout)

    def show_cont1(self):
        pass

    def cpu_btn(self):
        print("cpu pressed")
        self.frame_2.show()
        self.frame_1.hide()
        self.name_frame_gpu.hide()
        self.name_frame.show()

    def gpu_btn(self):
        print("gpu pressed")
        self.frame_1.show()
        self.frame_2.hide()
        self.name_frame.hide()
        self.name_frame_gpu.show()

    def on_focusChanged(self, widget):
        print(self.lcdNumber_2)
        self.lcdNumber_2.setStyleSheet(u"border: 2px solid black;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style.qss', 'r') as f:
        print("ready")
        style = f.read()
        app.setStyleSheet(style)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
