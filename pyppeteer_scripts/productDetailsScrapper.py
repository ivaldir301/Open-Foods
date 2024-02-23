import pyppeteer
import logging
from pyppeteer_scripts.configuration.pyppeteerConfigurations import pyppeteer_configurations
from pyppeteer_scripts.steps.productDetails.checkForNoProductsFoundError import checkForNoProductsFoundError
from pyppeteer_scripts.steps.productDetails.buildAndGoToWebsiteUrl import buildAndGoToWebsiteUrl
from pyppeteer_scripts.steps.productDetails.getProductNovaDetails import getProductNovaDetails
from pyppeteer_scripts.steps.productDetails.getProductNutritionFactsDetails import getProductNutritionFactsDetails
from pyppeteer_scripts.steps.productDetails.getProductServingSizeAndNutritionDetails import getProductServingSizeAndNutritionDetails
from pyppeteer_scripts.steps.productDetails.getProductTitleQuantAndIngridients import getProductTitleQuantAndIngridients

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addHandler(logging.StreamHandler())

async def getProductWithId(id: str):
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
    
    logging.info("Browser as being setup for a scrape. ENDPOINT-> GET-PRODUCT-DETAILS")
    
    await buildAndGoToWebsiteUrl(page, id) 
    await checkForNoProductsFoundError(page, browser)     
    
    specificProductInfo = {}
    specificProductInfo = await getProductTitleQuantAndIngridients(page, specificProductInfo)  

    specificProductInfo['nutrition'] = {}
    specificProductInfo = await getProductServingSizeAndNutritionDetails(page, specificProductInfo)

    specificProductInfo = await getProductNutritionFactsDetails(page, specificProductInfo)

    specificProductInfo["nova"] = {}
    specificProductInfo = await getProductNovaDetails(page, specificProductInfo)
    
    await browser.close()
    return specificProductInfo

