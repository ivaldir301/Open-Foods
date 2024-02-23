from pyppeteer_scripts.utils.parseProductData import formatProductNovaScore, formatProductNutriScore, setProductNovaScoreTitle, setProductNutriScoreTitle
from pyppeteer_scripts.utils.productInformationFormat import formatNutritionAndNovaDetails, formatProductId, formatProductName

async def getListOfProductsAndTheirDetails(pageReference: any):
    # wait for the #products_match_all to load and store it in a variable
    await pageReference.waitForSelector("#products_match_all")
    product_elements = await pageReference.querySelectorAll("#products_match_all li")
    
    print("----------> Saving all products found ...")
        
    # going throught all the li elements that contains each product and picking the needed information
    listOfAllProducts = []
    for product_element in product_elements:
        print("----------> Parsing all products before returning ...")
        product_info = {}
        
        try:
            product_info['id'] = await product_element.querySelectorEval('.list_product_a', '(element) => element.getAttribute("href")')
            product_info['id'] = formatProductId(product_info['id'])
        except:
            print("----------> Wasn't able to get the product id")
            
        try:
            product_info['name'] = await product_element.querySelectorEval('.list_product_name', '(element) => element.textContent')
            product_info['name'] = formatProductName(product_info['name'])
        except:
            print("-----------> Wasn't able to get the product name")
        
        # going through all the images inside the .list_product_sc div and picking all the titles containing information about nutrition and nova
        try:
            product_scores_element = await product_element.querySelector('.list_product_sc')
        except:
            print("----------> There was a problem while getting the list of products component")
        
        try:
            product_score_icons = await product_scores_element.querySelectorAll('.list_product_icons')
        except:
            print("----------> There was a problem getting the list of images")
            
        product_info['nutrition'] = {}
        product_info['nova'] = {}
        i: int = 0
        for icon in product_score_icons:
            try:
                title = await pageReference.evaluate('(element) => element.getAttribute("title")', icon)
                title = formatNutritionAndNovaDetails(title)
            except:
                print("----------> There was a problem getting the title")
            if i == 0:
                product_info['nutrition'][f'score'] = formatProductNutriScore(title)
                product_info['nutrition'][f'title'] = setProductNutriScoreTitle(title)
            elif i == 1:
                product_info['nova'][f'score'] = formatProductNovaScore(title)
                product_info['nova'][f'title'] = setProductNovaScoreTitle(title)
            i += 1
        listOfAllProducts.append(product_info)
    return listOfAllProducts