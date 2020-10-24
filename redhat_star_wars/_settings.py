import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
