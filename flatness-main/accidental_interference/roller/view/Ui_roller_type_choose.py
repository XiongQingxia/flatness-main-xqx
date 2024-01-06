# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roller_type_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rollingChooseDialog(object):
    def setupUi(self, rollingChooseDialog):
        rollingChooseDialog.setObjectName("rollingChooseDialog")
        rollingChooseDialog.resize(450, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/成功.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rollingChooseDialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(rollingChooseDialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CardWidget = CardWidget(rollingChooseDialog)
        self.CardWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CardWidget.setObjectName("CardWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.CardWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.CheckBox = CheckBox(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox.sizePolicy().hasHeightForWidth())
        self.CheckBox.setSizePolicy(sizePolicy)
        self.CheckBox.setObjectName("CheckBox")
        self.gridLayout.addWidget(self.CheckBox, 0, 0, 1, 1)
        self.CheckBox_2 = CheckBox(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_2.sizePolicy().hasHeightForWidth())
        self.CheckBox_2.setSizePolicy(sizePolicy)
        self.CheckBox_2.setObjectName("CheckBox_2")
        self.gridLayout.addWidget(self.CheckBox_2, 1, 0, 1, 1)
        self.CheckBox_3 = CheckBox(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_3.sizePolicy().hasHeightForWidth())
        self.CheckBox_3.setSizePolicy(sizePolicy)
        self.CheckBox_3.setObjectName("CheckBox_3")
        self.gridLayout.addWidget(self.CheckBox_3, 2, 0, 1, 1)
        self.CheckBox_4 = CheckBox(self.CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox_4.sizePolicy().hasHeightForWidth())
        self.CheckBox_4.setSizePolicy(sizePolicy)
        self.CheckBox_4.setObjectName("CheckBox_4")
        self.gridLayout.addWidget(self.CheckBox_4, 3, 0, 1, 1)
        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.gridLayout.addWidget(self.PrimaryPushButton, 4, 0, 1, 1)
        self.horizontalLayout.addWidget(self.CardWidget)

        self.retranslateUi(rollingChooseDialog)
        QtCore.QMetaObject.connectSlotsByName(rollingChooseDialog)

    def retranslateUi(self, rollingChooseDialog):
        _translate = QtCore.QCoreApplication.translate
        rollingChooseDialog.setWindowTitle(_translate("rollingChooseDialog", "选择具体轧辊sheet"))
        self.CheckBox.setText(_translate("rollingChooseDialog", "TCM-BUR"))
        self.CheckBox_2.setText(_translate("rollingChooseDialog", "TCM-IMR"))
        self.CheckBox_3.setText(_translate("rollingChooseDialog", "TCM 1-4架"))
        self.CheckBox_4.setText(_translate("rollingChooseDialog", "TCM-5架"))
        self.PrimaryPushButton.setText(_translate("rollingChooseDialog", "确定"))
from qfluentwidgets import CardWidget, CheckBox, PrimaryPushButton
from qtResource import resource_rc