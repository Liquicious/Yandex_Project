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
            print(':: Encrypt A1Z26 ::')
        elif self.but_rot13.isChecked():
            print(':: Encrypt ROT13 ::')
        elif self.but_xor.isChecked():
            print(':: Encrypt XOR ::')
        elif self.but_rsa.isChecked():
            print(':: Encrypt RSA ::')
        elif self.but_atbash.isChecked():
            print(':: Encrypt Atbash ::')
        elif self.but_vishener.isChecked():
            print(':: Encrypt Vishener ::')
        elif self.but_vernam.isChecked():
            print(':: Encrypt Vernam ::')
        elif self.but_affine.isChecked():
            print(':: Encrypt Affine ::')
        elif self.but_bacon.isChecked():
            print(':: Encrypt Bacon ::')
        elif self.but_polibiy.isChecked():
            print(':: Encrypt Polibiy ::')
        elif self.but_book.isChecked():
            print(':: Encrypt Book ::')
        elif self.but_thritemius.isChecked():
            print(':: Encrypt Thritemius ::')
        elif self.but_couples.isChecked():
            print(':: Encrypt Couples ::')
        elif self.but_rotors.isChecked():
            print(':: Encrypt Rotors ::')
        elif self.but_homophonic.isChecked():
            print(':: Encrypt Homophonic ::')
        elif self.but_gronsfeld.isChecked():
            print(':: Encrypt Gronsfeld ::')
        elif self.but_replace.isChecked():
            print(':: Encrypt Replace ::')
        elif self.but_caesar.isChecked():
            print(':: Encrypt Caesar ::')

    def decrypt(self):
        if self.but_a1z26.isChecked():
            print(':: Decrypt A1Z26 ::')
        elif self.but_rot13.isChecked():
            print(':: Decrypt ROT13 ::')
        elif self.but_xor.isChecked():
            print(':: Decrypt XOR ::')
        elif self.but_rsa.isChecked():
            print(':: Decrypt RSA ::')
        elif self.but_atbash.isChecked():
            print(':: Decrypt Atbash ::')
        elif self.but_vishener.isChecked():
            print(':: Decrypt Vishener ::')
        elif self.but_vernam.isChecked():
            print(':: Decrypt Vernam ::')
        elif self.but_affine.isChecked():
            print(':: Decrypt Affine ::')
        elif self.but_bacon.isChecked():
            print(':: Decrypt Bacon ::')
        elif self.but_polibiy.isChecked():
            print(':: Decrypt Polibiy ::')
        elif self.but_book.isChecked():
            print(':: Decrypt Book ::')
        elif self.but_thritemius.isChecked():
            print(':: Decrypt Thritemius ::')
        elif self.but_couples.isChecked():
            print(':: Decrypt Couples ::')
        elif self.but_rotors.isChecked():
            print(':: Decrypt Rotors ::')
        elif self.but_homophonic.isChecked():
            print(':: Decrypt Homophonic ::')
        elif self.but_gronsfeld.isChecked():
            print(':: Decrypt Gronsfeld ::')
        elif self.but_replace.isChecked():
            print(':: Decrypt Replace ::')
        elif self.but_caesar.isChecked():
            print(':: Decrypt Caesar ::')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
