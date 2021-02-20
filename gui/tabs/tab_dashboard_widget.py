from gui import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, Qt, QFont, QGridLayout
from reference import FONT_SIZE
from models import DATABASE_PATH, BASE_DIR, Assets, Debt, Income, Expenses, func, session

DEFAULT_FONT = QFont('宋体', FONT_SIZE)


def new_label(parent, content, align):
    temp = QLabel(parent)
    temp.setText(content)
    temp.setAlignment(align)
    temp.setFont(DEFAULT_FONT)
    return temp


def new_line_edit(parent, content, align, no=True):
    temp = QLineEdit(parent)
    temp.setFont(DEFAULT_FONT)
    temp.setAlignment(align)
    temp.setText(content)
    if no:
        temp.setFocusPolicy(Qt.NoFocus)

    return temp


class TabDashboard(QWidget):
    def __init__(self):
        super(TabDashboard, self).__init__()

        root_layout = QVBoxLayout()

        root_layout.addLayout(self.init_python_label_layout())
        root_layout.addLayout(self.init_database_label_layout())

        self.setLayout(root_layout)

    def init_python_label_layout(self):
        temp = QHBoxLayout()

        temp.addWidget(new_label(self, '进程路径：', Qt.AlignRight))
        temp.addWidget(new_line_edit(self, str(BASE_DIR), Qt.AlignLeft))

        return temp

    def init_database_label_layout(self):
        temp = QHBoxLayout()

        temp.addWidget(new_label(self, '数据库路径：', Qt.AlignRight))
        temp.addWidget(new_line_edit(self, str(DATABASE_PATH), Qt.AlignLeft))

        return temp

    def init_asset_layout(self):
        temp = QGridLayout()

        temp.addWidget(new_label(self, '资产', Qt.AlignCenter), 0, 1)
        temp.addWidget(new_label(self, '负债', Qt.AlignCenter), 0, 2)

        temp.addWidget(new_label(self, '本金', Qt.AlignRight), 1, 0)
