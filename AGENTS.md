# 작업 계약

> **현행 범용 디자인 기준:** `guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md` (**APPROVED, 2026-10-21**). 일상 작업은 `guidelines/quick-start/Universal_Visual_Design_v1.3_QUICK_START.md`부터, 상세 참조는 필요할 때만 확인한다. **프로젝트 운영 지침:** `project/PROJECT_OPERATING_INSTRUCTIONS_v1.2.md`. 제품별 승인 계약이 우선한다.

## 목적과 권한

- 이 저장소는 상황에 맞는 디자인 판단·구현·검증을 연구한다. 개인 취향을 범용 규칙으로 자동 전환하지 않는다.
- 일반 ChatGPT 채팅은 디자인 개발·이미지 분석·비교·개선을, GitHub는 지침·코드·연구자료·결정 이력 보존을, Work는 저장소 운영 작업을 담당한다.
- 범용 지침의 정식 채택·개정, 핵심 UX·브랜드 방향·기능·저장 구조 변경은 사용자 승인 없이는 수행하지 않는다.
- 새 견본·기능·작업형 웹앱은 명시적으로 선정되기 전까지 생성하지 않는다.

## 우선순위

개별 프로젝트의 승인된 기능·데이터·안전·UX 계약 → 관련 전문 제약 → 범용 디자인 지침 → 프로젝트의 실험·평가·개정 절차 순서로 판단한다.

## 이미지 및 레퍼런스

1. 사용자 제공 이미지는 일반 ChatGPT 채팅에서만 분석한다. GitHub에는 원본·캡처·미리보기·스크린샷·이미지 포함 ZIP을 올리지 않는다.
2. 분석 결과는 타이포그래피, 색상, 질감, 레이아웃, 정보 구조, 표현 목적과 장점·한계·적합/부적합 상황을 텍스트(Markdown/JSON)로 기록한다.
3. 개인 취향과 검증된 설계 원칙을 구분하며, 레퍼런스 분석은 실험으로 검증되기 전까지 후보로 취급한다.
4. 출처는 기록한다. 제작자 또는 원본 URL이 불명확하면 `미확인`으로 표시한다.
5. 자세한 보존·검증 규칙은 `IMAGE_POLICY.md`를 따른다.

## 변경·검증

1. 대상 프로젝트의 README·운영 문서·승인된 제약과 현재 파일 상태를 확인한다.
2. 변경 전 보존할 기능·데이터·상태와 위험을 고정하고, 코드 변경과 구조 정리를 가능한 한 분리한다.
3. 평가는 미적 완성도·맥락 적합성·사용성/접근성·기능/상태 정확성을 분리하며, 결과를 `PASS` / `FAIL` / `NOT RUN` / `N/A`로 기록한다.
4. 실행하지 않은 검증은 통과로 기록하지 않는다. 과거 테스트 기록과 현재 실행 결과를 구분한다.
5. 이력 정리 전에는 보존 파일 목록·체크섬·참조를 확인하고, 새 이력에서는 제외할 파일이 도달 가능하지 않은지 확인한다.

## MUL. GitHub Pages 최신본 동기화

- **고정 실행 경로:** 루트 `index.html`의 MUL. 버튼 → `cases/mul-cup/latest/`. 과거 버전 링크로 되돌리지 않는다.
- **매번 함께 갱신:** EXP-001 MUL.의 새 승인 HTML을 GitHub에 게시하거나 버전을 갱신할 때 `cases/mul-cup/latest/index.html`(실행 가능한 공개용 전체 HTML)과 `cases/mul-cup/latest/release.json`을 같은 작업에서 반드시 동기화한다. 이전 버전의 스냅샷은 보존한다.
- **E8 3D 배포 계약:** 승인된 `glass-3d.js`, 로컬 Three.js ES module, MIT 라이선스, 의존 파일 해시를 HTML·release.json과 함께 보존·게시한다. 사용자의 최신 E8 승인은 과거의 큰 별도 3D 패널 거부와 구분한다. 세부 계약은 `cases/mul-cup/PUBLISHING.md` 참조.
- **배포 전 점검:** `python scripts/check_mul_latest.py`, 관련 기능 회귀, PC·모바일, 저장·복원, 접근성, Pages 실제 공개 URL을 확인한다. 미실행 사항은 `NOT RUN`으로 기록한다. 게시 절차는 `cases/mul-cup/PUBLISHING.md` 참고.
- **자체 생성 이미지 승인 예외:** 사용자가 MUL. 자체 제작 사진 2장의 공개를 승인했으므로 `cases/mul-cup/latest/index.html`에는 해당 사진을 최적화한 WebP 내장 이미지를 허용한다. `release.json`에 SHA-256·출처를 기록하고 `scripts/check_mul_latest.py`로 검사한다. 외부 레퍼런스, 스크린샷, 이미지 ZIP 및 다른 프로젝트까지 자동 허용하지 않는다. 원본 로컬 HTML은 별도로 보존한다.


