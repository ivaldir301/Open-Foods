from pyppeteer_scripts.utils.dateTimeFormatGenerator import generateDateTimeInFormat
import logging

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

options = {
    "WaitUntil": ["load", "domcontentloaded"],
    "timeout": "90000"
}
    
async def buildAndGoToWebsiteUrl(pageReference: any, id: str):
    formatedWebsiteUrl: str = f"https://br.openfoodfacts.org/produto/{id}/"
    logging.info(f"----------> Starting to scrape ...")
    logging.info("----------> Formated url for product searching: ", formatedWebsiteUrl)
    logging.info("----------> Waiting for the website to load")    
    try:
        await pageReference.goto(formatedWebsiteUrl, options=options)
    except:
        logging.warning("----------> Website didn't load, check the url and their following paramethers")
    logging.info("----------> Website is fully loaded")
    
