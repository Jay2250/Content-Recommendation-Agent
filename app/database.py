
from app.config import config
from supabase import create_client



supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)

async def init_db():
    # Example: Create a users table
    await supabase.postgrest.from_("users").upsert({
        "id": "test_user",
        "preferences": ["AI", "Data Science"]
    }).execute()

async def fetch_user_preferences(user_id: str):
    response = await supabase.postgrest.from_("users").select("preferences").eq("id", user_id).execute()
    return response.data[0]["preferences"] if response.data else []