## SIDE-001 메뉴 슬롯 운영

- `cases/menu-roulette/`는 연구용 사례 문서·소개 페이지이며, 실행 앱 코드의 복제본이 아니다.
- 앱의 **단일 진실 원본은 `pchjesus/menu-roulette` main**; 디자인 깎기 홈페이지의 SIDE-001 카드는 정식 GitHub Pages 실행 URL로 연결한다.
- 이후 발견하는 디자인 교훈은 사용자 관찰·설계 가설·검증 결과를 구분하여 `LESSONS.md`에 적는다. 현재 **승인된 Universal v1.3**을 사용자 요청 없는 실험 피드백으로 자동 개정하지 않는다. v1.2는 이력용으로 보존한다.

## KRDS 구현 레퍼런스 고속 탐색

- 요청이 KRDS·공공 UI·컴포넌트·토큰 분석에 해당할 때만 `references/krds/README.md`를 진입점으로 사용한다. 일반 디자인 작업에 자동 로드하지 않는다.
- `component_catalog.json`에서 정확한 HTML 파일 하나를 특정 → 필요한 경우에만 `COMPONENT_GUIDE.md`의 관련 SCSS·JS·`TOKEN_GUIDE.md`로 범위를 넓힌다. 245개 원본이나 축약 번들 전체를 선로딩하지 않는다.
- 이 저장소는 외부 KRDS 원본 HTML·CSS·JS·폰트·이미지 미러가 아니라 **출처/경로/분석/검증 가이드**를 보관한다. 공식 GitHub `main`은 변경될 수 있으므로 `SOURCE_PROVENANCE.md`의 v1.1.0 ZIP 해시와 구별한다.
- KRDS 적용은 프로젝트별 명시 승인과 접근성·기능 회귀 검증이 필요한 **선택적 참조**다. 승인된 범용 지침 v1.3, 프로젝트 UX, 이미지 정책을 자동 변경하지 않는다.

## KRDS 페이지·패턴 아틀라스 활용 규칙

- 사용자의 문제가 **홈페이지 구조·페이지 다양화·레이아웃·정보 구조**이면 `references/krds/LAYOUT_ATLAS.md`와 필요 시 `PATTERN_ATLAS.md`를 먼저 읽고, 해당 세부 패턴 URL을 확인한다. 개별 UI 구현 문제에서만 컴포넌트 색인/SCSS/JS를 바로 읽는다.
- **탐색은 선택적으로 진행한다.** 페이지 전체 문제 → 공식 레이아웃/패턴 → 컴포넌트/토큰 필요한 것만. 모든 참고 문서를 매번 로드하지 않는다.
- `references/krds/REFERENCE_SELECTION.md`의 근거 구분·비교/거절 조건을 준수한다. KRDS 정량값/공식 원문과 디자인 깎기가 제안한 L1~L6 아키타입(가설)을 혼동하지 않는다.
- 기존 사용자 확정 선호·프로젝트 기능·브랜드 판단 우선. Apple 27 Figma 연결 라이브러리의 일부 컴포넌트 이름은 확인했으나 원본 전체·variants·토큰/공식 출처 동등성은 미검증이다. 라이선스/폰트/이미지 공개 범위를 검토한다.

