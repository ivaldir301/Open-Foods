import asyncio
import pyppeteer
from configuration.pyppeteerConfigurations import pyppeteer_configurations

chromiunMode = pyppeteer_configurations['browserConfigurations']['headless']
browserArgs = pyppeteer_configurations['browserConfigurations']['args']

websiteUrl = pyppeteer_configurations['websiteConfigurations']['url']

async def main():
    browser = await pyppeteer.launch({"headless": chromiunMode, "args": [browserArgs]})
    page = await browser.newPage()
    await page.goto(websiteUrl)
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()   
    
asyncio.get_event_loop().run_until_complete(main())
