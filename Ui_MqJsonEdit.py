# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\MqJsonEdit\MqJsonEdit.ui'
#
# Created: Tue Mar 07 18:35:00 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MqJsonEdit(object):
    def setupUi(self, MqJsonEdit):
        MqJsonEdit.setObjectName(_fromUtf8("MqJsonEdit"))
        MqJsonEdit.resize(490, 415)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("MJE.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("MJE.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MqJsonEdit.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MqJsonEdit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit_logShow = QtGui.QTextEdit(self.frame_2)
        self.textEdit_logShow.setObjectName(_fromUtf8("textEdit_logShow"))
        self.verticalLayout_2.addWidget(self.textEdit_logShow)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_filePath = QtGui.QLineEdit(self.frame)
        self.lineEdit_filePath.setMinimumSize(QtCore.QSize(251, 20))
        self.lineEdit_filePath.setObjectName(_fromUtf8("lineEdit_filePath"))
        self.gridLayout.addWidget(self.lineEdit_filePath, 0, 2, 1, 1)
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)
        self.lineEdit_modelVhost = QtGui.QLineEdit(self.frame)
        self.lineEdit_modelVhost.setMaximumSize(QtCore.QSize(101, 20))
        self.lineEdit_modelVhost.setObjectName(_fromUtf8("lineEdit_modelVhost"))
        self.gridLayout.addWidget(self.lineEdit_modelVhost, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_newVhost = QtGui.QLineEdit(self.frame)
        self.lineEdit_newVhost.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_newVhost.setObjectName(_fromUtf8("lineEdit_newVhost"))
        self.gridLayout.addWidget(self.lineEdit_newVhost, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        MqJsonEdit.setCentralWidget(self.centralwidget)

        self.retranslateUi(MqJsonEdit)
        QtCore.QMetaObject.connectSlotsByName(MqJsonEdit)

    def retranslateUi(self, MqJsonEdit):
        MqJsonEdit.setWindowTitle(_translate("MqJsonEdit", "MqJsonEdit", None))
        self.label.setText(_translate("MqJsonEdit", "文件目录：", None))
        self.toolButton.setText(_translate("MqJsonEdit", "...", None))
        self.lineEdit_modelVhost.setText(_translate("MqJsonEdit", "wms_test", None))
        self.label_2.setText(_translate("MqJsonEdit", "模板Vhost：", None))
        self.label_3.setText(_translate("MqJsonEdit", "新建Vhost：", None))
        self.pushButton.setText(_translate("MqJsonEdit", "生成", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MqJsonEdit = QtGui.QMainWindow()
    ui = Ui_MqJsonEdit()
    ui.setupUi(MqJsonEdit)
    MqJsonEdit.show()
    sys.exit(app.exec_())

