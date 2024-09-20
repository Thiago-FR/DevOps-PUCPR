from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    num1: float
    num2: float


class Number(BaseModel):
    num: int


@app.post("/sum")
async def odd_even(number: Number):
    result = number.num % 2
    return {"odd_even": "odd" if result != 0 else "even"}


@app.post("/sum")
async def sum(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"sum": result}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
