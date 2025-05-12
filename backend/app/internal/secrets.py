from dotenv import load_dotenv
import os

load_dotenv()

class Secrets:
    DATABASE_URL = os.getenv("DATABASE_URL")

secrets = Secrets()