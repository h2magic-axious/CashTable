from gui import QWidget, QHBoxLayout
from gui.functions import new_table, item
from models import session, Assets


class TabAssets(QWidget):
    def __init__(self):
        super(TabAssets, self).__init__()

        root_layout = QHBoxLayout()

        self.table = new_table(20, 4, self, ['ID', '项目', '金额', '类别'])
        self.init_row()

        root_layout.addWidget(self.table)

        self.setLayout(root_layout)

    def init_row(self):
        self.table.setItem(0, 0, item("汇总", True))
        self.table.setItem(0, 1, item('', True))
        self.table.setItem(0, 3, item('', True))

        items = session.query(Assets).all()
        self.table.setItem(0, 2, item(0.0, True))
