# напиши здесь код третьего экрана приложения
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout
from instr import*
from PyQt5.QtCore import Qt
class FinalWin(QWidget):
    def __init__(self):
        super().__init__ ()
        self.set_appear ()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.work_heart_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.line = QVBoxLayout()
        self.line.addWidget(self.work_heart_text,alignment=Qt.AlignCenter)
        self.line.addWidget(self.index_text,alignment=Qt.AlignCenter)
        self.setLayout(self.line)



         