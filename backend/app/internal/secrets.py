from dotenv import load_dotenv
import os

load_dotenv()

class DBsecrets:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")