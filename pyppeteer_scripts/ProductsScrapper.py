from asyncio import wait
import pyppeteer
from pyppeteer_scripts.utils.productInformationFormat import formatNutritionAndNovaDetails
from pyppeteer_scripts.utils.productInformationFormat import formatProductId
from pyppeteer_scripts.utils.productInformationFormat import formatProductName
from pyppeteer_scripts.configuration.pyppeteerConfigurations import pyppeteer_configurations
from pyppeteer_scripts.utils.parseProductData import formatProductNovaScore, formatProductNutriScore, setProductNovaScoreTitle, setProductNutriScoreTitle

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']

async def getAllProductsFromWebsite(nutriscore: str, nova: int):
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
    options = {
        "WaitUntil": ["load", "domcontentloaded"],
        "timeout": "90000"
    }
    
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
    print("----------> Starting to scrape ...")
    print("----------> Formated url for product searching: ", formatedWebsiteUrl)
    
    print("----------> Waiting for the website to load")    
    await page.goto(formatedWebsiteUrl, options=options)
        
    # verify if the page didn't return no products found
    try:
        print("----------> Checking if the website returned no products found error")
        errorMessage = await page.querySelectorEval(".if-empty-dnone", "(element) => element.textContent")
        if errorMessage is not None:
            await browser.close()       
            return []
    except:
        print("----------> Didn't find any errors")

    # wait for the #products_match_all to load and store it in a variable
    await page.waitForSelector("#products_match_all")
    product_elements = await page.querySelectorAll("#products_match_all li")
    
    print("----------> Saving all products found ...")
        
    # going throught all the li elements that contains each product and picking the needed information
    listOfAllProducts = []
    for product_element in product_elements:
        print("----------> Parsing all products before returning ...")
        product_info = {}
        
        product_info['id'] = await product_element.querySelectorEval('.list_product_a', '(element) => element.getAttribute("href")')
        product_info['name'] = await product_element.querySelectorEval('.list_product_name', '(element) => element.textContent')
                    
        product_info['name'] = formatProductName(product_info['name'])
        product_info['id'] = formatProductId(product_info['id'])
        
        # going through all the images inside the .list_product_sc div and picking all the titles containing information about nutrition and nova
        product_scores_element = await product_element.querySelector('.list_product_sc')
        product_score_icons = await product_scores_element.querySelectorAll('.list_product_icons')
        product_info['nutrition'] = {}
        product_info['nova'] = {}
        i: int = 0
        for icon in product_score_icons:
            title = await page.evaluate('(element) => element.getAttribute("title")', icon)
            title = formatNutritionAndNovaDetails(title)
            if i == 0:
                product_info['nutrition'][f'score'] = formatProductNutriScore(title)
                product_info['nutrition'][f'title'] = setProductNutriScoreTitle(title)
            elif i == 1:
                product_info['nova'][f'score'] = formatProductNovaScore(title)
                product_info['nova'][f'title'] = setProductNovaScoreTitle(title)
            i += 1
        listOfAllProducts.append(product_info)

    print("----------> Operation was succesfull!")
    await browser.close()       
    return listOfAllProducts
   
