from pyppeteer_scripts.utils.dateTimeFormatGenerator import generateDateTimeInFormat

options = {
        "WaitUntil": ["load", "domcontentloaded"],
        "timeout": "90000"
}

async def buildAndGoToWebsiteUrl(pageReference: any, browserReference: any, nova: int, nutriscore: str):
    print(f"----------> Starting to scrape: at ({generateDateTimeInFormat})")
    print("----------> Formated url for product searching: ", formatWebsiteUrl(nova, nutriscore))
    print("----------> Waiting for the website to load") 
    try:   
        await pageReference.goto(formatWebsiteUrl(nova, nutriscore), options=options)
        print("----------> Website loaded successfully!!")
    except:
        print("----------> Error loading the website, check the url and the paramethers passed")
        
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