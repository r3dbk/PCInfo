import sys
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3
import datetime

conn = sqlite3.connect('wholelist.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ds_users(
   login TEXT,
   passw TEXT,
   name TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS ds_rem(
   login TEXT,
   name_rem TEXT,
   text_rem TEXT,
   time TEXT,
   date TEXT);
""")
conn.commit()

# cur.execute("""CREATE TABLE IF NOT EXISTS users_rem_db(
#                        user TEXT,
#                        name TEXT,
#                        comment TEXT,
#                        date-time TEXT);
#                     """)
# conn.commit()

login_name = ''


def check_list(checking_line):
    print(checking_line + " checking line")
    counter = 0
    cur.execute("SELECT * FROM ds_users;")
    one_res = cur.fetchall()
    print(one_res)
    for array in one_res:
        if array[0] == checking_line:
            print('got')
            counter += 1
    if counter != 0:
        return True


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        global date_on_cal, time_on_cal
        self.pushButton_4.hide()
        self.pushButton_2.clicked.connect(self.registration)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.show_registration_frame)
        self.pushButton_4.clicked.connect(self.show_login_frame)
        self.pushButton_5.clicked.connect(self.push_remind)
        self.pushButton_6.clicked.connect(lambda state, show_all=True: self.draw_ev(show_all))
        self.pushButton_7.clicked.connect(lambda state, show_all='td': self.draw_ev(show_all))
        self.pushButton_8.clicked.connect(self.clear_rem)
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Comment", "Time", "Date"])
        date_on_cal = self.calendarWidget.selectedDate().toPyDate()
        time_on_cal = self.timeEdit.time().toPyTime()
        self.frame_2.hide()
        self.frame_3.hide()

    def registration(self):
        # self.frame.hide()
        # self.frame_3.hide()
        # self.frame_2.show()
        # print('in')
        if self.lineEdit_3.text() == '' or check_list(self.lineEdit_3.text()):
            self.label_2.setText('This login is already exists')
        else:
            user = (self.lineEdit_3.text().lower(), self.lineEdit_4.text(), self.lineEdit_5.text())
            cur.execute("INSERT INTO ds_users VALUES(?, ?, ?);", user)
            conn.commit()
            self.frame.show()
            self.frame_2.hide()
            self.frame_3.hide()
            self.pushButton_4.hide()

    def show_registration_frame(self):
        self.pushButton_4.show()
        self.frame.hide()
        self.frame_2.show()
        self.frame_3.hide()

    def show_login_frame(self):
        self.pushButton_4.setText('Back to Login')
        self.pushButton_4.hide()
        self.frame.show()
        self.frame_2.hide()
        self.frame_3.hide()

    def calendar_clicked(self):
        global date_on_cal
        date_on_cal = self.calendarWidget.selectedDate().toPyDate()
        print(str(date_on_cal))
        self.label_7.setText(date_on_cal.strftime("%B %d, %Y"))
        self.draw_ev(False)

    def time_clicked(self):
        time_on_cal = self.timeEdit.selectedTime.toPyTime()
        print(str(time_on_cal))

    def push_remind(self):
        # rem = (login_name, self.lineEdit_6.text(), self.textEdit.text(), str(self.timeEdit.time().toPyTime()),
        #        str(self.calendarWidget.selectedDate().toPyDate()))
        rem = (login_name, self.lineEdit_6.text(), self.textEdit.toPlainText(), str(self.timeEdit.time().toPyTime()),
               self.calendarWidget.selectedDate().toPyDate())
        cur.execute("INSERT INTO ds_rem VALUES(?, ?, ?, ?, ?);", rem)
        conn.commit()
        self.draw_ev(False)

    def draw_ev(self, show_all):
        print(show_all)
        row = 0
        x = ""
        cou = 0
        cur.execute("SELECT * FROM ds_rem;")
        one_ges = cur.fetchall()
        print(login_name + ' login')
        for any_item in one_ges:
            if any_item[0] == login_name.lower():
                if show_all == True:
                    for somethingx in any_item:
                        if cou >= 4:
                            x += str(
                                datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y")) + '; \n'
                            cou = 0
                        elif cou == 3:
                            x += str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                            cou += 1
                        else:
                            x += somethingx + ", "
                            self.tableWidget.setItem(row, 0, QTableWidgetItem(any_item[0]))
                            cou += 1
                elif show_all == 'td':
                    if any_item[4] == str(datetime.date.today().strftime("%Y-%m-%d")):
                        for somethingx in any_item:
                            if cou >= 4:
                                x += str(datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                    "%B %d, %Y")) + '; \n'
                                cou = 0
                            elif cou == 3:
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                cou += 1
                            else:
                                x += somethingx + ", "
                                cou += 1
                else:
                    print(date_on_cal)
                    if any_item[4] == str(date_on_cal.strftime("%Y-%m-%d")):
                        for somethingx in any_item:
                            if cou >= 4:
                                x += str(datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                    "%B %d, %Y")) + '; \n'
                                cou = 0
                            elif cou == 3:
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                cou += 1
                            else:
                                x += somethingx + ", "
                                cou += 1
        self.textEdit_2.setText(str(x))
        print(one_ges)
        if x == '':
            self.textEdit_2.setText('No events!')
        self.label_7.setText(date_on_cal.strftime("%B %d, %Y"))
        self.label_8.setText('Today is: ' + datetime.date.today().strftime("%B %d, %Y"))

    def clear_rem(self):
        print('ds_rem cleared')
        cur.execute("DELETE FROM ds_rem;")
        conn.commit()
        self.draw_ev(True)

    def login(self):
        global login_name
        cur.execute("SELECT * FROM ds_users;")
        one_res = cur.fetchall()
        for something in one_res:
            if self.lineEdit.text().lower() in something:
                # print(self.lineEdit.text(), "\t", something[0], '\n')
                # print(self.lineEdit_2.text(), "\t", something[1])
                if self.lineEdit_2.text() == something[1]:
                    self.frame.hide()
                    self.frame_2.hide()
                    self.frame_3.show()
                    self.label_3.setText('Welcome, ' + str(something[-1]) + '!')
                    login_name = self.lineEdit.text()
                    self.draw_ev(False)
                    self.pushButton_4.setText('Log out ' + self.lineEdit.text().upper())
                    self.pushButton_4.show()
                    break
                else:
                    self.label.setText("Wrong password")
                print('x')
                break
            else:
                self.label.setText("Such login doesn't exist")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
