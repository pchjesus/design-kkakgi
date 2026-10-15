import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
P=Path('/mnt/data/MUL_v1.2_reimagined'); H=(P/'index.html').read_text()
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'],headless=True)
  page=await browser.new_page(viewport={'width':1440,'height':900})
  await page.evaluate("""() => {const d={'mul-demo-bag-v1':'[{"color":"smoke","qty":3}]'};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k]}})}""")
  await page.set_content(H,wait_until='load')
  await page.wait_for_timeout(250)
  print('legacy storage restores smoke 3:',await page.locator('#bag-count').inner_text())
  await page.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('is-visible'))")
  for color in ['clear','amber','smoke']:
   await page.locator(f'#colors button[data-color="{color}"]').click()
   await page.wait_for_timeout(150)
   await page.locator('#product-display').screenshot(path=str(P/f'stage_{color}.png'),animations='disabled')
  await page.locator('#section-purchase').click()
  await page.screenshot(path=str(P/'purchase_drawer.png'),animations='disabled')
  print('storage now:',await page.evaluate("localStorage.getItem('mul-demo-bag-v1')"))
  await page.set_content(H,wait_until='load')
  print('stored re-render:',await page.locator('#bag-count').inner_text())
  await browser.close()
asyncio.run(main())
