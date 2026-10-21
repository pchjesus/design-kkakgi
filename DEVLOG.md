# DEVLOG

## v0.1 — 초기 이관 (2026-10-16)

- Private `main`에 지침, 레퍼런스 분석, EXP-001 MUL. 다섯 버전, EXP-002 SAI v0.1·v0.2, 운영 문서를 이관했다.
- 당시 원본 패키지의 SHA-256 매니페스트 검증 결과는 `MANIFEST_SHA256.tsv`에 보존한다.

## v0.1 — Public 전환 및 이미지 정책 변경 (2026-10-16)

- 사용자 승인에 따라 이미지가 포함된 기존 커밋을 부모 없는 새 루트 커밋 `cd715d942d59272dea6d0b6b199c463a561490ff`으로 교체했다.
- 현행 트리에서 이미지 원본·미리보기·스크린샷 32개를 제외하고 코드·문서·피드백·분석 결과를 보존했다.
- EXP-003 계획 문서를 추가했다. 실제 앱 구현은 하지 않았다.
- Public 전환 뒤에도 GitHub Pages·CI/CD·릴리스를 새로 만들지 않았다.

### 검증 기록

| 항목 | 결과 | 근거 |
|---|---|---|
| 이전 `main` 확인 | PASS | 정책 전환 전 HEAD와 전체 트리 확인 |
| 현재 트리 이미지 식별·제거 | PASS | 32개 래스터 이미지 제거, 새 `main` 이미지·ZIP 0개 |
| 텍스트·코드 내 내장 이미지 데이터 | PASS | `data:image` 패턴 미발견 |
| 일반 비밀정보 패턴 | PASS | private key, GitHub token, AWS key, 일반 API key 패턴 미발견 |
| 원본 코드·문서 보존 | PASS | 변경 대상 운영 문서 8개 외 기존 80개 파일의 Git blob SHA 동일 |
| 접근 가능한 Git 참조 | PASS | `refs/heads/main`만 존재; 태그·추가 브랜치·릴리스 없음 |
| Git LFS | PASS | 기존·신규 트리에 LFS pointer 없음, 이미지 파일은 일반 Git blob으로만 존재했음 |
| GitHub Pages·외부 자동 배포 | PASS | Pages 비활성, 워크플로 파일·릴리스 없음 |
| Public 전환 | PASS | GitHub 원격 메타데이터와 설정 화면에서 `public` 확인 |
| MUL·SAI 실제 실행/사용자 검증 | NOT RUN | 이번 정책 전환 범위 밖 |
| 플랫폼 캐시·외부 복사본·미참조 객체 완전 삭제 | NOT RUN | GitHub 가비지 컬렉션·외부 복사본은 즉시 또는 완전 삭제를 보장할 수 없음 |


## 2026-10-17 — SIDE-001 뭐먹지? 디자인 사례 추가

- 별도 `menu-roulette` 웹앱의 사용자 승인 Warm-centered v0.1.5 최종안을 참조하는 작은 디자인 사례를 추가.
- 디자인 실패/선호/부분 채택/후속 마감 판단을 `cases/menu-roulette/LESSONS.md`에 기록.
- 루트 Pages 인덱스에 실행 사이트·사례 소개 링크 추가, `cases/menu-roulette/index.html` 작성.
- EXP-001 MUL. 최신판 및 SAI 프로젝트 경로는 변경하지 않음. EXP-003 계획 문서는 유지.
- 새 앱 코드·사용자 화면 캡처/이미지는 아카이브에 중복 게시하지 않음.
- **검증:** GitHub 파일 링크·카드 연결·원래 링크 유지 여부를 정적으로 확인. 실기기/브라우저 렌더링·Pages 배포 결과는 별도 검증.

## 2026-10-17 — MUL. E7 branch experiment

- 사용자 요청에 따라 `experiment/mul-material-softness`에서 E6-C5-HERO를 개선. main 병합은 사용자 결과 검토 후 결정.
- HERO 높이/글꼴 폴백, 컵 회전 변형, 사진 경계, 읽기 대비, 단발 재조합, 모달 및 색상 동기화 개선.
- 진단·참조·검증·제약: `cases/mul-cup/latest/DESIGN_REVIEW_E7.md`.

