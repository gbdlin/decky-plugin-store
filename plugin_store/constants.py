from enum import Enum
from pathlib import Path

BASE_DIR = Path(__file__).expanduser().resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

CDN_URL = "https://cdn.tzatzikiweeb.moe/file/steam-deck-homebrew/"
CDN_ERROR_RETRY_TIMES = 5


class SortDirection(Enum):
    desc = "desc"
    asc = "asc"


class SortType(Enum):
    name = "name"
    date = "date"
