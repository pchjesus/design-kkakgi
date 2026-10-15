from pathlib import Path
import re
old=Path('/mnt/data/mul-cup-site/index.html').read_text()
sprite=re.search(r'<svg xmlns="http://www.w3.org/2000/svg" width="0".*?</svg>',old,re.S).group(0)
script=re.search(r'<script>\s*(\(\(\)=>.*?</script>)',old,re.S).group(0)
# Clarify version reference to v1.2 in on-page help, selectors/feature set kept unchanged.
script=script.replace("const PRICE=19800,KEY='mul-demo-bag-v1'", "const PRICE=19800,KEY='mul-demo-bag-v1'")
head='''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#1454ec">
<meta name="description" content="MUL 데일리 글라스. 380 mL 물컵의 색상과 구성을 경험하는 인터랙티브 제품 쇼케이스. 가상 상품·결제 없음.">
<title>MUL. | 데일리 글라스 380 mL</title>
<style>'''
css=Path('/mnt/data/MUL_v1.2/styles.css').read_text()
body='''
</style>
</head>
<body>
'''+sprite+'''
<a href="#product" class="skip-link">제품 선택으로 건너뛰기</a>
<div class="notice">MUL STUDIO의 가상 제품 전시입니다. 실제 구매·결제는 지원하지 않습니다.</div>
<header class="site-header" id="top">
 <div class="header-inner wrap">
  <a href="#top" class="brand" aria-label="MUL 처음으로">mul<span>.</span></a>
  <nav class="nav" aria-label="주 메뉴"><a href="#product">제품</a><a href="#philosophy">특징</a><a href="#design">디자인</a><a href="#faq">안내</a></nav>
  <div class="header-actions">
   <button type="button" id="open-bag" class="bag-button" aria-label="데모 장바구니 열기, 현재 0개"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 8h16l-1 12H5L4 8Z M8 9V6a4 4 0 0 1 8 0v3"/></svg><span class="bag-label">장바구니</span><span id="bag-count" class="bag-number">0</span></button>
   <button type="button" class="menu-button" id="menu-toggle" aria-label="메뉴 열기" aria-expanded="false" aria-controls="mobile-menu"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
  </div>
 </div>
 <nav id="mobile-menu" class="mobile-menu" aria-label="모바일 메뉴"><a href="#product">제품</a><a href="#philosophy">특징</a><a href="#design">디자인</a><a href="#faq">안내</a></nav>
</header>
<main>
 <section class="hero" id="product" aria-labelledby="product-heading">
  <div class="product-display" data-tone="clear" id="product-display">
    <div class="stage-top"><span>MUL / OBJECT 01</span><span>THE DAILY GLASS</span></div>
    <div class="stage-watermark" aria-hidden="true">MUL.</div>
    <div class="stage-art">
     <svg class="glass-art" viewBox="0 0 560 680" role="img" aria-label="현재 선택한 색상의 데일리 글라스 일러스트"><use href="#cup-illustration"/></svg>
    </div>
    <div class="stage-base"><span>01 — 03<br>COLOR STUDY</span><span>하나의 형태,<br>세 가지 색.</span></div>
  </div>
  <div class="product-details">
   <div class="product-meta"><span class="meta-dot" aria-hidden="true"></span><span>데일리 컬렉션 / 001</span></div>
   <h1 id="product-heading">데일리<br>글라스<span class="title-period">.</span></h1>
   <p class="subline">380 mL · 유리컵 콘셉트</p>
   <p class="hero-description">매일 물을 마실 때 쓰는 심플한 컵. 형태와 색상을 직접 살펴보고 원하는 조합을 골라보세요.</p>
   <div class="price-line"><strong class="price num" id="unit-price">₩ 19,800</strong><span class="price-note">시연용 가격</span></div>
   <p class="price-info">가상 제품입니다. 용량·재질·가격은 실제 검증된 사양이 아닙니다.</p>
   <div class="product-form">
    <div class="form-title"><span>01 / 색상</span><strong id="color-name" aria-live="polite">클리어 / Clear</strong></div>
    <div class="swatches" role="group" aria-label="컵 색상 선택"><button type="button" class="swatch" data-color="clear" aria-pressed="true" style="--swatch:#d5e8e5"><span class="dot"></span><span>클리어</span></button><button type="button" class="swatch" data-color="amber" aria-pressed="false" style="--swatch:#d8ac76"><span class="dot"></span><span>앰버</span></button><button type="button" class="swatch" data-color="smoke" aria-pressed="false" style="--swatch:#819797"><span class="dot"></span><span>스모크</span></button></div>
    <div class="qty-row"><div class="form-title"><span>02 / 수량</span><span class="qty-limit">최대 10개</span></div><div class="quantity-control" role="group" aria-label="수량 조정"><button type="button" id="qty-minus" aria-label="수량 1개 줄이기" disabled>−</button><output id="qty-output" class="num" aria-live="polite">1</output><button type="button" id="qty-plus" aria-label="수량 1개 늘리기">+</button></div></div>
    <div class="purchase-buttons"><button type="button" class="btn btn-primary" id="add-bag">데모 장바구니 담기 <span aria-hidden="true">↗</span></button><button type="button" id="share-selection" class="icon-button" title="선택한 컵 구성 복사" aria-label="선택한 컵 구성 복사"><svg fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/></svg></button></div>
    <p class="fineprint">실제 주문은 진행되지 않으며, 선택 내용은 이 브라우저에만 저장됩니다.</p>
   </div>
  </div>
 </section>
 <section class="stat-strip" aria-label="제품 요약"><div class="wrap stat-inner"><div><strong>380 <small>mL</small></strong><span>용량(예시)</span></div><div><strong>03</strong><span>선택 가능한 색상</span></div><div><strong>01</strong><span>하나의 기본 형태</span></div><a href="#design" class="stat-link">디자인 살펴보기 <span aria-hidden="true">↘</span></a></div></section>
 <section class="features-section wrap" id="philosophy" aria-labelledby="features-heading">
  <div class="section-head"><div><span class="section-index">01 / DETAILS</span><h2 id="features-heading">일상에 필요한<br>세 가지 디테일</h2></div><p>장식보다는 손에 잡히는 형태, 물을 보여주는 투명함, 매일 사용하기 편안한 인상을 먼저 생각했습니다.</p></div>
  <div class="features" aria-label="제품 디자인 특징">
   <article class="feature"><span class="feature-number">01</span><div class="feature-symbol" aria-hidden="true"><svg fill="none" stroke="currentColor" viewBox="0 0 60 60"><ellipse cx="30" cy="12" rx="18" ry="6"/><path d="M12 12l4 32q14 11 28 0l4-32M16 44q14 9 28 0"/></svg></div><h3>단순한 실루엣</h3><p>눈에 들어오는 요소를 덜고 컵의 기본 형태에 집중한 디자인 콘셉트입니다.</p></article>
   <article class="feature"><span class="feature-number">02</span><div class="feature-symbol" aria-hidden="true"><svg fill="none" stroke="currentColor" viewBox="0 0 60 60"><path d="M8 47 29 7l23 40M17 30h25M30 7v40"/></svg></div><h3>보이는 투명함</h3><p>물의 높이와 빛의 변화를 자연스럽게 보여주는 유리 소재의 인상을 살렸습니다.</p></article>
   <article class="feature"><span class="feature-number">03</span><div class="feature-symbol" aria-hidden="true"><svg fill="none" stroke="currentColor" viewBox="0 0 60 60"><path d="M12 15h36v32H12zM12 29h36M23 15v32"/></svg></div><h3>다양한 공간</h3><p>식탁·책상·선반 어디에 놓아도 과하게 튀지 않는 비례를 목표로 했습니다.</p></article>
  </div>
 </section>
 <section class="editorial" id="design" aria-labelledby="design-heading">
  <div class="editorial-content"><span class="section-index">02 / MATERIAL & COLOR</span><h2 id="design-heading">색이 바뀌면,<br>같은 컵도 다르게.</h2><p>투명한 클리어, 따뜻한 앰버, 차분한 스모크. 아래에서 색상을 선택하면 컵 이미지가 바로 바뀝니다.</p><a href="#product" class="btn btn-light">세 가지 색상 비교하기 <span aria-hidden="true">↗</span></a><div class="editorial-points"><span>동일한 형태</span><span>다른 색상 표현</span><span>콘셉트 시연</span></div></div>
  <div class="editorial-visual"><span class="editorial-kicker">GLASS / MATERIAL STUDY</span><div class="editorial-asset"><svg class="glass-art" viewBox="0 0 560 680" role="img" aria-label="반투명 유리컵의 형태를 보여주는 제품 콘셉트 일러스트"><use href="#cup-illustration"/></svg></div><span class="editorial-caption">투명도와 굴절을 표현한 일러스트</span></div>
 </section>
 <section class="spec-section wrap" aria-labelledby="spec-heading"><div><span class="section-index">03 / PRODUCT NOTE</span><h2 id="spec-heading">제품 정보</h2><p>구매 가능한 실제 제품이 아니라 인터랙션 검증용 콘셉트입니다.</p></div><dl class="spec-list"><div><dt>제품명</dt><dd>데일리 글라스</dd></div><div><dt>용량</dt><dd>380 mL (예시)</dd></div><div><dt>소재</dt><dd>유리 콘셉트 (실측·검증 없음)</dd></div><div><dt>색상</dt><dd>클리어 / 앰버 / 스모크</dd></div><div><dt>가격</dt><dd>₩ 19,800 (시연용)</dd></div></dl></section>
 <section class="faq wrap" id="faq" aria-labelledby="faq-heading"><div><span class="section-index">04 / INFORMATION</span><h2 id="faq-heading">자주 묻는 질문</h2><p class="faq-intro">실제 판매 제품이 아닌 디자인 시연 페이지입니다. 이용 전에 아래 내용을 확인해 주세요.</p></div><div class="faq-list">
  <details><summary>이 컵을 실제로 구매할 수 있나요?</summary><p>현재는 UI/UX 디자인 가이드 적용을 확인하기 위한 가상 브랜드 쇼케이스입니다. 장바구니와 색상 선택은 작동하지만 주문과 결제는 진행되지 않습니다.</p></details>
  <details><summary>색상과 용량은 실제 상품 정보인가요?</summary><p>아니요. 클리어·앰버·스모크 색상 구성, 380 mL 용량 및 가격은 디자인 시연을 위해 설정한 예시입니다. 제조사에서 검증한 사양이 아닙니다.</p></details>
  <details><summary>담아둔 제품은 어디에 저장되나요?</summary><p>선택한 구성은 사용 중인 브라우저의 로컬 저장소에만 보관합니다. 별도의 서버 전송이나 회원 가입이 없으며, 브라우저 데이터 삭제 시 사라질 수 있습니다.</p></details>
  <details><summary>디자인은 어떤 원칙을 따랐나요?</summary><p>Universal Visual Design &amp; UI/UX Guidelines v1.2의 소재 중심 화면, 명확한 정보 위계, 타이포그래피·색상 방향, 목적형 모션, 접근성 기준을 적용했습니다. 제품 이미지는 독립 제작한 SVG 콘셉트 일러스트입니다.</p></details>
 </div></section>
</main>
<footer><div class="wrap"><div class="footer-main"><div><a class="footer-logo" href="#top" aria-label="MUL 맨 위로">mul<span>.</span></a><p>물 한 잔을 위한 제품 콘셉트.</p></div><nav class="footer-menu" aria-label="하단 메뉴"><a href="#top">맨 위로</a><a href="#product">제품</a><a href="#philosophy">특징</a><a href="#faq">안내</a></nav></div><div class="footer-bottom"><span>© 2026 MUL STUDIO — 가상 제품 · 독립 UI/UX 디자인 시연</span><span>실제 판매·배송·결제 없음</span></div></div></footer>
<div class="toast" id="toast" role="status" aria-live="polite" aria-atomic="true"></div>
<div class="backdrop" id="backdrop"></div>
<aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="데모 장바구니" aria-hidden="true" inert><div class="drawer-head"><h2>데모 장바구니 <span id="drawer-count" class="muted num">(0)</span></h2><button type="button" class="close-drawer" id="close-drawer" aria-label="장바구니 닫기">×</button></div><div class="drawer-content" id="drawer-content"></div><div class="drawer-foot" id="drawer-foot" hidden><div class="total"><span>합계 (시연용)</span><span class="num" id="bag-total">₩ 0</span></div><button type="button" class="btn btn-primary" id="copy-bag">장바구니 목록 복사 <span aria-hidden="true">↗</span></button><p>결제 기능은 없습니다. 이 목록은 시연용이며 실제 주문으로 이어지지 않습니다.</p></div></aside>
'''
# original script uses classes open, reveal, all preserved
html=head+css+body+script+'\n</body>\n</html>\n'
Path('/mnt/data/MUL_v1.2/MUL_Cup_v1.2.html').write_text(html)
print('created',len(html),'bytes')
