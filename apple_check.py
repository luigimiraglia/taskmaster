from dotenv import load_dotenv
import os
from caldav import DAVClient
from caldav.lib.error import AuthorizationError
import sys

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

client = DAVClient(url=os.getenv('ICLOUD_CALDAV_URL'), username=os.getenv(
    "ICLOUD_USER"), password=os.getenv("ICLOUD_APP_PASSWORD"))

try:
    principal = client.principal()
except AuthorizationError:
    print('Your iCloud credentials are invalid')
    sys.exit(1)
except Exception as e:
    print('Unknown error!')

calendars = principal.calendars()

if not calendars:
    print('No calendar was found :(')
    sys.exit(1)

for cal in calendars:
    print(cal.name)
    print(cal.url)
