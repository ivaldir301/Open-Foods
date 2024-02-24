from fastapi import APIRouter, Body, FastAPI

from pyppeteer_scripts.productDetailsScrapper import getProductWithId

router = APIRouter()

app = FastAPI()

@router.get("/Product/", tags=['produto'])
async def getSpecificProductNutritionDetails(id: str):
    scrappedProduct = await getProductWithId(id)
    if scrappedProduct is not []:
        return scrappedProduct
    else:
        return "products was not found"
