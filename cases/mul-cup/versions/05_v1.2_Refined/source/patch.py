from pathlib import Path
orig=Path('/mnt/data/MUL_v1.2_reimagined/index.html').read_text()
t=orig
# style overrides right before reduced motion query; lower specificity in contexts handle 420 special
style='''
/* Refinement: neutral gallery, concise copy, lighter section boundary. */
.hero h1 strong::after{border-color:#92c7cb;bottom:-7px;height:8px}
.colors{background:#f6fafb;border-top-color:#e5eff1;border-bottom-color:#e5eff1}
.color-stage{background:#fff;border-color:#dee9ed;cursor:grab;touch-action:pan-y;user-select:none;-webkit-user-select:none;overscroll-behavior:contain}
.color-stage.is-dragging{cursor:grabbing}
.color-stage.rotatable-ready>svg.glass-art{opacity:0;pointer-events:none}
.color-stage.rotatable-ready canvas{position:absolute;inset:0;width:100%;height:100%;z-index:2;display:block;touch-action:pan-y;outline:0}
.color-stage.rotatable-ready canvas:focus-visible{outline:3px solid #1763c6;outline-offset:-6px;border-radius:10px}
.color-stage.color-changed canvas{animation:swap-glass .38s ease}
.color-stage .stage-caption{left:18px;bottom:17px;background:rgba(249,252,252,.92);font-size:.75rem}
.rotate-hint{position:absolute;right:17px;top:16px;z-index:5;color:#5c7883;font-size:.78rem;line-height:1.5;pointer-events:none;display:flex;gap:7px;align-items:center}
.rotate-reset{position:absolute;right:17px;bottom:17px;z-index:5;min-height:39px;padding:7px 13px;border:1px solid #c9dbe2;background:rgba(255,255,255,.95);border-radius:999px;color:#315a70;font-size:.77rem;cursor:pointer}
.rotate-reset:hover{background:#eef7f9}
.rotate-reset:focus-visible{outline:3px solid #1763c6;outline-offset:2px}
.sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
.detail-list p{max-width:36ch;text-wrap:balance;word-break:keep-all;overflow-wrap:break-word}
.closing{padding:22px 0;background:#e7f3f5;border-block:1px solid #d2e4e8;text-align:center}
.closing .container{display:flex;align-items:center;justify-content:center;gap:18px}
.closing .small-mark{margin:0;width:15px;height:22px;color:#5d9eb3;flex:none}
.closing h2{font-size:.95rem;font-weight:550;line-height:1.4;letter-spacing:-.025em;margin:0;color:#3c697b}
.closing p{display:none}
@media(max-width:420px){.closing{padding-block:20px}.color-stage .stage-caption{left:12px;bottom:13px;max-width:180px;font-size:.68rem}.rotate-reset{bottom:12px;right:12px}.rotate-hint{top:12px;right:12px;font-size:.7rem}}
'''
t=t.replace('@media(prefers-reduced-motion:reduce){',style+'\n@media(prefers-reduced-motion:reduce){')
old='<div class="color-stage reveal" id="product-display" data-tone="clear"><svg class="glass-art" viewBox="0 0 560 680" role="img" aria-label="선택된 클리어 색상의 MUL 데일리 글라스 콘셉트 컵"><use href="#cup-illustration"/></svg><span class="stage-caption">고정된 배경에서 컵 색상 비교</span></div>'
new='<div class="color-stage reveal" id="product-display" data-tone="clear"><svg class="glass-art" viewBox="0 0 560 680" role="img" aria-label="선택된 클리어 색상의 MUL 데일리 글라스 콘셉트 컵"><use href="#cup-illustration"/></svg><span class="rotate-hint" aria-hidden="true">↔ 드래그하여 회전</span><button class="rotate-reset" type="button" id="rotate-reset" hidden>각도 초기화 ↺</button><span class="stage-caption">컵의 색과 각도를 살펴보세요</span><span id="rotation-status" class="sr-only" aria-live="polite"></span></div>'
assert old in t
t=t.replace(old,new)
t=t.replace('모양과 배경은 그대로 두고, 컵의 색만 바꿔보세요. 다른 색이 만드는 인상을 비교할 수 있습니다.','같은 배경에서 세 가지 컵 색을 비교해 보세요. 컵을 드래그하면 다른 각도도 볼 수 있어요.')
t=t.replace('투명한 소재의 인상을 보여주는 빛과 그림자를 일러스트에 담았습니다.','빛이 통과하며 생기는 부드러운 그림자를 담았습니다.')
t=t.replace('반듯한 입구와 완만하게 좁아지는 윤곽을 기본 형태로 삼았습니다.','반듯한 입구와 부드럽게 좁아지는 곡선.')
t=t.replace('클리어, 앰버, 스모크. 같은 모양을 서로 다른 인상으로 살펴보세요.','같은 형태에도 색에 따라 분위기가 달라집니다.')
t=t.replace('<section class="closing" aria-labelledby="closing-title"><div class="container reveal"><svg class="small-mark" viewBox="0 0 24 34" aria-hidden="true"><path d="M12 2C9 9 3 15 3 21a9 9 0 0 0 18 0C21 15 15 9 12 2Z" fill="currentColor"/></svg><h2 id="closing-title">오늘도, 물 한 잔.</h2><p>매일의 물컵을 생각하는 작은 디자인 실험.</p><a class="link-secondary" href="#colors">다른 색도 살펴보기 ↗</a></div></section>','<section class="closing" aria-labelledby="closing-title"><div class="container"><svg class="small-mark" viewBox="0 0 24 34" aria-hidden="true"><path d="M12 2C9 9 3 15 3 21a9 9 0 0 0 18 0C21 15 15 9 12 2Z" fill="currentColor"/></svg><h2 id="closing-title">오늘도, 물 한 잔.</h2></div></section>')
# renderer see below
renderer=Path('/mnt/data/MUL_v1.2_refined/renderer_fragment.js').read_text()
mark="function setQty(n){"
assert mark in t
t=t.replace(mark,renderer+'\n'+mark)
# integrate with setColor
part="const stage=$('product-display');stage.dataset.tone=color;stage.style.setProperty('--tint',info.tint);stage.querySelector('svg').setAttribute('aria-label',`${info.name} 색상 MUL 데일리 글라스 콘셉트 컵`);"
assert part in t
t=t.replace(part,part+"\n if(rotator)rotator.setTint(info.tint,info.name);")
# init rotation on init, before setColor
init='readBag();setColor(\'clear\');setQty(1);updateCount();'
assert init in t
t=t.replace(init,"rotator=makeRotator();"+init)
# ensure animation relabel after adding canvas
Path('/mnt/data/MUL_v1.2_refined/index.html').write_text(t)
print('wrote', len(t))
