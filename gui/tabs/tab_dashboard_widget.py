from gui import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel, Qt, QFont
from reference import FONT_SIZE
from models import DATABASE_PATH, BASE_DIR


class TabDashboard(QWidget):
    def __init__(self):
        super(TabDashboard, self).__init__()

        root_layout = QVBoxLayout()

        root_layout.addLayout(self.init_python_label_layout())
        root_layout.addLayout(self.init_database_label_layout())

        self.setLayout(root_layout)

    def init_python_label_layout(self):
        temp = QHBoxLayout()

        temp_label = QLabel(self)
        temp_label.setText('进程路径：')
        temp_label.setAlignment(Qt.AlignRight)
        temp_label.setFont(QFont('宋体', FONT_SIZE))
        temp.addWidget(temp_label)

        temp_line_edit = QLineEdit(self)
        temp_line_edit.setFont(QFont('宋体', FONT_SIZE))
        temp_line_edit.setAlignment(Qt.AlignLeft)
        temp_line_edit.setFocusPolicy(Qt.NoFocus)
        temp_line_edit.setText(str(BASE_DIR))
        temp.addWidget(temp_line_edit)

        return temp

    def init_database_label_layout(self):
        temp = QHBoxLayout()

        temp_label = QLabel(self)
        temp_label.setText('数据库路径：')
        temp_label.setAlignment(Qt.AlignRight)
        temp_label.setFont(QFont('宋体', FONT_SIZE))
        temp.addWidget(temp_label)

        temp_line_edit = QLineEdit(self)
        temp_line_edit.setFont(QFont('宋体', FONT_SIZE))
        temp_line_edit.setAlignment(Qt.AlignLeft)
        temp_line_edit.setFocusPolicy(Qt.NoFocus)
        temp_line_edit.setText(str(DATABASE_PATH))
        temp.addWidget(temp_line_edit)

        return temp
