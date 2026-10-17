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


## SIDE-001 · 뭐먹지? 메뉴 슬롯 (2026-10-17)

- **상태:** 디자인 최종안 채택 · 별도 정식 사이트 운영. 디자인 깎기의 경량 서브 사례.
- 사용자 검토: 청백색 실험의 배경-슬롯 조화 부족, 좌측 정렬 관성, 중앙 집중형과 1.3:.82 비율의 장점, 마지막 패널 높이/아코디언 모션 요구를 기록.
- 현행 앱: [menu-roulette/main](https://github.com/pchjesus/menu-roulette) v0.1.5 / [실행 사이트](https://pchjesus.github.io/menu-roulette/).
- 연구 노트: [cases/menu-roulette/LESSONS.md](cases/menu-roulette/LESSONS.md); 디자인 깎기 루트 GitHub Pages에 실행 링크 카드 추가.
- 동일 기능의 코드 복사본을 별도로 두지 않음. 현행 앱은 메뉴 저장소 main에서만 유지.
- Universal Design v1.2는 **DRAFT 유지**, 연구 사례가 범용 규칙을 자동 개정하지 않는다.

## 브랜치 전용 실험 — E7

`experiment/mul-material-softness`의 latest는 E7-MATERIAL-STUDY 검토 후보이다. main의 E6-C5-HERO와 기존 Pages는 유지한다. 사용자 승인 전 main에 병합하지 않는다. 진단·검증은 `cases/mul-cup/latest/DESIGN_REVIEW_E7.md` 참조.

## 브랜치 전용 후속 실험 — E8

같은 `experiment/mul-material-softness` 브랜치의 검토 후보를 E8-SPATIAL-GLASS로 발전시켰다. 사용자가 실제 3D와 전체 방향 회전을 이번에 명시적으로 요청했으며, 큰 별도 패널 대신 기존 페이지 안에 통합했다. 우측 정보 폭과 조작부를 수정하고 기존 반동 높이는 보존했다. `cases/mul-cup/latest/DESIGN_REVIEW_E8.md` 참고. main의 승인본은 변경하지 않는다.

## 현재 승인본 — MUL. E8-SPATIAL-GLASS (2026-10-17)

사용자가 E8의 main 반영을 명시적으로 승인했다. 앞의 E7/E8 ‘브랜치 전용/병합 대기’ 문구는 실험 당시의 기록이다. 현재 적용 기준은 E8 승인 소스와 `latest/release.json`이다.

- 현행 경로: `cases/mul-cup/latest/`. 홈페이지 카드도 E8로 갱신.
- 디자인 학습: `cases/mul-cup/DESIGN_LEARNINGS_E7_E8.md`.
- 원래 SIDE-001 메뉴 슬롯 카드/문서와 SAI 링크는 보존.
- 소스 병합 후 검사·Pages 실행 결과는 최종 작업 보고에서 확인. 기존의 미실행 검증을 자동 PASS로 승격하지 않음.

### E8 배포 확인 완료

main 병합 커밋 `1ef7174`의 자동 검사와 GitHub Pages 배포가 성공했다. 정식 latest 주소에서 E8 태그·사진 2장·실제 3D 회전/초기화를 확인했고, 3D 모듈 파일도 HTTP 200으로 제공된다. 자세한 근거는 `cases/mul-cup/latest/DESIGN_REVIEW_E8.md`의 main 배포 확인 절을 따른다. 실물 모바일 등 앞서 미실행한 항목은 그대로 미검증이다.
