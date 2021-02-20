from gui import QTableWidget, QHeaderView, QTableWidgetItem, Qt, QFont, QComboBox
from reference import FONT_SIZE, AssetsMap


def new_table(row, col, parent, headers: list):
    table = QTableWidget(row, col, parent)
    table.setStyleSheet("background-color:#FAEBD7")
    table.setHorizontalHeaderLabels(headers)
    table.verticalHeader().hide()
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.horizontalHeader().setStyleSheet(f"font:{FONT_SIZE}pt '宋体';color: black")

    return table


def new_item(content, disable=False):
    i = QTableWidgetItem(content)

    i.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
    i.setFont(QFont('Times', FONT_SIZE))

    if disable:
        i.setFlags(Qt.ItemIsEditable)

    return i


def new_combo_box(parent):
    temp_combox_box = QComboBox(parent)
    for key, value in AssetsMap.items():
        temp_combox_box.addItem(str(key))
        temp_combox_box.setItemText(key, value)

    temp_combox_box.setStyleSheet(
        'QComboBox{font-family:"宋体";font-size:$1px;color:green}'.replace('$1', str(FONT_SIZE)))

    return temp_combox_box


def get_item_content(table: QTableWidget, row, col):
    item = table.item(row, col)
    if item:
        return item.text()
    else:
        return None


def get_combo_content(table: QTableWidget, row, col):
    widget = table.cellWidget(row, col)
    if widget:
        return widget.currentIndex()
    else:
        return 0
