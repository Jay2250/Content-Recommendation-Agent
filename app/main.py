from fastapi import FastAPI, Depends
from app.models import UserRequest, ContentResponse
from app.langchain_agent import generate_content
from app.database import init_db

from app.config import config

app = FastAPI(
    title="Personalized Content Recommendation Agent",
    debug=config.DEBUG
)

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/recommend", response_model=ContentResponse)
async def recommend_content(request: UserRequest):
    response = await generate_content(request.user_id, request.interests)
    return response
