import sys

from gui.main_window import Example
from gui import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()

    sys.exit(app.exec_())
