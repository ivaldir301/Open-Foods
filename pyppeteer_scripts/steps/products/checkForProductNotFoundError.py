async def checkForProductNotFoundError(pageReference: any, browserReference: any):
    # verify if the page didn't return no products found
    try:
        print("----------> Checking if the website returned no products found error")
        errorMessage = await pageReference.querySelectorEval(".if-empty-dnone", "(element) => element.textContent")
        if errorMessage is not None:
            await browserReference.close()       
            return []
    except:
        print("----------> Didn't find any errors")