# SRC-24 — 목록 표현·비교·탐색 방식 9종 아틀라스 v0.1

> **2026-11-12 · RESEARCH / 사용자 제공 정적 Instagram 캡처 1장**  
> **현행 기준:** Universal Visual Design & UI/UX Guidelines **v1.3 APPROVED** (미변경). 이미지·영상·타사 코드·폰트를 GitHub에 업로드하지 않음.
>
> **[CAP]** 화면에 `@uxwoodytips`가 표시되며 제목은 ‘목록 보여주는 방식 9가지’. 직접 확인한 것은 캡처의 **명칭·순서·정적 예시**뿐이다. 실제 원본 게시물 URL·게시 날짜·원작자 권리·애니메이션·터치 동작은 **미확인**.
>
> **[USER]** 사용자는 새 자료를 발견해 아틀라스에 반영해 달라고 요청함. **9가지 개별 방식에 대한 개인적 미감·선호도는 직접 평가하지 않음**.
>
> **[AI-HYP]** 아래 선택과 적용 기준은 캡처에서 검증된 사용자 성능이 아니라, 개념 분류·공식 문서·기존 프로젝트 취향 지도를 토대로 한 설계 가설이다.
>
> **집계:** **SRC-24 = 1장 × 9칸**. 기존 **216칸 → 225칸(중복 포함)**. 225개의 독립 UI 패턴·사용성 시험 또는 사용자 선호 평가를 의미하지 않는다. [기존 UI 현장 아틀라스](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md), [화면 배치 아틀라스](UI_LAYOUT_FIRST_USE_ATLAS_v0.1_20261111.md), [동작·피드백 증보](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md)와 중복은 연결한다.

## 1. 원본 순서와 레벨 혼합 문제

| 번호 | 화면 표기 [CAP] | 본질적 설계 차원 | 이전 항목과 관계 |
|---|---|---|---|
| **01** | 리스트 / List | **개별 행을 연속해서 배치** | [기존 Card vs List 비교, SRC-16](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md) |
| **02** | 그리드 / Grid | **행·열 기반의 공간 배치** | [SRC-19 Card grid·Bento](UI_LAYOUT_FIRST_USE_ATLAS_v0.1_20261111.md) |
| **03** | 카드 / Card | **내용·행동을 묶는 콘텐츠 단위** | SRC-16 Card vs List, SRC-19 Card grid |
| **04** | 캐러셀 / Carousel | **슬라이드 단위 탐색·노출 메커니즘** | [SRC-01 Carousel](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md) |
| **05** | 테이블 / Table | **행·열의 의미 있는 비교 구조** | 기존 일반 Grid와 목적 구분 |
| **06** | 타임라인 / Timeline | **시간·사건의 순서/단계/상태 표시** | 일반 목록과 시간/과정 의미 구분 |
| **07** | 아코디언 / Accordion | **섹션 공개·접기 상호작용** | 별도 명칭·키보드 동작 연구 보강 |
| **08** | 메이슨리 / Masonry | **높이가 다른 항목의 빈틈을 줄이는 배치** | SRC-19 Bento와 혼동 방지 |
| **09** | 무한 스크롤 / Infinite scroll | **다음 데이터의 로딩/연속 탐색 방식** | [SRC-08 Infinite scroll](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md) |

**이 아홉 개는 상호 배타적인 ‘9종의 리스트’가 아니다.** List·Grid·Masonry는 배치, Card는 정보 단위, Table·Timeline은 정보의 관계, Carousel·Accordion은 탐색·공개 조작, Infinite scroll은 데이터 이어 불러오기다. **카드 그리드 + 무한 스크롤**, **리스트 + 아코디언**, **가로 카드 + 캐러셀** 등 조합이 가능하다. 다른 구조가 같은 시각적 외관을 가질 수도 있다.

## 2. 목적에 맞는 선택과 실패 위험

