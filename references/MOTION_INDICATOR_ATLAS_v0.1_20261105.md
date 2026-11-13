# 디자인 깎기 — UI 인디케이터·마이크로인터랙션 아틀라스 v0.1

> 조사일 2026-11-05 · 상태 **RESEARCH DRAFT / 레퍼런스** · 현행 기준 Universal Visual Design & UI/UX Guidelines **v1.3 APPROVED**
>
> 범위: 사용자 제공 9종 인디케이터의 의미·구현·실사용 패턴, 확장 마이크로인터랙션 18종, 공개 자료실·기술 선택·접근성·실험 계획. **원본 이미지/영상/타사 예제 코드는 업로드하지 않는다.** 기존 앱·사이트·범용 지침 변경 및 배포 승인 아님.
>
> 근거 코드: [S] 외부 공식 문서 또는 표준 설명 · [D] 공개 예제/동작 샘플의 존재와 설명 · [I] 디자인 깎기에서 시험할 가설/적용 예시 · [NOT RUN] 실물 조작/프로덕션 테스트 미실시. 원본 소셜 영상의 캡처에서 계정이 @uxwoodytips로 보이나 원본 URL·제작자·모션 동작은 미확인.

> **후속 데이터 시각화와 비교 (2026-11-13):** [SRC-25 데이터 시각화·SRC-26 검색 UX](UI_DATA_VISUALIZATION_SEARCH_ATLAS_v0.1_20261113.md)에서 **Progress ring vs Donut vs Gauge**, **KPI 카드 vs 차트**의 데이터 의미·분모·상태 정확성을 보강한다. 본 문서의 기존 9종/확장 18종 집계는 작성 당시 기준으로 유지한다.

## 1. 핵심 발견 — 형태가 비슷해도 데이터 의미는 다르다

| 정보 종류 | 원본 9종 | 사용자에게 전할 정보 | 설계의 금기 |
|---|---|---|---|
| 작업 진행 | 01 Progress bar, 06 Progress ring | 처리한 작업량 또는 처리 중임 | 근거 없는 퍼센트·허위 완료 |
| 단계·위치 | 02 Step, 03 Page, 08 Tab | 현재 순서·선택한 위치 | 선택 상태와 완료 상태를 혼동 |
| 콘텐츠 소비 위치 | 04 Story, 05 Scroll | 전환까지 남은 시간 또는 화면 스크롤 위치 | 시청·독해 완료로 주장 |
| 범위 안의 값 평가 | 07 Strength meter | 측정/평가값·권장 수준 | 작업 진행률과 혼동 |
| 운영체제 전용 | 09 Home indicator | OS 시스템 제스처 영역 | 웹앱이 OS 동작 복제 |

**[S]** HTML progress는 작업 완료 정도를, HTML meter는 알려진 범위 안의 수치를 의미한다. WAI-ARIA Meter Pattern 역시 meter에 다운로드 완료율 같은 progress를 쓰지 말라고 명시한다. (MDN, n.d.; W3C WAI, n.d.)

## 2. 원본 9종에 대한 구현·활용 레퍼런스

### 01 — Progress bar / 프로그레스 바

- **[S] 사용법:** 분모와 실제 처리량이 알려졌을 때 결정형(Determinate), 예측 불가일 때 비결정형(Indeterminate). 예: 파일 4/10 업로드. 분모가 바뀌는 작업은 값 계산 방식을 문서화한다.
- **[I] 형태/모션:** 짧고 명확한 선형 트랙 + 처리한 개수/상태 설명. 파란 바의 길이는 진짜 데이터와 연동. 실패·취소·재시도 때도 UI 상태를 진실하게 표시.
- **구현:** 네이티브 HTML progress 요소, React Aria ProgressBar, Radix Progress, shadcn Progress, Material Web Linear progress. CSS/JS/Motion은 시각적 표시를 덧씌울 뿐 처리상태의 근원은 별도.
- **금기:** 처리량을 모르면서 90%까지 자동 증가시키기, 실제 실패했는데 체크 표시.
- **바로 보기:** https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress · https://react-aria.adobe.com/ProgressBar · https://www.radix-ui.com/primitives/docs/components/progress · https://www.carbondesignsystem.com/building-blocks/core/components/progress-bar/guidelines

