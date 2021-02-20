import sys
import os

from gui.main_window import MainWindow
from gui import QApplication
from models import session

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow(session)
    ex.show()

    sys.exit(app.exec_())
