# Apple UI Kit — 선택적 Figma 디자인 레퍼런스

> **역할:** iOS/iPadOS·macOS의 화면 구조, 시스템 컨트롤, 정보 계층, 상호작용을 이해하기 위한 **참고 색인**. Apple의 원본 UI Kit/이미지/폰트/SF Symbols나 저작물을 이 저장소에 미러링하지 않는다. Apple의 native 플랫폼 UI를 일반 웹페이지에 강제하거나 그대로 복제하지 않는다.

## 탐색 시작 — 필요한 문서만 열기

| 하려는 일 | 가장 먼저 볼 문서 | 추가 탐색 |
|---|---|---|
| 실제 Figma 라이브러리에서 확인한 컴포넌트 이름 찾기 | [95개 확인 항목 카테고리 JSON](component_catalog.json) | [용도별 컴포넌트 해설](COMPONENT_ATLAS.md) |
| 사이트 전체 구성, 모바일↔데스크톱 전환 | [레이아웃·플랫폼 아틀라스](LAYOUT_AND_PLATFORM.md) | Apple HIG 공식 Layout |
| 탭/사이드바/툴바/모달이 언제 적합한가 | [컴포넌트 해설](COMPONENT_ATLAS.md) | [선택·비교 규칙](REFERENCE_SELECTION.md) |
| 유리 재질, 시각 계층, 글꼴, 색/상태 | [시각 언어·검증](VISUAL_LANGUAGE.md) | 공식 Apple HIG |
| KRDS와 Apple을 어떻게 조합하는가 | [레퍼런스 선택 규칙](REFERENCE_SELECTION.md) | [KRDS 허브](../krds/README.md) |
| 버전, Figma 접근 범위, 권리/사용 가능 여부 | [출처 및 검증](SOURCE_PROVENANCE.md) | Apple 공식 자료실 |

### 작업 시작 기본 순서

**과업/플랫폼 판단 → 레이아웃·내비게이션 후보 비교 → 정확한 컴포넌트명 조회 → 필요시 Figma 연결로 상세 확인 → 프로젝트 맥락에서 수정 → 실제 실행 검증.**

컴포넌트를 찾으려고 매번 Apple 라이브러리 전체를 조회하지 않는다. `component_catalog.json`은 이미 확인된 이름으로 좁혀 찾아가기 위한 색인이고, 모르는 세부 사항(변형/토큰값/모션)은 확인한 척하지 않고 Figma·HIG를 그 부분만 재조회한다.

## Figma 라이브러리 — 실제 연결 상태

- **연결 파일:** [사용자 Figma의 디자인 파일](https://www.figma.com/design/HAobgfDkid1Jezh8OYSd6H/) · `HAobgfDkid1Jezh8OYSd6H` · `Page 1` (현재 빈 캔버스)
- **현재 주 대상:** `iOS and iPadOS 27` 및 `macOS 27`의 **연결된 Community 디자인 라이브러리**.
- **확인한 검색 결과:** iOS/iPadOS 27 **52개**, macOS 27 **43개**, 합계 **95개**의 중복 제거된 *선별 컴포넌트 명칭*. 전체 UI Kit 수는 **미확인**.
- **추가 연결되어 있는 라이브러리:** `iOS and iPadOS 26`, `macOS 26`, `watchOS 26`, `visionOS 26`, `Material 3 Design Kit`, `Simple Design System`. **이 6개의 컴포넌트 내용은 미분석**이며 Apple 27 결과와 섞지 않는다.
- 연결된 Community 라이브러리 이름과 Apple 공식 배포본의 완전한 동일성/게시자 확인은 별개다. [공식 Apple Design Resources](https://developer.apple.com/design/resources/)에 iOS/iPadOS 27 및 macOS 27 Figma UI Kit이 등재되어 있음을 확인했고, **연결 라이브러리의 소유자/해시 비교는 수행하지 않았다.**

## 이 자료를 활용하는 원칙

1. **좋은 것만 추출한다:** 목적, 사용자 주도권, 컨트롤 위치, 플랫폼별 레이아웃 적응, 콘텐츠/조작 계층, 일관된 컴포넌트 상태.
2. **복제하지 않는다:** Apple 고유 화면·고유 UI 자산·아이콘·폰트·원본 템플릿을 웹에 그대로 이식하지 않는다.
3. **과잉 적용 금지:** Liquid Glass·하단 탭바·사이드바·모달은 상황에 맞을 때만 검토한다.
4. **검증은 별개:** 디자인 파일의 존재가 웹 접근성, 구현 정확도 또는 의료·행정 UX의 안전성 검증을 뜻하지 않는다.
5. **기존 계약 우선:** 사용자 승인된 디자인/기능, Universal v1.2 DRAFT, 프로젝트별 요구사항을 자동 변경하지 않는다.

## 검증 범위

- **PASS:** 실제 연결 파일에서 8개 라이브러리 구독 확인, 2개 Apple 27 라이브러리의 카테고리 검색, 선택된 95개 고유 항목 정리.
- **NOT RUN:** 전체 라이브러리 인벤토리 수집, 모든 variants/Auto Layout 값, 시각적 프레임 정밀 분석, 동작/모션 실제 검증, CSS 변수값 전체 열람, 공식 Figma 원본과 연결된 Community 라이브러리의 동일성, 다른 6개 라이브러리 상세 조사.
- **권리:** Apple 원본 리소스는 Apple Design Resources License를 적용받을 수 있고 사용 범위가 제한된다. 자세한 범위와 서체 별도 계약은 [출처·라이선스](SOURCE_PROVENANCE.md) 참고.
