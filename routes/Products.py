import asyncio
from fastapi import APIRouter
from pyppeteer_scripts.ProductsScrapper import getAllProductsFromWebsite

router = APIRouter()

@router.get("/produtos", tags=['produtos'])
async def getAllProductsBasedOnNutritionAndNovaParamethers(nutriscore: str, nova: int):
    scrappedProducts = await asyncio.ensure_future(getAllProductsFromWebsite(nutriscore, nova))
    if scrappedProducts is not []:
        return scrappedProducts
    else:
        return "no products where found"