import sys

from gui.main_window import MainWindow
from gui import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()

    sys.exit(app.exec_())