### 02 — Step indicator / 스텝 인디케이터

- **[S] 사용법:** 선형 다단계 작업에서 완료·현재·예정·오류·비활성 단계를 명확하게 나눔. Carbon은 단계가 너무 적거나, 순서가 자유롭거나, 조건에 따라 단계 개수가 달라질 때 적합하지 않을 수 있다고 설명.
- **[I] 활용 예:** 가입/서류·장기 양식/교육 단계. 순차형 교육 시나리오의 4단계라는 **가상 적용 예**가 될 수 있으나 현재 사용자 앱에 구현되어 있다고 주장하지 않음.
- **구현:** 의미 있는 순서 목록(ol)과 라벨, 현재 항목의 aria-current="step"; Carbon Progress Indicator / Atlassian Progress Tracker. 실제 상태 모델(complete/current/blocked/error)을 먼저 정의.
- **금기:** 현재 선택한 단계 = 실제 완료로 오인, 다음으로 갈 수 없는 단계가 버튼처럼 보임.
- **바로 보기:** https://www.carbondesignsystem.com/building-blocks/core/components/progress-indicator/guidelines · https://atlassian.design/components/progress-tracker/ · https://component.gallery/components/progress-indicator/

### 03 — Page indicator / 페이지 인디케이터

- **[S] 사용법:** 순서 있는 같은 수준의 페이지/슬라이드/온보딩. Apple은 Page Controls를 평면적인 페이지 목록용으로 소개하며 복잡한 계층 탐색에는 다른 방식 권장.
- **[I] 형태/모션:** 점 또는 짧은 알약 모양의 현재 페이지 강조. 페이지가 많으면 모든 점을 늘어놓기보다 몇 번째 페이지인지 문자로도 제공.
- **구현:** 실제 slideIndex를 단일 원천으로 관리하고 점의 활성 상태·콘텐츠를 동기화. 점을 누를 수 있다면 이름이 있는 버튼/탭으로 제공. Motion Carousel·Embla 등 참조.
- **금기:** 자동 진행하지만 멈출 수 없는 슬라이드, 포커스를 받으면 계속 바뀌는 슬라이드.
- **바로 보기:** https://developer.apple.com/design/human-interface-guidelines/page-controls · https://www.w3.org/WAI/ARIA/apg/patterns/carousel/ · https://motion.dev/docs/react-carousel

### 04 — Story progress / 스토리 진행률

- **[S/I] 의미:** 여러 장면 중 '각 장면의 남은 전환 시간'을 나타내는 분절된 바. 읽기 완료/학습 완료의 증거는 아님.
- **[I] 사용 맥락:** 짧은 제품 소개, 사진 쇼케이스, 체험형 온보딩. 의료 교육·안전 결정처럼 사용자 속도가 중요한 곳에는 무조건 자동 진행하는 방식이 부적절할 수 있음.
- **구현:** activeIndex + elapsedMs + durationMs + paused/playing + loading을 분리. 동영상이라면 실제 미디어 재생시각/길이와 동기화. Embla Autoplay의 pause/play/timeUntilNext와 상태 이벤트를 참고.
- **금기:** 사용자가 화면을 나갔는데 타이머가 계속 돌아감, 키보드 초점/읽기 중 자동으로 다음 장면으로 넘어감, 정지/재시작 수단 누락. W3C APG Carousel 및 WCAG Pause·Stop·Hide 기준 검토.
- **바로 보기:** https://www.embla-carousel.com/docs/plugins/autoplay · https://www.w3.org/WAI/ARIA/apg/patterns/carousel/ · https://www.w3.org/WAI/WCAG22/quickref/#pause-stop-hide

### 05 — Scroll progress / 스크롤 진행률

