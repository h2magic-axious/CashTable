from gui import QWidget, QHBoxLayout
from gui.functions import new_table, new_item


class TabIncome(QWidget):
    def __init__(self):
        super(TabIncome, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 3, self, ['ID', '项目', '金额'])
        self.table.setItem(0, 0, new_item("汇总", True))
        self.table.setItem(0, 1, new_item('', True))
        self.table.setItem(0, 2, new_item('0.0', True))

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)
