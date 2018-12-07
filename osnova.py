import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from shifr_ui import Ui_Encryptor


class MyWidget(QMainWindow, Ui_Encryptor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.but_en.clicked.connect(self.encrypt)
        self.but_de.clicked.connect(self.decrypt)

    def encrypt(self):
        if self.but_a1z26.isChecked():
            print('1')
        elif self.but_rot13.isChecked():
            print('2')
        elif self.but_xor.isChecked():
            print('3')
        elif self.but_rsa.isChecked():
            print('4')
        elif self.but_atbash.isChecked():
            print('5')
        elif self.but_vishener.isChecked():
            print('6')
        elif self.but_vernam.isChecked():
            print('7')
        elif self.but_affine.isChecked():
            print('8')
        elif self.but_bacon.isChecked():
            print('9')
        elif self.but_polibiy.isChecked():
            print('10')
        elif self.but_book.isChecked():
            print('11')
        elif self.but_thritemius.isChecked():
            print('12')
        elif self.but_couples.isChecked():
            print('13')
        elif self.but_rotors.isChecked():
            print('14')
        elif self.but_homophonic.isChecked():
            print('15')
        elif self.but_gronsfeld.isChecked():
            print('16')
        elif self.but_replace.isChecked():
            print('17')
        elif self.but_caesar.isChecked():
            print('18')

    def decrypt(self):
        if self.but_a1z26.isChecked():
            print('1')
        elif self.but_rot13.isChecked():
            print('2')
        elif self.but_xor.isChecked():
            print('3')
        elif self.but_rsa.isChecked():
            print('4')
        elif self.but_atbash.isChecked():
            print('5')
        elif self.but_vishener.isChecked():
            print('6')
        elif self.but_vernam.isChecked():
            print('7')
        elif self.but_affine.isChecked():
            print('8')
        elif self.but_bacon.isChecked():
            print('9')
        elif self.but_polibiy.isChecked():
            print('10')
        elif self.but_book.isChecked():
            print('11')
        elif self.but_thritemius.isChecked():
            print('12')
        elif self.but_couples.isChecked():
            print('13')
        elif self.but_rotors.isChecked():
            print('14')
        elif self.but_homophonic.isChecked():
            print('15')
        elif self.but_gronsfeld.isChecked():
            print('16')
        elif self.but_replace.isChecked():
            print('17')
        elif self.but_caesar.isChecked():
            print('18')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
