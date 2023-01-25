from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from my_app import *
from instr import *
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Здоровье')
my_win.move(200, 100)
my_win.resize(1000, 600)

v_line1 = QVBoxLayout()
LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()

number1 = QLabel('Индекс Руфье: какой-то там')
number2 = QLabel('Работоспособность сердца: вы умерли')

LayoutH1.addWidget(number1, alignment = Qt.AlignCenter)
LayoutH2.addWidget(number2, alignment = Qt.AlignCenter)

v_line1.addLayout(LayoutH1)
v_line1.addLayout(LayoutH2)
my_win.setLayout(v_line1)


my_win.show()
app.exec_()