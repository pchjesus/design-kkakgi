# 디자인 깎기

콘텐츠·목적·이용자·매체·기능에 맞는 디자인 판단과 구현·검증 능력을 연구하는 독립 저장소다. 개인 취향을 보편 규칙으로 자동 전환하지 않는다.

## 색채 구성·제품 물성 레퍼런스 (2026-11-12)

- [**COLOR-001 — 색면 비율과 대비**](references/COLOR_BALANCE_CONTRAST_NOTE_v0.1_20261110.md): 버터크림/그린/핑크 선호, 블루/라임 긍정, 60/30/10의 비강제적 참고.
- [**COLOR-002·003 — 색채 선호 및 기능적 활용 사례 9장**](references/COLOR_APPLICATION_MATERIAL_ATLAS_v0.1_20261112.md): 샌드/브라운/일렉트릭 블루를 가장 선호한 사용자 평가와, 선호도는 낮지만 부품 설명·제품 물성·색과 정보 위계 측면에서 연구할 만한 6개 팔레트. 원본 이미지는 게시하지 않음.

## UI 인디케이터·모션 레퍼런스 (2026-11-05)

- [**인디케이터 9종 및 추가 마이크로인터랙션 18종 — 구현·설계 자료실**](references/MOTION_INDICATOR_ATLAS_v0.1_20261105.md): 진행·선택·값 평가·OS 제스처의 차이, 실제 UI 사례, 공개 구현 자료/모션 갤러리와 후속 검증 계획. 외부 자산·영상 미게시. **연구 DRAFT이며 앱/지침 변경 아님.**
- [**UI 패턴 현장 아틀라스 — 신규 12개 캡처 분류와 선택 기준**](references/UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md): 108개 항목(중복 포함)의 출처별 명칭과 실무 선택표, 로딩·빈 상태·입력·알림·시각 스타일·행동 심리 분리. 앞선 9종 심층 아틀라스와 상호 참조.
- [**UI 움직임·전환·완료 피드백 심층 근거 (추가 6장·54항목)**](references/UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md): 텍스트 모션·화면 이동·iOS 피드백·완료 표시·헷갈리는 컴포넌트 비교를 공식 구현 자료와 연결. 원본 소셜 영상의 실제 프레임은 미검증.
- [**화면 배치·앱 첫 사용 UX 아틀라스 (3장·27칸)**](references/UI_LAYOUT_FIRST_USE_ATLAS_v0.1_20261111.md): Hero/Bento/Split/Magazine 등 배치 9종, Splash/Onboarding/Permission 등 첫 사용 9종, 기존 iOS 피드백 9종 중복 연계. 원본 영상·실기기 NOT RUN.
- [**날짜 선택·행동심리 보강 (2장·18칸)**](references/UI_DATE_SELECTION_BEHAVIOR_ATLAS_v0.1_20261111.md): Calendar/Wheel/Date range/Time slots/Recurrence 등 날짜 UX 9종 신규 정리, 행동심리 9종은 기존 분류와 연결해 심리 효과 과장·기만적 패턴의 위험을 보강.
- [**텍스트 모션 실험 01 — 페이드·스크램블 사용자 평가**](references/TEXT_MOTION_LAB_NOTE_01_20261108.md): 짧은 단회 실험의 실제 취향 반응과 구현 한계, 이후 레퍼런스 중심 운영 방침을 기록. **기존 앱/사이트는 변경 없음.**

## 디자인 깎기의 출발점 — ORIGIN-001

- [**심장의 전도계: 초기 교육용 시뮬레이터**](references/ORIGIN_REFERENCE_CARDIAC_SIMULATOR_v0.1_20261022.md) — 사용자에게 디자인 탐구를 시작하게 만든 기원 레퍼런스. 학습에 적합한 색채·여백·정보 위계·조작 구조의 강점과, 정적 이미지로 검증할 수 없는 인터랙션·임상 정확성·접근성을 분리한 기록이다. **스크린샷은 저장소에 게시하지 않는다.**

## 이용 구분

- 일반 ChatGPT 채팅: 이미지 분석, 견본 개발, 비교와 개선
- GitHub: 지침, 코드, 연구자료, 결정 이력 보존
- Work: 초기 구축·정책 전환 같은 저장소 운영 작업
- 사용자: 방향 결정과 지침의 정식 채택 승인

## 구성

- `guidelines/`: **승인된 범용 v1.3**, 보존된 v1.2·v1.3 DRAFT, 빠른 실행 카드, 전문 제약과 실험 이력
- `references/`: 텍스트 기반 레퍼런스 분석·출처·검증 이력
- `cases/mul-cup/`: EXP-001 제품·홍보형 MUL. 물컵 사이트의 다섯 버전
- `cases/sai-blog/`: EXP-002 정보·콘텐츠형 SAI 블로그 v0.1·v0.2
- `cases/work-app/`: EXP-003 작업·도구형 사례의 계획 문서
- `cases/menu-roulette/`: SIDE-001 점메추·저메추 메뉴 슬롯 UI의 디자인 피드백·비교·교훈 (앱은 별도 저장소에서 실행)
- `decisions/`: 사용자 승인 운영 결정
- 루트 운영 문서: `AGENTS.md`, `DEVLOG.md`, `CURRENT_STATUS.md`, `IMAGE_POLICY.md`

