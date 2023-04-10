import sys
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtCore import QStringListModel, Qt
import sqlite3
import datetime
import requests
from autocorrect import Speller

# url = "https://jspell-checker.p.rapidapi.com/check"

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


# spell = Speller(lang='ru')
#
#
# def check_list(checking_line):
#     print(checking_line + " checking line")
#     counter = 0
#     cur.execute("SELECT * FROM ds_users;")
#     one_res = cur.fetchall()
#     print(one_res)
#     for array in one_res:
#         if array[0] == checking_line:
#             print('got')
#             counter += 1
#     if counter != 0:
#         return True


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
        # self.pushButton_11.clicked.connect(self.check_text)
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Comment", "Time", "Date"])
        date_on_cal = self.calendarWidget.selectedDate().toPyDate()
        time_on_cal = self.timeEdit.time().toPyTime()
        self.frame_2.hide()
        self.frame_3.hide()
        self.cou = 1
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.listView.doubleClicked.connect(self.change_func)
        # self.listView.setModel(self.model)

    # def check_text(self):
    # print(self.textEdit.toPlainText())
    # payload = {
    #     "language": "enUS",
    #     "fieldvalues": self.textEdit.toPlainText(),
    #     "config": {
    #         "forceUpperCase": False,
    #         "ignoreIrregularCaps": False,
    #         "ignoreFirstCaps": True,
    #         "ignoreNumbers": True,
    #         "ignoreUpper": False,
    #         "ignoreDouble": False,
    #         "ignoreWordsWithNumbers": True
    #     }
    # }
    # headers = {
    #     "content-type": "application/json",
    #     "X-RapidAPI-Key": "49807b3fd3msh96b96d700dc68f6p1ab4b7jsn854bae043bdd",
    #     "X-RapidAPI-Host": "jspell-checker.p.rapidapi.com"
    # }
    #
    # response = requests.request("POST", url, json=payload, headers=headers)
    #
    # # for k, value in response.items():
    # #     print(k)
    # #     print(value)
    #
    # print(headers.get("elements").text())
    # print(spell('Провереа'))

    def registration(self):
        # self.frame.hide()
        # self.frame_3.hide()
        # self.frame_2.show()
        # print('in')
        if self.lineEdit_3.text() == '':
            self.label_2.setText('This login is already exists')
        else:
            user = (self.lineEdit_3.text().lower(), self.lineEdit_4.text(), self.lineEdit_5.text())
            cur.execute("INSERT INTO ds_users VALUES(?, ?, ?);", user)
            conn.commit()
            self.frame.show()
            self.frame_2.hide()
            self.frame_3.hide()
            self.pushButton_4.hide()

    def change_func(self, index):
        print('GOT! ' + self.listView.currentIndex().data())

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
        cur.execute("SELECT * FROM ds_rem;")
        one_ges = cur.fetchall()
        self.cou = 1
        print(login_name + ' login')
        self.tableWidget.setRowCount(0)
        self.model.setRowCount(0)
        for any_item in one_ges:
            if any_item[0] == login_name.lower():
                if show_all == True:
                    self.tableWidget.insertRow(row)
                    for somethingx in any_item:

                        if self.cou == 5:
                            print("any_item = 4")
                            print(somethingx)

                            x += str(
                                datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y")) + '; \n'
                            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                            self.cou = 1

                        elif self.cou == 4:
                            print("any_item = 3")
                            print(somethingx)
                            x += str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                            self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                            self.cou += 1
                            print("count on cou = 3: " + str(self.cou))
                        elif self.cou == 3:
                            print("any_item = 2")
                            x += somethingx + ", "
                            self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                            self.cou += 1
                            print("count on cou = 2: " + str(self.cou))
                        elif self.cou == 2:
                            print("any_item = 1")
                            print(somethingx)
                            # print(somethingx + " smthn 2 " + cou)
                            x += somethingx + ", "
                            self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                            # print('yes')
                            # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                            self.cou += 1
                        elif self.cou == 1:
                            self.cou += 1
                    row += 1
                    self.model.appendRow(QStandardItem(x))
                    print('that is x: ' + x)
                    x = ''
                elif show_all == 'td':
                    print(any_item[4] + 'this is fourth item')
                    if any_item[4] == str(datetime.date.today().strftime("%Y-%m-%d")):
                        self.tableWidget.insertRow(row)
                        for somethingx in any_item:

                            if self.cou == 5:
                                print("any_item = 4")
                                print(somethingx)

                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                        "%B %d, %Y")) + '; \n'
                                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                                self.cou = 1

                            elif self.cou == 4:
                                print("any_item = 3")
                                print(somethingx)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                    str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                                self.cou += 1
                                print("count on cou = 3: " + str(self.cou))
                            elif self.cou == 3:
                                print("any_item = 2")
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                                self.cou += 1
                                print("count on cou = 2: " + str(self.cou))
                            elif self.cou == 2:
                                print("any_item = 1")
                                print(somethingx)
                                # print(somethingx + " smthn 2 " + cou)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                                # print('yes')
                                # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                                self.cou += 1
                            elif self.cou == 1:
                                self.cou += 1
                        row += 1
                        self.model.appendRow(QStandardItem(x))
                        print('that is x: ' + x)
                        x = ''
                else:
                    print(date_on_cal)
                    if any_item[4] == str(date_on_cal.strftime("%Y-%m-%d")):
                        self.tableWidget.insertRow(row)
                        for somethingx in any_item:

                            if self.cou == 5:
                                print("any_item = 4")
                                print(somethingx)

                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                        "%B %d, %Y")) + '; \n'
                                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                                self.cou = 1

                            elif self.cou == 4:
                                print("any_item = 3")
                                print(somethingx)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                    str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                                self.cou += 1
                                print("count on cou = 3: " + str(self.cou))
                            elif self.cou == 3:
                                print("any_item = 2")
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                                self.cou += 1
                                print("count on cou = 2: " + str(self.cou))
                            elif self.cou == 2:
                                print("any_item = 1")
                                print(somethingx)
                                # print(somethingx + " smthn 2 " + cou)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                                # print('yes')
                                # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                                self.cou += 1
                            elif self.cou == 1:
                                self.cou += 1
                        row += 1
                        self.model.appendRow(QStandardItem(x))
                        print('that is x: ' + x)
                        x = ''
        self.textEdit_2.setText(str(x))
        # print(one_ges)
        # if there are no events for this date:
        if row == 0:
            self.textEdit_2.setText('No events!')
            # inserting new row in table
            self.tableWidget.insertRow(row)
            # inserting 'No events!' in table
            self.tableWidget.setItem(row, 0, QTableWidgetItem('No events!'))
        # if we want to show all events:
        if show_all == True:
            # set label_7 text 'All events'
            self.label_7.setText('All events')
        # if we want to show today's events:
        elif show_all == 'td':
            # set label_7 text '*date* (today)'
            self.label_7.setText(datetime.date.today().strftime("%B %d, %Y") + ' (today)')
        # if we want to show events on selected date:
        else:
            # set label_7 text '*date*'
            self.label_7.setText(date_on_cal.strftime("%B %d, %Y"))
        self.label_8.setText('Today is: ' + datetime.date.today().strftime("%B %d, %Y"))

    def clear_rem(self):
        print('ds_rem cleared')
        cur.execute("DELETE FROM ds_rem;")
        conn.commit()
        self.tableWidget.setRowCount(0)
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
