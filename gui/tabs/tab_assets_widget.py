from sqlalchemy import func, distinct

from gui import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton
from gui.functions import new_table, item
from models import session, Assets, sum_assets
from reference import ROW_SET, AssetsMap, AssetsCategory


class TabAssets(QWidget):
    def __init__(self):
        super(TabAssets, self).__init__()
        n_row = session.query(func.count(distinct(Assets.id))).scalar() // ROW_SET + 1

        self.headers = ['ID', '项目', '金额', '类别']
        self.table = new_table(n_row * ROW_SET, 4, self, self.headers)

        root_layout = QVBoxLayout()

        table_layout = QHBoxLayout()

        panel_layout = QHBoxLayout()
        button_update_commit = QPushButton('提交修改', self)
        button_cancel = QPushButton('撤销修改', self)
        panel_layout.addWidget(button_update_commit)
        panel_layout.addWidget(button_cancel)

        self.init_table(sum_assets())
        self.display(session.query(Assets).all())

        table_layout.addWidget(self.table)

        root_layout.addLayout(table_layout)
        root_layout.addLayout(panel_layout)

        self.setLayout(root_layout)

    def init_table(self, s, currentKey=0):
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item(str(s), True))
        AssetsCategoryFilerComboBox = QComboBox(self)
        for key, value in AssetsMap.items():
            AssetsCategoryFilerComboBox.addItem(str(key))
            AssetsCategoryFilerComboBox.setItemText(key, value)
        AssetsCategoryFilerComboBox.setCurrentIndex(currentKey)
        AssetsCategoryFilerComboBox.currentIndexChanged.connect(self.update_assets_category)

        self.table.setCellWidget(0, 3, AssetsCategoryFilerComboBox)

    def display(self, items):
        row = 1
        for i in items:
            self.table.setItem(row, 0, item(str(i.id), True))
            self.table.setItem(row, 1, item(i.project))
            self.table.setItem(row, 2, item(str(i.balance)))
            # self.table.setItem(row, 3, item())

            AssetsCategoryFilerComboBox = QComboBox(self)
            for key, value in AssetsMap.items():
                AssetsCategoryFilerComboBox.addItem(str(key))
                AssetsCategoryFilerComboBox.setItemText(key, value)

            AssetsCategoryFilerComboBox.setCurrentIndex(i.category)

            self.table.setCellWidget(row, 3, AssetsCategoryFilerComboBox)

            row += 1

    def update_assets_category(self, key):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(self.headers)

        if key == AssetsCategory.ALL:
            s = sum_assets()
            query_set = session.query(Assets).all()
        else:
            s = session.query(func.sum(Assets.balance).filter(Assets.category == key)).scalar()
            query_set = session.query(Assets).filter(Assets.category == key).all()

        self.init_table(s, key)
        self.display(query_set)
