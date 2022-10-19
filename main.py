import fastapi, uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query
import asyncio

app = FastAPI()
# 127.0.0.1:8000/docs
# 127.0.0.1:8000/redoc


class Category(BaseModel):
    name: str = Field(title='Name')
    id: int = Field(title='Unique ID')


@app.get(path='/')
async def index():
    return {'Hello': '<b>Hello</b>'}


@app.get('/category', response_model=Category)
async def get_category(category_id: int = Query(ge=1)):
    category = Category(id=category_id, name=f'category {category_id}')
    return category


