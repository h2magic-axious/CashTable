from enum import Enum
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

WINDOW_WIDTH = 1680
WINDOW_HEIGHT = 1050


class AssetsCategory(Enum):
    # 不动产
    STATIC = 0
    # 纸资产
    CURRENCY = 1
    # 存款
    BANK = 2
    # 预算
    BUDGET = 3
