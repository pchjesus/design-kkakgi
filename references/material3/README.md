# Material 3 레퍼런스 — 선별 조사 v0.1

> **2026-10-20 / CURATED / NOT EXHAUSTIVE.** 사용자 Figma 파일 `HAobgfDkid1Jezh8OYSd6H`에 연결된 **Material 3 Design Kit** (검색 응답상 `source: community`)을 대상으로 필요한 컴포넌트 이름을 직접 검색한 기록. Google 공식 Material Design 3 자료와 **연결 Community 라이브러리의 정확한 동일성은 미검증**. Figma 원본 프레임·아이콘·폰트·바이너리는 업로드하지 않음.

## 1. 역할 — KRDS/Apple과 다른 참조 가치

Material 3는 앱의 **크기 적응형 탐색, 상태·행동·선택 컴포넌트, 디자인 토큰의 역할**을 비교하는 세 번째 선택지다. 단, 같은 제품에 세 시스템의 외형을 한꺼번에 결합하라는 뜻은 아니다. 레퍼런스별 역할·충돌 해결은 [통합 선택 지도](../DESIGN_SYSTEM_SELECTION.md)에 따름.

## 2. 확인된 컴포넌트 이름 — Figma 검색 결과

| 분야 | 실제 존재를 확인한 명칭 예시 | 웹에 응용할 판단 질문 |
|---|---|---|
| 상위 탐색 | `Navigation Rail`, `Navigation Rail: Expanded`, `Navigation Drawer`, `Navigation Bar: Horizontal items`, `Navigation Bar: Vertical items` | 폭·과업·탐색 깊이에 따라 내비게이션이 어떻게 바뀌는가 |
| 행동 | `Button - outline`, `Button - text`, `Toggle button`, `Toggle button - elevated`, `Split button`, `Connected button group` | 1차 행동/보조 행동/상태 전환의 시각적 차이가 분명한가 |
| 입력·탐색 | `Text field`, `Search bar`, `Search full-screen layout`, `Search docked layout` | 입력·검색 진입과 결과를 찾기 쉬운가 |
| 콘텐츠 | `Horizontal card`, `Stacked card` | 카드 자체가 정말 유효한 콘텐츠 단위인가 |
| 다이얼로그 | `Basic dialog`, `Scrollable list dialog`, `List dialog` | 전체 페이지 전환보다 확인·한정된 선택에 적합한가 |
| 탭 | `Tabs`, `Primary tabs/Label only`, `Primary tabs/Icon and label`, `Secondary tabs/Label only` | 관련 콘텐츠의 모드를 구분하고 현재 위치를 유지하는가 |

**특이사항:** `Data Table`이라는 검색어의 결과는 `Carousel` 1개뿐이었다. 이를 M3 UI Kit의 '테이블 확인'으로 계산하지 않았다. 검색이 유사 매칭인 탓에 일부 쿼리에서 이름과 직접 관계없는 결과가 섞인다. `Navigation Drawer`는 Material 3 Expressive 최신 가이드에서 **expanded navigation rail로 전환이 권장되는 변화**가 있으므로 최신 공식 문서/컴포넌트 버전을 확인한다.

## 3. 공식 문서와 실제 사용 규칙

- [Material Design 3 공식 사이트](https://m3.material.io/) · [Adaptive design](https://m3.material.io/foundations/adaptive-design/overview): 크기와 사용 맥락에 따른 레이아웃·내비게이션 적응.
- [Navigation rail](https://m3.material.io/components/navigation-rail/overview) · [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview): Expressive 등 버전에 따른 권고 변경 가능. **오래된 Drawer 패턴을 새 공식 기본값으로 고정하지 않는다.**
- [Color](https://m3.material.io/styles/color/overview): 브랜드·상태에 따른 의미 기반 색상 선택의 관점. **실제 토큰 값·동적 색 알고리즘은 아직 추출하지 않았다.**
- [Google Android Material Components의 NavigationDrawer 문서](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationDrawer.md): M3 Expressive에서는 Drawer 대신 expanded rail을 안내함.
- [Google Android Material Components의 NavigationRail 문서](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md): collapsed/expanded rail을 다룸.

**읽기 제약:** `m3.material.io` 본문은 웹 텍스트 수집 시 JavaScript 의존성으로 직접 판독이 제한되었음. 가이드 문구의 확인에는 Google의 Android 컴포넌트 공식 GitHub 문서를 함께 사용했고, Figma 라이브러리 목록/자산명은 연결 도구에서 확인함.

## 4. 개발 응용 후보 (디자인 깎기 가설)

- **모바일 환자용 홈:** 고정 1차 목적지의 개수·라벨·현재 위치 표시를 Apple Tab Bar, Material Navigation Bar/Tab과 비교.
- **의료진 웹 워크벤치:** 화면 폭에 따라 KRDS 선택적 좌측 메뉴 / Apple Sidebars / Material Navigation Rail을 비교. 좁은 화면에서 정보 손실 없이 탐색 방식 전환.
- **목록 검색:** M3 Search bar와 KRDS 필터링·정렬의 역할을 비교하고, 실제 데이터 양과 과업에 맞는 진입점을 선택.
- **브랜드 홍보:** M3 토큰·기본 Card를 기계적으로 복제하지 않음. 소재·아트 디렉션을 먼저 결정.

## 5. 검증 범위 및 다음 작업

- **PASS:** 연결된 Material 3 Community 라이브러리 식별, 10개 지정 검색어의 일부 컴포넌트 이름·세트 키 조회.
- **NOT RUN:** 전체 인벤토리, variant 수치, 스타일/변수 값, 렌더 스크린샷·반응형·모션 구현, 공식 Figma 원본의 동일성, 실제 사용자 A/B.
- **운영:** UI Kit 업데이트가 필요한 경우 우선 공식 제품 문서 버전을 확인하고 **필요한 컴포넌트만** 다시 검색. 사용자의 무료 Figma 호출량을 고려해 전체 라이브러리 전수 수집 금지.
