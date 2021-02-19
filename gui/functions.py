from gui import QTableWidget, QHeaderView, QTableWidgetItem, Qt, QFont


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
