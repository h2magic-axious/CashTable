from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

WINDOW_WIDTH = 1680
WINDOW_HEIGHT = 1050

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
