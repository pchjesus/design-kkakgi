# Apple Figma 레퍼런스 — 출처·범위·권리·검증 기록

## A. 식별

- **조사일:** 2026-10-20 KST
- **사용자 제공 연결 파일:** [Figma '제목 없음'](https://www.figma.com/design/HAobgfDkid1Jezh8OYSd6H/?node-id=0-1)
- **Figma fileKey:** `HAobgfDkid1Jezh8OYSd6H`
- **원본 페이지:** `Page 1` / `0:1`, 조회 시 빈 캔버스(`0×0`).
- **라이브러리 접근 방식:** 빈 디자인 파일에 추가된 디자인 라이브러리 구독 목록 조회 → `search_design_system`으로 대상 라이브러리만 좁혀 구성요소 검색.
- **확인된 연결 라이브러리 8종:**
  1. `iOS and iPadOS 27` (**주요 조사**)
  2. `macOS 27` (**주요 조사**)
  3. `iOS and iPadOS 26` (이름만)
  4. `macOS 26` (이름만)
  5. `watchOS 26` (이름만)
  6. `visionOS 26` (이름만)
  7. `Material 3 Design Kit` (이름만)
  8. `Simple Design System` (이름만)

**원본 출처 상태:** 라이브러리 검색 응답의 `source`는 `community`. [Apple 공식 Design Resources](https://developer.apple.com/design/resources/)는 iOS/iPadOS 27 및 macOS 27 Figma UI Kit을 제공한다. 그러나 **이 연결된 라이브러리 키가 Apple 공식 게시 원본과 완전히 동일한지, 게시자/소스 commit/파일 hash까지 독립 검증한 것은 아님**. 따라서 `Apple 27 라이브러리 이름으로 연결된 Figma 자료`와 `Apple 공식 HIG`를 구분한다.

## B. 실제 검색 범위

| 라이브러리 | 쿼리 | 고유 이름 선별 수 |
|---|---|---:|
| iOS and iPadOS 27 | `Button, Tab Bar, Navigation Bar, Toolbar, Search, Sheet, Alert, Text Field, List, Table, Menu, Segmented Control, Popover` | **52개** |
| macOS 27 | `Sidebar, Toolbar, Window, Table, Popover, Button, Menu, Inspector, Tab` | **43개** |
| 합계 | 유형별 검색에서 서로 중복되는 이름을 정리한 탐색 샘플 | **95개** |

- Figma 검색이 **유사 매칭**을 반환하므로, 쿼리 결과에 이름이 포함되었다고 특정 카테고리의 전체 자산을 수집했다는 뜻은 아니다.
- 소속별 카테고리는 디자인 깎기가 편집한 것이다. 샘플 이름과 일부 `componentSetKey`는 [component_catalog.json](component_catalog.json)에 보존.
- iOS `style: Text`, `variable: color` 조회 결과 **0개**. macOS `component: Inspector` 조회 결과 **0개**. 이는 해당 기능/변수가 **없다**는 결론이 아니다.
- 26 시리즈, watchOS, visionOS, Material 3, Simple DS의 상세 컴포넌트 검색은 **NOT RUN**.

## C. Apple HIG에서 별도로 읽은 원리

| 공식 출처 | 확인한 내용 |
|---|---|
| [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | 시각 계층, 관련 항목 그룹화, 적응형 레이아웃, 플랫폼별 safe area, 컨트롤/콘텐츠 분리 |
| [Apple HIG Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) | 화면별 행동 및 검색용 toolbar와 상위 영역 이동용 tab bar 구별 |
| [Apple HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | Liquid Glass는 UI 컨트롤/탐색 계층에 적합하고 콘텐츠 영역을 모두 덮는 데 쓰지 않음 |
| [Apple Fonts](https://developer.apple.com/fonts/) | SF Pro/Compact 등 플랫폼 서체의 역할, 별도 폰트 사용 조건 |
| [Apple Design Resources](https://developer.apple.com/design/resources/) | 공식 UI Kit·폰트·도구 배포 링크 |

**주의:** 일반 HIG의 공식 원리는 해당 버전의 Figma 라이브러리 내부 값과 동일하다는 증거가 아니다. 디자인 시스템의 소스와 라이선스는 시점에 따라 바뀔 수 있다.

## D. Apple 리소스의 권리·제약

**중요:** Apple 공식 [Apple Design Resources License](https://developer.apple.com/support/downloads/terms/apple-design-resources/Apple-Design-Resources-License-20230621-English.pdf)의 사용 목적은 Apple 운영체제(macOS/iOS/watchOS/tvOS/visionOS) 전용 소프트웨어 UI의 목업으로 제한되어 있다. **일반 웹사이트에 원본 템플릿·디자인 자산을 가져다 쓰는 전면적인 라이선스가 아니다.** 리소스·UI Kit 원본 파일/프레임·로고·이미지·SF Symbols 등을 Public GitHub에 보관하거나 재배포하지 않는다. 구체적인 각 릴리스의 라이선스 조건은 실제 다운로드 전에 확인해야 한다.

Apple [San Francisco font license](https://developer.apple.com/fonts/)는 별도이고, SF Pro/관련 시스템 폰트를 웹 서버에 업로드해 배포하는 것을 허용한다고 해석하지 않는다. Apple 시스템 서체 사용에는 플랫폼/API 조건이 있다.

**이 저장소가 보관하는 것:** 인용 가능한 공식 설명, 고유하지 않은 추상적 설계 원리와 교육용 분석, 컴포넌트의 **이름·범주**, 검색 키워드, 버전/출처 및 검증 범위. 원본 디자인 아트워크/폰트/컴포넌트 프레임·이미지 바이너리·재배포용 코드 없음.

## E. 검증 기록

| 검증 항목 | 상태 | 내용 |
|---|---|---|
| Figma 사용자 파일 접근 | **PASS** | 공유 fileKey 및 `Page 1` 확인 |
| 연결 라이브러리 조회 | **PASS** | 8종 |
| iOS/iPadOS 27 항목 검색 | **PASS** | 52개 고유 이름(선별 조사) |
| macOS 27 항목 검색 | **PASS** | 43개 고유 이름(선별 조사) |
| 컴포넌트 속성·Variants·레이아웃 실제 수치 | **NOT RUN** | 본인 캔버스 빈 상태, 라이브러리 내부 레이어 열람 안 함 |
| 디자인 토큰 전체 값 | **NOT RUN** | 스타일·색 변수 질의 결과 0 |
| Apple 공식 Figma 파일과 연결 라이브러리 동일성 | **NOT RUN** | 공식 제공 여부 확인과 연결 Community 자산 동일성은 별개 |
| 모든 검색 후보 시각 검사 | **NOT RUN** | screenshot/실제 레이어 비교 미진행 |
| 무료 계정 사용량·플러그인 잔여치 | **NOT RUN** | 정량적 크레딧/쿼터는 계정별 UI에서 확인 |
| 범용 디자인 지침 v1.2 수정 | **N/A** | 변경 안 함 |
| 웹/의료 앱 코드 이식·실기기 테스트 | **NOT RUN** | 설명·탐색 문서만 작성 |

## F. 지속 관리

- 새 Figma 원본을 받으면 게시자·릴리스·라이브러리 키·실제 소유권 및 재배포 제한부터 확인.
- `component_catalog.json`에 **원래 존재하던 것과 새로 확인한 것의 차이**만 추가.
- 측정하지 않은 `spacing`, `corner radius`, `type scale`, `color`는 사용자 프로젝트의 값으로 부정확하게 채우지 않는다.
- GitHub 분석 기록은 사용자 계정 연결·크레딧이 소진돼도 이름/용도 검색에 재사용 가능하지만, Figma의 미래 상태/업데이트를 보증하지 않는다.

## 참고문헌 (APA 7판)

Apple. (n.d.). *Apple Design Resources*. https://developer.apple.com/design/resources/

Apple. (n.d.). *Layout*. *Human Interface Guidelines*. https://developer.apple.com/design/human-interface-guidelines/layout

Apple. (n.d.). *Materials*. *Human Interface Guidelines*. https://developer.apple.com/design/human-interface-guidelines/materials

Apple. (2023). *License agreement for Apple Design Resources*. https://developer.apple.com/support/downloads/terms/apple-design-resources/Apple-Design-Resources-License-20230621-English.pdf