## 2026-10-17 — MUL. E8 spatial glass

- 사용자 요청에 따라 우측 정보 폭/행 배치 확장, 같은 높이의 단단한 반동, 테두리 없는 컬러 조작부로 개선.
- 기존 실험 브랜치에 중공 3D 컵·상하좌우/대각 회전·초기화·색상 동기화 추가. 고정된 로컬 Three.js ES module과 SVG fallback 사용.
- 상세 계약·검증·한계: `cases/mul-cup/latest/DESIGN_REVIEW_E8.md`. main 병합 대기.

## 2026-10-17 — MUL. E8 사용자 승인·main 채택

- 사용자 승인에 따라 E8 실험을 main으로 병합. 동시에 추가된 SIDE-001 변경을 보존하며 CURRENT_STATUS/DEVLOG의 추가 기록 충돌을 양쪽 보존 방식으로 해결.
- 제품 코드는 승인된 bff90ca 그대로 유지. 릴리스의 approved/main/고정 route를 갱신하고 의존 파일 해시 검사를 유지.
- `DESIGN_LEARNINGS_E7_E8.md`에 WHY/WHEN/HOW, 지침·레퍼런스 적용표, 폭/물성/재조합/조작부/3D에 관한 수정 경험과 재사용 절차를 기록.
- 범용 v1.2 DRAFT는 변경하지 않음. 인덱스·README·배포 계약·결정 기록에서 현재 채택 상태를 연결.

## 2026-10-20 — KRDS v1.1.0 외부 컴포넌트 레퍼런스 색인

- 사용자가 제공한 `krds-uiux-main.zip` (SHA-256: `e915e378d35e52ff8172c4c98f4f0bfedbd53177a8f9e6ff521298d82fa2bf3b`)의 245개 파일을 정적 조사함.
- `references/krds/`에 허브 `README.md`, HTML 예제 **74개**의 `component_catalog.json`, 용도별 HTML/SCSS/JS 경로 `COMPONENT_GUIDE.md`, 토큰 지도 `TOKEN_GUIDE.md`, 구현·QA 계약 `INTEGRATION_AND_QA.md`, 출처/해시 `SOURCE_PROVENANCE.md`를 추가함.
- `README.md`, `references/README.md`, `AGENTS.md`에 조건부 탐색 진입점을 연결함. 일반 디자인 작업에 KRDS 선로딩 금지, 관련 1~3개 원본만 조회, 필요할 때 세부 파일로 확대하는 규칙을 기록함.
- **정책 유지:** 외부 PNG/SVG/폰트·ZIP·전체 소스 미복제, 기존 실험/앱 코드 변경 없음, Universal v1.2 DRAFT 미변경.
- **PASS (정적/원격):** 74개 색인 경로의 ZIP과 일치성, GitHub 새 문서 6개 및 상위 문서 3개 원격 읽기, 공식 KRDS GitHub 대표 파일 **8개** Git blob SHA 일치, 원본 버전/출처 기록.
- **NOT RUN:** 245개 전체 원격 Git blob 동등성, 모든 GitHub 링크의 HTTP 열림 여부, 실제 브라우저 동작·접근성/시각 회귀·GitHub Pages 반영. 이번 작업은 **레퍼런스 문서 저장**이며 애플리케이션 릴리스가 아님.

## 2026-10-20 — KRDS 사이트·패턴 레퍼런스 확장

