from typing import Dict
from pydantic import BaseModel


class ProductNutrition(BaseModel):
    score: str
    values: list[str, str]
    servingSize: str
    data: Dict[str, Dict[str, str]]