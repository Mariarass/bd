# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogflight.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Flight(object):
    def setupUi(self, Dialog_Flight):
        Dialog_Flight.setObjectName("Dialog_Flight")
        Dialog_Flight.resize(895, 111)
        self.frame = QtWidgets.QFrame(Dialog_Flight)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 111))
        self.frame.setStyleSheet("background-color:rgb(219, 219, 195);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.tableWidget_4.setStyleSheet("QTableWidget {\n"
"\n"
"background-color:rgb(219, 219, 195);\n"
"\n"
"\n"
"border:none;\n"
"backcground:red;\n"
" selection-background-color:rgb(137,137,121);}\n"
"\n"
"\n"
"QHeaderView:section{\n"
"font:8pt \"Trebuchet MS\";\n"
"color:rgb(39,39,45);\n"
"border: none;\n"
"\n"
"background-color: #c68383;\n"
"}\n"
"QScrollBar:horizontal {\n"
"border: none;\n"
"background: rgb(76, 76, 81);\n"
"height: 14px;\n"
"margin: 0px 21px 0 21px;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"background: rgb(137, 137, 121);\n"
"min-width: 25px;\n"
"border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"border: none;\n"
"background: rgb(76, 76,81);\n"
"width: 20px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"border: none;\n"
"background: rgb(76, 76,81);\n"
"width: 20px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: rgb(76, 76, 81);\n"
"width: 14px;\n"
"margin: 21px 0 21px 0;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: rgb(137, 137, 121);\n"
"min-height: 25px;\n"
"border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 20px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 20px;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"QHeaderView{\n"
"background-color:rgb(219, 219, 195);;\n"
"}\n"
"")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(8)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(830, 50, 42, 22))
        self.spinBox.setStyleSheet("QSpinBox {\n"
"color:white;\n"
"background-color: rgb(137, 137, 121);\n"
" border:none;\n"
"\n"
"}\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(820, 10, 71, 16))
        self.label.setStyleSheet("color:rgb(76,76,81);\n"
"font:8pt \"Trebuchet MS\";")
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Flight)
        self.buttonBox.setGeometry(QtCore.QRect(160, 70, 341, 32))
        self.buttonBox.setStyleSheet("QPushButton{color:white;\n"
"    color: #dfdac2;\n"
"background-color: rgb(137, 137, 121);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"background-color:#5a606b;}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog_Flight)
        self.buttonBox.accepted.connect(Dialog_Flight.accept)
        self.buttonBox.rejected.connect(Dialog_Flight.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Flight)

    def retranslateUi(self, Dialog_Flight):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Flight.setWindowTitle(_translate("Dialog_Flight", "Добавить/Изменить"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Flight", "НомерРейса"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Flight", "КодМаршрута"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Flight", "НомерВодителя"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Flight", "КодМашины"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Flight", "ВремяОтправления"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Flight", "ВремяПрибытия"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Flight", "Дата"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_Flight", "ЦенаБилета"))
        self.label.setText(_translate("Dialog_Flight", "Номер записи"))