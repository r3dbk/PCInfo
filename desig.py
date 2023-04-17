import sys
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QWidget
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt6.QtCore import QStringListModel
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
        self.pushButton_9.clicked.connect(self.delete_sel)
        self.pushButton_10.clicked.connect(lambda state, ret=True: self.done_edit(ret))
        self.pushButton_12.clicked.connect(self.done_edit)
        # self.pushButton_11.clicked.connect(self.check_text)
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Comment", "Time", "Date"])
        date_on_cal = self.calendarWidget.selectedDate().toPyDate()
        time_on_cal = self.timeEdit.time().toPyTime()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.cou = 1
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger(0))
        self.listView.doubleClicked.connect(self.change_func)
        self.listViewList = []
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

    def done_edit(self, ret):
        element = self.listViewList[self.listView.currentIndex().row()]
        if ret == True:
            self.frame_5.show()
            self.frame_4.hide()
            self.pushButton_6.show()
            self.pushButton_7.show()
            self.pushButton_8.show()
            self.label_7.show()
            self.draw_ev(True)
        else:
            cur.execute(
                '''UPDATE ds_rem SET name_rem = ?, text_rem = ?, time = ?, date = ? WHERE login = ? AND name_rem = ? AND text_rem = ? AND time = ? AND date = ?''',
                (str(self.label_9.text()), str(self.textEdit_3.toPlainText()), str(self.timeEdit_2.time().toPyTime()),
                 str(self.dateEdit.date().toPyDate()), str(element[-5]), str(element[-4]), str(element[-3]),
                 str(element[-2]), str(element[-1])))
            conn.commit()
            self.frame_5.show()
            self.frame_4.hide()
            self.pushButton_6.show()
            self.pushButton_7.show()
            self.pushButton_8.show()
            self.label_7.show()
            self.draw_ev(True)

    def change_func(self, index):
        tr_res = self.listView.currentIndex().row()
        element = self.listViewList[tr_res]
        print('GOT! ' + self.listView.currentIndex().data())
        self.frame_5.hide()
        self.frame_4.show()
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.pushButton_8.hide()
        self.label_7.hide()
        self.textEdit_3.setText(str(element[-3]))
        self.label_9.setText(element[1])
        self.timeEdit_2.setTime(
            QtCore.QTime(int(datetime.datetime.strptime(str(element[-2]), "%H:%M:%S").strftime("%H")),
                         int(datetime.datetime.strptime(str(element[-2]), "%H:%M:%S").strftime("%M"))))
        self.dateEdit.setDate(QtCore.QDate().fromString(element[-1], "yyyy-MM-dd"))
        print(self.listViewList[tr_res])
        print(tr_res)
        print(self.timeEdit_2.time().toPyTime(), self.dateEdit.date().toPyDate())

    def delete_sel(self):
        element = self.listViewList[self.listView.currentIndex().row()]
        cur.execute(
            '''DELETE FROM ds_rem WHERE login = ? AND name_rem = ? AND text_rem = ? AND time = ? AND date = ?''',
            (str(element[-5]), str(element[-4]), str(element[-3]),
             str(element[-2]), str(element[-1])))
        conn.commit()
        self.frame_5.show()
        self.frame_4.hide()
        self.pushButton_6.show()
        self.pushButton_7.show()
        self.pushButton_8.show()
        self.label_7.show()
        self.draw_ev(True)

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
        cur.execute("SELECT * FROM ds_rem;")
        one_ges = cur.fetchall()
        rem_r = (login_name, self.lineEdit_6.text(), self.textEdit.toPlainText(), str(self.timeEdit.time().toPyTime()),
                 self.calendarWidget.selectedDate().toPyDate().strftime("%Y-%m-%d"))
        print('HERE             :', one_ges, ' gg ', rem_r)
        if rem_r in one_ges:
            print(rem_r, "SUCH ELEMENT ALREADY EXISTS")
        else:
            cur.execute("INSERT INTO ds_rem VALUES(?, ?, ?, ?, ?);", rem)
            conn.commit()
        self.draw_ev(False)

    def draw_ev(self, show_all):
        print(show_all)
        row = 0
        x = ""
        elem = ()
        self.listViewList = []
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
                            elem = elem + (somethingx,)
                            x += str(
                                datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y")) + '\n'
                            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                            self.cou = 1

                        elif self.cou == 4:
                            print("any_item = 3")
                            elem = elem + (somethingx,)
                            print(somethingx)
                            x += str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                            self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                            self.cou += 1
                            print("count on cou = 3: " + str(self.cou))
                        elif self.cou == 3:
                            print("any_item = 2")
                            elem = elem + (somethingx,)
                            x += somethingx + ", "
                            self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                            self.cou += 1
                            print("count on cou = 2: " + str(self.cou))
                        elif self.cou == 2:
                            print("any_item = 1")
                            print(somethingx)
                            elem = elem + (somethingx,)
                            # print(somethingx + " smthn 2 " + cou)
                            x += somethingx + ", "
                            self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                            # print('yes')
                            # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                            self.cou += 1
                        elif self.cou == 1:
                            elem = elem + (somethingx,)
                            self.cou += 1
                    row += 1
                    print("Elem is: " + str(self.listViewList))
                    self.listViewList.append(elem)
                    elem = ()
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
                                elem = elem + (somethingx,)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                        "%B %d, %Y")) + '\n'
                                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                                self.cou = 1

                            elif self.cou == 4:
                                print("any_item = 3")
                                elem = elem + (somethingx,)
                                print(somethingx)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                    str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                                self.cou += 1
                                print("count on cou = 3: " + str(self.cou))
                            elif self.cou == 3:
                                print("any_item = 2")
                                elem = elem + (somethingx,)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                                self.cou += 1
                                print("count on cou = 2: " + str(self.cou))
                            elif self.cou == 2:
                                print("any_item = 1")
                                print(somethingx)
                                elem = elem + (somethingx,)
                                # print(somethingx + " smthn 2 " + cou)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                                # print('yes')
                                # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                                self.cou += 1
                            elif self.cou == 1:
                                elem = elem + (somethingx,)
                                self.cou += 1
                        row += 1
                        print("Elem is: " + str(self.listViewList))
                        self.listViewList.append(elem)
                        elem = ()
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
                                elem = elem + (somethingx,)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime(
                                        "%B %d, %Y")) + '\n'
                                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(
                                    datetime.datetime.strptime(str(somethingx), "%Y-%m-%d").strftime("%B %d, %Y"))))
                                self.cou = 1

                            elif self.cou == 4:
                                print("any_item = 3")
                                elem = elem + (somethingx,)
                                print(somethingx)
                                x += str(
                                    datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M")) + ", "
                                self.tableWidget.setItem(row, 2, QTableWidgetItem(
                                    str(datetime.datetime.strptime(str(somethingx), "%H:%M:%S").strftime("%H:%M"))))
                                self.cou += 1
                                print("count on cou = 3: " + str(self.cou))
                            elif self.cou == 3:
                                print("any_item = 2")
                                elem = elem + (somethingx,)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 1, QTableWidgetItem(somethingx))
                                self.cou += 1
                                print("count on cou = 2: " + str(self.cou))
                            elif self.cou == 2:
                                print("any_item = 1")
                                print(somethingx)
                                elem = elem + (somethingx,)
                                # print(somethingx + " smthn 2 " + cou)
                                x += somethingx + ", "
                                self.tableWidget.setItem(row, 0, QTableWidgetItem(somethingx))
                                # print('yes')
                                # self.model.appendRow(QtGui.QStandardItem(any_item[-4]))
                                self.cou += 1
                            elif self.cou == 1:
                                elem = elem + (somethingx,)
                                self.cou += 1
                        row += 1
                        print("Elem is: " + str(self.listViewList))
                        self.listViewList.append(elem)
                        elem = ()
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
