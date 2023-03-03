import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber
from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow, QCheckBox


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.songs = ['song 1', 'song 2', 'song 3']
        self.currentSong = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 400, 250, 500)
        self.setWindowTitle('PyQT6 урок 2')
        self.disp = QLCDNumber(self)
        self.disp.display(self.currentSong)
        self.disp.move(5, 5)
        self.login = QLabel('Now playing:', self)
        self.login.move(20, 50)
        self.password = QLabel(self.songs[self.currentSong], self)
        self.password.move(20, 100)
        self.btn01 = QPushButton('Pause', self)
        self.btn01.resize(self.btn01.sizeHint())
        self.btn01.move(80, 150)
        self.btn01.clicked.connect(self.switch)
        self.btn02 = QPushButton('|<', self)
        self.btn02.resize(self.btn01.sizeHint())
        self.btn02.move(2, 150)
        self.btn02.clicked.connect(self.back)
        self.btn03 = QPushButton('>|', self)
        self.btn03.resize(self.btn01.sizeHint())
        self.btn03.move(158, 150)
        self.btn03.clicked.connect(self.forward)

        self.regL = QLabel('Reggae', self)
        self.regL.move(150, 200)
        self.regL.hide()
        self.jazzL = QLabel('Jazz', self)
        self.jazzL.move(150, 230)
        self.jazzL.hide()
        self.folkL = QLabel('Folk', self)
        self.folkL.move(150, 260)
        self.folkL.hide()
        self.bluesL = QLabel('Blues', self)
        self.bluesL.move(150, 290)
        self.bluesL.hide()
        self.reggae = QCheckBox('Reggae', self)
        self.reggae.move(20, 200)
        self.reggae.clicked.connect(self.check)
        self.jazz_blues = QCheckBox('Jazz', self)
        self.jazz_blues.move(20, 230)
        self.jazz_blues.clicked.connect(self.check)
        self.folk_blues = QCheckBox('Folk', self)
        self.folk_blues.move(20, 260)
        self.folk_blues.clicked.connect(self.check)
        self.var_blues = QCheckBox('Blues', self)
        self.var_blues.move(20, 290)
        self.var_blues.clicked.connect(self.check)

    def switch(self):
        if self.login.text() == "Now playing:":
            self.login.setText("Paused")
            self.btn01.setText("Play")
        else:
            self.login.setText("Now playing:")
            self.btn01.setText("Pause")

    def forward(self):
        if self.currentSong == 2:
            self.currentSong = 0
            self.password.setText(self.songs[self.currentSong])
            self.disp.display(self.currentSong + 1)
        else:
            self.currentSong += 1
            self.password.setText(self.songs[self.currentSong])
            self.disp.display(self.currentSong + 1)

    def back(self):
        if self.currentSong == 0:
            self.currentSong = 2
            self.password.setText(self.songs[self.currentSong])
            self.disp.display(self.currentSong + 1)
        else:
            self.currentSong -= 1
            self.password.setText(self.songs[self.currentSong])
            self.disp.display(self.currentSong + 1)

    def check(self):
        if self.reggae.isChecked():
            self.regL.show()
        else:
            self.regL.hide()

        if self.jazz_blues.isChecked():
            self.jazzL.show()
        else:
            self.jazzL.hide()

        if self.folk_blues.isChecked():
            self.folkL.show()
        else:
            self.folkL.hide()

        if self.var_blues.isChecked():
            self.bluesL.show()
        else:
            self.bluesL.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
