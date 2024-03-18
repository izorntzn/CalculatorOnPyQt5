import sys
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
        self.ui.pushButton_15.clicked.connect(lambda: self.set_num(0))
        self.ui.pushButton_12.clicked.connect(self.devision)
        self.ui.pushButton_10.clicked.connect(self.equal)

    def set_num(self, num):

        self.curnum = self.ui.label.text()
        self.num = str(num)

        if str(self.curnum) != '0':
            self.ui.label.setText(self.curnum + self.num)

        else:
            self.ui.label.clear()
            self.ui.label.setText(self.num)

    def devision(self):
        self.f_num = self.ui.label.text()
        self.ui.label.clear()
        self.math = 'devision'

    def equal(self):
        self.t_num = self.ui.label.text()

        if self.math == 'devision':
            ans = int(self.f_num) / int(self.t_num)
            self.ui.label.setText(str(ans))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
