# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dmitry\Desktop\PyInspect.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 600)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 351, 581))
        self.treeView.setObjectName("treeView")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(370, 10, 351, 581))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyInspect"))

    def make_tree(self):
        model = QtGui.QStandardItemModel()
        rootNode = model.invisibleRootItem()
        branch1 = QtGui.QStandardItem("Branch 1")
        branch1.appendRow([QtGui.QStandardItem("Child A"), None])
        childnode = QtGui.QStandardItem("Child B")
        branch1.appendRow([childnode, None])

        branch2 = QtGui.QStandardItem("Branch 2")
        branch2.appendRow([QtGui.QStandardItem("Child C"), None])
        branch2.appendRow([QtGui.QStandardItem("Child D"), None])

        rootNode.appendRow([branch1, None])
        rootNode.appendRow([branch2, None])

        self.treeView.setModel(model)
        self.treeView.setColumnWidth(0, 150)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.make_tree()
    MainWindow.show()
    sys.exit(app.exec_())

