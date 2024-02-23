async def getProductNutritionFactsDetails(pageReference: any, specificProductInfo):
    try:            
        amountOfEnergyPer100gValue: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of energy per 100g not found in the page ")
        amountOfEnergyPer100gValue = "unknown"
        
    try:    
        amountOfEnergyPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amout of energy in product was not found in the page")
        amountOfEnergyPerServing = "unknown"
        
    amountOfEnergy = {
        "per100g": amountOfEnergyPer100gValue.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfEnergyPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    try:
        amountOfFatsPer100g: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of fats per 100g was not found in the page")  
        amountOfFatsPer100g = "unknown"      
        
    try:
        amountOfFatsPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of fats per serving was not found in the page")
        amountOfFatsPerServing = "unknown"
        
    amountOfFatsNutrition = {
        "per100g": amountOfFatsPer100g.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfFatsPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    try:    
        amountOfCarbohydratesPer100g: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of carbohydrates per 100g was not found in the page")
        
    try:
        amountOfCarbohydratesPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(4) > td:nth-child(3) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of carbohydrates per serving was not found in the page")
        amountOfCarbohydratesPerServing = "unknown"
        
    amountOfCarbohydrates = {
        "per100g": amountOfCarbohydratesPer100g.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfCarbohydratesPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    try:
        amountOfDietaryFiberPer100g: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of dietary fiber per 100g was not found in the page")
        amountOfDietaryFiberPer100g = "unknown"
        
    try:
        amountOfDietaryFiberPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(6) > td:nth-child(3) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of dietary fiber per serving was not found in the page")
        amountOfDietaryFiberPerServing = "unknown"
        
    amountOfDietaryFiber = {
        "per100g": amountOfDietaryFiberPer100g.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfDietaryFiberPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    try:
        amountOfProteinPer100g: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(7) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of protein per 100g was not found in the page")
        amountOfProteinPer100g = "unknown"
        
    try:    
        amountOfProteinPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(7) > td:nth-child(3) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of protein per serving was not found in the page")
        amountOfProteinPerServing = "unknown"
        
    amountOfProtein = {
        "per100g": amountOfProteinPer100g.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfProteinPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    try:
        amountOfSaltPer100g: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of salt per 100g was not found in the page")
        amountOfSaltPer100g = "unknown"
    
    try:
        amountOfSaltPerServing: str = await pageReference.querySelectorEval("#panel_nutrition_facts_table_content > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > span", "(element) => element.textContent")
    except:
        print("----------> Component for amount of salt per serving was not found in the page")
        amountOfSaltPerServing = "unknown"
        
    amountOfSalt = {
        "per100g": amountOfSaltPer100g.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip(),
        "perServing": amountOfSaltPerServing.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    }
    
    specificProductInfo["nutrition"]["data"] = {
        "Energia": amountOfEnergy,
        "Gorduras/lípidos": amountOfFatsNutrition,
        "Carboidratos": amountOfCarbohydrates,
        "Fibra alimentar": amountOfDietaryFiber,
        "Proteínas": amountOfProtein, 
        "Sal": amountOfSalt
    }
    
    return specificProductInfo