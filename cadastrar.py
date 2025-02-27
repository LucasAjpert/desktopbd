# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrarZQXEUt.ui'
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
import cadastro

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(488, 265)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-280, -180, 891, 661))
        self.label.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 441, 41))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius: 8px;")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 50, 121, 101))
        self.label_3.setStyleSheet(u"image: url(:/cadastro/icons/pen.svg);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 41, 21))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 81, 21))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 120, 41, 21))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 150, 121, 21))
        self.cadastrarbotao = QPushButton(Dialog)
        self.cadastrarbotao.setObjectName(u"cadastrarbotao")
        self.cadastrarbotao.setGeometry(QRect(50, 220, 81, 24))
        self.cadastrarbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.cancelarbotao = QPushButton(Dialog)
        self.cancelarbotao.setObjectName(u"cancelarbotao")
        self.cancelarbotao.setGeometry(QRect(170, 220, 75, 24))
        self.cancelarbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.limparbotao = QPushButton(Dialog)
        self.limparbotao.setObjectName(u"limparbotao")
        self.limparbotao.setGeometry(QRect(290, 220, 75, 24))
        self.limparbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.nomecadastro = QLineEdit(Dialog)
        self.nomecadastro.setObjectName(u"nomecadastro")
        self.nomecadastro.setGeometry(QRect(60, 60, 281, 21))
        self.documentocadastro = QLineEdit(Dialog)
        self.documentocadastro.setObjectName(u"documentocadastro")
        self.documentocadastro.setGeometry(QRect(90, 90, 151, 21))
        self.emailcadastro = QLineEdit(Dialog)
        self.emailcadastro.setObjectName(u"emailcadastro")
        self.emailcadastro.setGeometry(QRect(60, 120, 281, 21))
        self.datadenascimentocadastro = QLineEdit(Dialog)
        self.datadenascimentocadastro.setObjectName(u"datadenascimentocadastro")
        self.datadenascimentocadastro.setGeometry(QRect(130, 150, 151, 21))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 180, 61, 21))
        self.enderecocadastro = QLineEdit(Dialog)
        self.enderecocadastro.setObjectName(u"enderecocadastro")
        self.enderecocadastro.setGeometry(QRect(70, 180, 281, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">CADASTRAR USUARIO</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">NOME:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">DOCUMENTO:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">EMAIL:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">DATA DE NASCIMETO:</span></p></body></html>", None))
        self.cadastrarbotao.setText(QCoreApplication.translate("Dialog", u"CADASTRAR", None))
        self.cancelarbotao.setText(QCoreApplication.translate("Dialog", u"CANCELAR ", None))
        self.limparbotao.setText(QCoreApplication.translate("Dialog", u"LIMPAR", None))
        self.nomecadastro.setPlaceholderText(QCoreApplication.translate("Dialog", u"nome a ser cadasrado", None))
        self.documentocadastro.setPlaceholderText(QCoreApplication.translate("Dialog", u"n\u00famero do documento", None))
        self.emailcadastro.setPlaceholderText(QCoreApplication.translate("Dialog", u"email a ser cadastrado", None))
        self.datadenascimentocadastro.setPlaceholderText(QCoreApplication.translate("Dialog", u"data de nascimento", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">ENDERE\u00c7O:</span></p></body></html>", None))
        self.enderecocadastro.setPlaceholderText(QCoreApplication.translate("Dialog", u"insira o endere\u00e7o a ser cadastrado", None))
    # retranslateUi

