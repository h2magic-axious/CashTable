from gui import QWidget, QHBoxLayout
from gui.functions import new_table, item


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
