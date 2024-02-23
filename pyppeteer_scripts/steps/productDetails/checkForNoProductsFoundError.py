async def checkForNoProductsFoundError(pageReference: any, browserReference: any):
    try:
        print("----------> Checking if the website returned no products found error")
        errorMessage = await pageReference.querySelectorEval(".if-empty-dnone", "(element) => element.textContent")
        if errorMessage is not None:
            print("----------> The product with the id you specified was not found")
            await browserReference.close()       
            return []
    except:
        print("----------> Didn't find any errors")