- **[S] 의미:** 스크롤 컨테이너의 현재 위치를 보여줌. 스크롤한 정도 ≠ 본문을 읽거나 이해한 정도.
- **[I] 사용 맥락:** 긴 블로그 글, 논문 리뷰, 설명서. 짧은 고정 화면에 굳이 도입하지 않음.
- **구현 A:** CSS Scroll-driven Animations의 animation-timeline: scroll(root) 방식. MDN은 2026년 10월부터 관련 기능을 Baseline 2026 신규 지원으로 표시하나 구형 브라우저 대비 필요.
- **구현 B:** JS가 scrollTop/(scrollHeight-clientHeight)를 계산해 0~1 범위로 제한; 글/이미지 지연 로딩과 크기 변화, 다중 스크롤 컨테이너, 스크롤 불필요 시 분모 0을 처리.
- **금기:** 스크롤 100%를 학습 완료 체크·과제 승인으로 표시.
- **바로 보기:** https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations · https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll · https://developer.chrome.com/docs/css-ui/scroll-driven-animations

### 06 — Progress ring / 원형 진행률

- **[S] 의미:** 선형 프로그레스 바와 동일하게 작업의 진행을 알리되 작은 둥근 영역에 표현.
- **[I] 사용 맥락:** 작은 상태 카드나 단일 작업 요약. 값 여러 개를 비교하거나 정확한 퍼센트 읽기가 핵심이면 막대와 원형을 동일 데이터로 A/B 비교.
- **구현:** SVG circle의 stroke-dashoffset, CSS conic-gradient(보조 시각 표현), React Aria ProgressCircle, Material Web Circular progress. 접근 가능한 상태 이름과 값 별도.
- **금기:** 원형이 예쁘다는 이유로 정확한 진행량과 동떨어진 반복 회전, 링 안의 작은 글자에만 의존.
- **바로 보기:** https://react-aria.adobe.com/ProgressBar · https://material-web.dev/components/progress/

### 07 — Strength meter / 강도 표시기

- **[S] 의미:** 일정 범위에 있는 입력/측정값의 평가. HTML meter 또는 ARIA role=meter가 맞는 개념이며 progressbar와 다름.
- **[I] 사용 맥락:** 비밀번호 강도, 데이터 용량, 소진율, 기타 기준이 명확한 값. 비밀번호 평가 규칙 자체가 부정확하다면 UI가 좋아도 신뢰할 수 없음.
- **구현:** HTML meter min/max/low/high/optimum/value; React Aria Meter. 4칸 세그먼트 디자인을 쓰더라도 '약함/보통/강함' 설명과 조치를 함께 제공.
- **금기:** 색상(초록/빨강)만으로 평가, 실제 보안을 인증하듯 '완전히 안전함' 표시.
- **바로 보기:** https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter · https://www.w3.org/WAI/ARIA/apg/patterns/meter/ · https://react-aria.adobe.com/Meter

### 08 — Tab indicator / 탭 인디케이터

- **[S] 의미:** 관련 콘텐츠를 동등한 탭으로 나눠 현재 탭을 표시. 탭은 상위 내비게이션, 페이지 인디케이터, 세그먼트 컨트롤과 구별해서 사용.
- **[I] 활용 예:** '요약 / 비교 / 상세', '설명 / 도식 / 퀴즈'처럼 내용 범위가 분명한 자료를 전환하는 인터페이스.
- **구현:** W3C tablist/tab/tabpanel, aria-selected와 키보드 화살표 탐색. React Aria/Material Tabs 같은 접근 가능한 기반에 Motion shared layout(layoutId) 방식으로 활성 밑줄/알약을 부드럽게 이동시키는 예.
- **금기:** 선택 표시만 움직이고 실제 콘텐츠와 상태가 불일치, 현재 선택이 색 변화에만 의존, 과도한 모션 때문에 재선택이 느림.
- **바로 보기:** https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ · https://material-web.dev/components/tabs/ · https://motion.dev/examples/react-smooth-tabs

### 09 — Home indicator / 시스템 홈 인디케이터

