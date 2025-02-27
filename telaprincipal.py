# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaprincipalKWPtgo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolBar, QWidget)
import atualizar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 457)
        self.actionadd = QAction(MainWindow)
        self.actionadd.setObjectName(u"actionadd")
        icon = QIcon()
        icon.addFile(u":/iconprincipal/icons/personal.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionadd.setIcon(icon)
        self.actioneditar = QAction(MainWindow)
        self.actioneditar.setObjectName(u"actioneditar")
        icon1 = QIcon()
        icon1.addFile(u":/iconprincipal/icons/pen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actioneditar.setIcon(icon1)
        self.actionpesquisar = QAction(MainWindow)
        self.actionpesquisar.setObjectName(u"actionpesquisar")
        icon2 = QIcon()
        icon2.addFile(u":/iconprincipal/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionpesquisar.setIcon(icon2)
        self.actionatualizar = QAction(MainWindow)
        self.actionatualizar.setObjectName(u"actionatualizar")
        icon3 = QIcon()
        icon3.addFile(u":/iconprincipal/icons/forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionatualizar.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-190, -160, 931, 701))
        self.label.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 35, 651, 51))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding-left: 10px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 40, 91, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.logado = QLabel(self.centralwidget)
        self.logado.setObjectName(u"logado")
        self.logado.setGeometry(QRect(560, 40, 111, 16))
        self.tableWidgeusuarios = QTableWidget(self.centralwidget)
        if (self.tableWidgeusuarios.columnCount() < 6):
            self.tableWidgeusuarios.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgeusuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidgeusuarios.setObjectName(u"tableWidgeusuarios")
        self.tableWidgeusuarios.setGeometry(QRect(20, 90, 651, 261))
        self.tableWidgeusuarios.setStyleSheet(u"border-radius: 8px;")
        self.botaorelatorio = QLabel(self.centralwidget)
        self.botaorelatorio.setObjectName(u"botaorelatorio")
        self.botaorelatorio.setGeometry(QRect(630, 0, 51, 31))
        self.botaorelatorio.setStyleSheet(u"image : url(:/iconprincipal/icons/document.svg);\n"
"border:none;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 703, 33))
        self.menuarquivos = QMenu(self.menubar)
        self.menuarquivos.setObjectName(u"menuarquivos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuarquivos.menuAction())
        self.menuarquivos.addAction(self.actionadd)
        self.menuarquivos.addAction(self.actioneditar)
        self.menuarquivos.addAction(self.actionpesquisar)
        self.menuarquivos.addAction(self.actionatualizar)
        self.toolBar.addAction(self.actionadd)
        self.toolBar.addAction(self.actioneditar)
        self.toolBar.addAction(self.actionpesquisar)
        self.toolBar.addAction(self.actionatualizar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionadd.setText(QCoreApplication.translate("MainWindow", u"add", None))
#if QT_CONFIG(tooltip)
        self.actionadd.setToolTip(QCoreApplication.translate("MainWindow", u"cadastrar pessoas", None))
#endif // QT_CONFIG(tooltip)
        self.actioneditar.setText(QCoreApplication.translate("MainWindow", u"editar", None))
#if QT_CONFIG(tooltip)
        self.actioneditar.setToolTip(QCoreApplication.translate("MainWindow", u"editar cadastro", None))
#endif // QT_CONFIG(tooltip)
        self.actionpesquisar.setText(QCoreApplication.translate("MainWindow", u"pesquisar", None))
#if QT_CONFIG(tooltip)
        self.actionpesquisar.setToolTip(QCoreApplication.translate("MainWindow", u"pesquisar cadastro", None))
#endif // QT_CONFIG(tooltip)
        self.actionatualizar.setText(QCoreApplication.translate("MainWindow", u"atualizar", None))
#if QT_CONFIG(tooltip)
        self.actionatualizar.setToolTip(QCoreApplication.translate("MainWindow", u"atualizar sistema", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionatualizar.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">USUARIOS CADASTRADOS RECENTEMENTE</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario logado:", None))
        self.logado.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem = self.tableWidgeusuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidgeusuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nome", None));
        ___qtablewidgetitem2 = self.tableWidgeusuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"documento", None));
        ___qtablewidgetitem3 = self.tableWidgeusuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"email", None));
        ___qtablewidgetitem4 = self.tableWidgeusuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"data de nascimento", None));
        ___qtablewidgetitem5 = self.tableWidgeusuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"endere\u00e7o", None));
        self.botaorelatorio.setText("")
        self.menuarquivos.setTitle(QCoreApplication.translate("MainWindow", u"arquivos", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

