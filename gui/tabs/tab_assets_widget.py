from sqlalchemy import func, distinct

from gui import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QComboBox, QPushButton
from gui.functions import new_table, item
from models import session, Assets, sum_assets
from reference import ROW_SET, AssetsMap, AssetsCategory


class TabAssets(QWidget):
    def __init__(self):
        super(TabAssets, self).__init__()
        n_row = session.query(func.count(distinct(Assets.id))).scalar() // ROW_SET + 1
        self.table = new_table(n_row * ROW_SET, 4, self, ['ID', '项目', '金额', '类别'])

        root_layout = QHBoxLayout()

        table_layout = QVBoxLayout()
        panel_layout = self.init_panel()

        self.init_table(sum_assets())
        self.display(session.query(Assets).all())

        table_layout.addWidget(self.table)

        root_layout.addLayout(table_layout)
        root_layout.addLayout(panel_layout)

        self.setLayout(root_layout)

    def init_table(self, s):
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item(str(s), True))
        self.table.setItem(0, 3, item('', True))

    def display(self, items):
        row = 1
        for i in items:
            self.table.setItem(row, 0, item(str(i.id), True))
            self.table.setItem(row, 1, item(i.project))
            self.table.setItem(row, 2, item(str(i.balance)))
            self.table.setItem(row, 3, item(AssetsMap[i.category]))
            row += 1

    def init_panel(self):
        layout = QGridLayout()
        layout.addWidget(QLabel('按类型过滤'), 0, 0)

        comboBox = QComboBox(self)

        for key, value in AssetsMap.items():
            comboBox.addItem(str(key))
            comboBox.setItemText(key, value)

        comboBox.currentIndexChanged.connect(self.update_assets_category)
        layout.addWidget(comboBox, 0, 1)

        return layout

    def update_assets_category(self, key):
        self.table.clear()

        if key == AssetsCategory.ALL:
            self.init_table(sum_assets())
            self.display(session.query(Assets).all())
        else:
            self.init_table(session.query(func.sum(Assets.balance)).filter(Assets.category == key).all())
            self.display(session.query(Assets).filter(Assets.category == key).all())
