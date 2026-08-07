import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DATABASE_URL = os.getenv("MY_DATABASE_URL")
