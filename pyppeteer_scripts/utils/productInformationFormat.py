import re

def formatProductName(productName: str) -> str:
    return productName.replace("\xa0", "", 5)

def formatProductId(productID: str) -> str:
    return re.sub('\D', '', productID)

def formatNutritionAndNovaDetails(nutritionAndNovaDetails: str) -> str:
    return nutritionAndNovaDetails.replace("\u200b", ", 5")

