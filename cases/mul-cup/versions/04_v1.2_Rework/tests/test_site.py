import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
BASE=Path('/mnt/data/MUL_v1.2_reimagined')
HTML=(BASE/'index.html').read_text()
async def main():
 result=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  for width,height in [(1440,900),(1024,768),(790,900),(700,840),(390,844),(360,780),(320,720)]:
   page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   errors=[]
   page.on('pageerror',lambda ex:errors.append(str(ex)))
   await page.evaluate("""() => {const data={}; Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>data[k]??null,setItem:(k,v)=>{data[k]=String(v)},removeItem:k=>delete data[k],clear:()=>Object.keys(data).forEach(k=>delete data[k])}})}""")
   await page.set_content(HTML,wait_until='load')
   navigation='set_content_with_mock_storage'
   await page.wait_for_timeout(330)
   r={'viewport':width,'navigation':navigation,'overflow':await page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth'),'errors':errors}
   if width in [1440,390,320]:
    await page.evaluate("document.querySelectorAll('.reveal').forEach(x=>x.classList.add('is-visible'))")
    await page.screenshot(path=str(BASE/f'preview_{width}.png'),full_page=True,animations='disabled')
    await page.screenshot(path=str(BASE/f'above_fold_{width}.png'),full_page=False,animations='disabled')
    orig=await page.locator('#product-display').evaluate('(el)=>getComputedStyle(el).backgroundImage')
    await page.locator('#colors .swatch[data-color="amber"]').click()
    r['color_change']=(await page.locator('#color-name').inner_text()).startswith('앰버')
    r['static_background']=orig==await page.locator('#product-display').evaluate('(el)=>getComputedStyle(el).backgroundImage')
    r['changed_tint']=await page.locator('#product-display').evaluate('(el)=>el.style.getPropertyValue("--tint")')
    await page.locator('#section-purchase').click()
    r['drawer_open']=(await page.locator('#drawer').get_attribute('aria-hidden'))=='false'
    r['price_deferred']=await page.locator('.purchase-info strong').inner_text()=='₩ 19,800'
    r['sync_color']=await page.locator('#drawer-color-name').inner_text()=='앰버'
    await page.locator('#qty-plus').click()
    r['quantity']=(await page.locator('#qty-output').inner_text())=='2'
    await page.locator('#add-bag').click()
    r['bag_count']=await page.locator('#bag-count').inner_text()=='2'
    r['total']=await page.locator('#bag-total').inner_text()=='₩ 39,600'
    await page.keyboard.press('Escape')
    r['escape_close']=(await page.locator('#drawer').get_attribute('aria-hidden'))=='true'
    await page.locator('#open-purchase').click()
    await page.locator('#tab-bag').click()
    await page.locator('.remove-item').click()
    r['remove']=await page.locator('#bag-count').inner_text()=='0'
    await page.locator('#close-drawer').click()
    await page.locator('#faq details').first.locator('summary').click()
    r['faq']=await page.locator('#faq details').first.evaluate('(el)=>el.open')
    if width<701:
     await page.locator('#menu-toggle').click()
     r['menu_open']=(await page.locator('#menu-toggle').get_attribute('aria-expanded'))=='true'
     await page.locator('#mobile-menu a').first.click()
     r['menu_close']=(await page.locator('#menu-toggle').get_attribute('aria-expanded'))=='false'
   result.append(r)
   await page.close()
  reduced=await browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce')
  await reduced.set_content(HTML)
  result.append({'reduced_motion_animation':await reduced.locator('.cup-svg').evaluate('(el)=>getComputedStyle(el).animationName')})
  await reduced.add_style_tag(content='html{font-size:200%!important}')
  result.append({'text_200pct_overflow':await reduced.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')})
  await reduced.screenshot(path=str(BASE/'preview_200pct.png'),full_page=False,animations='disabled')
  await browser.close()
 (BASE/'test_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
 print(json.dumps(result,ensure_ascii=False,indent=2))
asyncio.run(main())
