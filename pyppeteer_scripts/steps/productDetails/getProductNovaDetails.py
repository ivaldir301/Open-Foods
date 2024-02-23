async def getProductNovaDetails(pageReference: any, specificProductInfo):
    try:
        novaScoreValue: str = await pageReference.querySelectorEval("#panel_nova > li > a > h4", "(element) => element.textContent")
    except:
        print("----------> Component for retrieving the nova score and title was not found in the page")
        novaScoreValue = "unknown"
    
    storeNovaScore(specificProductInfo, novaScoreValue)
    return specificProductInfo
    
        
def storeNovaScore(specificProductInfo, novaScoreValue):
    if "Alimentos não processados ​​ou minimamente processados" in novaScoreValue:
        specificProductInfo["nova"]["score"] = "1"
        specificProductInfo["nova"]["title"] = novaScoreValue.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    elif "Ingredientes culinários processados" in novaScoreValue:
        specificProductInfo["nova"]["score"] = "2"
        specificProductInfo["nova"]["title"] = novaScoreValue.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    elif "Alimentos processados" in novaScoreValue:
        specificProductInfo["nova"]["score"] = "3"
        specificProductInfo["nova"]["title"] = novaScoreValue.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    elif "Alimentos ultra-processados" in novaScoreValue:
        specificProductInfo["nova"]["score"] = "4"
        specificProductInfo["nova"]["title"] = novaScoreValue.replace("\xa0", "", 5).replace("\n", "", 5).strip("\t").strip()
    return specificProductInfo