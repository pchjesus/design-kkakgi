import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
u=(Path('/mnt/data/MUL_v1.2_refined/index.html')).as_uri()
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  c=await b.new_context(viewport={'width':390,'height':844})
  page=await c.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(u)
  await page.evaluate('localStorage.clear()')
  await page.reload()
  await page.locator('#section-purchase').click();await page.locator('#qty-plus').click();await page.locator('#add-bag').click()
  before=await page.locator('#bag-count').inner_text()
  stored=await page.evaluate('localStorage.getItem("mul-demo-bag-v1")')
  await page.reload();after=await page.locator('#bag-count').inner_text()
  print({'page_url':page.url,'before':before,'after_reload':after,'stored':stored,'errors':errors})
  await b.close()
asyncio.run(main())
