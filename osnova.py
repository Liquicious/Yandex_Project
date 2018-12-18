import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from shifr_ui import Ui_Encryptor
from crypts import Crypts


class MyWidget(QMainWindow, Ui_Encryptor, Crypts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.but_en.clicked.connect(self.encrypt)
        self.but_de.clicked.connect(self.decrypt)

    def encrypt(self):
        self.text_out.clear()
        text_in = self.text_in.toPlainText()
        text_key = self.text_key.toPlainText()
        if self.but_a1z26.isChecked():
            self.text_out.append(self.a1z26('E', text_in))
        elif self.but_rot13.isChecked():
            self.text_out.append(self.rot13(text_in))
        elif self.but_xor.isChecked():
            self.text_out.append(self.xor(text_in, text_key))
        elif self.but_rsa.isChecked():
            self.text_out.append(self.rsa('E', text_in, text_key))
        elif self.but_atbash.isChecked():
            self.text_out.append(self.atbash(text_in))
        elif self.but_vishener.isChecked():
            self.text_out.append(self.vishener('E', text_in, text_key))
        elif self.but_vernam.isChecked():
            self.text_out.append(self.vernam('E', text_in, text_key))
        elif self.but_affine.isChecked():
            self.text_out.append(self.affine('E', text_in, text_key))
        elif self.but_bacon.isChecked():
            self.text_out.append(self.bacon('E', text_in, text_key))
        elif self.but_polibiy.isChecked():
            self.text_out.append(self.polibiy('E', text_in))
        elif self.but_book.isChecked():
            self.text_out.append(self.book('E', text_in, text_key))
        elif self.but_thritemius.isChecked():
            self.text_out.append(self.thritemius(text_in))
        elif self.but_couples.isChecked():
            self.text_out.append(self.couples(text_in))
        elif self.but_rotors.isChecked():
            self.text_out.append(self.rotors('E', text_in))
        elif self.but_homophonic.isChecked():
            self.text_out.append(self.homophonic('E', text_in))
        elif self.but_gronsfeld.isChecked():
            self.text_out.append(self.gronsfeld('E', text_in))
        elif self.but_replace.isChecked():
            self.text_out.append(self.replace('E', text_in))
        elif self.but_caesar.isChecked():
            try:
                self.text_out.append(self.caesar('E', text_in, int(text_key)))
            except Exception:
                raise

    def decrypt(self):
        self.text_out.clear()
        text_in = self.text_in.toPlainText()
        text_key = self.text_key.toPlainText()
        if self.but_a1z26.isChecked():
            self.text_out.append(self.a1z26('D', text_in))
        elif self.but_rot13.isChecked():
            self.text_out.append(self.rot13(text_in))
        elif self.but_xor.isChecked():
            self.text_out.append(self.xor(text_in, text_key))
        elif self.but_rsa.isChecked():
            self.text_out.append(self.rsa('D', text_in, text_key))
        elif self.but_atbash.isChecked():
            self.text_out.append(self.atbash(text_in))
        elif self.but_vishener.isChecked():
            self.text_out.append(self.vishener('D', text_in, text_key))
        elif self.but_vernam.isChecked():
            self.text_out.append(self.vernam('D', text_in, text_key))
        elif self.but_affine.isChecked():
            self.text_out.append(self.affine('D', text_in, text_key))
        elif self.but_bacon.isChecked():
            self.text_out.append(self.bacon('D', text_in, text_key))
        elif self.but_polibiy.isChecked():
            self.text_out.append(self.polibiy('D', text_in))
        elif self.but_book.isChecked():
            self.text_out.append(self.book('D', text_in, text_key))
        elif self.but_thritemius.isChecked():
            self.text_out.append(self.thritemius(text_in))
        elif self.but_couples.isChecked():
            self.text_out.append(self.couples(text_in))
        elif self.but_rotors.isChecked():
            self.text_out.append(self.rotors('D', text_in))
        elif self.but_homophonic.isChecked():
            self.text_out.append(self.homophonic('D', text_in))
        elif self.but_gronsfeld.isChecked():
            self.text_out.append(self.gronsfeld('D', text_in))
        elif self.but_replace.isChecked():
            self.text_out.append(self.replace('D', text_in))
        elif self.but_caesar.isChecked():
            self.text_out.append(self.caesar('D', text_in, text_key))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
