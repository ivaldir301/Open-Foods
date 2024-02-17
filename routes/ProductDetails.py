from fastapi import APIRouter, Body, FastAPI, HTTPException, status
from pydantic import Json

router = APIRouter()

app = FastAPI()

router.get("/Product/{id}")
def getSpecificProductNutritionDetails(id: str) -> Json:
    return "specific product details"