- **[S] 의미:** 네이티브 모바일 시스템의 제스처 영역·핸들. 9종 중 유일하게 앱이 임의로 다시 만드는 일반적 UI 요소가 아님.
- **구현/설계:** Android System Bars와 WindowInsets, Apple Safe Area를 확인하고 하단 버튼·탭 바·모달 시트가 제스처 영역을 침범하지 않게 배치. 웹/PWA에서 임의로 OS 제스처를 구현하거나 홈 핸들을 복제하지 않는다.
- **금기:** 스크린샷의 막대만 따라 그려 시스템 탐색 구현이라고 주장하거나 터치 타깃을 제스처 영역에 겹치게 배치.
- **바로 보기:** https://developer.android.com/design/ui/mobile/guides/foundations/system-bars · https://developer.android.com/develop/ui/views/layout/insets · https://developer.apple.com/design/human-interface-guidelines/layout

## 3. 9종 밖에서 추가로 수집할 18개 마이크로인터랙션

| 추가 유형 | 주요 역할·적합성 | 유의점 |
|---|---|---|
| 10 Spinner / Inline loading | 짧은 비동기 처리 중 | 완료율이 없음을 정직하게 보여주기 |
| 11 Skeleton / Progressive loading | 카드·목록 구조 로딩 | 과도한 shimmer·엉뚱한 레이아웃 |
| 12 Pending → Success/Error 버튼 | 제출·다운로드 결과 | 실제 성공 확인 전 체크표시 금지 |
| 13 Toast / Snackbar | 비차단 안내 | 필수 오류를 사라지는 메시지로만 처리 금지 |
| 14 Undo / Revert | 조작 실행 취소 | 실제 되돌리기 가능성과 일치 |
| 15 Auto-save status | 저장 중/저장됨/오류 | 저장 요청 ≠ 영구 저장 확인 |
| 16 Inline validation | 입력 형식/오류/완료 | 색·흔들림에만 의존하지 않기 |
| 17 Toggle / Switch feedback | 켜짐/꺼짐/실제 설정 반영 | 서버 실패 시 복구 |
| 18 Hover / Focus / Press | 조작 가능·활성 상태 | 터치·키보드 대체 동작 |
| 19 Hold to confirm | 위험 작업 재확인 | 접근 가능한 대체 수단 필요 |
| 20 Accordion | 열림/닫힘·상세 설명 | 열림 상태·초점 이동 |
| 21 Bottom sheet / Dialog | 일시적 작업·전환 | 닫기·초점 복귀 |
| 22 Shared element transition | 공간 사이 연결성 | 크고 긴 이동의 피로 |
| 23 Pull to refresh | 콘텐츠 재조회 | 갱신 실패·오프라인 |
| 24 Swipe to dismiss | 항목 숨김/삭제 | 우발 삭제·키보드 대안 |
| 25 Drag to reorder | 순서 변경 | 드롭 표적·키보드 대안 |
| 26 Number/data change | 수치의 변화 | 값 원인과 상태 보존 |
| 27 Animated icon/celebration | 감성적 피드백/완료 인상 | 반복 과잉·과업 방해 |

**[D]** IBM Carbon의 Loading/Inline Loading, Motion Examples의 Loading·Navigation·Carousel·Scroll·Toast·Slider·Swipe, Rive의 인터랙티브 버튼/상태 머신/교육용 그래픽, React Aria의 제스처·탭 예시에서 관련 자료를 확인했다. 단일 패턴의 구현 예시가 모든 상용 제품에 적합하다는 뜻은 아니다.

## 4. 공식·실행·영감 자료실의 역할 구분

