import sys

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

window_titles = [
    'My App',
    'Still my',
    'Smthg went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets")

        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit, ]

        for w in widgets:
            layout.addWidget(w())

            widget = QWidget()
            widget.setLayout(layout)

            self.setCentralWidget(widget)


    #     # self.show()
    #     self.label = QLabel("Click in this window")
    #     self.setCentralWidget(self.label)
    #     # self.setContextMenuPolicy(Qt.CustomContextMenu)
    #     # self.customContextMenuRequested.connect(self.on_context_menu)
    #
    # def contextMenuEvent(self, e):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(e.globalPos())
    #
    #
    # def mouseMoveEvent(self, e):
    #     self.label.setText("mouseMoveEvent")
    #
    # def mousePressEvent(self, e):
    #     print('1')
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         print('2')
    #         self.label.setText("mouseLeftPressEvent")
    #
    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("mouseMidPressEvent")
    #
    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mouseRightPressEvent")

    # def mouseReleaseEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         self.label.setText("mouseLeftReleaseEvent")
    #
    #     elif e.button() == Qt.MiddleButton:
    #         self.label.setText("mouseMidReleaseEvent")
    #
    #     elif e.button() == Qt.RightButton:
    #         self.label.setText("mouseRightReleaseEvent")
    #
    # def mouseDoubleClickEvent(self, e):
    #     if e.button() == Qt.LeftButton:
    #         self.label.setText("mouseLeftDblEvent")
    #
    #     elif e.button() == Qt.MiddleButton:
    #         self.label.setText("mouseMidDblEvent")
    #
    #     elif e.button() == Qt.RightButton:
    #         self.label.setText("mouseRightDblEvent")

    # def the_button_was_clicked(self):
    #     print('Button was clicked')
    #     new_window_title = choice(window_titles)
    #     print("Setting title: %s" % new_window_title)
    #     self.setWindowTitle(random.choice(window_titles))
    #
    # def the_window_title_changed(self, window_title):
    #     print("Window title has changed: %s" % window_title)
    #
    #     if window_title == 'Smthg went wrong':
    #         self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
