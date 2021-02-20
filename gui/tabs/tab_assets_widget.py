from sqlalchemy import func, distinct

from gui import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from gui.functions import new_table, new_item, new_combo_box, get_combo_content, get_item_content
from models import session, Assets, sum_assets
from reference import ROW_SET, AssetsCategory


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
        button_update_commit.clicked.connect(self.button_update_commit_clicked)

        button_cancel = QPushButton('撤销修改', self)
        button_cancel.clicked.connect(self.button_cancel_clicked)

        button_delete_by_id = QPushButton('删除记录', self)
        self.line_id_edit = QLineEdit(self)
        self.line_id_edit.setPlaceholderText('输入要删除的记录的ID')
        button_delete_by_id.clicked.connect(self.button_delete_clicked)

        panel_layout.addWidget(button_update_commit)
        panel_layout.addWidget(button_cancel)
        panel_layout.addWidget(button_delete_by_id)
        panel_layout.addWidget(self.line_id_edit)

        self.init_table(sum_assets())
        self.display(session.query(Assets).all())

        table_layout.addWidget(self.table)
        root_layout.addLayout(panel_layout)
        root_layout.addLayout(table_layout)

        self.setLayout(root_layout)

    def init_table(self, s, currentKey=0):
        self.table.setItem(0, 0, new_item("汇总", True))
        self.table.setItem(0, 1, new_item('', True))
        self.table.setItem(0, 2, new_item(str(round(s, 4)), True))

        assets_category_filter_combo_box = new_combo_box(self)
        assets_category_filter_combo_box.setCurrentIndex(currentKey)
        assets_category_filter_combo_box.currentIndexChanged.connect(self.update_assets_category)

        self.table.setCellWidget(0, 3, assets_category_filter_combo_box)
        self.table.cellDoubleClicked.connect(self.activated_cell_to_build_item)

    def display(self, items):
        row = 1
        for i in items:
            self.table.setItem(row, 0, new_item(str(i.id), True))
            self.table.setItem(row, 1, new_item(i.project))
            self.table.setItem(row, 2, new_item(str(i.balance)))

            temp_combo = new_combo_box(self)
            temp_combo.setCurrentIndex(i.category)

            self.table.setCellWidget(row, 3, temp_combo)

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

    def activated_cell_to_build_item(self, row, col):
        if col != 3:
            return

        self.table.setCellWidget(row, col, new_combo_box(self))

    def button_update_commit_clicked(self):
        for row in range(1, self.table.rowCount()):
            ident = get_item_content(self.table, row, 0)
            balance = get_item_content(self.table, row, 2)

            if not ident and not balance:
                continue

            record = session.query(Assets).get(ident) if ident else Assets()

            record.project = get_item_content(self.table, row, 1)
            record.balance = float(balance)
            record.category = int(get_combo_content(self.table, row, 3))

            session.add(record)

        session.commit()
        self.update_assets_category(0)

    def button_cancel_clicked(self):
        self.update_assets_category(0)

    def button_delete_clicked(self):
        ident = self.line_id_edit.text()
        self.line_id_edit.clear()

        if ident:
            record = session.query(Assets).get(ident)
            session.delete(record)

        session.commit()
        self.update_assets_category(0)
