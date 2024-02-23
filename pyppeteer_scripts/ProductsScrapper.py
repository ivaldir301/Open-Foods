import pyppeteer
import logging
from pyppeteer_scripts.steps.products.buildAndGoToWebsiteUrl import buildAndGoToWebsiteUrl
from pyppeteer_scripts.steps.products.checkForProductNotFoundError import checkForProductNotFoundError
from pyppeteer_scripts.steps.products.getListOfProductsAndTheirDetails import getListOfProductsAndTheirDetails
from pyppeteer_scripts.configuration.pyppeteerConfigurations import pyppeteer_configurations

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addHandler(logging.StreamHandler())

async def getAllProductsFromWebsite(nutriscore: str, nova: int):
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
    
    logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Browser as being setup for a scrape. ENDPOINT-> GET-ALL-PRODUCTS")
   
    await buildAndGoToWebsiteUrl(page, browser, nova, nutriscore)
    await checkForProductNotFoundError(page, browser)

    listOfAllProducts = await getListOfProductsAndTheirDetails(page)

    logging.info("----------> Operation was succesfull!")
    await browser.close()       
    return listOfAllProducts
   
