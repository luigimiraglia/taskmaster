from datetime import datetime
from zoneinfo import ZoneInfo
import dateparser

settings = {
    "PREFER_DATES_FROM": "future",
    "RELATIVE_BASE": datetime.now(ZoneInfo("America/Los_Angeles")),
}

print("domani alle 9 →", dateparser.parse(
    "monday at 9:00", settings=settings))
