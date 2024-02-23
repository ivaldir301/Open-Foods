import logging

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

async def checkForNoProductsFoundError(pageReference: any, browserReference: any):
    try:
        logging.info("----------> Checking if the website returned no products found error")
        errorMessage = await pageReference.querySelectorEval(".if-empty-dnone", "(element) => element.textContent")
        if errorMessage is not None:
            logging.info("----------> The product with the id you specified was not found")
            await browserReference.close()       
            return []
    except:
        logging.warning("----------> Didn't find any errors")