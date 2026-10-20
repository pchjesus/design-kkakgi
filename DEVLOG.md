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