## 이미지와 출처

이미지 원본·미리보기·스크린샷은 저장소에 보관하지 않는다. ChatGPT 채팅에서 분석한 뒤 텍스트 분석 결과와 출처만 이관한다. 세부 절차와 한계는 [IMAGE_POLICY.md](IMAGE_POLICY.md)를 따른다.

`MANIFEST_SHA256.tsv`와 사례별 매니페스트는 초기 이관 당시의 **원본 보존 기록**이다. 이미지 항목이 기록에 남아 있어도 현재 트리에 이미지 바이트가 존재한다는 뜻은 아니다.

현재 범용 기준은 **[v1.3 APPROVED](guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md)**이다(2026-10-21 사용자 승인). 새 개정이나 다른 제품에의 적용은 별도 승인·검증이 필요하다.

## KRDS 코드 레퍼런스

- [KRDS HTML Component Kit v1.1.0 탐색 허브](references/krds/README.md) — 74개 컴포넌트 색인, 토큰 지도, HTML/SCSS/JS 경로와 검증 규칙. **원본 소스·폰트·아이콘을 저장소에 복제하지 않음.**
- 외부 참고자료는 승인된 v1.3의 자동 개정이나 개별 프로젝트 UX 표준 채택을 의미하지 않는다.

## KRDS 사이트 구조·서비스 패턴 자료

- [레이아웃 아틀라스](references/krds/LAYOUT_ATLAS.md), [기본 11종·서비스 5종 패턴](references/krds/PATTERN_ATLAS.md), [레퍼런스 선택 프로토콜](references/krds/REFERENCE_SELECTION.md) — 홈페이지·서브페이지 구조부터 사용자 과업, 세부 UI로 내려가는 설계 탐색.
- 디자인/UX 가설과 공식 KRDS 원칙을 구분하며, 승인된 범용 **v1.3**이나 프로젝트 UI를 자동 변경하지 않는다.

## Apple Figma 디자인 레퍼런스 (2026-10-20)

- [Apple Figma 레퍼런스 허브](references/apple/README.md): iOS·iPadOS 27 및 macOS 27의 **실제로 검색된 95개 선별 컴포넌트**를 용도별 카테고리로 탐색
- [컴포넌트 아틀라스](references/apple/COMPONENT_ATLAS.md) · [레이아웃/플랫폼 구조](references/apple/LAYOUT_AND_PLATFORM.md) · [시각 언어](references/apple/VISUAL_LANGUAGE.md) · [Apple × KRDS 선택 규칙](references/apple/REFERENCE_SELECTION.md)
- 연결된 Figma 라이브러리의 선별 컴포넌트 이름만 색인화하며 **원본 디자인/폰트/이미지 등은 재배포하지 않음**. 개별 프로젝트 코드는 자동 변경하지 않는다.

## 범용 지침 v1.3 정식 채택 (2026-10-21)

- [**범용 v1.3 승인본 — 현행 기준**](guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md) · [**빠른 실행 카드**](guidelines/quick-start/Universal_Visual_Design_v1.3_QUICK_START.md).
- [프로젝트 운영 지침 v1.2](project/PROJECT_OPERATING_INSTRUCTIONS_v1.2.md) · [이전 운영 지침 v1.1 보존](project/PROJECT_OPERATING_INSTRUCTIONS_v1.1_ARCHIVE.md).
- [v1.2 과거 DRAFT](guidelines/universal/drafts/Universal_Visual_Design_UI_UX_Guidelines_v1.2.md) · [v1.3 실험 초안](guidelines/universal/drafts/Universal_Visual_Design_UI_UX_Guidelines_v1.3_DRAFT.md) · [1~3차 실험/개정 감사](guidelines/universal/drafts/V1_3_REVISION_AUDIT.md).
- [KRDS × Apple × Material 3 × 돌봄 플랫폼 선택 지도](references/DESIGN_SYSTEM_SELECTION.md) · [Material 3 선별 조사](references/material3/README.md).
- **범위:** 문서 기준과 운영 절차의 승인·전환만 수행. 기존 실서비스 코드, 브랜드, 데이터/저장, GitHub Pages 동작을 일괄 변경하거나 배포하지 않음. ChatGPT 프로젝트 설정의 맞춤 지침/첨부물은 사용자가 별도 갱신해야 한다.

## Creative Coding · 인터랙티브 디자인 신규 참고자료 (2026-10-26)

- [Creative Coding 선택형 탐색 허브](references/creative-coding/README.md): Castle Jelly, Anime.js, Coolors, Codrops의 역할·한계·출처.
- [상황별 디자인/개발 지시문과 검증 플레이북 v0.1 DRAFT](references/creative-coding/INTERACTION_PLAYBOOK_v0.1_DRAFT.md): 행동·상태·모션·시뮬레이션 명세와 사용 시점.
- **연구 참고자료만 추가.** Universal v1.3 APPROVED / 운영 v1.2, 기존 프로젝트 코드와 GitHub Pages 배포는 변경하지 않음.
