import os
import pathlib

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from functools import lru_cache


BASE_DIR = pathlib.Path(__file__).parent # src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates")


@lru_cache()
def cached_dotenv():
    load_dotenv()
    
cached_dotenv()


# Routes
'''
- Use this command to run:
uvicorn src.app:app --reload
'''
@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/")
def home_signup_view(request: Request, email:str=Form(...)):
    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email})
