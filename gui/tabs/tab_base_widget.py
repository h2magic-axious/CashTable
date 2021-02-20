from gui import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from gui.functions import new_table, new_item
from models import session, func, distinct  # , sum_debt, Debt
from reference import ROW_SET


class TabBase(QWidget):
    def __init__(self, model, sum_func):
        super(TabBase, self).__init__()

        self.model = model
        self.sum_func = sum_func

        n_row = session.query(func.count(distinct(self.model.id))).scalar() // ROW_SET + 1

        self.headers = ['ID', '项目', '金额']
        self.table = new_table(n_row * ROW_SET, 3, self, self.headers)

        root_layout = QVBoxLayout()
        table_layout = QHBoxLayout()
        panel_layout = QHBoxLayout()

        button_update_commit = QPushButton('提交', self)
        # button_update_commit.clicked.connect(self.button_update_commit_clicked)

        button_cancel = QPushButton('撤销', self)
        # button_cancel.clicked.connect(self.button_cancel_clicked)

        button_delete_by_id = QPushButton('删除', self)
        self.line_id_edit = QLineEdit(self)
        self.line_id_edit.setStyleSheet("background-color:#00CED1")
        self.line_id_edit.setPlaceholderText('输入要删除的记录的ID')
        # button_delete_by_id.clicked.connect(self.button_delete_clicked)

        panel_layout.addWidget(button_update_commit)
        panel_layout.addWidget(button_cancel)
        panel_layout.addWidget(button_delete_by_id)
        panel_layout.addWidget(self.line_id_edit)

        self.init_table(self.sum_func())
        self.display(session.query(self.model).all())

        table_layout.addWidget(self.table)
        root_layout.addLayout(panel_layout)
        root_layout.addLayout(table_layout)

        self.setLayout(root_layout)

    def init_table(self, s):
        self.table.setItem(0, 0, new_item("汇总", True))
        self.table.setItem(0, 1, new_item('', True))
        self.table.setItem(0, 2, new_item(str(round(s or 0, 4)), True))

    def display(self, items):
        row = 1
        for i in items:
            self.table.setItem(row, 0, new_item(str(i.id), True))
            self.table.setItem(row, 1, new_item(i.project))
            self.table.setItem(row, 2, new_item(str(i.balance)))

            row += 1
