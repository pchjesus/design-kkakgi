import asyncio, json
from playwright.async_api import async_playwright
HTML=open('/mnt/data/MUL_v1.2/MUL_Cup_v1.2.html').read()
async def test():
 results=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
  for w,h in [(1440,900),(1024,768),(790,900),(390,844),(360,780),(320,720)]:
   page=await browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
   errors=[]
   page.on('pageerror',lambda err:errors.append(str(err)))
   await page.evaluate("""() => { const data={}; Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>data[k]??null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>delete data[k],clear:()=>Object.keys(data).forEach(k=>delete data[k])}})}""")
   await page.set_content(HTML, wait_until='load')
   await page.wait_for_timeout(800)
   measure=await page.evaluate('''() => ({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth,heading:getComputedStyle(document.querySelector('h1')).fontFamily,primary:getComputedStyle(document.querySelector('#add-bag')).backgroundColor, motion: window.matchMedia('(prefers-reduced-motion:reduce)').matches})''')
   row={'viewport':w,'overflow':measure['scroll']-measure['client'],'errors':errors,'font':measure['heading']}
   if w in (1440,390,320):
    await page.evaluate("document.querySelectorAll('.reveal-item').forEach(e=>e.classList.add('is-visible'))")
    await page.screenshot(path=f'/mnt/data/MUL_v1.2/preview_{w}.png',full_page=True,animations='disabled')
    await page.screenshot(path=f'/mnt/data/MUL_v1.2/above_fold_{w}.png',full_page=False,animations='disabled')
   # all interactive regressions across desktop & mobile width 390 and smallest 320
   if w in (1440,390,320):
    await page.locator('button[data-color="amber"]').click()
    row['tone_changes']=await page.locator('#product-display').get_attribute('data-tone')=='amber'
    await page.locator('#qty-plus').click()
    row['qty_inc']=(await page.locator('#qty-output').inner_text())=='2'
    await page.locator('#add-bag').click()
    row['badge_update']=(await page.locator('#bag-count').inner_text())=='2'
    await page.set_content(HTML, wait_until='load')
    row['persist_after_rerender']=(await page.locator('#bag-count').inner_text())=='2'
    await page.locator('#open-bag').click()
    row['bag_open']=await page.locator('#drawer').get_attribute('aria-hidden')=='false' and await page.locator('#bag-total').inner_text()=='₩ 39,600'
    await page.keyboard.press('Escape')
    row['esc_closes']=await page.locator('#drawer').get_attribute('aria-hidden')=='true'
    await page.locator('#open-bag').click()
    await page.locator('.remove-button').click()
    row['remove']=await page.locator('#drawer-count').inner_text()=='(0)'
    await page.locator('#close-drawer').click()
    await page.locator('.faq details').first.locator('summary').click()
    row['faq_works']=await page.locator('.faq details').first.evaluate('(e)=>e.open')
    if w<760:
     await page.locator('#menu-toggle').click()
     row['mobile_nav']=await page.locator('#menu-toggle').get_attribute('aria-expanded')=='true'
     await page.locator('#mobile-menu a').first.click()
     row['menu_closes']=await page.locator('#menu-toggle').get_attribute('aria-expanded')=='false'
   results.append(row)
   await page.close()
  # reduced motion option
  page=await browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce')
  await page.set_content(HTML)
  results.append({'reduced_motion':await page.evaluate("getComputedStyle(document.querySelector('.stage-art .glass-art')).animationName")})
  # try 200% text style injection and test overflow
  await page.add_style_tag(content='html {font-size:200% !important}')
  results.append({'200pct_root_text_overflow':await page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')})
  await browser.close()
  print(json.dumps(results,ensure_ascii=False,indent=2))
  open('/mnt/data/MUL_v1.2/test_results.json','w').write(json.dumps(results,ensure_ascii=False,indent=2))
asyncio.run(test())
