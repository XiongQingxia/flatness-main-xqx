# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_learn_self.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instruction(object):
    def setupUi(self, Instruction):
        Instruction.setObjectName("Instruction")
        Instruction.resize(1253, 899)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Instruction)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.LargeTitleLabel = LargeTitleLabel(Instruction)
        self.LargeTitleLabel.setWordWrap(True)
        self.LargeTitleLabel.setObjectName("LargeTitleLabel")
        self.horizontalLayout.addWidget(self.LargeTitleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Instruction)
        QtCore.QMetaObject.connectSlotsByName(Instruction)

    def retranslateUi(self, Instruction):
        _translate = QtCore.QCoreApplication.translate
        Instruction.setWindowTitle(_translate("Instruction", "Form"))
        self.LargeTitleLabel.setText(_translate("Instruction", "        此模块实现预设定表格的预设定值在线优化功能，为后台自动执行，禁止随意修改，若使用或修改此功能，请联系技术支持人员！"))
from qfluentwidgets import LargeTitleLabel