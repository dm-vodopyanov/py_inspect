import sys

from pywinauto import uia_element_info

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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

        self.tree_model = MyTreeModel(self.element_info)
        self.tree_model.setHeaderData(0, Qt.Horizontal, 'Controls')
        self.tree_view.setModel(self.tree_model)

        self.table_view = QTableView(self.central_widget)
        self.table_view.setGeometry(QRect(370, 10, 351, 581))

        self.tree_view.clicked.connect(self.__show_property)

    def __show_property(self, index=None):
        data = index.data()
        self.table_model = MyTableModel(self.tree_model.props_dict.get(data), self.element_info, self)
        self.table_view.setModel(self.table_model)


class MyTreeModel(QStandardItemModel):
    def __init__(self, element_info):
        QStandardItemModel.__init__(self)
        root_node = self.invisibleRootItem()
        self.props_dict = {}
        self.branch = QStandardItem(self.__node_name(element_info))
        self.branch.setEditable(False)
        root_node.appendRow(self.branch)
        self.__generate_props_dict(element_info)
        self.__get_next(element_info, self.branch)

    def __get_next(self, element_info, parent):
        for child in element_info.children():
            self.__generate_props_dict(child)
            child_item = QStandardItem(self.__node_name(child))
            child_item.setEditable(False)
            parent.appendRow(child_item)
            self.__get_next(child, child_item)

    @staticmethod
    def __node_name(element_info):
        return '%s_%s' % (str(element_info.name), id(element_info))

    def __generate_props_dict(self, element_info):
        node_dict = {self.__node_name(element_info): [
                                                        ['control_id', str(element_info.control_id)],
                                                        ['class_name', str(element_info.class_name)],
                                                        ['control_type', str(element_info.control_type)],
                                                        ['element', str(element_info.element)],
                                                        ['enabled', str(element_info.enabled)],
                                                        ['framework_id', str(element_info.framework_id)],
                                                        ['handle', str(element_info.handle)],
                                                        ['name', str(element_info.name)],
                                                        ['process_id', str(element_info.process_id)],
                                                        ['rectangle', str(element_info.rectangle)],
                                                        ['rich_text', str(element_info.rich_text)],
                                                        ['parent', str(element_info.parent)],
                                                        ['runtime_id', str(element_info.runtime_id)],
                                                        ['visible', str(element_info.visible)],
                                                     ]}
        self.props_dict.update(node_dict)


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, element_info, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.header_labels = ['Property', 'Value']

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

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)


if __name__ == "__main__":
    main()
