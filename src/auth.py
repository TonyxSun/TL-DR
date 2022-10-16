from dotenv import load_dotenv
load_dotenv()
import os

DATABASE_URL = os.environ.get("DATABASE_URL")