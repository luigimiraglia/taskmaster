from dotenv import load_dotenv
import os

# Carica il file .env
load_dotenv()

# iCloud
ICLOUD_USER = os.getenv("ICLOUD_USER")
ICLOUD_APP_PASSWORD = os.getenv("ICLOUD_APP_PASSWORD")
ICLOUD_CALDAV_URL = os.getenv(
    "ICLOUD_CALDAV_URL", "https://caldav.icloud.com/")

# Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
MY_WHATSAPP_NUMBER = os.getenv("MY_WHATSAPP_NUMBER")

# Generali
PORT = int(os.getenv("PORT", 5000))
TIMEZONE = os.getenv("TIMEZONE", "America/Los_Angeles")
DEFAULT_DURATION_MIN = int(os.getenv("DEFAULT_DURATION_MIN", 60))
