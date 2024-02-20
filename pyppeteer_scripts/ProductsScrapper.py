import asyncio
import pyppeteer
from pyppeteer_scripts.utils.productInformationFormat import formatNutritionAndNovaDetails
from pyppeteer_scripts.utils.productInformationFormat import formatProductId
from pyppeteer_scripts.utils.productInformationFormat import formatProductName
from pyppeteer_scripts.configuration.pyppeteerConfigurations import pyppeteer_configurations

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']
websiteUrl = pyppeteer_configurations['websiteConfigurations']['url']

async def getAllProductsFromWebsite():
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
    options = {
        "WaitUntil": "load",
        "timeout": 0
    }
    
    await page.goto(websiteUrl, options=options)

    # wait for the #products_match_all to load and store it in a variable
    await page.waitForSelector("#products_match_all")
    product_elements = await page.querySelectorAll("#products_match_all li")
           
    # going throught all the li elements that contains each product and picking the needed information
    listOfAllProducts = []
    for product_element in product_elements:
        product_info = {}
        
        product_info['name'] = await product_element.querySelectorEval('.list_product_name', '(element) => element.textContent')
        product_info['id'] = await product_element.querySelectorEval('.list_product_a', '(element) => element.getAttribute("href")')
                    
        product_info['name'] = formatProductName(product_info['name'])
        product_info['id'] = formatProductId(product_info['id'])
        
        # going through all the images inside the .list_product_sc div and picking all the titles containing information about nutrition and nova
        product_scores_element = await product_element.querySelector('.list_product_sc')
        product_score_icons = await product_scores_element.querySelectorAll('.list_product_icons')
        product_info['scores'] = {}
        i: int = 0
        for icon in product_score_icons:
            title = await page.evaluate('(element) => element.getAttribute("title")', icon)
            title = formatNutritionAndNovaDetails(title)
            if i == 0:
                product_info['scores'][f'nutrition'] = title
            elif i == 1:
                product_info['scores'][f'nova'] = title
            elif i == 2:
                product_info['scores'][f'eco'] = title
            i += 1
        listOfAllProducts.append(product_info)

    await browser.close()       
    return listOfAllProducts
    
scrappedProducts = asyncio.get_event_loop().run_until_complete(getAllProductsFromWebsite())
print(scrappedProducts)
