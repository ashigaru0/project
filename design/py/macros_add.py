# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'macros_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Добавть макрос")
        Form.resize(352, 128)
        self.comb_btn = QtWidgets.QPushButton(Form)
        self.comb_btn.setGeometry(QtCore.QRect(180, 10, 161, 31))
        self.comb_btn.setObjectName("comb_btn")
        self.name_btn = QtWidgets.QPushButton(Form)
        self.name_btn.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.name_btn.setObjectName("name_btn")
        self.url_btn = QtWidgets.QPushButton(Form)
        self.url_btn.setGeometry(QtCore.QRect(10, 50, 331, 31))
        self.url_btn.setObjectName("url_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout.addWidget(self.reset_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.done_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.done_btn.setObjectName("done_btn")
        self.horizontalLayout.addWidget(self.done_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comb_btn.setText(_translate("Form", "Указать комбинацию клавишь"))
        self.name_btn.setText(_translate("Form", "Указать название макроса"))
        self.url_btn.setText(_translate("Form", "Указать ссылку на файл"))
        self.reset_btn.setText(_translate("Form", "Сброс"))
        self.done_btn.setText(_translate("Form", "Готово"))
        self.cancel_btn.setText(_translate("Form", "Отмена"))
