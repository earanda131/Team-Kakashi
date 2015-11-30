# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Eric\PycharmProjects\LAA\resources\widget\Assignment3Widget\Widget.ui'
#
# Created: Sun Nov 29 20:45:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class PySideUiFileSetup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 422)
        Form.label = QtGui.QLabel(Form)
        Form.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        Form.label.setObjectName("label")
        Form.scriptBtn = QtGui.QPushButton(Form)
        Form.scriptBtn.setGeometry(QtCore.QRect(10, 40, 111, 31))
        Form.scriptBtn.setObjectName("scriptBtn")
        Form.homeBtn = QtGui.QPushButton(Form)
        Form.homeBtn.setGeometry(QtCore.QRect(10, 160, 111, 31))
        Form.homeBtn.setObjectName("homeBtn")
        Form.animateLegsBtn = QtGui.QPushButton(Form)
        Form.animateLegsBtn.setGeometry(QtCore.QRect(10, 80, 112, 34))
        Form.animateLegsBtn.setObjectName("animateLegsBtn")
        Form.animateBallBtn = QtGui.QPushButton(Form)
        Form.animateBallBtn.setGeometry(QtCore.QRect(10, 120, 112, 34))
        Form.animateBallBtn.setObjectName("animateBallBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.label.setText(QtGui.QApplication.translate("Form", "Assignment 3", None, QtGui.QApplication.UnicodeUTF8))
        Form.scriptBtn.setText(QtGui.QApplication.translate("Form", "Animate Arm", None, QtGui.QApplication.UnicodeUTF8))
        Form.homeBtn.setText(QtGui.QApplication.translate("Form", "Return Home", None, QtGui.QApplication.UnicodeUTF8))
        Form.animateLegsBtn.setText(QtGui.QApplication.translate("Form", "Animate Legs", None, QtGui.QApplication.UnicodeUTF8))
        Form.animateBallBtn.setText(QtGui.QApplication.translate("Form", "Animate Ball", None, QtGui.QApplication.UnicodeUTF8))

