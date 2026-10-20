# Apple Figma 컴포넌트 아틀라스 v1.0 — 무엇을 어디에 쓸까

이 문서의 명칭은 **연결된 Apple 27 라이브러리 검색 결과에서 확인한 것**만 사용했다. 정확한 경로·검색 범위·고유 항목 목록은 [기계 색인](component_catalog.json). 카테고리/적합성 평가는 **디자인 깎기의 해석**이며 Apple HIG의 공식 분류나 개별 variants 검증이 아니다.

## 1. iOS / iPadOS 27 — 모바일과 태블릿

| 분류 | 실제 검색된 컴포넌트 | 응용 가능한 UX 문제 | 주의 |
|---|---|---|---|
| 1차 화면 내비게이션 | `Tab Bar - iPhone`, `Tab Bar - iPhone Duo`, `Tab Bar - iPad` | 화면 영역 전환, 현재 위치 | 모바일/태블릿 플랫폼 관습을 그대로 웹에 강제하지 않는다 |
| 화면별 명령 | `Toolbar - Top - iPhone`, `Toolbar - Top - iPhone Duo`, `Toolbar - Top - iPad`, `Toolbar - Bottom - iPhone`, `Toolbar - Bottom - iPad` | 현재 콘텐츠에 작용하는 주요 행동 | 탐색과 편집 행동 혼재/과도한 아이콘 밀도 점검 |
| 검색·빠른 이동 | `Accessory Bar - iPhone/Search`, `Sidebar Search Field`, `Index Bar` | 콘텐츠 검색·목록 내 이동 | 키보드 호출, 검색 상태 복구와 필터 표시 |
| 기본 버튼 | `Button - Liquid Glass - Text`, `Button - Liquid Glass - Symbol`, `Button - Content Area` | 텍스트/아이콘 행동, 터치 영역 | Liquid Glass는 **컨트롤 레이어**를 구분하는 수단이지 모든 카드의 표면이 아님 |
| 입력·선택 | `Text Field`, `Picker Button`, `Popup Button`, `Segmented Control` | 짧은 입력, 선택, 동일 위치 모드 전환 | 레이블·오류·키보드·선택 상태 별도 검증 |
| 목록·콘텐츠 | `Row`, `Row with Swipe Actions`, `Row - Button`, `Header`, `Section Title` | 목록 읽기·선택·행별 작업 | 스와이프에만 중요한 행동을 묶지 않는다 |
| 메뉴 | `Menu`, `Menu Items`, `Menu Items - Submenus`, `Context Menu` | 자주 쓰지 않는 보조 명령 | 검색·키보드/터치 접근성 및 깊은 메뉴 경로 |
| 알림·시트 | `Alert`, `Sheet - iPhone`, `Sheet - iPad`, `Action Sheet`, `Popovers (iPad Only)` | 작업 확인·보조 입력·일시적인 맥락 | 중대한 정보를 임시 레이어 속에만 넣지 않기 |
| 진행·상태 | `Progress Bar - Determinate Linear`, `Progress Bar - Indeterminate Circular ("Spinner")`, `Page Control` | 진행·페이지·로딩 피드백 | 실제 진행량이 없는데 확정 퍼센트처럼 보이지 않게 |
| 플랫폼 특화 | `Notification - Collapsed - List`, 잠금화면 Widget 예제 | 알림·위젯의 정보 압축·스캔 | 일반 홈페이지에 OS 시스템 셸을 복제하지 않음 |

**Figma에서 확인된 예제 그룹:** `Examples/Tab Bar`, `Examples/Tab Bars`, `Examples/Toolbars - Top`, `Examples/Toolbars - Bottom`, `Examples/Sheets (Modals)`, `Examples/List`, `Examples/Menus`, `Examples/Alert`, `Examples/Keyboard`, `Examples/Popover`. **검색 결과 존재만 확인**했고 내부 레이어/스크린샷은 아직 분석하지 않았다.

## 2. macOS 27 — 복잡한 작업형 UI

