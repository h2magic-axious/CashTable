from pathlib import Path
import os, sys

DEBUT = False
if DEBUT:
    BASE_DIR = Path(__file__).parent.resolve()
else:
    BASE_DIR = Path(os.path.realpath(sys.executable)).parent.resolve()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 768

ROW_SET = 50
FONT_SIZE = 15


class AssetsCategory:
    ALL = 0
    STATIC = 1
    CURRENCY = 2
    BANK = 3


AssetsMap = {
    AssetsCategory.ALL: '全部',
    AssetsCategory.STATIC: '不动产',
    AssetsCategory.CURRENCY: '纸资产',
    AssetsCategory.BANK: '存款'
}

MESSAGE_BOARD_TEMPLATE = """
软件介绍：
    Assets 和 Debt 中的金额记录的是当前已有的数值
    Income 和 Expenses 中的金额记录的是月度收入/月度支出
"""
