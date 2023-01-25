# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__():
        super().__init__()
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.resize(win_width, win_height)
            self.move(win_x, win_y)
        def initUI(self):
            self.hello_text = QLabel(txt_hello)
            self.instruction = QLabel(txt_instruction)
            self.button = QPushButton(txt_next)
            self.layout = QVBoxLayout()
            self.hello_text.addWidget(self.layout)
            self.instruction.addWidget(self.layout)
            self.button.addWidget(self.layout)
        def next_click(self):
            self.hide
            