| 분류 | 실제 검색된 컴포넌트 | 응용 가능한 UX 문제 | 주의 |
|---|---|---|---|
| 윈도우의 큰 구조 | `Windows - Composed`, `Window BG`, `Window Titles/Window`, `Desktop Template` | 전역 내비게이션·본문·도구 계층의 결합 | 웹페이지에서 macOS 창 테두리를 그대로 흉내 내지 않기 |
| 사이드바·세부 탐색 | `Sidebars - Composed`, `Outline View`, `Item`, `Section Header` | 계층 정보, 많은 메뉴, 세부 설정 | 좁은 웹 화면에서 본문을 압축시키지 않기 |
| 테이블·데이터 탐색 | `Table Rows`, `Table Rows - Blank`, `Column Header`, `Sort Order Indicator`, `Group Title` | 밀도 높은 목록·정렬·비교 | 표 헤더, 키보드, 정렬 결과, 상태·선택을 의미로 연결 |
| 상단 도구·탐색 | `Examples/Windows/Unified Toolbar + Title`, `Examples/Windows/Unified Compact Toolbar + Title`, `Segmented Control`, `Search` | 제목과 화면별 행동 통합, 좁은 툴바 | 제목/액션 구분·컨트롤 혼잡 |
| 버튼·컨트롤 | `Button`, `Button Group`, `Buttons - Toggle`, `Toggles - Radio Buttons`, `Pop-Up Button`, `Pulldown Button` | 즉각 행동과 모드 전환 | hover 전용/작은 hit area의 웹 재사용 위험 |
| 메뉴·맥락 도움 | `Menu`, `Menu Bar`, `Menu Items`, `Menu Background`, `Popover`, `Utility Panel Tab Bar` | 설정·보기·보조 기능을 분리 | 모달 남발, 발견성 저하, 키보드 접근 |
| 데스크톱 플랫폼 셸 | `Window Controls`, `Window Controls/Standard`, `Window Controls/Utility` | 시스템 창과 콘텐츠의 물리적 구분 참고 | 기본 웹 UI에서 운영체제 창 버튼 복제 불필요 |

원본의 `Examples/Windows/Expaned Toolbar + Title`은 검색 결과 이름을 그대로 보존했다. **철자 오류를 임의로 수정해 존재하지 않는 이름으로 검색하지 않는다.**

## 3. 이름은 확인했지만 세부 구조를 확인하지 않은 항목

**현재 모두 확인된 범위:** 연결 라이브러리에 해당 이름의 컴포넌트 또는 컴포넌트 세트가 검색됨.

**아직 알 수 없는 범위:** 각 variant의 값, 개수·기본값·Auto Layout 규칙, 실제 색/간격 수치, 프로토타입 동작, 접근성, 최신 배포와의 동등성. 이 내용을 결과에 추측으로 채워 넣지 않는다.

특히 `component_catalog.json`의 **95개**는 조사를 위해 의도적으로 고른 대표 항목이며 **전체 Figma UI Kit의 95개 전부라는 뜻이 아니다**. 검색 결과에는 다른 질의와 중복되는 이름·예제 등이 있기 때문에 중복을 제거했다.

## 4. 실무에서 쓰는 빠른 예시

- **환자·보호자 모바일 홈:** `Tab Bar - iPhone`과 `Row`의 정보 밀도·탐색 방식을 비교하고, 실제 행동 구조는 환자 JTBD·KRDS 기본 패턴에 맞춰 설계한다.
- **의료진 업무용 A1 목록:** `Sidebars - Composed`, `Table Rows`, `Column Header`, `Sort Order Indicator`에서 항목 비교·선택 상태를 관찰하고, 최종 화면은 웹 표/그리드 접근성으로 구현한다.
- **A2 다영역 평가:** `Segmented Control`, `Outline View`, `Popover`, `Text Field`에서 페이지 맥락/부분 상세의 구분을 연구한다. 의료 위험도 숫자는 UI Kit으로 검증되지 않는다.
- **MUL. 제품 사이트:** `Button - Liquid Glass - Text` 등에서 '컨트롤/콘텐츠의 시각적 분리'라는 원리를 공부하되, Apple 고유 재질/코드를 제품 사이트에 그대로 복사하지 않는다.

## 5. 문제 → 소스 선택법

1. 과업과 플랫폼을 먼저 정한다. **홈페이지/웹 작업이면** [레이아웃 아틀라스](LAYOUT_AND_PLATFORM.md), [KRDS 레이아웃](../krds/LAYOUT_ATLAS.md)도 함께 확인한다.
2. 위 표에서 관련 컴포넌트명 **1~3개**를 고른다.
3. [기계 색인](component_catalog.json)의 `groups`에서 이름과 라이브러리 확인.
4. 내용의 실제 variants·색/간격이 필요할 경우 그 **이름과 라이브러리로 Figma를 좁혀 검색**한다.
5. 웹 표준 및 앱 계약에 맞게 재해석한다. 사용성·구현 테스트를 하지 않았으면 **NOT RUN**.

## 참고 원문

- [Apple Human Interface Guidelines — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple Human Interface Guidelines — Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [Apple Design Resources](https://developer.apple.com/design/resources/)
