# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Eric\PycharmProjects\LAA\resources\widget\Assignment4Widget\Widget.ui'
#
# Created: Sun Nov 29 20:45:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class PySideUiFileSetup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 515)
        Dialog.assignment4Label = QtGui.QLabel(Dialog)
        Dialog.assignment4Label.setGeometry(QtCore.QRect(30, 10, 111, 21))
        Dialog.assignment4Label.setObjectName("assignment4Label")
        Dialog.upBtn = QtGui.QPushButton(Dialog)
        Dialog.upBtn.setGeometry(QtCore.QRect(20, 40, 112, 34))
        Dialog.upBtn.setObjectName("upBtn")
        Dialog.downBtn = QtGui.QPushButton(Dialog)
        Dialog.downBtn.setGeometry(QtCore.QRect(20, 80, 112, 34))
        Dialog.downBtn.setObjectName("downBtn")
        Dialog.returnHomeBtn = QtGui.QPushButton(Dialog)
        Dialog.returnHomeBtn.setGeometry(QtCore.QRect(20, 120, 112, 34))
        Dialog.returnHomeBtn.setObjectName("returnHomeBtn")
        Dialog.schnauzUpBtn = QtGui.QPushButton(Dialog)
        Dialog.schnauzUpBtn.setGeometry(QtCore.QRect(170, 40, 131, 34))
        Dialog.schnauzUpBtn.setObjectName("schnauzUpBtn")
        Dialog.schnauzDownBtn = QtGui.QPushButton(Dialog)
        Dialog.schnauzDownBtn.setGeometry(QtCore.QRect(170, 80, 131, 34))
        Dialog.schnauzDownBtn.setObjectName("schnauzDownBtn")
        Dialog.eyebrowUpBtn = QtGui.QPushButton(Dialog)
        Dialog.eyebrowUpBtn.setGeometry(QtCore.QRect(350, 40, 131, 34))
        Dialog.eyebrowUpBtn.setObjectName("eyebrowUpBtn")
        Dialog.eyebrowDwnBtn = QtGui.QPushButton(Dialog)
        Dialog.eyebrowDwnBtn.setGeometry(QtCore.QRect(350, 80, 131, 34))
        Dialog.eyebrowDwnBtn.setObjectName("eyebrowDwnBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.assignment4Label.setText(QtGui.QApplication.translate("Dialog", "Assignment 4", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.upBtn.setText(QtGui.QApplication.translate("Dialog", "Smile Up", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.downBtn.setText(QtGui.QApplication.translate("Dialog", "Smile Down", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.returnHomeBtn.setText(QtGui.QApplication.translate("Dialog", "Return Home", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.schnauzUpBtn.setText(QtGui.QApplication.translate("Dialog", "Schnauz Up", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.schnauzDownBtn.setText(QtGui.QApplication.translate("Dialog", "Schnauz Down", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.eyebrowUpBtn.setText(QtGui.QApplication.translate("Dialog", "Eyebrows Up", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.eyebrowDwnBtn.setText(QtGui.QApplication.translate("Dialog", "Eyebrows Down", None, QtGui.QApplication.UnicodeUTF8))

