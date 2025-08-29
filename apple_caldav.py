import load_dotenv
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import sys
from caldav import DAVClient


load_dotenv()

required = ["ICLOUD_CALDAV_URL", "ICLOUD_USER", "ICLOUD_APP_PASSWORD"]
missing = []

for name in required:
    value = os.getenv(name)
    if not value:
        missing.append(name)
if missing:
    print(f"Error: you are missing {missing}")
    sys.exit(1)


def get_client():
    client = DAVClient(url=os.getenv('ICLOUD_CALDAV_URL'), username=os.getenv(
        "ICLOUD_USER"), password=os.getenv("ICLOUD_APP_PASSWORD"))
    return client


def get_calendar(client):
    cal_url = os.getenv('ICLOUD_CALENDAR_URL')
    calendar = client.principal().calendar(url=cal_url)
    if not calendar:
        print('Calendar not found at url')
        sys.exit(1)
    return calendar


def create_event(title, start_dt, duration_min=60, location=None):
    client = get_client()
    calendar = get_calendar()

    if start_dt.tzinfo:
        start_dt = start_dt.replace(tzinfo=ZoneInfo("America/Los_Angeles"))
    start_dt = start_dt.astimezone(ZoneInfo("America/Los_Angeles"))
    start_dt.replace(second=0, microsecond=0)
