# напиши здесь код для второго экран
from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout
from instr import*
from PyQt5.QtCore import Qt
from final_win import*
class TestWin(QWidget):
    def __init__(self):
        super().__init__ ()
        self.initUI()
        self.connects()
        self.set_appear ()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.button_next = QPushButton (txt_sendresults,self)
        self.button_test_1 = QPushButton (txt_starttest1,self)
        self.button_test_2 = QPushButton (txt_starttest2,self)
        self.button_test_3 = QPushButton (txt_starttest3,self)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test_1 = QLabel(txt_test1)
        self.text_test_2 = QLabel(txt_test2)
        self.text_test_3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.left_line = QVBoxLayout()
        self.right_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.right_line.addWidget(self.text_timer,alignment=Qt.AlignCenter)
        self.left_line.addWidget(self.text_name,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_name,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_age,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_age,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_test_1,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_test_1,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_test1,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_test_2,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_test_2,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_test2,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.text_test_3,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_test_3,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.line_test3,alignment=Qt.AlignLeft)
        self.left_line.addWidget(self.button_next,alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.left_line)
        self.h_line.addLayout(self.right_line)
        self.setLayout(self.h_line)
    def next_click (self):
        self.hide()
        self.fw = FinalWin()
    def connects (self):
        self.button_next.clicked.connect(self.next_click)


