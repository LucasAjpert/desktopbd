# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBbEPgQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import templete.img as img

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(317, 259)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-50, -50, 471, 401))
        self.label.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 51, 51))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"image: url(:/img/icons/personal.svg);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 100, 49, 101))
        self.label_3.setStyleSheet(u"image: url(:/img/icons/browse.svg)")
        self.entrarbotao = QPushButton(Dialog)
        self.entrarbotao.setObjectName(u"entrarbotao")
        self.entrarbotao.setGeometry(QRect(130, 190, 75, 24))
        self.entrarbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.usuario = QLineEdit(Dialog)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(120, 80, 113, 21))
        self.senha = QLineEdit(Dialog)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(120, 140, 113, 21))
        self.senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 20, 211, 41))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText("")
        self.entrarbotao.setText(QCoreApplication.translate("Dialog", u"LOGAR", None))
        self.usuario.setText("")
        self.senha.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">SISTEMA CRUD DESKTOP</span></p></body></html>", None))
    # retranslateUi

