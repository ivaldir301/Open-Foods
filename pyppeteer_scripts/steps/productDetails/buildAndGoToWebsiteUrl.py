from pyppeteer_scripts.utils.dateTimeFormatGenerator import generateDateTimeInFormat

options = {
    "WaitUntil": ["load", "domcontentloaded"],
    "timeout": "90000"
}
    
async def buildAndGoToWebsiteUrl(pageReference: any, id: str):
    formatedWebsiteUrl: str = f"https://br.openfoodfacts.org/produto/{id}/"
    print(f"----------> Starting to scrape: at ({generateDateTimeInFormat})")
    print("----------> Formated url for product searching: ", formatedWebsiteUrl)
    print("----------> Waiting for the website to load")    
    try:
        await pageReference.goto(formatedWebsiteUrl, options=options)
    except:
        print("----------> Website didn't load, check the url and their following paramethers")
    print("----------> Website is fully loaded")
    
