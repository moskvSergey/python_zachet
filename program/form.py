from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(20, 555, 281, 41))
        self.add_button.setObjectName("add_button")
        self.product_name = QtWidgets.QLineEdit(self.centralwidget)
        self.product_name.setGeometry(QtCore.QRect(20, 515, 181, 31))
        self.product_name.setObjectName("product_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 475, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(400, 555, 181, 41))
        self.delete_btn.setObjectName("delete_btn")
        self.product_list = QtWidgets.QTableWidget(self.centralwidget)
        self.product_list.setGeometry(QtCore.QRect(10, 0, 1161, 401))
        self.product_list.setObjectName("product_list")
        self.product_list.setColumnCount(0)
        self.product_list.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.delete_btn.setText(_translate("MainWindow", "Удалить"))
