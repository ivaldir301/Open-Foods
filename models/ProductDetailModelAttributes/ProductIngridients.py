from typing import List
from pydantic import BaseModel


class ProductIngridients(BaseModel):
    hasPalmOil: str
    isVegan: bool
    isVegeterian: bool
    list: List
