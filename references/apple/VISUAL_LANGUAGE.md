# Apple 시각 언어·상태·검증 아틀라스 v1.0

**출처 수준을 분리함:** Apple 공식 HIG/Fonts 설명에서 확인한 일반 원리와, Figma 연결 라이브러리에서 이름만 찾은 실제 컴포넌트, 디자인 깎기의 응용 가설은 서로 다른 증거다. **실제 Figma 토큰 값이나 각종 변형을 추정해서 쓰지 않는다.**

## 1. 재질(Materials) — 무엇을 구분하기 위한 표면인가

Apple HIG [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)에서 확인:

- Liquid Glass는 **내비게이션·조작 요소가 콘텐츠와 구별되는 기능 레이어**를 시각화한다.
- 본문·데이터 카드 등 **콘텐츠 레이어 전체에 Liquid Glass를 적용하지 말 것**을 Apple은 명시한다.
- 콘텐츠 내부의 바탕·구획에는 표준 머티리얼이나 일반 색·경계·여백 등을 사용한다.
- 재질 효과는 대비/명료성을 보존해야 하며, '깊이감이 강하다'만으로 좋아지는 것이 아니다.

**디자인 깎기 적용 질문:** 밝기, 블러, 반사, 투명도가 **조작 계층 인식**을 돕는가? 아니면 읽기 성능을 해치는가? 3D 컵 같은 **실제 제품의 물성**을 표현하는 문제와 Apple의 **UI 계층 머티리얼**은 다른 설계 문제다.

## 2. 타이포그래피

- Apple은 SF Pro 계열을 플랫폼별 시스템 서체로 제공하며, 텍스트 크기·언어·접근성·맥락에 따라 시스템 API가 적절한 글꼴을 선택하도록 권장한다.
- 장문의 한국어·숫자·혼합 영문을 웹에 렌더링할 때는 해당 서비스의 웹폰트·한글 대체 폰트·줄바꿈을 **프로젝트별로 별도 확인**해야 한다.
- SF Pro/Figma 원본 폰트를 그대로 일반 웹의 `@font-face` 파일로 복제·번들링하지 않는다. Apple 서체는 별도의 사용 조건이 있다.
- 이 분석에서는 **연결 Figma 파일의 실제 font family/size/line-height/letter spacing 값을 읽지 않았다**.

참고: [Apple Typography HIG](https://developer.apple.com/design/human-interface-guidelines/typography), [Apple Fonts](https://developer.apple.com/fonts/).

## 3. 색과 디자인 토큰 — 아직 비워 두는 게 맞는 부분

Figma 연결 라이브러리 검색에서:
- iOS/iPadOS 27 `variable: color` → **검색 결과 0건**
- iOS/iPadOS 27 `style: Text` → **검색 결과 0건**

이는 **라이브러리에 색 변수나 텍스트 스타일이 전혀 없다는 증거가 아니다.** 해당 조회 조건에서 검색된 항목이 없었다는 뜻이다. 현재 연결된 사용자의 캔버스는 빈 `Page 1`이고, 노드별 `get_variable_defs`로 사용할 실제 대상 컴포넌트도 없었다.

따라서 `Apple 27` 디자인 토큰의 정확한 RGB/HEX/points/spacing/이름/모드 수는 **NOT VERIFIED**. 실제 프로젝트에 복사 가능한 토큰 목록은 생성하지 않는다.

**대신 적용 가능한 원칙**
- 의미 기반 컬러·상태(disabled/selected/focus/error)를 구분하여 대조.
- 광학적 깊이·레이어가 있어도 명도 대비·실제 글자 렌더링과 조작 단서 보존.
- 접근성을 위해 색만으로 위험/성공을 표현하지 않음.
- Figma에서 변수가 확보되면 라이브러리/플랫폼/Light·Dark/고대비/실제 값의 출처를 필드별로 기록.

## 4. 상태·동작 인터페이스

**이름이 확인된 컴포넌트**
- iOS: `Button - Liquid Glass - Text`, `Segmented Control`, `Text Field`, `Alert`, `Sheet - iPhone`, `Row with Swipe Actions`
- macOS: `Button`, `Buttons - Toggle`, `Toggles - Radio Buttons`, `Search`, `Popover`, `Table Rows`

**실제 검증해야 하는 상태 목록 (아직 variant 확인 아님)**

| 상태·전환 | 웹에서 확인할 점 |
|---|---|
| Default/hover/focus | 마우스뿐 아니라 키보드 초점으로 위치·행동이 인식되는가 |
| Selected/active | 현재 선택과 수행 가능한 행동이 구별되는가 |
| Disabled/read-only | 비활성 이유·권한 부족·추가 조건을 오해하지 않는가 |
| Busy/pending/success | UI에 보이는 결과가 실제 저장/반영 상태와 일치하는가 |
| Error/incomplete | 오류·결측·모순이 '0' 또는 '정상'으로 둔갑하지 않는가 |
| Overlay open/close | 열기 전 맥락·포커스·입력 상태를 보존하는가 |
| Reduced motion | 움직임을 줄여도 핵심 의미/이벤트를 잃지 않는가 |

이 표는 디자인 깎기의 **검증 계약**이고, Figma Kit이 해당 variant를 각각 제공한다는 주장은 아니다.

## 5. 물성·색·모션 관련 기존 실험과 대조

| 실험 자료 | Apple HIG에서 가져올 원리 | 복제하면 안 되는 것 |
|---|---|---|
| MUL. 투명 유리컵 | 콘텐츠(컵)와 조작층 분리, 맥락 유지 | 모든 카드의 Liquid Glass화, Apple 원본 광학 효과 강제 |
| 메뉴 룰렛 | 컨트롤과 결과의 상태·역할 구분 | iOS 하단 탭바의 기계적 복제 |
| 환자 모바일 서비스 | 조작 영역과 읽기 영역 구분, 상태 식별 | 의료적 확실성이 없는 내용을 '시스템 승인'처럼 보이게 |
| 의료진 워크스페이스 | macOS의 사이드바/테이블/보조 작업과 같은 작업 패턴 비교 | macOS 창 컨트롤의 웹 페이지 복제 |

## 범위와 검증

- **PASS:** Apple HIG Materials/Fonts/Typographic 자료에서 원칙 확인; 대표 컴포넌트 검색 결과 존재 확인.
- **NOT RUN:** Figma 실제 스타일·변수·Variant 값, Light/Dark 모드 전체·명도 대비·실기기 접근성·렌더 시뮬레이션.