| 등급 | 자료/URL | 무엇을 얻는가 | 주의 |
|---|---|---|---|
| [S] 의미·접근성 | W3C ARIA APG https://www.w3.org/WAI/ARIA/apg/ | Tabs, Carousel, Meter, 키보드 패턴 | 기준을 실제 앱에서 재검증 |
| [S] HTML/CSS | MDN progress, meter, scroll timeline | 웹 기본 의미·지원 범위 | 구형 브라우저 대안 |
| [S] 플랫폼 | Apple HIG https://developer.apple.com/design/human-interface-guidelines/ | page controls, tab bars, 안전 영역 | iOS 외 시스템에 표면적 복제 금지 |
| [S] 플랫폼 | Android https://developer.android.com/design/ui/mobile/guides/foundations/system-bars | gesture navigation, insets | 기기/OS 간 차이 실측 |
| [S] 디자인 시스템 | IBM Carbon https://www.carbondesignsystem.com/building-blocks/core/patterns/loading | spinner vs skeleton vs progress 선택 | 제품별 맥락 재검토 |
| [S] 디자인 시스템 | Material Web https://material-web.dev/components/progress/ | Linear/Circular progress, tabs | 실제 버전·구현 범위 확인 |
| [D] 접근성 기본 구현 | React Aria https://react-aria.adobe.com/ | progressbar, meter, tabs, 예시 | 전체 앱 접근성 자동 인증은 아님 |
| [D] Headless 구현 | Radix https://www.radix-ui.com/primitives/docs/components/progress | React 기반 상태/ARIA 역할 | 스타일·버전은 별도 |
| [D] UI 구현 | shadcn/ui https://ui.shadcn.com/docs/components/base/progress | 코드 조합 및 수정 | 추가 패키지·라이선스·버전 확인 |
| [D] 애니메이션 | Motion https://motion.dev/examples | 탭·슬라이더·알림·스크롤·레이아웃 예시 | Motion+ 소스 일부 유료 |
| [D] 상태 머신 | Rive https://rive.app/use-cases | 고급 벡터 애니메이션·직접 입력 | 에셋별 권리·런타임 확인 |
| [D] 캐러셀 | Embla https://www.embla-carousel.com/docs/plugins/autoplay | autoplay/pause/timeUntilNext | RC/stable 버전 구분 |
| [D] 시스템 비교 | Component Gallery https://component.gallery/components/progress-indicator/ | 여러 라이브러리의 38개 Step 유사 사례 | 각 라이브러리의 유지 상태 다름 |
| [D] 실시간 작은 예시 | Microinteractions.dev https://microinteractions.dev/ | 누름·길게 누름·정렬 등 데모와 코드 | 실사용 적합성 별도 |
| [I] 창의적 영감 | Codrops https://tympanus.net/codrops/category/articles/ui-interactions-animations-roundups/ | 표현적인 전환·모션 | 성능·접근성 검증 전제 |
| [I] 시각 실험 | Style Gallery https://style.gallery/en/ | 다양한 CSS 스타일/모션 미리보기 | 미적 예시≠승인 UI |
| [I] 수집 자료실 | 60fps.design https://60fps.design/ · Design Spells https://www.designspells.com/ | 제품 모션·미세 결정 참고 | 원본 권리/실제 상태 미확인 |

**탐색 순서:** 의미는 공식 표준 → 기능적 코드는 접근 가능한 컴포넌트 → 매력적인 모션은 Motion/Rive → 새로운 사례는 갤러리에서. 독립 프로젝트의 UI 기준을 외부 라이브러리로 무단 교체하지 않는다.

## 5. 구현 수단 선택 지도

| 구현 경로 | 적합 상황 | 장점 | 한계 |
|---|---|---|---|
| HTML progress/meter + CSS | 단순 진행·강도 표기 | 의미·복잡도 최소화 | 브라우저 기본 디자인 차이 |
| 시맨틱 컴포넌트 + 기본 CSS 전환 | tabs, page, input 상태 | 키보드·상태 안정성 | 복잡한 물리적 모션 한계 |
| React Aria/Radix/Material/Carbon | React 앱/공통 UI 시스템 | 동작 계약과 예제 | 중복 라이브러리 조합 위험 |
| Motion | 공유 레이아웃 탭, 스프링 슬라이더, 화면 변환 | 연속적 움직임 | 과도한 모션·의존성 |
| Rive 상태 머신 | 브랜드/3D풍 그래픽, 반응형 상태 표현 | 디자이너와 개발자 간 상태 연결 | 런타임/에셋/라이선스 |
| Embla | 캐러셀/스토리형 진행 | 인덱스·자동재생 이벤트 | 나머지 앱 상태 해결하지 않음 |
| OS Native & Insets | Home indicator/safe area | 제스처를 운영체제가 관리 | 임의 웹 인디케이터 복제 불가 |

**[I] 선택 원칙:** 먼저 의미와 상태가 정확한 가장 간단한 구성요소를 만들고, 특정한 필요가 확인될 때만 모션 라이브러리를 적용한다. '복잡한 애니메이션이 더 세련돼 보인다'는 취향을 범용 규칙으로 두지 않는다.

