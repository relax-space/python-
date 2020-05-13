# 用pyppeteer登录淘宝
import random
import time
import asyncio
from pyppeteer import launch
from retrying import retry

async def page_evaluate(page):
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

async def taobao_login(username,password):
    browser = await launch({
        'headless': False,
        'executablePath':r'D:\file\chromium\chrome-win32\chrome.exe',
        'userDataDir': r'D:\file\chromium\userData',
        'args': ['–no-sandbox'], 
        'dumpio': True
    })

    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    await page.goto("https://login.taobao.com/member/login.jhtml")
