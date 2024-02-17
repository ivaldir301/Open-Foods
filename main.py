from itertools import product
from fastapi import FastAPI
from routes import Products, ProductDetails
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Products)
app.include_router(ProductDetails)

# Simple endpoint to test if api is up and running 
@app.get("/test")
def hello_world():
    return "It's working!!"

# Line added here for fastapi debugging porpuses
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