### 최소 구현 원리의 차이

- 작업 처리: HTML progress 요소에 실제 현재 값/최댓값과 이름 연결.
- 수치 평가: HTML meter 요소에 범위/좋음·나쁨 구간, 평가 기준과 설명 연결.
- 탭: tablist-tab-tabpanel 관계 및 활성 tab 값을 실제 표시 패널과 연결.
- 슬라이드: activeIndex와 실제 슬라이드 순서, 점/버튼의 선택 상태를 같은 상태 근원에서 생성.
- 스토리: activeIndex와 elapsedMs/durationMs, paused/playing, visibility 상태를 별도로 제어.
- 홈 제스처: 시스템 영역을 감안한 콘텐츠 padding/WindowInsets.

## 6. 실험할 4가지 대표 비교 과제 [I / NOT RUN]

1. **Progress vs Meter — 의미 착각 실험.** 같은 모양의 60% 막대를 두 상황(파일 처리, 보안 강도 등)에 사용해 목적과 상태 해석을 비교. 표시 수치 근거를 제공.
2. **Page vs Story — 사용자 통제 실험.** 동일 5장 카드에 대해 수동 페이지와 자동 전환/중단/재시작을 비교. 키보드 초점·탭 이동·화면 비활성에서 콘텐츠 소실 검사.
3. **Tabs — 모션 있는/없는 상태 비교.** 동일한 콘텐츠에서 즉시 전환과 Motion shared layout 밑줄 이동을 비교. 빠른 반복 탭, 모바일, 모션 감소 설정을 확인.
4. **Scroll + System insets — 환경 적합성.** 실제 긴 문서에서 문서 길이 변화, 화면 회전, 200% 확대, Android gesture bar, 모바일 키보드와 스크롤 표시의 충돌 검증.

### 우선 적용 가능한 프로젝트 후보(현재 기능 변경 아님)

| 사용자 프로젝트 | 연구 후보 | 보존할 조건 |
|---|---|---|
| 심장 전도계 기원 시뮬레이터 | 현재 학습 구간 피드백 | 도식 집중 구조·기존 정확성·가독성 보존 |
| Nurse Interview Lab | Pending/Done/Error, 저장됨 상태 | 로컬 저장 성공 확인 전 완료 주장 금지 |
| US Stock Lab | Tab, 비동기 데이터 상태 | 시세/투자 결과의 가상·실제 구분 |
| SAI 블로그 | Scroll progress | 스크롤 위치를 학습 완료로 표시 금지 |
| MUL. | 의도 있는 물리적 모션 | 기존 승인 3D·UI의 강점 보호 |
| 돌봄/의료 업무 도구 | 단계·승인·오류 상태 | 실제 데이터·권한·안전 계약 최우선 |

## 7. 접근성·상태 정확성의 비협상 게이트

- **[S] 정보 정직성:** 100% = 실제 완료. 저장됨 = 실제 저장 확인. 승인됨/처리됨 등은 제품 상태 모델의 참값을 따른다.
- **[S] 시각적 상태:** 색만으로 구별하지 않음. WCAG 2.2의 SC 1.4.11은 적용 대상 UI와 정보 그래픽의 인접 대비 **3:1**을 요구(예외 고려); 표준 일반 문자 대비 4.5:1 / 큰 텍스트 3:1도 해당 범위 점검. 가느다란 선은 실제 렌더에선 더 흐릿해질 수 있음.
- **[S] 접근 가능한 조작:** 탭의 화살표 키/초점/선택, 캐러셀의 이전/다음/일시정지, 손쉬운 터치 영역과 오류 복구 경로 확보.
- **[S] 모션 감소:** prefers-reduced-motion에서 불필요한 공간 이동을 제거하거나 대체. WCAG 2.2 SC 2.3.3 Animation from Interactions는 **AAA** 기준(AA라고 잘못 표기하지 않음).
- **[S] 자동 진행:** WCAG SC 2.2.2 Pause·Stop·Hide의 조건에 따라 사용자가 움직임/자동 업데이트를 통제할 수 있게 함. 무조건 모든 애니메이션이 5초 이상이면 금지라는 식의 과잉 일반화 금지.
- **실행 검증:** 조작 전/중/후, 빠른 중복 탭, 오류/취소/재시도, 저장/복원, 좁은 모바일, 200% 확대, 다크 모드, 키보드, 색각, OS 제스처 영역, 오프라인. 코드·문서만 보면 **NOT RUN**.

