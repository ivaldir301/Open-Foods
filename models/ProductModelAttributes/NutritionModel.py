from asyncio import streams
from pydantic import BaseModel


class NutritionModel(BaseModel):
    def __init__(self, score: str, title: str):
        self.score = score
        self.title = title