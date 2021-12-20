#import statements
from fastapi import APIRouter
from models.text import Text
from services.summarize import summarize

api_router = APIRouter()


@api_router.get('/hello')
async def hello_world():
    return "Hello world"


@api_router.post('/summarize')
async def summarize_text(text: Text):
    return summarize(text)
