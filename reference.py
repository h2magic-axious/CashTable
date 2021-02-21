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