| 방식 | 대표 과업 [AI-HYP] | 강점/왜 적합한가 | 문제·반례·필수 상태 |
|---|---|---|---|
| **List** | 환자·주문·검색 결과 등 빠른 훑어보기 | 제목·상태·시간·핵심 행동을 같은 위치에서 찾음 | 행 간 위계, 선택·초점·빈 목록·정렬/검색 후 위치 복원. 많은 수치의 다열 비교는 Table이 나음 |
| **Grid** | 사진·상품·기능처럼 동등한 독립 항목 찾기 | 여러 후보의 전체 모습을 동시에 봄 | 화면 폭에 따른 열수·순서·키보드 이동. 설명이 길어지면 카드 높이 불균형 |
| **Card** | 한 항목 안에 이미지·요약·행동 결합 | 콘텐츠 경계를 분명히 표현하고 독립 행동 제공 | 카드를 중첩하거나 모든 정보를 카드화해 밀도·비교성 저하. Table/List 대안 검토 |
| **Carousel** | 제한된 공간에서 소수 대표 항목·이미지 순회 | 한 번에 보여줄 양을 통제 | 뒤에 숨은 항목의 **발견성**, 다음/이전·위치 표시·초점·자동 회전 정지. 중요한 필수정보를 캐러셀 속에만 숨기지 않기 |
| **Table** | 여러 상품·수치·설정의 공통 속성 비교 | 같은 열에 동일 기준이 놓여 차이를 파악하기 쉬움 | 표제·단위·정렬·빈 값·키보드·좁은 화면 가로 스크롤/핵심 열 고정 등 검증. 단순 공간 정렬용 Grid와 구별 |
| **Timeline** | 배송 진행, 진료·학습 단계, 사건 이력 | 전후 순서와 현재 단계가 명확 | 미래·완료·진행중·오류를 **색 외 텍스트/아이콘으로 구별**. 여러 병렬 과정과 예외는 선형 목록만으로 표현 곤란 |
| **Accordion** | FAQ·부가 설명·상세 옵션 공개 | 일단 핵심만 보여주고 원할 때 세부정보 확장 | 필수 경고·핵심 설명을 숨기지 않기. 헤더는 버튼/확장 상태가 보이고 키보드로 조작·초점 유지 |
| **Masonry** | 크기 비율이 다양한 사진·시각 작품 둘러보기 | 서로 다른 이미지 높이를 여백 낭비 없이 조합 | 시각 순서와 읽기/키보드 순서 일치, 콘텐츠 비교성·모바일 재배치. **CSS grid lanes는 실험적**이므로 대체 구현·브라우저 확인 필요 |
| **Infinite scroll** | 새로운 콘텐츠를 연속적으로 탐색하는 피드 | 중단 없는 읽기와 이어 보기 | 위치 복원, 신규 로딩/끝/오류/중복, 푸터 접근, 특정 항목 재검색. 비교·회귀가 잦은 업무/상품 목록에는 페이지네이션 또는 '더 보기'가 더 나을 수 있음 |

### 선택할 때 자주 발생하는 혼동

- **Grid vs Table:** 둘 다 격자처럼 보여도 Table은 **속성별 데이터 관계**가 핵심이다. 상품 이미지 나열과 동일 종목의 수익률·변동성 비교는 요구되는 구조가 다르다.
- **Bento vs Masonry:** Bento는 **의도적인 정보 비중/면적 차이**에, Masonry는 **서로 다른 높이의 콘텐츠가 만들어내는 빈 공간 정리**에 초점이 있다. 유사하게 보이더라도 같은 패턴으로 일반화하지 않는다.
- **Carousel vs Infinite scroll:** 전자는 **현재 보여줄 콘텐츠를 좌우/순차 전환**, 후자는 **전체 목록을 아래로 이어 로딩**한다. 두 방식은 함께 쓰거나 따로 쓸 수 있다.
- **Card vs List:** Card는 단위의 시각적 경계·요약/행동, List는 빠른 스캔과 반복 구조가 일반적인 장점이다. 같은 카드 모양이 곧 좋은 탐색 UX라는 증거는 없다.
- **Timeline vs Steps:** 사건의 실제 기록(일정/배송 내역)과 미래 작업의 단계(워크플로)는 둘 다 선형으로 그릴 수 있지만 데이터 의미·오류 처리·완료 조건이 달라야 한다.

## 3. 공식 구현·접근성 근거와 확신 범위

- **[OFFICIAL] W3C WAI-ARIA Carousel APG:** 이전/다음 선택 수단, 자동 회전 시 정지·재개, 키보드 초점 진입 시 회전 중단, 보조기술의 슬라이드 인지 등 실제 구현 항목을 설명한다. **인스타 캡처의 캐러셀이 실제로 이를 구현했다고 검증한 것은 아님.** https://www.w3.org/WAI/ARIA/apg/patterns/carousel/
- **[OFFICIAL] W3C WAI-ARIA Accordion APG:** 헤더 버튼과 확장 여부(`aria-expanded`), 연결 패널(`aria-controls`), Enter/Space 키보드 조작 등을 설명한다. 캡처의 동작 구현 성공을 보증하지 않는다. https://www.w3.org/WAI/ARIA/apg/patterns/accordion/
- **[OFFICIAL] MDN Grid lanes layout:** Masonry와 비슷하게 한 축은 정렬된 레인, 다른 축은 쌓는 레이아웃의 원리를 설명하며 **제한된 지원/실험적 상태**를 알린다. 프로덕션 도입은 사용 브라우저의 실제 지원을 확인해야 한다. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes
- **[RESEARCH] Nielsen Norman Group:** 무한 스크롤은 탐색 흐름에 따라 유리할 수 있으나 재탐색, 비교, 위치 복원 등의 과업에서는 불리할 수 있다는 연구·실무 분석을 참고한다. **특정 제품에서 성능 차이를 실제 측정하지 않았음.** https://www.nngroup.com/articles/infinite-scrolling-tips/
- **[OFFICIAL] W3C WCAG 이해 자료:** 의미 있는 관계가 단지 위치나 색에만 의존하지 않도록 해야 하며, Table·Timeline의 표제/상태 표현에도 적용할 필요가 있다. https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html

