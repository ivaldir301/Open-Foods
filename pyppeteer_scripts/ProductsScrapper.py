import pyppeteer
from pyppeteer_scripts.steps.products.buildAndGoToWebsiteUrl import buildAndGoToWebsiteUrl
from pyppeteer_scripts.steps.products.checkForProductNotFoundError import checkForProductNotFoundError
from pyppeteer_scripts.steps.products.getListOfProductsAndTheirDetails import getListOfProductsAndTheirDetails
from pyppeteer_scripts.configuration.pyppeteerConfigurations import pyppeteer_configurations

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']

async def getAllProductsFromWebsite(nutriscore: str, nova: int):
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
   
    await buildAndGoToWebsiteUrl(page, browser, nova, nutriscore)
    await checkForProductNotFoundError(page, browser)

    listOfAllProducts = await getListOfProductsAndTheirDetails(page)

    print("----------> Operation was succesfull!")
    await browser.close()       
    return listOfAllProducts
   
