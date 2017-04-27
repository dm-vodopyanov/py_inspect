# -*- coding: utf-8 -*-

import sys

import pywinauto

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

my_array = [['AAA','BBB'],
            ['CCC','DDD'],
            ['EEE','FFF']]

my_dict = {}


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.resize(731, 600)
        self.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.setWindowTitle(QCoreApplication.translate("MainWindow", "PyInspect"))

        self.central_widget = QWidget(self)

        self.tree_view = QTreeView(self.central_widget)
        self.tree_view.setGeometry(QRect(10, 10, 351, 581))
        self.tree_view.setColumnWidth(0, 150)

        tree_model = MyTreeModel()
        self.tree_view.setModel(tree_model)

        self.table_view = QTableView(self.central_widget)
        self.table_view.setGeometry(QRect(370, 10, 351, 581))

        table_model = MyTableModel(my_array, self)
        self.table_view.setModel(table_model)


class MyTreeModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        root_node = self.invisibleRootItem()

        branch1 = QStandardItem("Branch 1")
        branch1.appendRow(QStandardItem("Child A"))
        branch1.appendRow(QStandardItem("Child B"))

        branch2 = QStandardItem("Branch 2")
        branch2.appendRow(QStandardItem("Child C"))
        branch2.appendRow(QStandardItem("Child D"))

        root_node.appendRow(branch1)
        root_node.appendRow(branch2)


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

if __name__ == "__main__":
    main()
