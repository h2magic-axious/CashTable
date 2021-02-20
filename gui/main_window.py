from gui import QMainWindow, QHBoxLayout, QTabWidget, Qt
from reference import WINDOW_WIDTH, WINDOW_HEIGHT

from gui.tabs import *

from models import Debt, Expenses, Income


class MainWindow(QMainWindow):
    def __init__(self, sess):
        super().__init__()
        self.sess = sess

        self.root_layout = QHBoxLayout()

        self.tab_widget = QTabWidget(self)
        self.init_tab_widget(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.root_layout.addWidget(self.tab_widget)
        self.setLayout(self.root_layout)

        self.init_ui()

    def init_tab_widget(self, width, height):
        self.tab_widget.setTabShape(QTabWidget.Triangular)

        self.tab_widget.setMinimumHeight(height)
        self.tab_widget.setMaximumHeight(height)

        self.tab_widget.setMinimumWidth(width)
        self.tab_widget.setMaximumWidth(width)

        style = "QTabBar::tab{width:$1px;height:25px;background-color:#66CDAA;font:15pt '宋体';color: black}"
        self.tab_widget.setStyleSheet(style.replace('$1', str(width / 5)))

    def init_ui(self):
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle('资产负债表')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.tab_widget.addTab(TabDashboard(), 'Dashboard')
        self.tab_widget.addTab(TabAssets(self.sess), 'Assets')

        self.tab_widget.addTab(TabBase(Debt, self.sess), 'Debt')
        self.tab_widget.addTab(TabBase(Income, self.sess), 'Income')
        self.tab_widget.addTab(TabBase(Expenses, self.sess), 'Expenses')
