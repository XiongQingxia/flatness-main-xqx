# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_strategy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SinglePolicyCompare")
        MainWindow.resize(1428, 1182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_xuanzeshuju = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_xuanzeshuju.setObjectName("pushButton_xuanzeshuju")
        self.horizontalLayout.addWidget(self.pushButton_xuanzeshuju)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.pushButton_shunxu = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_shunxu.setObjectName("pushButton_shunxu")
        self.verticalLayout.addWidget(self.pushButton_shunxu)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_bili = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_bili.setObjectName("pushButton_bili")
        self.gridLayout.addWidget(self.pushButton_bili, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_wrbbili = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_wrbbili.setObjectName("lineEdit_wrbbili")
        self.gridLayout.addWidget(self.lineEdit_wrbbili, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_irbbili = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_irbbili.setObjectName("lineEdit_irbbili")
        self.gridLayout.addWidget(self.lineEdit_irbbili, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_irsbili = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_irsbili.setObjectName("lineEdit_irsbili")
        self.gridLayout.addWidget(self.lineEdit_irsbili, 3, 1, 1, 1)
        self.pushButton_bilijisuan = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_bilijisuan.setObjectName("pushButton_bilijisuan")
        self.gridLayout.addWidget(self.pushButton_bilijisuan, 4, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_adam_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_adam_2.setObjectName("lineEdit_adam_2")
        self.gridLayout_3.addWidget(self.lineEdit_adam_2, 3, 2, 1, 1)
        self.lineEdit_adam_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_adam_1.setObjectName("lineEdit_adam_1")
        self.gridLayout_3.addWidget(self.lineEdit_adam_1, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 2)
        self.lineEdit_adam_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_adam_3.setObjectName("lineEdit_adam_3")
        self.gridLayout_3.addWidget(self.lineEdit_adam_3, 4, 2, 1, 1)
        self.pushButton_Adam = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Adam.setObjectName("pushButton_Adam")
        self.gridLayout_3.addWidget(self.pushButton_Adam, 1, 0, 1, 3)
        self.pushButton_Adamjisuan = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Adamjisuan.setObjectName("pushButton_Adamjisuan")
        self.gridLayout_3.addWidget(self.pushButton_Adamjisuan, 5, 0, 1, 3)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 4, 3, 1, 2)
        self.lineEdit_danzhen_2 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_danzhen_2.setObjectName("lineEdit_danzhen_2")
        self.gridLayout_4.addWidget(self.lineEdit_danzhen_2, 4, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 3, 4, 1, 1)
        self.lineEdit_danzhen_1 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_danzhen_1.setObjectName("lineEdit_danzhen_1")
        self.gridLayout_4.addWidget(self.lineEdit_danzhen_1, 3, 2, 1, 2)
        self.pushButton_xianshituxiang = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_xianshituxiang.setObjectName("pushButton_xianshituxiang")
        self.gridLayout_4.addWidget(self.pushButton_xianshituxiang, 2, 0, 1, 5)
        self.pushButton_xianshituxiang_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_xianshituxiang_2.setObjectName("pushButton_xianshituxiang_2")
        self.gridLayout_4.addWidget(self.pushButton_xianshituxiang_2, 5, 0, 1, 5)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 2)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.graphicsView_tuxing_3 = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView_tuxing_3.setObjectName("graphicsView_tuxing_3")
        self.gridLayout_11.addWidget(self.graphicsView_tuxing_3, 0, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_qingkonghuabu_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_qingkonghuabu_3.setObjectName("pushButton_qingkonghuabu_3")
        self.horizontalLayout_8.addWidget(self.pushButton_qingkonghuabu_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.setStretch(0, 6)
        self.verticalLayout_8.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 1, 0, 1, 2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphicsView_tuxing_2 = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView_tuxing_2.setObjectName("graphicsView_tuxing_2")
        self.gridLayout_10.addWidget(self.graphicsView_tuxing_2, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_qingkonghuabu_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_qingkonghuabu_2.setObjectName("pushButton_qingkonghuabu_2")
        self.horizontalLayout_7.addWidget(self.pushButton_qingkonghuabu_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.setStretch(0, 6)
        self.verticalLayout_7.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphicsView_tuxing = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView_tuxing.setObjectName("graphicsView_tuxing")
        self.gridLayout_9.addWidget(self.graphicsView_tuxing, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_qingkonghuabu = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_qingkonghuabu.setObjectName("pushButton_qingkonghuabu")
        self.horizontalLayout_6.addWidget(self.pushButton_qingkonghuabu)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.setStretch(0, 6)
        self.verticalLayout_6.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 5)
        self.gridLayout_5.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 9)
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 9)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SinglePolicyCompare", "single_strategy"))
        self.pushButton_xuanzeshuju.setText(_translate("SinglePolicyCompare", "选择数据"))
        self.groupBox_4.setTitle(_translate("SinglePolicyCompare", "板形控制策略"))
        self.groupBox.setTitle(_translate("SinglePolicyCompare", "顺序控制策略"))
        self.radioButton.setText(_translate("SinglePolicyCompare", "固定优先序列"))
        self.radioButton_2.setText(_translate("SinglePolicyCompare", "动态优先序列"))
        self.pushButton_shunxu.setText(_translate("SinglePolicyCompare", "模型计算"))
        self.groupBox_2.setTitle(_translate("SinglePolicyCompare", "比例控制策略"))
        self.pushButton_bili.setText(_translate("SinglePolicyCompare", "初始化比例系数"))
        self.label.setText(_translate("SinglePolicyCompare", "工作辊弯辊比例："))
        self.label_2.setText(_translate("SinglePolicyCompare", "中间辊弯辊比例："))
        self.label_3.setText(_translate("SinglePolicyCompare", "中间辊窜辊比例："))
        self.pushButton_bilijisuan.setText(_translate("SinglePolicyCompare", "模型计算"))
        self.groupBox_3.setTitle(_translate("SinglePolicyCompare", "优化控制策略"))
        self.label_4.setText(_translate("SinglePolicyCompare", "学习率："))
        self.label_6.setText(_translate("SinglePolicyCompare", "二阶矩估计指数衰减率："))
        self.label_5.setText(_translate("SinglePolicyCompare", "一阶矩估计指数衰减率："))
        self.pushButton_Adam.setText(_translate("SinglePolicyCompare", "初始化Adam参数"))
        self.pushButton_Adamjisuan.setText(_translate("SinglePolicyCompare", "模型计算"))
        self.groupBox_7.setTitle(_translate("SinglePolicyCompare", "显示选择"))
        self.label_8.setText(_translate("SinglePolicyCompare", "帧图像"))
        self.label_7.setText(_translate("SinglePolicyCompare", "选择第"))
        self.label_9.setText(_translate("SinglePolicyCompare", "该卷带钢共"))
        self.label_10.setText(_translate("SinglePolicyCompare", "帧"))
        self.pushButton_xianshituxiang.setText(_translate("SinglePolicyCompare", "显示图像"))
        self.pushButton_xianshituxiang_2.setText(_translate("SinglePolicyCompare", "显示该帧图像"))
        self.groupBox_5.setTitle(_translate("SinglePolicyCompare", "图形展示模块"))
        self.pushButton_qingkonghuabu_3.setText(_translate("SinglePolicyCompare", "清空画布"))
        self.pushButton_qingkonghuabu_2.setText(_translate("SinglePolicyCompare", "清空画布"))
        self.pushButton_qingkonghuabu.setText(_translate("SinglePolicyCompare", "清空画布"))