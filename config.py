import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_UI_URL = os.getenv("BASE_UI_URL")
    BASE_API_URL = os.getenv("BASE_API_URL")
    RUN_MODE = os.getenv("RUN_MODE", "local").lower()

    SELENOID_URL = os.getenv("SELENOID_URL")
    ENABLE_VNC = os.getenv("ENABLE_VNC")
    ENABLE_VIDEO = os.getenv("ENABLE_VIDEO")

settings = Settings()
