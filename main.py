import math
import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow


def Input_file_equal(func):
    def wrapper(self):
        equal = func(self)
        with open("history.txt", "a+") as f:
            f_input = f'{self.f_num} {self.math} {self.s_num} = {self.ans}'
            f.write(f'{f_input}\n')
        return equal
    return wrapper

def Input_file_other(func):
    def wrapper(self):
        other = func(self)
        with open("history.txt", "a+") as f:
            f_input = f'{self.math}({self.f_num}) = {self.ans}'
            f.write(f'{f_input}\n')
        return other
    return wrapper

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.one.clicked.connect(lambda: self.set_num(1))
        self.ui.two.clicked.connect(lambda: self.set_num(2))
        self.ui.three.clicked.connect(lambda: self.set_num(3))
        self.ui.four.clicked.connect(lambda: self.set_num(4))
        self.ui.five.clicked.connect(lambda: self.set_num(5))
        self.ui.six.clicked.connect(lambda: self.set_num(6))
        self.ui.seven.clicked.connect(lambda: self.set_num(7))
        self.ui.eight.clicked.connect(lambda: self.set_num(8))
        self.ui.nine.clicked.connect(lambda: self.set_num(9))
        self.ui.zero.clicked.connect(lambda: self.set_num(0))
        self.ui.comma.clicked.connect(lambda: self.set_num('.'))
        self.ui.division.clicked.connect(self.division)
        self.ui.multiply.clicked.connect(self.multiply)
        self.ui.equal.clicked.connect(self.equal)
        self.ui.plus.clicked.connect(self.plus)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.square.clicked.connect(self.square)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.deleteAll.clicked.connect(self.delete)

    def set_num(self, num):
        self.curnum = self.ui.inputLabel.text()
        self.num = str(num)

        if self.curnum != '0':
            self.curnum = self.ui.inputLabel.text()
            n = self.curnum.count('.')
            if n == 1 and self.num == '.':
                pass
            else:
                self.ui.inputLabel.setText(self.curnum + self.num)

        else:
            self.ui.inputLabel.clear()
            self.ui.inputLabel.setText(self.num)

    def delete(self):
        self.ui.inputLabel.clear()

    def division(self):
        self.f_num = self.ui.inputLabel.text()
        self.ui.inputLabel.clear()
        self.math = '/'

    def multiply(self):
        self.f_num = self.ui.inputLabel.text()
        self.ui.inputLabel.clear()
        self.math = '*'

    def plus(self):
        self.f_num = self.ui.inputLabel.text()
        self.ui.inputLabel.clear()
        self.math = '+'

    def minus(self):
        self.f_num = self.ui.inputLabel.text()
        self.ui.inputLabel.clear()
        self.math = '-'

    @Input_file_other
    def square(self):
        self.f_num = self.ui.inputLabel.text()
        self.ans = int(self.f_num) ** 2
        self.ui.inputLabel.setText(str(self.ans))
        self.math = 'square'

    @Input_file_other
    def sqrt(self):
        self.f_num = self.ui.inputLabel.text()
        self.ans = math.sqrt(int(self.f_num))
        self.ui.inputLabel.setText(str(self.ans))
        self.math = 'sqrt'

    @Input_file_equal
    def equal(self):
        self.s_num = self.ui.inputLabel.text()

        if self.math == '/':
            self.ans = int(self.f_num) / int(self.s_num)
            self.ui.inputLabel.setText(str(self.ans))

        elif self.math == '*':
            self.ans = int(self.f_num) * int(self.s_num)
            self.ui.inputLabel.setText(str(self.ans))

        elif self.math == '-':
            self.ans = int(self.f_num) - int(self.s_num)
            self.ui.inputLabel.setText(str(self.ans))

        elif self.math == '+':
            self.ans = int(self.f_num) + int(self.s_num)
            self.ui.inputLabel.setText(str(self.ans))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
