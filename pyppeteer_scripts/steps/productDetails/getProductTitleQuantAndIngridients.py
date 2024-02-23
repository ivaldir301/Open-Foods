import logging 

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

async def getProductTitleQuantAndIngridients(pageReference: any, specificProductInfo):
    logging.info("----------> Getting product quantitity and ingridients ...")
    
    productTitle: str = (await pageReference.querySelectorEval(".title-1", "(element) => element.textContent"))   
    specificProductInfo['title'] = productTitle.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    specificProductInfo['quantity']: str = await pageReference.querySelectorEval("#field_quantity_value", "(element) => element.textContent")
    specificProductInfo['ingridients'] = {}
    
    try:
        hasPalmOilDomComponent: str = await pageReference.querySelectorEval("#panel_ingredients_analysis_en-palm-oil-content-unknown > li > a > h4", "(element) => element.textContent")
        if "Desconhece-se se contém óleo de palma" in hasPalmOilDomComponent:
            specificProductInfo['ingridients']['hasPalmOil'] = "Unknown"
        elif "Sem óleo de palma" in hasPalmOilDomComponent:
            specificProductInfo['ingridients']['hasPalmOil'] = True
    except:
        try:
            hasPalmOilDomComponent: str = await pageReference.querySelectorEval("#panel_ingredients_analysis_en-may-contain-palm-oil > li > a > h4", "(element) => element.textContent")
            if "Pode conter óleo de palma" in hasPalmOilDomComponent:
                specificProductInfo['ingridients']['hasPalmOil'] = True 
        except:
            logging.warning("-----------> Component for palm oil presence in product not found")
       
    try: 
        isVeganComponent = await pageReference.querySelectorAll("#panel_ingredients_analysis_en-vegan")
        if isVeganComponent == []:
            specificProductInfo['ingridients']['isVegan'] = False
        else:
            logging.info(isVeganComponent)
            specificProductInfo['ingridients']['isVegan'] = True
    except:
        logging.warning("----------> Component with vegan presence in product value was not found in the page")

    try:
        isVegetarianComponent = await pageReference.querySelectorAll("#panel_ingredients_analysis_en-vegetarian")
        if isVegetarianComponent == []:
            specificProductInfo['ingridients']['isVegetarian'] = False
        else:
            specificProductInfo['ingridients']["isVegetarian"] = True 
    except:
        logging.warning("----------> Component with vegeterian presence in product value was not found")
        
    try:    
        panelIngridientDomContent: str = await pageReference.querySelectorEval("#panel_ingredients_content > div:nth-child(1) > div > div", "(element) => element.textContent")
        if panelIngridientDomContent is not None:
            ingridientContentList = []
            ingridientContentList.append((panelIngridientDomContent.replace("\n", "", int(len(panelIngridientDomContent))).strip("\t")).replace(": ", "").strip())
            specificProductInfo["ingridients"]["list"] = ingridientContentList
    except:
        logging.warning("----------> Component with product ingridients was not found in the page")
    return specificProductInfo