## 8. 검증 상태 / 한계

| 항목 | 결과 | 증거 |
|---|---|---|
| 사용자 제공 9종 정적 이미지 명칭/형태 분류 | PASS | 제공 캡처의 시각적 설명 |
| 9종 의미·구현 후보·사용/오용 사례 구분 | PASS | 공식 문서와 라이브 예시의 공개 설명 |
| 추가 18종 패턴·자료실 탐색 | PASS | 공개 카탈로그/기술 문서 |
| v1.3 현행 기준과 조화 검토 | PASS (문서) | 승인 기준의 상태/모션/접근성 항목 |
| 외부 데모 전수 직접 클릭·동작 속도 측정 | NOT RUN | 페이지/문서 중심 조사 |
| 실제 React/CSS/Rive 구현·브라우저 검증 | NOT RUN | 코드·UI 견본 제작 전 |
| 원본 영상 모션/제작자/에셋 저작권 검증 | NOT RUN | 스크린샷과 외부 링크만 확보 |
| 실제 사용자 선호/과업 성과 평가 | NOT RUN | 실험 전 |
| 범용 지침 개정·웹앱 코드/Pages 배포 | N/A | 수행하지 않음 |

## 9. 참고문헌 (APA 7판 간략)

Adobe. (n.d.). *ProgressBar*. React Aria. https://react-aria.adobe.com/ProgressBar

Adobe. (n.d.). *Meter*. React Aria. https://react-aria.adobe.com/Meter

Apple. (n.d.). *Page controls*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/page-controls

Apple. (n.d.). *Tab bars*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/tab-bars

Apple. (n.d.). *Layout*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/layout

Carbon Design System. (2026, August 11). *Loading*. https://www.carbondesignsystem.com/building-blocks/core/patterns/loading

Carbon Design System. (2026, September 30). *Progress indicator*. https://www.carbondesignsystem.com/building-blocks/core/components/progress-indicator/guidelines

Embla Carousel. (n.d.). *Autoplay*. https://www.embla-carousel.com/docs/plugins/autoplay

Google. (n.d.). *Android system bars*. Android Developers. https://developer.android.com/design/ui/mobile/guides/foundations/system-bars

MDN Web Docs. (n.d.). *The HTML progress element*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress

MDN Web Docs. (n.d.). *The HTML meter element*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter

MDN Web Docs. (n.d.). *Scroll-driven animation timelines*. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines

Motion. (n.d.). *Examples*. https://motion.dev/examples

Rive. (n.d.). *Use cases*. https://rive.app/use-cases

W3C Web Accessibility Initiative. (n.d.). *Carousel (slide show or image rotator) pattern*. https://www.w3.org/WAI/ARIA/apg/patterns/carousel/

W3C Web Accessibility Initiative. (n.d.). *Tabs pattern*. https://www.w3.org/WAI/ARIA/apg/patterns/tabs/

W3C Web Accessibility Initiative. (n.d.). *Meter pattern*. https://www.w3.org/WAI/ARIA/apg/patterns/meter/

W3C Web Accessibility Initiative. (n.d.). *Understanding SC 1.4.11: Non-text contrast*. https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast

W3C Web Accessibility Initiative. (n.d.). *Understanding SC 2.3.3: Animation from interactions*. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

사용자 제공 소셜 영상 캡처. (2026, November 5). *인디케이터 이름 9가지* [대화 첨부 정적 이미지; 제작자·원본 URL·모션 미확인].

> 실제 구현에 앞서 링크의 유지/버전·라이선스·브라우저 지원을 다시 확인한다. 외부 자산/폰트/소스를 복제하지 않았으며, 자료에 등장한 패턴이 해당 제품에 적합하다는 점은 사용자 시험 전까지 가설이다.
