# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CoffeeApp(object):
    def setupUi(self, CoffeeApp):
        CoffeeApp.setObjectName("CoffeeApp")
        CoffeeApp.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(parent=CoffeeApp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        CoffeeApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(CoffeeApp)
        QtCore.QMetaObject.connectSlotsByName(CoffeeApp)

    def retranslateUi(self, CoffeeApp):
        _translate = QtCore.QCoreApplication.translate
        CoffeeApp.setWindowTitle(_translate("CoffeeApp", "Кофейня"))
        self.titleLabel.setText(_translate("CoffeeApp", "Список кофе"))
