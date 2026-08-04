import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    LOGIN = os.getenv("LOGIN_ADMIN")
    PASSWORD = os.getenv("PASSWORD_ADMIN")
    REQUEST_URL = 'https://ru.yougile.com/'
    NAME_COMPANY = "Test_API_Postman"