- KRDS 공식 `style_05.html`, 기본 패턴 11종의 `global_01~11.html`, 서비스 패턴 5종의 `service_01_01~05_01.html` 상세 페이지를 확인했다.
- `references/krds/LAYOUT_ATLAS.md`: 6단계 그리드/브레이크포인트, 고정·유동 콘텐츠, 좌우 메뉴, 8pt 기반 간격과 별도로 **파생된 페이지 아키타입 L1~L6(가설)** 기록.
- `references/krds/PATTERN_ATLAS.md` 및 `pattern_catalog.json`: 기본 11종·서비스 5종의 직접 링크, 과업-패턴-컴포넌트 결합 탐색.
- `references/krds/REFERENCE_SELECTION.md`: 문제 유형별 selective routing, 2안 비교, KRDS/Apple/기존 미감 레퍼런스 역할 분리 및 향후 Figma 입수 시 라이선스·검증 계약.
- 허브, 루트 README, 레퍼런스 README, AGENTS에 연결. HTML Kit v1.1.0 원본은 복제하지 않음. **Universal v1.2 DRAFT/기존 제품 코드·이미지 정책 미변경.**
- **PASS:** 공식 분류 11+5·레이아웃 표·16개 직접 URL 원문 확인, JSON count/unique, 문서와 상위 링크 원격 읽기 확인.
- **NOT RUN:** 사용자/브라우저 레이아웃 실험, Apple Figma 실제 파일 분석, 패턴 전체 공식 Figma 프로토타입 검증, 제품 기능 회귀(앱 코드 미변경).

## 2026-10-20 — Apple Figma 라이브러리 레퍼런스 인덱스

- 사용자 공유 Figma `HAobgfDkid1Jezh8OYSd6H`의 빈 `Page 1`을 확인하고, **8개 연결 Community 라이브러리**(Apple iOS/iPadOS/macOS 26·27, watchOS 26, visionOS 26, Material 3, Simple DS)를 읽기 전용으로 확인.
- `iOS and iPadOS 27`의 13종 UI 컴포넌트명 검색어와 스타일/변수 질의, `macOS 27`의 9종 UI 컴포넌트명 검색어로 선별 조회. 검색 결과에서 **iOS/iPadOS 52개, macOS 43개, 95개의 서로 다른 이름**을 카테고리로 색인함. 6개 나머지 라이브러리는 등록명만 확인.
- `references/apple/`에 `README.md`, `component_catalog.json`, `COMPONENT_ATLAS.md`, `LAYOUT_AND_PLATFORM.md`, `VISUAL_LANGUAGE.md`, `REFERENCE_SELECTION.md`, `SOURCE_PROVENANCE.md`를 추가. JSON은 중복을 제거한 그룹형으로 압축(원안 27k→6.2k 문자).
- Apple 공식 HIG Layout/Materials/Toolbars/Fonts의 확인된 일반 원리와 **Figma 검색 결과 존재**만을 구분. 원본 Kit 전체 인벤토리/variant/토큰/Apple 공식 파일과의 키 동일성은 미검증.
- **라이선스:** Apple Design Resources/폰트는 Apple 플랫폼 및 별도 계약 제약이 있으므로 원본 프레임·폰트·이미지·SF Symbols/디자인 아트워크를 Public GitHub에 복제하지 않음.
- 루트·레퍼런스 README, AGENTS의 선택적 로딩 규칙, KRDS 레퍼런스 문서를 연계. **범용 디자인 지침 v1.2 DRAFT, 사례 웹사이트, 데이터·상태/이미지 정책은 불변.**
- **PASS:** 연결 8개 라이브러리 확인, Apple 27 컴포넌트 검색, 95개 고유 색인 생성 및 GitHub 파일 원격 재조회.
- **NOT RUN:** Figma 실제 컴포넌트 상세 variant/레이아웃, 타 라이브러리 인벤토리, 시각·상호작용/접근성 A/B 실험, 라이브러리 출처 동일성/개별 실기기 검증.

## 2026-10-20 — 범용 v1.3 모듈형 개정 후보 작성

