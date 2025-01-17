import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Supabase configurations
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # OpenAI API configurations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Application settings
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    DEFAULT_RECOMMENDATION_COUNT = int(os.getenv("DEFAULT_RECOMMENDATION_COUNT", 5))

# Access configurations via Config class
config = Config()
