from fastapi import FastAPI
from routes import Products, ProductDetails
import uvicorn

app = FastAPI()

app.include_router(Products.router)
app.include_router(ProductDetails.router)

# Simple endpoint to test if api is up and running 
@app.get("/test")
def hello_world():
    return "It's working!!"

# Line added here for fastapi debugging purposes
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
