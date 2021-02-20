from gui import QTableWidget, QHeaderView, QTableWidgetItem, Qt, QFont
from reference import FONT_SIZE


def new_table(row, col, parent, headers: list):
    table = QTableWidget(row, col, parent)
    table.setStyleSheet("background-color:#FAEBD7")
    table.setHorizontalHeaderLabels(headers)
    table.verticalHeader().hide()
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.horizontalHeader().setStyleSheet(f"font:{FONT_SIZE}pt '宋体';color: black")

    return table


def item(content, disable=False):
    i = QTableWidgetItem(content)

    i.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    i.setFont(QFont('Times', FONT_SIZE))

    if disable:
        i.setFlags(Qt.ItemIsEditable)

    return i
