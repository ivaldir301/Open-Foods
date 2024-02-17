from models.ProductDetailModelAttributes.NovaModel import NovaModel
from models.ProductDetailModelAttributes.ProductNutrition import ProductNutrition
from models.ProductDetailModelAttributes.ProductIngridients import ProductIngridients
from pydantic import BaseModel


class ProductDetailModel(BaseModel):
    title: str
    quantitiy: str
    ingredients: ProductIngridients
    nutrition: ProductNutrition
    nova: NovaModel