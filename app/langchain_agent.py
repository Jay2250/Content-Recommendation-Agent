from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from app.database import fetch_user_preferences

from langchain.llms import OpenAI
from app.config import config



async def generate_content(user_id: str, interests: list):
    preferences = await fetch_user_preferences(user_id)
    llm = OpenAI(api_key=config.OPENAI_API_KEY, model="gpt-4", temperature=0.7)


    # Combine preferences and interests
    combined_interests = preferences + interests

    # Define a prompt
    prompt = PromptTemplate(
        input_variables=["interests"],
        template="Recommend 5 personalized articles for someone interested in {interests}.",
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    recommendations = await chain.run(interests=", ".join(combined_interests))

    return {"user_id": user_id, "recommendations": recommendations.split("\n")}