## Apple Figma 레퍼런스 선택적 탐색

- **진입 조건:** Apple HIG, iOS/iPadOS/macOS 컨트롤·레이아웃, 네이티브와 웹 UX 비교, Liquid Glass 계층 연구가 필요한 경우에만 `references/apple/README.md`를 읽는다. 일반 디자인 작업에서 선로딩하지 않는다.
- **탐색 경로:** 사용자 과업 → `LAYOUT_AND_PLATFORM.md` 또는 `COMPONENT_ATLAS.md`에서 해결할 문제를 찾기 → `component_catalog.json`의 iOS/iPadOS 27·macOS 27 중 **확인된 이름 1~3개** 특정 → 필요할 때만 연결 Figma 라이브러리의 해당 범위를 조회. 대량 반복 검색으로 사용자 무료 계정 한도 낭비 금지.
- 시각 계층·시스템 컨트롤·사용자 주도권 등의 **일반 원리**만 참고하고, Apple 원본 UI Kit의 아트워크/프레임/폰트·SF Symbols/컴포넌트 원본 코드를 일반 웹에 복제하거나 GitHub Public에 재배포하지 않는다. Apple Design Resources License와 SF 폰트 별도 조건 준수.
- 연결 라이브러리의 이름/검색 결과를 확인한 것은 사실이나, 전체 원본 Apple Figma UI Kit의 세부 레이어·variant/토큰값이나 Apple 공식 게시본과의 동등성은 **미검증**이다. `SOURCE_PROVENANCE.md`를 확인해 정확히 표기한다.
- `references/apple/REFERENCE_SELECTION.md`에서 KRDS와 Apple의 역할을 분리해 적용하고, 사용자 선호/기존 기능·안전 계약을 우선한다. 승인된 범용 지침 v1.3 및 프로젝트 UX를 자동 개정하지 않는다.

## 범용 v1.3 APPROVED — 효율·검증 계약

- **현행 기준:** `guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md`은 **2026-10-21 사용자 정식 승인본**이다. `guidelines/universal/drafts/`의 v1.2 및 v1.3 DRAFT는 **이력·비교용**, 기본 기준이 아니다.
- **진입 비용:** 일반 작업은 `guidelines/quick-start/Universal_Visual_Design_v1.3_QUICK_START.md`에서 시작하고, 중요 신규 설계/접근성/상태·저장·권한 변경은 본문에서 필요한 MUST를 확인한다. 전체 레퍼런스 선로딩은 금지하며, 필요 시 `references/DESIGN_SYSTEM_SELECTION.md`로 KRDS/Apple/Material 3 중 적합한 곳만 조회한다.
- **운영 절차:** `project/PROJECT_OPERATING_INSTRUCTIONS_v1.2.md`가 현행 프로젝트의 실험·비교·검증·개정 계약이다. A/B 실험에서 선택한 시안과 변수가 **실제로 렌더링·적용되는지** 확인한 후 평가한다. 구현 결함/평가자의 취향/지침 결함을 구분한다.
- **출처 경계:** Apple 27 Figma는 일부 검색된 이름(95개)만 확인되었고, Material 3도 선별된 Community 라이브러리 명칭만 확인했다. 두 시스템의 전체 variant·토큰값과 공식 파일 동일성은 미검증. `references/apple/SOURCE_PROVENANCE.md`, `references/material3/README.md` 참조.
- **돌봄 플랫폼 근거 경계:** 환자 중심 PRD v0.2는 현재 ACTIVE DESIGN DRAFT; 병원 A1/A2/A3는 별도 연구/확장/시연 설계. 실제 의료기관 제휴·임상/고령 환자 검증이나 안전 인증으로 간주하지 않는다.
- **안전 계약:** 비용 절감을 이유로 접근성, 기존 상태·데이터 호환성, 민감정보, 실제 검사 근거, 안전·권한 계약을 생략하지 않는다.
- **권한 경계:** v1.3 채택은 다른 제품의 디자인·저장 구조·브랜드·기능 또는 Pages 배포를 일괄 승인하지 않는다. 별도 사용자 요청과 제품별 검증 계약이 필요하다.
