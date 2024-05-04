import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    INVALID_USERNAME = os.getenv("INVALID_USERNAME")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
