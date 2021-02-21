from gui import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, Qt, QFont, QGridLayout, QPushButton, QTextBrowser
from reference import FONT_SIZE, MESSAGE_BOARD_TEMPLATE
from models import DATABASE_PATH, Assets, Debt, Income, Expenses, sum_models

DEFAULT_FONT = QFont('宋体', FONT_SIZE)


def new_label(parent, content, align):
    temp = QLabel(parent)
    temp.setText(content)
    temp.setAlignment(align)
    temp.setFont(DEFAULT_FONT)
    return temp


def new_line_edit(parent, content, align, no=True, color=None):
    temp = QLineEdit(parent)
    temp.setFont(DEFAULT_FONT)
    temp.setAlignment(align)
    temp.setText(content)
    if color:
        temp.setStyleSheet(f"color:{color}")
    if no:
        temp.setFocusPolicy(Qt.NoFocus)

    return temp


class TabDashboard(QWidget):
    def __init__(self):
        super(TabDashboard, self).__init__()

        root_layout = QVBoxLayout()

        root_layout.addLayout(self.init_database_label_layout())

        s_assets = sum_models(Assets)
        self.line_assets = new_line_edit(self, str(s_assets), Qt.AlignRight, color='green')
        s_debt = sum_models(Debt)
        self.line_debt = new_line_edit(self, str(s_debt), Qt.AlignRight, color='red')
        s_a_d = round(s_assets - s_debt, 2)
        self.line_sad = new_line_edit(self, str(s_a_d), Qt.AlignRight, color='green' if s_a_d >= 0 else 'red')

        s_income = sum_models(Income)
        self.line_income = new_line_edit(self, str(s_income), Qt.AlignRight, color='green')
        s_expenses = sum_models(Expenses)
        self.line_expenses = new_line_edit(self, str(s_expenses), Qt.AlignRight, color='red')
        s_i_e = round(s_income - s_expenses, 2)
        self.line_sie = new_line_edit(self, str(s_i_e), Qt.AlignRight, color='green' if s_i_e >= 0 else 'red')

        root_layout.addLayout(self.init_asset_layout())
        root_layout.addLayout(self.init_message_board())

        self.setLayout(root_layout)

    def init_database_label_layout(self):
        temp = QHBoxLayout()

        temp.addWidget(new_label(self, '数据库路径：', Qt.AlignRight))
        temp.addWidget(new_line_edit(self, str(DATABASE_PATH), Qt.AlignLeft))

        return temp

    def init_message_board(self):
        temp = QHBoxLayout()

        temp_text_browser = QTextBrowser(self)
        temp_text_browser.setText(MESSAGE_BOARD_TEMPLATE)

        temp.addWidget(temp_text_browser)

        return temp

    def init_asset_layout(self):
        temp = QGridLayout()

        label_asset = new_line_edit(self, '资产', Qt.AlignCenter)
        label_asset.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        temp.addWidget(label_asset, 0, 1)
        label_debt = new_line_edit(self, '负债', Qt.AlignCenter)
        label_debt.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        temp.addWidget(label_debt, 0, 2)

        temp.addWidget(new_label(self, '本金', Qt.AlignRight), 1, 0)
        temp.addWidget(self.line_assets, 1, 1)
        temp.addWidget(self.line_debt, 1, 2)
        temp.addWidget(self.line_sad, 1, 3)

        label_income = new_line_edit(self, '收入', Qt.AlignCenter)
        label_income.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        temp.addWidget(label_income, 2, 1)
        label_expenses = new_line_edit(self, '支出', Qt.AlignCenter)
        label_expenses.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        temp.addWidget(label_expenses, 2, 2)

        temp.addWidget(new_label(self, '现金流', Qt.AlignRight), 3, 0)
        temp.addWidget(self.line_income, 3, 1)
        temp.addWidget(self.line_expenses, 3, 2)
        temp.addWidget(self.line_sie, 3, 3)

        button_flush = QPushButton('刷新', self)
        button_flush.clicked.connect(self.update_balance)

        temp.addWidget(button_flush, 4, 0)

        return temp

    def update_balance(self):
        s_assets = sum_models(Assets)
        s_debt = sum_models(Debt)
        s_income = sum_models(Income)
        s_expenses = sum_models(Expenses)

        self.line_assets.setText(str(s_assets))
        self.line_debt.setText(str(s_debt))
        self.line_sad.setText(str(round(s_assets - s_debt, 2)))
        self.line_income.setText(str(s_income))
        self.line_expenses.setText(str(s_expenses))
        self.line_sie.setText(str(round(s_income - s_expenses, 2)))
