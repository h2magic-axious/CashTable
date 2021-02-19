import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QTableWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidgetItem,
    QHeaderView
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from reference import WINDOW_WIDTH, WINDOW_HEIGHT
from models import Assets, Debt, Income, Expenses, session


def new_table(row, col, parent, headers: list):
    table = QTableWidget(row, col, parent)
    table.setStyleSheet("background-color:#FAEBD7")
    table.setHorizontalHeaderLabels(headers)
    table.verticalHeader().hide()
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.horizontalHeader().setStyleSheet("font:15pt '宋体';color: black")

    return table


def item(content, disable=False):
    i = QTableWidgetItem(content)
    i.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    i.setFont(QFont('Times', 15))
    if disable:
        i.setFlags(Qt.ItemIsEditable)

    return i


class TabAssets(QWidget):
    def __init__(self):
        super(TabAssets, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 4, self, ['ID', '项目', '金额', '类别'])

        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item('0.0', True))
        self.table.setItem(0, 3, item('', True))

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)


class TabDebt(QWidget):
    def __init__(self):
        super(TabDebt, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 3, self, ['ID', '项目', '金额'])
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item('0.0', True))

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)


class TabIncome(QWidget):
    def __init__(self):
        super(TabIncome, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 3, self, ['ID', '项目', '金额'])
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item('0.0', True))

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)


class TabExpenses(QWidget):
    def __init__(self):
        super(TabExpenses, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 3, self, ['ID', '项目', '金额'])
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item('0.0', True))

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.root_layout = QHBoxLayout()

        self.tab_widget = QTabWidget(self)
        self.init_tab_widget(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.root_layout.addWidget(self.tab_widget)
        self.setLayout(self.root_layout)

        self.init_ui()

    def init_tab_widget(self, width, height):
        self.tab_widget.setTabShape(QTabWidget.Triangular)

        self.tab_widget.setMinimumHeight(height)
        self.tab_widget.setMaximumHeight(height)

        self.tab_widget.setMinimumWidth(width)
        self.tab_widget.setMaximumWidth(width)

        style = "QTabBar::tab{width:$1px;height:25px;background-color:#66CDAA;font:15pt '宋体';color: black}"
        self.tab_widget.setStyleSheet(style.replace('$1', str(width / 5)))

    def init_ui(self):
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle('资产负债表')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.tab_widget.addTab(QWidget(), 'Dashboard')
        self.tab_widget.addTab(TabAssets(), 'Assets')
        self.tab_widget.addTab(TabDebt(), 'Debt')
        self.tab_widget.addTab(TabIncome(), 'Income')
        self.tab_widget.addTab(TabExpenses(), 'Expenses')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()

    sys.exit(app.exec_())
