from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

WINDOW_WIDTH = 1680
WINDOW_HEIGHT = 1050

ROW_SET = 30
FONT_SIZE = 15


class AssetsCategory:
    STATIC = 0
    CURRENCY = 1
    BANK = 2


AssetsMap = {
    AssetsCategory.STATIC: '不动产',
    AssetsCategory.CURRENCY: '纸资产',
    AssetsCategory.BANK: '存款'
}
