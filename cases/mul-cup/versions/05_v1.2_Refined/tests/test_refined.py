import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path('/mnt/data/MUL_v1.2_refined'); HTML=(ROOT/'index.html').read_text()
async def main():
 result=[]
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  for width,height in [(1440,900),(1024,768),(790,900),(390,844),(360,780),(320,720)]:
   page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   await page.evaluate('''() => {const d={}; Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>d[k]??null,setItem:(k,v)=>d[k]=String(v),removeItem:k=>delete d[k]}})}''')
   await page.set_content(HTML,wait_until='load');await page.wait_for_timeout(800)
   row={'width':width,'overflow':await page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth'),'errors':errors.copy(), 'canvas':await page.locator('#product-display canvas').count()}
   if width in [1440,390,320]:
    await page.evaluate("document.querySelectorAll('.reveal').forEach(x=>x.classList.add('is-visible'))")
    await page.screenshot(path=str(ROOT/f'full_{width}.png'),full_page=True,animations='disabled')
    await page.screenshot(path=str(ROOT/f'fold_{width}.png'),full_page=False,animations='disabled')
    await page.locator('#colors').scroll_into_view_if_needed();await page.wait_for_timeout(170)
    await page.locator('#product-display').screenshot(path=str(ROOT/f'stage_clear_{width}.png'),animations='disabled')
    bg=await page.locator('#product-display').evaluate('(el)=>getComputedStyle(el).backgroundColor')
    await page.locator('#colors button[data-color="amber"]').click()
    row['color_text']='앰버' in await page.locator('#color-name').inner_text()
    row['bg_same']=bg==await page.locator('#product-display').evaluate('(el)=>getComputedStyle(el).backgroundColor')
    await page.locator('#product-display').screenshot(path=str(ROOT/f'stage_amber_{width}.png'),animations='disabled')
    canvas=page.locator('#product-display canvas');box=await canvas.bounding_box();sx=box['x']+box['width']*.5;sy=box['y']+box['height']*.5
    await page.mouse.move(sx-55,sy);await page.mouse.down();await page.mouse.move(sx+110,sy,steps=12);await page.mouse.up()
    row['reset_after_drag']=not await page.locator('#rotate-reset').is_hidden()
    await page.locator('#product-display').screenshot(path=str(ROOT/f'stage_rotated_{width}.png'),animations='disabled')
    await page.locator('#rotate-reset').click();row['reset_hidden']=await page.locator('#rotate-reset').is_hidden()
    await canvas.focus();await page.keyboard.press('ArrowRight');row['keyboard_rotation']=not await page.locator('#rotate-reset').is_hidden()
    await page.locator('#section-purchase').click();row['drawer_open']=(await page.locator('#drawer').get_attribute('aria-hidden'))=='false'
    await page.locator('#qty-plus').click();await page.locator('#add-bag').click()
    row['cart_count']=await page.locator('#bag-count').inner_text();row['cart_total']=await page.locator('#bag-total').inner_text()
    await page.keyboard.press('Escape');row['drawer_close']=(await page.locator('#drawer').get_attribute('aria-hidden'))=='true'
    await page.locator('#open-purchase').click();await page.locator('#tab-bag').click();await page.locator('.remove-item').click();row['cart_removed']=await page.locator('#bag-count').inner_text()=='0'
    await page.locator('#close-drawer').click();await page.locator('#faq details').first.locator('summary').click();row['faq']=await page.locator('#faq details').first.evaluate('(el)=>el.open')
    if width<700:
     await page.locator('#menu-toggle').click();row['menu_open']=(await page.locator('#menu-toggle').get_attribute('aria-expanded'))=='true'
   row['errors_after']=errors
   result.append(row)
   await page.close()
  reduced=await browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce')
  await reduced.set_content(HTML,wait_until='load')
  result.append({'reduced_animation':await reduced.locator('.cup-svg').evaluate('(e)=>getComputedStyle(e).animationName')})
  await reduced.add_style_tag(content='html{font-size:200%!important}')
  result.append({'text_200pct_overflow':await reduced.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')})
  await browser.close()
 (ROOT/'test_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
 print(json.dumps(result,ensure_ascii=False,indent=2))
asyncio.run(main())
