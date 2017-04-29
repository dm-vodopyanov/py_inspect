# -*- coding: utf-8 -*-

import sys

from pywinauto import uia_element_info

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

my_array = [['AAA', 'BBB'],
            ['CCC', 'DDD'],
            ['EEE', 'FFF']]


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

        self.element_info = uia_element_info.UIAElementInfo()

        tree_model = MyTreeModel(self.element_info)
        self.tree_view.setModel(tree_model)

        self.table_view = QTableView(self.central_widget)
        self.table_view.setGeometry(QRect(370, 10, 351, 581))

        table_model = MyTableModel(my_array, self.element_info, self)
        self.table_view.setModel(table_model)


class MyTreeModel(QStandardItemModel):
    def __init__(self, element_info):
        QStandardItemModel.__init__(self)
        root_node = self.invisibleRootItem()

        self.branch = QStandardItem(self.__node_name(element_info))
        self.branch.setEditable(False)
        root_node.appendRow(self.branch)
        self.__get_next(element_info, self.branch)

    def __get_next(self, element_info, parent):
        for child in element_info.children():
            child_item = QStandardItem(self.__node_name(child))
            child_item.setEditable(False)
            parent.appendRow(child_item)
            self.__get_next(child, child_item)

    def __node_name(self, element_info):
        return '%s_%s' % (str(element_info.name), str(element_info.handle))


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, element_info, parent=None, *args):
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