## 4. 디자인 깎기·기존 취향 지도와의 관계

**[USER: 이전 직접 진술과 이번 수집 사실의 구분]** 사용자는 이전에 심장 시뮬레이터의 **정보량·정보 간 위계·간편한 조작**, 다른 작업에서 **너무 빽빽한 한 화면/반복적 카드 구성 문제**를 직접 평가했다. **이번 SRC-24의 개별 유형에 대한 선호 평가는 아직 없음**. 해당 유형의 유행 여부나 계정에 대한 호감이 곧 개별 패턴 선호는 아니다.

**[AI-HYP: 일치]** ‘정보 표현 형태는 과업에 맞아야 한다’는 기존 목적 중심 판단과 정합적이다. 같은 9개의 카드라도 수치 비교가 목적이면 Table, 진행 내역이면 Timeline, 작품 탐색이면 Masonry를 후보로 삼는 것이 타당할 수 있다.

**[AI-HYP: 새 발견]** 장식적인 카드 또는 화면 비율뿐 아니라 **보이는 정보의 의미 관계 / 공개 시점 / 추가 로드 / 복귀 위치**를 별개 축으로 평가해야 한다. 특히 리스트/그리드/카드와 무한 스크롤을 동급으로 비교하면 원인 판단이 흐려진다.

**[COUNTEREXAMPLE]** Masonry의 시각적 개성이 높아도 과제·병원 업무의 우선순위와 읽기 순서를 흐트러뜨릴 수 있다. 반면 단조로운 Table이나 List가 정확한 비교에는 더 낫다. **특정 레이아웃의 채택을 범용 정답으로 확정하지 않는다.**

### 예시 적용 후보 (검증 전)

| 과업 | 우선 후보 | 왜/주의할 점 |
|---|---|---|
| 의료진의 환자·업무 탐색 | **List + 상태 필터** | 빠른 위치 파악과 환자 식별/상태가 우선. 환자정보 보호·오류 구분 필요 |
| 주식·포트폴리오 수치 비교 | **Table** | 여러 자산의 동일 지표 비교. 모바일에서 열 선택/스크롤·정렬 회귀 확인 |
| 학습 시뮬레이터의 상세 설명 | **Accordion / 단계 목록** | 초보자 인지부담 감소 가능. 필수 안전 메시지는 숨기지 않기 |
| 제품·사진·작품 탐색 | **Grid / Masonry** | 이미지 비율·정보량·읽는 흐름에 따라 선택 |
| 주문·배송·진행 이력 | **Timeline** | 과정·단계·상태·예외 표시. 일괄 완료처럼 오인할 여지 제거 |

## 5. 검증 상태

| 검증 항목 | 결과 | 근거 수준 |
|---|---|---|
| 캡처 9개 명칭·배치·단순 예시 확인 | **PASS** | 사용자 제공 정적 화면 |
| 기존 SRC-01·08·16·19와 중복 및 범주 차이 점검 | **PASS** | 저장소 문서 대조 |
| W3C Carousel/Accordion·MDN masonry·NN/g 무한 스크롤 근거 확인 | **PASS (문서)** | 공식 공개 문서 및 외부 UX 연구 |
| Instagram 원본 영상/스크롤·터치·전환 애니메이션 | **NOT RUN** | 게시물 URL 및 원본 재생 미확인 |
| 모바일/PC/보조기술/실제 사용자 비교 | **NOT RUN** | 구현 시안·사용성 시험 없음 |
| 개별 디자인에 대한 사용자 선호 순위 | **NOT RUN** | 평가 없음 |
| 기존 범용 v1.3·제품 UI/기능/Pages 변경 | **N/A** | 진행하지 않음 |

## 6. 참고문헌 (APA 7판)

Mozilla. (n.d.). *Grid lanes layout*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes

Neusesser, T. (2022, September 4). *Infinite scrolling: When to use it, when to avoid it*. Nielsen Norman Group. https://www.nngroup.com/articles/infinite-scrolling-tips/

World Wide Web Consortium. (n.d.). *Accordion pattern (sections with show/hide functionality)*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/accordion/

World Wide Web Consortium. (n.d.). *Carousel (slide show or image rotator) pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/carousel/

World Wide Web Consortium. (n.d.). *Understanding SC 1.3.1: Info and relationships*. Web Content Accessibility Guidelines 2.2. https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html

사용자 제공 Instagram 정적 캡처 1장. (2026, November 12). *목록 보여주는 방식 9가지* [화면에 @uxwoodytips 계정 표시, 원본 게시 URL·권리 미확인].

**운영 결론:** 이번 자료는 ‘무엇을 리스트로 그릴까’뿐 아니라 **콘텐츠의 관계·배치·공개·추가 로드를 분해해 선택하는 판단 능력**을 보완한다. 분석만으로 특정 디자인 스타일이나 UI가 우수하다고 확정하지 않는다.