- 사용자 요청에 따라 v1.2를 원본 보존하고 **별도 `Universal_Visual_Design_UI_UX_Guidelines_v1.3_DRAFT.md`**를 신규 작성. `Universal_Visual_Design_v1.3_QUICK_START_DRAFT.md`·`V1_3_REVISION_AUDIT.md`를 함께 생성.
- 본문 문자 수 **v1.2 25,569 → v1.3 13,450(약 47.4% 감소)**, 줄 443→219. 실제 API 토큰/요금 측정값은 아니며 중복된 상세 사례·외부 컴포넌트 목록을 참고 모듈로 분리함. 접근성, 위험도 L/M/H, 구버전 데이터 호환성·마이그레이션/복구, 상태/승인·공개, 검증 수준은 본문에 보존.
- 새 [디자인 시스템 선택 지도](references/DESIGN_SYSTEM_SELECTION.md) 및 `references/material3/README.md` 생성. 사용자 연결 Figma Material 3 Community Kit에서 Button/Nav Rail/Drawer/Text field/Card/Dialog/Search/Tabs 계열을 선별 검색. Google Android Material 컴포넌트 자료의 M3 Expressive 변화 참고. Kit 전체 인벤토리와 공식 파일 동등성은 NOT RUN.
- 돌봄 플랫폼의 **환자 중심 현재 ACTIVE DRAFT**와 **병원 A1/A2/A3 확장 설계**를 구분. 의료진/환자 역할의 정보 밀도·근거/결측·검토/승인/환자 공개 범위를 범용 UX 원리의 사례로 제시하되 실증 효과 미주장.
- 리뷰 상태: **DRAFT / 사용자 승인 전**. 기존 v1.2 및 제품 코드/정식 사이트/기존 프로젝트 상태 불변. 신규 시안의 실제 사람 대상 사용성·완전한 Figma variants·실기기 검증은 NOT RUN.

## 2026-10-21 — 1~3차 시안 피드백과 v1.3 개정 후보 보완

- 사용자 직접 피드백 1차 3유형 비교, 2차 제품 4건/정보 2건, 3차 제품·정보 각 1건을 대조. 제품의 자연광 계열 색·절제된 세리프/브랜드명 반복, 의미 있는 제목 줄바꿈, 정보형 상단 검색·필터와 목록:상세 가변 폭, 업무형 적절한 정보 위계가 핵심 관찰.
- 이 결과는 **사용자 1인의 시각적 평가**이며 전체 사용성·임상 검증 근거가 아님. 2차 초기 A/B 표시 오류는 구현·테스트 문제로 분리.
- v1.3 DRAFT는 기존 MUST 추가 없이 §3.1 레이아웃·§3.2 타이포·§3.3 색·§6.4 A/B 확인 문장을 **수정**, 이력과 기존 증거 상태 정정. [빠른 카드](guidelines/quick-start/Universal_Visual_Design_v1.3_QUICK_START_DRAFT.md) 및 [개정 감사](guidelines/universal/drafts/V1_3_REVISION_AUDIT.md) 동기화.
- 지침 본문 v1.2 **25,569자**, v1.3 최초 **13,450자** → 1~3차 피드백 개정 후보 **14,136자** (**v1.2 대비 44.7% 축소**). 문자 수이며 실제 토큰 사용량 측정값 아님.
- v1.2 원본, 기존 사례 HTML·서비스 코드/Pages, 기본 지침 채택 상태는 변경하지 않음. **사용자 승인 대기**.

## 2026-10-21 — v1.3 승인·정식 기준 반영 및 운영 지침 v1.2

- 사용자 최종 승인에 따라 v1.3의 문서 상태를 **APPROVED**로 전환하고 `guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md`에 승인본을 신규 등록. `guidelines/quick-start/Universal_Visual_Design_v1.3_QUICK_START.md` 생성.
- 상대 링크를 승인본의 실제 위치에 맞게 갱신하고, 기존 `drafts/` v1.2 및 v1.3 후보 문서를 **변경 없이 보존**함.
- 사용자 제공 프로젝트 운영 지침 v1.1을 `project/PROJECT_OPERATING_INSTRUCTIONS_v1.1_ARCHIVE.md`로 보존, 승인 지침/선택적 KRDS·Apple·Material 3 참조/실험 화면 실제 표시 검증·근거 구분 등을 반영한 `project/PROJECT_OPERATING_INSTRUCTIONS_v1.2.md`를 신규 작성.
- 루트 README, AGENTS, CURRENT_STATUS, DECISION_LOG 및 관련 기본 참조를 현행 v1.3/운영 v1.2에 맞춰 정리. ChatGPT 프로젝트 설정 및 기존 프로젝트 앱/Pages는 **직접 수정하지 않음**.
- **검증 대상:** 문서 존재·상대 링크·규범 보존·DRAFT 아카이브 상태, 운영 문서 기준의 일치. 실제 브라우저/실사용자/토큰 계측과 혼동하지 않음.
