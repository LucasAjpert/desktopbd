# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atualizarUxTzeQ.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(722, 385)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-290, -150, 1331, 781))
        self.label.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 441, 41))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.pesquisartext = QLineEdit(Dialog)
        self.pesquisartext.setObjectName(u"pesquisartext")
        self.pesquisartext.setGeometry(QRect(470, 20, 241, 41))
        self.pesquisartext.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radios: 20px;\n"
"padding-left: 45px;")
        self.pesquisarbotao = QLabel(Dialog)
        self.pesquisarbotao.setObjectName(u"pesquisarbotao")
        self.pesquisarbotao.setGeometry(QRect(470, 20, 41, 31))
        self.pesquisarbotao.setStyleSheet(u"image: url(:/atualizo/icons/search.svg);\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 60%;")
        self.editarbotao = QPushButton(Dialog)
        self.editarbotao.setObjectName(u"editarbotao")
        self.editarbotao.setGeometry(QRect(610, 90, 81, 24))
        self.editarbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.limparbotao = QPushButton(Dialog)
        self.limparbotao.setObjectName(u"limparbotao")
        self.limparbotao.setGeometry(QRect(610, 140, 81, 24))
        self.limparbotao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.excluirbotao = QPushButton(Dialog)
        self.excluirbotao.setObjectName(u"excluirbotao")
        self.excluirbotao.setGeometry(QRect(620, 180, 61, 51))
        self.excluirbotao.setStyleSheet(u"image: url(:/atualizo/icons/delete.svg);\n"
"background-color: rgb(209, 209, 209);\n"
"border: none;")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 591, 171))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 270, 81, 21))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 270, 81, 21))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 310, 41, 21))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 310, 131, 21))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 350, 81, 21))
        self.nometext = QLineEdit(Dialog)
        self.nometext.setObjectName(u"nometext")
        self.nometext.setGeometry(QRect(50, 270, 261, 21))
        self.documentotext = QLineEdit(Dialog)
        self.documentotext.setObjectName(u"documentotext")
        self.documentotext.setGeometry(QRect(410, 270, 191, 21))
        self.emailtext = QLineEdit(Dialog)
        self.emailtext.setObjectName(u"emailtext")
        self.emailtext.setGeometry(QRect(50, 310, 261, 21))
        self.datadenascimentotext = QLineEdit(Dialog)
        self.datadenascimentotext.setObjectName(u"datadenascimentotext")
        self.datadenascimentotext.setGeometry(QRect(450, 310, 191, 21))
        self.enderecotext = QLineEdit(Dialog)
        self.enderecotext.setObjectName(u"enderecotext")
        self.enderecotext.setGeometry(QRect(70, 350, 261, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">ALTERAR DADOS DOS USUARIOS</span></p></body></html>", None))
        self.pesquisartext.setPlaceholderText(QCoreApplication.translate("Dialog", u"nome ou documento", None))
        self.pesquisarbotao.setText("")
        self.editarbotao.setText(QCoreApplication.translate("Dialog", u"EDITAR", None))
        self.limparbotao.setText(QCoreApplication.translate("Dialog", u"LIMPAR", None))
        self.excluirbotao.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"documento", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"endere\u00e7o", None));
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">NOME:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">DOCUMENTO:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">EMAIL:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">DATA DE NASCIMENTO:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700;\">ENDERE\u00c7O:</span></p></body></html>", None))
    # retranslateUi

