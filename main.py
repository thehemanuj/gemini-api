from fastapi import FastAPI
from pydantic import BaseModel
import google.genai as genai

app = FastAPI()

# Request schema
class PromptRequest(BaseModel):
    api_key: str
    prompt: str

@app.post("/generate")
def generate_content(req: PromptRequest):
    try:
        # Initialize Gemini client with provided API key
        client = genai.Client(api_key=req.api_key)

        # Call Gemini with the given prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=req.prompt
        )

        return {"response": response.text}

    except Exception as e:
        return {"error": str(e)}
