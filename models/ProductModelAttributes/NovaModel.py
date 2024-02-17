from pydantic import BaseModel


class NovaModel(BaseModel):
    def __init__(self, score: str, title: str):
        self.score = score
        self.title = title