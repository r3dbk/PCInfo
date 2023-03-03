import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber
from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow, QCheckBox
import string

shift_d = False
upp = False

arr = {'[': '{', ']': '}', ';': ':', "'": "'", ',': '<', '.': '>', '/': '?'}


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.alph = list("QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./")
        # print(self.alph)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 700, 500, 300)
        self.setWindowTitle('PyQT6')
        self.main_label = QLineEdit('', self)
        self.main_label.resize(450, 32)
        self.main_label.move(5, 3)
        self.tab_btn = QPushButton('|<-->|', self)
        self.tab_btn.resize(48, 28)
        self.tab_btn.move(5, 70)
        self.caps_btn = QPushButton('[A]', self)
        self.caps_btn.resize(51, 28)
        self.caps_btn.move(5, 100)
        self.caps_btn.clicked.connect(self.caps_switch)
        self.shift_btn = QPushButton('SHIFT', self)
        self.shift_btn.resize(63, 28)
        self.shift_btn.move(5, 130)
        self.shift_btn.clicked.connect(self.case_switch)
        self.ctrl_btn = QPushButton('CTRL', self)
        self.ctrl_btn.resize(35, 28)
        self.ctrl_btn.move(5, 160)
        self.alt_btn = QPushButton('ALT', self)
        self.alt_btn.resize(35, 28)
        self.alt_btn.move(75, 160)
        self.rctrl_btn = QPushButton('CTRL', self)
        self.rctrl_btn.resize(35, 28)
        self.rctrl_btn.move(420, 160)
        self.ralt_btn = QPushButton('ALT', self)
        self.ralt_btn.resize(35, 28)
        self.ralt_btn.move(300, 160)
        self.spcbar_btn = QPushButton('------', self)
        self.spcbar_btn.resize(180, 28)
        self.spcbar_btn.move(115, 160)
        self.spcbar_btn.clicked.connect(lambda: self.key(keydata=' '))
        self.sl_btn = QPushButton('| :', self)
        self.sl_btn.resize(40, 28)
        self.sl_btn.move(415, 70)
        self.bckspc_btn = QPushButton('<--', self)
        self.bckspc_btn.resize(60, 28)
        self.bckspc_btn.move(395, 39)
        self.bckspc_btn.clicked.connect(lambda: self.key(keydata='backspace'))
        self.enter_btn = QPushButton('<-/', self)
        self.enter_btn.resize(60, 28)
        self.enter_btn.move(395, 100)
        self.rshift_btn = QPushButton('RSHIFT', self)
        self.rshift_btn.resize(85, 28)
        self.rshift_btn.move(370, 130)

        self.esc_btn = QPushButton('ESC', self)
        self.esc_btn.resize(28, 28)
        self.esc_btn.move(5, 39)
        self.esc_btn.clicked.connect(lambda: self.top_row(self.esc_btn.text()))
        self.one_btn = QPushButton('1 !', self)
        self.one_btn.resize(28, 28)
        self.one_btn.move(35, 39)
        self.one_btn.clicked.connect(lambda: self.top_row(self.one_btn.text()))
        self.two_btn = QPushButton('2 @', self)
        self.two_btn.resize(28, 28)
        self.two_btn.move(65, 39)
        self.two_btn.clicked.connect(lambda: self.top_row(self.two_btn.text()))
        self.thr_btn = QPushButton('3 #', self)
        self.thr_btn.resize(28, 28)
        self.thr_btn.move(95, 39)
        self.thr_btn.clicked.connect(lambda: self.top_row(self.thr_btn.text()))
        self.fr_btn = QPushButton('4 $', self)
        self.fr_btn.resize(28, 28)
        self.fr_btn.move(125, 39)
        self.fr_btn.clicked.connect(lambda: self.top_row(self.fr_btn.text()))
        self.fv_btn = QPushButton('5 %', self)
        self.fv_btn.resize(28, 28)
        self.fv_btn.move(155, 39)
        self.fv_btn.clicked.connect(lambda: self.top_row(self.fv_btn.text()))
        self.sx_btn = QPushButton('6 ^', self)
        self.sx_btn.resize(28, 28)
        self.sx_btn.move(185, 39)
        self.sx_btn.clicked.connect(lambda: self.top_row(self.sx_btn.text()))
        self.sv_btn = QPushButton('7 ?', self)
        self.sv_btn.resize(28, 28)
        self.sv_btn.move(215, 39)
        self.sv_btn.clicked.connect(lambda: self.top_row(self.sv_btn.text()))
        self.eg_btn = QPushButton('8 *', self)
        self.eg_btn.resize(28, 28)
        self.eg_btn.move(245, 39)
        self.eg_btn.clicked.connect(lambda: self.top_row(self.eg_btn.text()))
        self.nn_btn = QPushButton('9 (', self)
        self.nn_btn.resize(28, 28)
        self.nn_btn.move(275, 39)
        self.nn_btn.clicked.connect(lambda: self.top_row(self.nn_btn.text()))
        self.zr_btn = QPushButton('0 )', self)
        self.zr_btn.resize(28, 28)
        self.zr_btn.move(305, 39)
        self.zr_btn.clicked.connect(lambda: self.top_row(self.zr_btn.text()))
        self.min_btn = QPushButton('-_', self)
        self.min_btn.resize(28, 28)
        self.min_btn.move(335, 39)
        self.min_btn.clicked.connect(lambda: self.top_row(self.min_btn.text()))
        self.pl_btn = QPushButton('+=', self)
        self.pl_btn.resize(28, 28)
        self.pl_btn.move(365, 39)
        self.pl_btn.clicked.connect(lambda: self.top_row(self.pl_btn.text()))

        x, y = 55, 70
        for letter in self.alph:
            # print(letter)
            self.btn = QPushButton(letter, self)
            self.btn.setText(letter)
            self.btn.clicked.connect(lambda state, lett=letter: self.key(keydata=lett))
            if self.btn.text() == "A":
                y += 30
                x = 65
            elif self.btn.text() == "Z":
                y += 30
                x = 70
            self.btn.resize(28, 28)
            self.btn.move(x, y)
            x += 30

    def key(self, keydata):
        global shift_d, upp, arr
        # print(keydata)

        if keydata == "backspace":
            self.main_label.backspace()
        elif shift_d or upp:
            if [i for i, x in enumerate(arr) if x == keydata]:
                self.main_label.setText(self.main_label.text() + str(arr[keydata]))
            else:
                self.main_label.setText(self.main_label.text() + str(keydata))
            shift_d = False
            self.shift_btn.setStyleSheet("background-color: none")

        else:
            self.main_label.setText(self.main_label.text() + str(keydata).lower())

    def caps_switch(self):
        global upp
        if upp:
            upp = False
            self.caps_btn.setStyleSheet("background-color: none")
            self.caps_btn.setText("[A]")
        elif not upp:
            upp = True
            self.caps_btn.setStyleSheet("background-color: #afe1bb")
            self.caps_btn.setText("(A)")

    def case_switch(self):
        global shift_d
        if shift_d:
            shift_d = False
            self.shift_btn.setStyleSheet("background-color: none")
        elif not shift_d:
            shift_d = True
            self.shift_btn.setStyleSheet("background-color: #afe1bb")

    def top_row(self, nam):
        global shift_d
        if shift_d:
            shift_d = False
            self.shift_btn.setStyleSheet("background-color: none")
            self.main_label.setText(self.main_label.text() + nam[-1])
        elif upp:
            self.main_label.setText(self.main_label.text() + nam[-1])
        else:
            self.main_label.setText(self.main_label.text() + nam[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
