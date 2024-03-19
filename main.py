import math
import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.set_num(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.set_num(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.set_num(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.set_num(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.set_num(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.set_num(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.set_num(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.set_num(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.set_num(9))
        self.ui.pushButton_18.clicked.connect(lambda: self.set_num('.'))
        self.ui.pushButton_15.clicked.connect(lambda: self.set_num(0))
        self.ui.pushButton_12.clicked.connect(self.devision)
        self.ui.pushButton_13.clicked.connect(self.multiply)
        self.ui.pushButton_10.clicked.connect(self.equal)
        self.ui.pushButton_14.clicked.connect(self.plus)
        self.ui.pushButton_11.clicked.connect(self.minus)
        self.ui.pushButton_16.clicked.connect(self.square)
        self.ui.pushButton_17.clicked.connect(self.sqrt)
        self.ui.pushButton_19.clicked.connect(self.clear)

    def set_num(self, num):
        self.curnum = self.ui.label.text()
        self.num = str(num)

        if self.curnum != '0':
            self.curnum = self.ui.label.text()
            n = self.curnum.count('.')
            if n == 1 and self.num == '.':
                pass
            else:
                self.ui.label.setText(self.curnum + self.num)

        else:
            self.ui.label.clear()
            self.ui.label.setText(self.num)

    def clear(self):
        self.ui.label.clear()

    def devision(self):
        self.f_num = self.ui.label.text()
        self.ui.label.clear()
        self.math = 'devision'

    def multiply(self):
        self.f_num = self.ui.label.text()
        self.ui.label.clear()
        self.math = 'multiply'

    def plus(self):
        self.f_num = self.ui.label.text()
        self.ui.label.clear()
        self.math = 'plus'

    def minus(self):
        self.f_num = self.ui.label.text()
        self.ui.label.clear()
        self.math = 'minus'

    def square(self):
        self.f_num = self.ui.label.text()
        ans = int(self.f_num) ** 2
        self.ui.label.setText(str(ans))

    def sqrt(self):
        self.f_num = self.ui.label.text()
        ans = math.sqrt(int(self.f_num))
        self.ui.label.setText(str(ans))

    def comm(self):
        # self.curnum = self.ui.label.text()
        # if '.' not in self.curnum:
        self.ui.label.setText('.')
#         if not self.f_num:
#             self.f_num = int(self.curnum)
#         else:
#             self.num = int(self.curnum)
#             self.f_num = self.f_num + self.num
    def equal(self):
        self.t_num = self.ui.label.text()

        if self.math == 'devision':
            ans = int(self.f_num) / int(self.t_num)
            self.ui.label.setText(str(ans))

        elif self.math == 'multiply':
            ans = int(self.f_num) * int(self.t_num)
            self.ui.label.setText(str(ans))

        elif self.math == 'minus':
            ans = int(self.f_num) - int(self.t_num)
            self.ui.label.setText(str(ans))

        elif self.math == 'plus':
            ans = int(self.f_num) + int(self.t_num)
            self.ui.label.setText(str(ans))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
