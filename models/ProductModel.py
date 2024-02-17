from models.ProductModelAttributes import NovaModel
from models.ProductModelAttributes import NutritionModel
from pydantic import BaseModel


class ProductModel(BaseModel):
    id: str
    name: str
    nutrition: NutritionModel
    nova: NovaModel