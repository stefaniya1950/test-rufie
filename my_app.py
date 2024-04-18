# напиши здесь код основного приложения и первого экрана
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QApplication
from instr import*
from second_win import*
class MainWin(QWidget):
    def __init__(self):
        super().__init__ ()
        self.set_appear ()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.hellow_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.line = QVBoxLayout()
        self.line.addWidget(self.hellow_text)
        self.line.addWidget(self.instruction)
        self.line.addWidget(self.button)
        self.setLayout (self.line)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
app = QApplication([])
mainwin = MainWin()
app.exec_()



