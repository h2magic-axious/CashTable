from gui import QWidget, QHBoxLayout
from gui.functions import new_table, item
from models import session, Assets, sum_assets
from reference import ROW_SET, AssetsMap


class TabAssets(QWidget):
    def __init__(self):
        super(TabAssets, self).__init__()

        root_layout = QHBoxLayout()
        self.query_set = session.query(Assets).all()
        n_row = len(self.query_set) // ROW_SET + 1

        self.table = new_table(n_row * ROW_SET, 4, self, ['ID', '项目', '金额', '类别'])
        self.init_row()

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)

    def init_row(self):
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 2, item(str(sum_assets()), True))
        self.table.setItem(0, 3, item('', True))

        row = 1
        for i in self.query_set:
            self.table.setItem(row, 0, item(str(i.id), True))
            self.table.setItem(row, 1, item(i.project))
            self.table.setItem(row, 2, item(str(i.balance)))
            self.table.setItem(row, 3, item(AssetsMap[i.category]))
            row += 1
