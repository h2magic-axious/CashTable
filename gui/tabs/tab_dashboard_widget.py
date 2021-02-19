from gui import QWidget, QHBoxLayout


class TabDashboard(QWidget):
    def __init__(self):
        super(TabDashboard, self).__init__()

        root_layout = QHBoxLayout()

        self.setLayout(root_layout)