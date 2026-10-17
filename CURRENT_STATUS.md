# CURRENT STATUS

## 현재 단계

- 저장소 운영 정책 전환: **COMPLETED** — 이미지 없는 새 Git 이력과 Public 전환 완료
- 범용 시각 디자인 지침: v1.2 **DRAFT** 유지
- EXP-001 MUL.: 다섯 버전 코드·문서·피드백·검증 기록 보존. 미리보기·공유 이미지 제거에 따른 화면 재현 영향은 사례 README에 기록됨.
- EXP-001 MUL. 동기화(2026-10-16): 통합 백업과 5개 실행 HTML·13개 문서/검증 파일 Git blob SHA 일치 확인. 동일 파일 재업로드 없이 [동기화 검증 기록](cases/mul-cup/SYNC_REVIEW_2026-10-16.md) 추가. 이미지 포함 ZIP은 기존 이미지 정책에 따라 제외.
- EXP-002 SAI: v0.1·v0.2 코드·문서 보존. 서로 다른 localStorage 키와 자동 이전 부재는 변경하지 않음.
- EXP-003 작업형 웹앱: `PLANNED / NOT STARTED`

## 다음 일반 ChatGPT 채팅의 시작점

1. 새 사례의 문제·가설·성공/실패 기준을 먼저 정한다.
2. 기존 EXP-001·002의 회고 자료를 통제된 신규 실험이나 사용자 연구로 과장하지 않는다.
3. 이미지가 필요하면 채팅에 업로드해 분석하고, 결과와 출처만 텍스트로 정리한다.
4. 작업형 웹앱의 주제가 확정되기 전에는 구현을 시작하지 않는다.

## EXP-001 MUL. 최신 GitHub Pages 미리보기 (2026-10-17)

- **GitHub 고정 실행 파일:** `cases/mul-cup/latest/index.html` — E6-C5 + 승인된 HERO 최초/상향 재진입 모션이 들어 있는 공개용 버전.
- **메인 카드:** 루트 `index.html`의 MUL. 실행 링크를 `./cases/mul-cup/latest/`로 변경. 이후 최신본은 이 고정 경로를 갱신한다.
- **사진 제한:** `IMAGE_POLICY.md` 유지. 새 GitHub HTML은 2장의 이미지 바이트를 포함하지 않는 공개 미리보기이며, 사진을 포함한 로컬 완전본과 다르다. 역사적 아카이브는 그대로 보존.
- **검증:** Chromium 1440/390/320px에서 공개 미리보기 기본 조작·HERO 재진입·모션 감소 테스트 PASS. 파일 동기화 및 이미지 미포함 정적 검증 PASS. GitHub Pages 외부 실제 응답과 브라우저 저장 영속성은 **NOT RUN**.
- **후속 릴리스 동기화:** `AGENTS.md`, `cases/mul-cup/PUBLISHING.md`, `cases/mul-cup/latest/release.json`, `scripts/check_mul_latest.py` 및 연계 Actions 확인.


## EXP-001 MUL. 생성 이미지 포함 최신 릴리스 (2026-10-17 · 사용자 정책 수정)

- 사용자는 MUL. 사이트에 사용된 사진 2장이 해당 프로젝트를 위해 생성된 이미지임을 확인하고 GitHub 게시를 승인함. 외부 레퍼런스·스크린샷·SAI 등에는 적용되지 않는 예외.
- **현재 온라인 실행 파일:** `cases/mul-cup/latest/index.html` — E6-C5 HERO 통합본, 승인된 사진 2장 고품질 WebP 내장, 기존 정보·회전·구매 기능 보존.
- **원본:** `MUL_E6C5_HERO_APPROVED_INTEGRATED.html` 로컬 보존. GitHub 파일은 2개 사진의 압축 표현만 다르다.
- 루트 `index.html`은 고정 `latest/` 경로를 사용. 원본 아카이브 5개를 수정하지 않음.
- 검증 스크립트·릴리스 메타·워크플로·정책을 새 이미지 예외에 맞게 갱신함. 실제 Pages 서비스 검증 상태는 별도 확인하며 미검증은 PASS로 처리하지 않는다.
- **이전 섹션의 ‘사진 제한/사진 없는 공개 미리보기’는 이 갱신 이전의 역사적 상태임. 현재 적용 정책은 위 기록과 `IMAGE_POLICY.md` 참조.**
