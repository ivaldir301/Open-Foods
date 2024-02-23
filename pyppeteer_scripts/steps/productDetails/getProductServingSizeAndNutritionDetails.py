import logging 

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addHandler(logging.StreamHandler())

async def getProductServingSizeAndNutritionDetails(pageReference: any, specificProductInfo):
    logging.info("----------> Getting the product serving size ...")
    try:
        productServingSize: str = await pageReference.querySelectorEval("#panel_serving_size_content > div > div > div", "(element) => element.textContent")
    except:
        logging.warning("----------> Product serving size component not found in the page")
        productServingSize = "unknown"
       
    if productServingSize != None:
        logging.info("----------> Serving size stored")
        specificProductInfo["nutrition"]["servingSize"] = specificProductInfo["nutrition"]["servingSize"] = (productServingSize.replace("\n", "", int(len(productServingSize))).strip("\t")).strip()
        
    logging.info("----------> Getting the product nutrition details ...")
    try:
        nutritionScoreDomComponent: str = await pageReference.querySelectorEval("#panel_nutriscore > li > a > h4", "(element) => element.textContent")
        nutritionScoreDomComponent.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
        if nutritionScoreDomComponent == "Qualidade nutricional muito boa":
            specificProductInfo["nutrition"]["score"] = "A"
        elif nutritionScoreDomComponent == "Qualidade nutricional boa":
            specificProductInfo["nutrition"]["score"] = "B"
        elif nutritionScoreDomComponent == "Qualidade nutricional média":
            specificProductInfo["nutrition"]["score"] = "C"
        elif nutritionScoreDomComponent == "Qualidade nutricional baixa":
            specificProductInfo["nutrition"]["score"] = "D"
        elif nutritionScoreDomComponent == "Má qualidade nutricional":
            specificProductInfo["nutrition"]["score"] = "D"
    except:
        logging.warning("----------> Component for nutrition score was not found in the page")
        nutritionScoreDomComponent = "unknown"
        
    specificProductInfo["nutrition"]["values"] = []
    
    try:
        amountOfFats: str = await pageReference.querySelectorEval("#panel_nutrient_level_fat > li > a > h4", "(element) => element.textContent")
    except:
        logging.warning("-----------> Component for fats not found in the page")
        amountOfFats = "unknown"
            
    try:
        amountOfFatsAndAcids: str = await pageReference.querySelectorEval("#panel_nutrient_level_saturated-fat > li > a > h4", "(element) => element.textContent")
    except:
        logging.warning("-----------> Component for fats and acids not found in the page")
        amountOfFatsAndAcids = "unknown"
        
    try:
        amountOfSalt: str = await pageReference.querySelectorEval("#panel_nutrient_level_salt > li > a > h4", "(element) => element.textContent")
    except:
        logging.warning("-----------> Component for salt not found in the page")
        amountOfSalt = "unknown"
            
    if "baixa" in amountOfFats:
        specificProductInfo["nutrition"]["values"].append(["low", amountOfFats.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "moderada" in amountOfFats:
        specificProductInfo["nutrition"]["values"].append(["moderate", amountOfFats.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "elevada" in amountOfFats:
        specificProductInfo["nutrition"]["values"].append(["high", amountOfFats.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    
    if "baixa" in amountOfFatsAndAcids:
        specificProductInfo["nutrition"]["values"].append(["low", amountOfFatsAndAcids.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "moderada" in amountOfFatsAndAcids:
        specificProductInfo["nutrition"]["values"].append(["moderate", amountOfFatsAndAcids.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "elevada" in amountOfFatsAndAcids:
        specificProductInfo["nutrition"]["values"].append(["high", amountOfFatsAndAcids.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    
    if "baixa" in amountOfSalt:
        specificProductInfo["nutrition"]["values"].append(["low", amountOfSalt.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "moderada" in amountOfSalt:
        specificProductInfo["nutrition"]["values"].append(["moderate", amountOfSalt.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    elif "elevada" in amountOfSalt:
        specificProductInfo["nutrition"]["values"].append(["high", amountOfSalt.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()])
    
    logging.info("----------> Product nutrition details stored")
    return specificProductInfo
     