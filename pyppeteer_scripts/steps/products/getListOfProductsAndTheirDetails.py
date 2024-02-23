from pyppeteer_scripts.utils.parseProductData import formatProductNovaScore, formatProductNutriScore, setProductNovaScoreTitle, setProductNutriScoreTitle
from pyppeteer_scripts.utils.productInformationFormat import formatNutritionAndNovaDetails, formatProductId, formatProductName
import logging

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addHandler(logging.StreamHandler())

async def getListOfProductsAndTheirDetails(pageReference: any):
    # wait for the #products_match_all to load and store it in a variable
    await pageReference.waitForSelector("#products_match_all")
    productElements = await pageReference.querySelectorAll("#products_match_all li")
    
    logging.info("----------> Saving all products found ...")
        
    # going throught all the li elements that contains each product and picking the needed information
    listOfAllProducts = []
    for productElements in product_elements:
        logging.info("----------> Parsing all products before returning ...")
        productInfo = {}
        
        try:
            productInfo['id'] = await productElements.querySelectorEval('.list_product_a', '(element) => element.getAttribute("href")')
            productInfo['id'] = formatProductId(productInfo['id'])
        except:
            logging.warning("----------> Wasn't able to get the product id")
            
        try:
            productInfo['name'] = await productElements.querySelectorEval('.list_product_name', '(element) => element.textContent')
            productInfo['name'] = formatProductName(productInfo['name'])
        except:
            logging.warning("-----------> Wasn't able to get the product name")
        
        # going through all the images inside the .list_product_sc div and picking all the titles containing information about nutrition and nova
        try:
            productScoresElement = await productElements.querySelector('.list_product_sc')
        except:
            logging.warning("----------> There was a problem while getting the list of products component")
        
        try:
            productScoreIcons = await productScoresElement.querySelectorAll('.list_product_icons')
        except:
            logging.warning("----------> There was a problem getting the list of images")
            
        productInfo['nutrition'] = {}
        productInfo['nova'] = {}
        i: int = 0
        for icon in productScoreIcons:
            try:
                title = await pageReference.evaluate('(element) => element.getAttribute("title")', icon)
                title = formatNutritionAndNovaDetails(title)
            except:
                logging.warning("----------> There was a problem getting the title")
            if i == 0:
                productInfo['nutrition'][f'score'] = formatProductNutriScore(title)
                productInfo['nutrition'][f'title'] = setProductNutriScoreTitle(title)
            elif i == 1:
                productInfo['nova'][f'score'] = formatProductNovaScore(title)
                productInfo['nova'][f'title'] = setProductNovaScoreTitle(title)
            i += 1
        listOfAllProducts.append(productInfo)
    return listOfAllProducts