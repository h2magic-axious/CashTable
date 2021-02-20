from gui import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from gui.functions import new_table, new_item, get_item_content
from models import func, distinct
from reference import ROW_SET


class TabBase(QWidget):
    def __init__(self, model, sess):
        super(TabBase, self).__init__()

        self.model = model
        self.sess = sess

        n_row = self.sess.query(func.count(distinct(model.id))).scalar() // ROW_SET + 1

        self.headers = ['ID', '项目', '金额']
        self.table = new_table(n_row * ROW_SET, 3, self, self.headers)

        root_layout = QVBoxLayout()
        table_layout = QHBoxLayout()
        panel_layout = QHBoxLayout()

        button_update_commit = QPushButton('提交', self)
        button_update_commit.clicked.connect(self.button_update_commit_clicked)

        button_cancel = QPushButton('刷新', self)
        button_cancel.clicked.connect(self.update_display)

        button_delete_by_id = QPushButton('删除', self)
        self.line_id_edit = QLineEdit(self)
        self.line_id_edit.setStyleSheet("background-color:#00CED1")
        self.line_id_edit.setPlaceholderText('输入要删除的记录的ID')
        button_delete_by_id.clicked.connect(self.button_delete_clicked)

        panel_layout.addWidget(button_update_commit)
        panel_layout.addWidget(button_cancel)
        panel_layout.addWidget(button_delete_by_id)
        panel_layout.addWidget(self.line_id_edit)

        self.init_table(self.sess.query(func.sum(model.balance)).scalar())
        self.display(self.sess.query(model).all())

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

    def update_display(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(self.headers)

        self.init_table(self.sess.query(func.sum(self.model.balance)).scalar())
        self.display(self.sess.query(self.model).all())

    def button_update_commit_clicked(self):
        for row in range(1, self.table.rowCount()):
            ident = get_item_content(self.table, row, 0)
            balance = get_item_content(self.table, row, 2)

            if not ident and not balance:
                continue

            record = self.sess.query(self.model).get(ident) if ident else self.model()
            record.project = get_item_content(self.table, row, 1)
            try:
                record.balance = float(balance)
            except:
                message = f"不规范的数值\n{balance}"
                QMessageBox.warning(self, '错误输入', message, QMessageBox.Ok)

                self.sess.commit()
                self.update_display()
                return

            self.sess.add(record)

        self.sess.commit()
        self.update_display()

    def button_delete_clicked(self):
        ident = self.line_id_edit.text()
        self.line_id_edit.clear()

        if ident:
            record = self.sess.query(self.model).get(ident)
            self.sess.delete(record)

        self.sess.commit()
        self.update_display()