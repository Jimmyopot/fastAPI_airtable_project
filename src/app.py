from fastapi import FastAPI

app = FastAPI()

# Routes
'''
- Use this command to run:
uvicorn src.app:app --reload
'''
@app.get("/")
def home_view():
    return {"hello": "world"}

