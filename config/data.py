import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    USERNAME = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
