# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shifr_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Encryptor(object):
    def setupUi(self, Encryptor):
        Encryptor.setObjectName("Encryptor")
        Encryptor.setEnabled(True)
        Encryptor.resize(831, 603)
        Encryptor.setStyleSheet("background-color: rgb(93, 93, 93);")
        self.centralwidget = QtWidgets.QWidget(Encryptor)
        self.centralwidget.setObjectName("centralwidget")
        self.text_key = QtWidgets.QTextEdit(self.centralwidget)
        self.text_key.setGeometry(QtCore.QRect(210, 10, 281, 41))
        self.text_key.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.text_key.setObjectName("text_key")
        self.but_a1z26 = QtWidgets.QRadioButton(self.centralwidget)
        self.but_a1z26.setEnabled(True)
        self.but_a1z26.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_a1z26.setFont(font)
        self.but_a1z26.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_a1z26.setChecked(True)
        self.but_a1z26.setObjectName("but_a1z26")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 0, 20, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 15, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(248, 255, 198);")
        self.label.setObjectName("label")
        self.text_in = QtWidgets.QTextEdit(self.centralwidget)
        self.text_in.setGeometry(QtCore.QRect(210, 80, 611, 191))
        self.text_in.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.text_in.setObjectName("text_in")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(248, 255, 198);")
        self.label_2.setObjectName("label_2")
        self.but_en = QtWidgets.QPushButton(self.centralwidget)
        self.but_en.setGeometry(QtCore.QRect(500, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.but_en.setFont(font)
        self.but_en.setStyleSheet("color: rgb(189, 255, 195);")
        self.but_en.setObjectName("but_en")
        self.but_de = QtWidgets.QPushButton(self.centralwidget)
        self.but_de.setGeometry(QtCore.QRect(670, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.but_de.setFont(font)
        self.but_de.setStyleSheet("color: rgb(189, 255, 195);")
        self.but_de.setObjectName("but_de")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 310, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(248, 255, 198);")
        self.label_3.setObjectName("label_3")
        self.text_out = QtWidgets.QTextEdit(self.centralwidget)
        self.text_out.setGeometry(QtCore.QRect(210, 310, 611, 191))
        self.text_out.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.text_out.setReadOnly(True)
        self.text_out.setObjectName("text_out")
        self.but_rot13 = QtWidgets.QRadioButton(self.centralwidget)
        self.but_rot13.setGeometry(QtCore.QRect(10, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_rot13.setFont(font)
        self.but_rot13.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_rot13.setObjectName("but_rot13")
        self.but_xor = QtWidgets.QRadioButton(self.centralwidget)
        self.but_xor.setGeometry(QtCore.QRect(10, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_xor.setFont(font)
        self.but_xor.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_xor.setObjectName("but_xor")
        self.but_atbash = QtWidgets.QRadioButton(self.centralwidget)
        self.but_atbash.setGeometry(QtCore.QRect(10, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_atbash.setFont(font)
        self.but_atbash.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_atbash.setObjectName("but_atbash")
        self.but_vishener = QtWidgets.QRadioButton(self.centralwidget)
        self.but_vishener.setGeometry(QtCore.QRect(10, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_vishener.setFont(font)
        self.but_vishener.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_vishener.setObjectName("but_vishener")
        self.but_vernam = QtWidgets.QRadioButton(self.centralwidget)
        self.but_vernam.setGeometry(QtCore.QRect(10, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_vernam.setFont(font)
        self.but_vernam.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_vernam.setObjectName("but_vernam")
        self.but_affine = QtWidgets.QRadioButton(self.centralwidget)
        self.but_affine.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_affine.setFont(font)
        self.but_affine.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_affine.setObjectName("but_affine")
        self.but_bacon = QtWidgets.QRadioButton(self.centralwidget)
        self.but_bacon.setGeometry(QtCore.QRect(10, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_bacon.setFont(font)
        self.but_bacon.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_bacon.setObjectName("but_bacon")
        self.but_polibiy = QtWidgets.QRadioButton(self.centralwidget)
        self.but_polibiy.setGeometry(QtCore.QRect(10, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_polibiy.setFont(font)
        self.but_polibiy.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_polibiy.setObjectName("but_polibiy")
        self.but_book = QtWidgets.QRadioButton(self.centralwidget)
        self.but_book.setGeometry(QtCore.QRect(10, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_book.setFont(font)
        self.but_book.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_book.setObjectName("but_book")
        self.but_couples = QtWidgets.QRadioButton(self.centralwidget)
        self.but_couples.setGeometry(QtCore.QRect(10, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_couples.setFont(font)
        self.but_couples.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_couples.setObjectName("but_couples")
        self.but_rotors = QtWidgets.QRadioButton(self.centralwidget)
        self.but_rotors.setGeometry(QtCore.QRect(10, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_rotors.setFont(font)
        self.but_rotors.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_rotors.setObjectName("but_rotors")
        self.but_homophonic = QtWidgets.QRadioButton(self.centralwidget)
        self.but_homophonic.setGeometry(QtCore.QRect(10, 370, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_homophonic.setFont(font)
        self.but_homophonic.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_homophonic.setObjectName("but_homophonic")
        self.but_replace = QtWidgets.QRadioButton(self.centralwidget)
        self.but_replace.setGeometry(QtCore.QRect(10, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_replace.setFont(font)
        self.but_replace.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_replace.setObjectName("but_replace")
        self.but_caesar = QtWidgets.QRadioButton(self.centralwidget)
        self.but_caesar.setEnabled(True)
        self.but_caesar.setGeometry(QtCore.QRect(10, 490, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_caesar.setFont(font)
        self.but_caesar.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_caesar.setObjectName("but_caesar")
        self.but_rsa = QtWidgets.QRadioButton(self.centralwidget)
        self.but_rsa.setGeometry(QtCore.QRect(10, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.but_rsa.setFont(font)
        self.but_rsa.setStyleSheet("color: rgb(192, 249, 255);")
        self.but_rsa.setObjectName("but_rsa")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 179, 179);")
        self.label_4.setObjectName("label_4")
        Encryptor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Encryptor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        self.menuLOL = QtWidgets.QMenu(self.menubar)
        self.menuLOL.setObjectName("menuLOL")
        Encryptor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Encryptor)
        self.statusbar.setObjectName("statusbar")
        Encryptor.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Encryptor)
        self.action.setObjectName("action")
        self.menuLOL.addAction(self.action)
        self.menubar.addAction(self.menuLOL.menuAction())

        self.retranslateUi(Encryptor)
        QtCore.QMetaObject.connectSlotsByName(Encryptor)

    def retranslateUi(self, Encryptor):
        _translate = QtCore.QCoreApplication.translate
        Encryptor.setWindowTitle(_translate("Encryptor", "MainWindow"))
        self.but_a1z26.setText(_translate("Encryptor", "A1Z26"))
        self.label.setText(_translate("Encryptor", "Key"))
        self.label_2.setText(_translate("Encryptor", "Input"))
        self.but_en.setText(_translate("Encryptor", "Encrypt"))
        self.but_de.setText(_translate("Encryptor", "Decrypt"))
        self.label_3.setText(_translate("Encryptor", "Output"))
        self.but_rot13.setText(_translate("Encryptor", "ROT13"))
        self.but_xor.setText(_translate("Encryptor", "XOR"))
        self.but_atbash.setText(_translate("Encryptor", "Atbash"))
        self.but_vishener.setText(_translate("Encryptor", "Vishener"))
        self.but_vernam.setText(_translate("Encryptor", "Vernam"))
        self.but_affine.setText(_translate("Encryptor", "Affine"))
        self.but_bacon.setText(_translate("Encryptor", "Bacon"))
        self.but_polibiy.setText(_translate("Encryptor", "Polibiy"))
        self.but_book.setText(_translate("Encryptor", "Book"))
        self.but_couples.setText(_translate("Encryptor", "Couples"))
        self.but_rotors.setText(_translate("Encryptor", "Rotors"))
        self.but_homophonic.setText(_translate("Encryptor", "Homophonic"))
        self.but_replace.setText(_translate("Encryptor", "Replace"))
        self.but_caesar.setText(_translate("Encryptor", "Caesar"))
        self.but_rsa.setText(_translate("Encryptor", "RSA"))
        self.label_4.setText(_translate("Encryptor", "Шифр"))
        self.menuLOL.setTitle(_translate("Encryptor", " "))
        self.action.setText(_translate("Encryptor", ":0"))

