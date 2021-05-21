# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time_con.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import datetime
import time
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(801, 327)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(50, 48, 45, 15))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 40, 50, 28))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 55, 15))
        self.label_2.setObjectName("label_2")

        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 81, 50, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.time_format_btn)

        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(550, 90, 72, 15))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(50, 140, 72, 15))
        self.label_4.setObjectName("label_4")

        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 131, 50, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.format_time_btn)

        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(100, 48, 100, 15))
        self.label_5.setText(f"{int(time.time())}")
        self.label_5.setObjectName("label_5")

        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 80, 171, 30))
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setText("11111111")

        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 80, 171, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 130, 171, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 171, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "现在："))
        self.pushButton.setText(_translate("Frame", "停止"))
        self.label_2.setText(_translate("Frame", "时间戳："))
        self.pushButton_2.setText(_translate("Frame", "转换"))
        self.label_3.setText(_translate("Frame", "北京时间"))
        self.label_4.setText(_translate("Frame", "北京时间："))
        self.pushButton_3.setText(_translate("Frame", "转换"))

    def is_number(self, number):
        try:
            int(number)
            return True
        except Exception as e:
            print(f"格式不对，{e}")
            return False

    def time_format_btn(self):
        """
        时间戳转时间
        %Y-%m-%d %H:%M:%S
        :return:
        """
        try:
            timestamp = self.lineEdit.text()
            # print(type(timestamp), timestamp)
            is_num = self.is_number(timestamp)
            if is_num:
                ctime = datetime.datetime.fromtimestamp(int(timestamp))
                self.lineEdit_2.setText(f"{ctime}")
            else:
                pass
                # QMessageBox.warning(Ui_Frame, "消息框标题", "这是一条警告。", QMessageBox.Yes)
        except Exception as e:
            print(f"出错：{e}")

    def format_time_btn(self):
        """
        字符类型(%Y-%m-%d %H:%M:%S)的时间转换时间数组，时间戳
        :return:
        """
        try:

            time_str = self.lineEdit_4.text()
            results = self.pat_find_num(time_str)
            # print(time_str)
            # print(results)
            time_str = f"{results[0]}-{results[1]}-{results[2]} {results[3]}:{results[4]}:{results[5]}"
            # print(time_str)
            # 转为时间数组
            timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            # # print(f"时间数组{timeArray}")
            # # timeArray可以调用tm_year等
            # print(timeArray.tm_year)
            # # 转为时间戳
            timeStamp = int(time.mktime(timeArray))
            # # print(f"时间戳{timeStamp}")
            self.lineEdit_3.setText(f"{timeStamp}")
        except Exception as e:
            print(f"出错：{e}")

    def pat_find_num(self, time_str):
        """
        提取字符串中的数字
        :return:
        """
        pattern = re.compile("\d+")
        results = pattern.findall(time_str)
        # print(results)
        if len(results) < 6:
            for i in range((6 - len(results))):
                results.append("00")
        # print(results)
        return results


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Frame()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
