# -*- coding: utf-8 -*-

import sys
import pywinauto
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setup(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(731, 600)
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 351, 581))
        self.treeView.setObjectName("treeView")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(370, 10, 351, 581))
        self.tableView.setObjectName("tableView")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate(self, main_window):
        translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(translate("MainWindow", "PyInspect"))

    def make_tree(self):
        model = QtGui.QStandardItemModel()
        root_node = model.invisibleRootItem()

        branch1 = QtGui.QStandardItem("Branch 1")
        branch1.appendRow(QtGui.QStandardItem("Child A"))
        branch1.appendRow(QtGui.QStandardItem("Child B"))

        branch2 = QtGui.QStandardItem("Branch 2")
        branch2.appendRow(QtGui.QStandardItem("Child C"))
        branch2.appendRow(QtGui.QStandardItem("Child D"))

        root_node.appendRow(branch1)
        root_node.appendRow(branch2)

        self.treeView.setModel(model)
        self.treeView.setColumnWidth(0, 150)

    def make_table(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Window()
    ui.setup(window)
    ui.make_tree()
    ui.make_table()
    window.show()
    sys.exit(app.exec_())

