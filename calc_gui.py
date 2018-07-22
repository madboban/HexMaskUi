from sys import argv, exit
from math import log
from calc_ui import *
from PyQt5 import QtWidgets

char_config = {'X_ITEM': '0x1',
               'X_REQ': '0x2',
               'X_CMD': '0x4',
               'X_INV': '0x8',
               'X_QUOT': '0x10',
               'X_APPROB': '0x20',
               'X_CONTRACT': '0x80',
               'X_COMP': '0x100',
               'X_CAT': '0x800',
               'X_ART': '0x1000',
               'X_SUP': '0x2000',
               'X_CODE': '0x8000',
               'X_POPUP': '0x10000'}


def calculation(config: str):
    try:
        if config not in char_config:
            pow_limit = int(log(int(config, 16), 2))  #find maximum pow of config in with cast to int. 0x123 => 291 => int(log(291, 2)) = 8
            possible_values = [str(hex(2 ** i)) for i in range(pow_limit + 1)] #list generator with possible values for inputted config
            res = [possible_value for possible_value in possible_values if int(possible_value, 16) & int(config, 16)] #list generator with enabled values.
        else:
            res = [char_config[config], ]
    except ValueError:
        res = -1

    return res


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.MyFunction)

    def MyFunction(self):
        user_value = self.ui.lineEdit.text()
        res = calculation(str(user_value).upper())
        if res == -1:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Error')
            error_dialog.showMessage('Entered value is incorrect. Please check the value')
        else:
            res1 = ''
            for line in res:
                res1 += line + '\n'
            self.ui.textEdit.setText(res1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())
