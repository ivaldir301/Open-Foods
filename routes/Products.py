from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import Json

router = APIRouter()

app = FastAPI()

router.get("/products")
def getAllProductsBasedOnNutritionAndNovaParamethers() -> Json:
    return "all products!!"