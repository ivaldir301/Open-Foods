import logging

options = {
        "WaitUntil": ["load", "domcontentloaded"],
        "timeout": "90000"
}

logging.basicConfig(
        filename="pyppeteer_scripts/logs/scrapping.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

async def buildAndGoToWebsiteUrl(pageReference: any, browserReference: any, nova: int, nutriscore: str):
    logging.info(f"----------> Starting to scrape ...")
    print("----------> Formated url for product searching: ", str(formatWebsiteUrl(nova, nutriscore)))
    logging.info("----------> Waiting for the website to load") 
    try:   
        await pageReference.goto(formatWebsiteUrl(nova, nutriscore), options=options)
        logging.info("----------> Website loaded successfully!!")
    except:
        logging.warning("----------> Error loading the website, check the url and the paramethers passed")
        
def formatWebsiteUrl(nova: int, nutriscore: str) -> str:
    websiteUrl: str = ""
    if nova == 1:
        websiteUrl = "https://br.openfoodfacts.org/nova-group/1-alimentos-nao-processados-ou-minimamente-processados"
    elif nova == 2:
        websiteUrl = "https://br.openfoodfacts.org/nova-group/2-Ingredientes-culinários-processados"    
    elif nova == 2:
        websiteUrl = "https://br.openfoodfacts.org/nova-group/3-Alimentos-processados"
    elif nova == 3:
        websiteUrl = "https://br.openfoodfacts.org/nova-group/4-Alimentos-ultra-processados"
    formatedWebsiteUrl = websiteUrl + "?nutriscore_score=" + nutriscore
    return formatedWebsiteUrl