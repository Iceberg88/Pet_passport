# Form implementation generated from reading ui file 'ui/ectoparasites_design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_ectoparasites_table_window(object):
    def setupUi(self, ectoparasites_table_window):
        ectoparasites_table_window.setObjectName("ectoparasites_table_window")
        ectoparasites_table_window.resize(552, 420)
        self.pushButton_add = QtWidgets.QPushButton(parent=ectoparasites_table_window)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 380, 75, 24))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_exit = QtWidgets.QPushButton(parent=ectoparasites_table_window)
        self.pushButton_exit.setGeometry(QtCore.QRect(110, 380, 75, 24))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.name_table = QtWidgets.QLabel(parent=ectoparasites_table_window)
        self.name_table.setGeometry(QtCore.QRect(110, 10, 201, 16))
        self.name_table.setObjectName("name_table")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=ectoparasites_table_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 531, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_ectoparasites = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.tableWidget_ectoparasites.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget_ectoparasites.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget_ectoparasites.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget_ectoparasites.setObjectName("tableWidget_ectoparasites")
        self.tableWidget_ectoparasites.setColumnCount(5)
        self.tableWidget_ectoparasites.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ectoparasites.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ectoparasites.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ectoparasites.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ectoparasites.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ectoparasites.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget_ectoparasites)
        self.pushButton_delete = QtWidgets.QPushButton(parent=ectoparasites_table_window)
        self.pushButton_delete.setGeometry(QtCore.QRect(200, 380, 75, 24))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.error_label = QtWidgets.QLabel(parent=ectoparasites_table_window)
        self.error_label.setGeometry(QtCore.QRect(10, 350, 441, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(ectoparasites_table_window)
        QtCore.QMetaObject.connectSlotsByName(ectoparasites_table_window)

    def retranslateUi(self, ectoparasites_table_window):
        _translate = QtCore.QCoreApplication.translate
        ectoparasites_table_window.setWindowTitle(_translate("ectoparasites_table_window", "Form"))
        self.pushButton_add.setText(_translate("ectoparasites_table_window", "добавить +"))
        self.pushButton_exit.setText(_translate("ectoparasites_table_window", "Выйти"))
        self.name_table.setText(_translate("ectoparasites_table_window", "Вакцинация против эктопаразитов"))
        self.tableWidget_ectoparasites.setSortingEnabled(True)
        item = self.tableWidget_ectoparasites.horizontalHeaderItem(0)
        item.setText(_translate("ectoparasites_table_window", "Препарат"))
        item = self.tableWidget_ectoparasites.horizontalHeaderItem(1)
        item.setText(_translate("ectoparasites_table_window", "Дата вакцинации"))
        item = self.tableWidget_ectoparasites.horizontalHeaderItem(2)
        item.setText(_translate("ectoparasites_table_window", "Действительно до"))
        item = self.tableWidget_ectoparasites.horizontalHeaderItem(3)
        item.setText(_translate("ectoparasites_table_window", "Вет.врач (клиника)"))
        item = self.tableWidget_ectoparasites.horizontalHeaderItem(4)
        item.setText(_translate("ectoparasites_table_window", "id"))
        self.pushButton_delete.setText(_translate("ectoparasites_table_window", "удалить -"))
