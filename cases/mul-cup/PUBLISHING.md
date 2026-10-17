# EXP-001 MUL. — GitHub Pages 최신 미리보기 게시 계약

## 현재 상태 (2026-10-17)

- **최신 승인 개발 기준:** `MUL_E6C5_HERO_APPROVED_INTEGRATED.html` (E6-C5 본편 + 승인된 HERO 최초/재진입 모션)
- **GitHub 실행 대상:** `cases/mul-cup/latest/index.html`
- **메인 화면 실행 링크:** 루트 `index.html` → `./cases/mul-cup/latest/`
- **버전 메타:** `cases/mul-cup/latest/release.json`
- **과거 비교 아카이브:** `cases/mul-cup/versions/` 그대로 유지. Refined를 최신본으로 간주하지 않는다.
- **현재 GitHub 버전의 제한:** 승인된 사진 2장을 GitHub 이미지 보관 정책에 따라 제거하고 블루 톤 CSS 배경으로 대체했다. **사진, 재질감, 사진-배경 블렌딩은 완전한 본편과 같지 않다.** 사진을 내장한 원본 HTML은 GitHub에 없다.
- **3D 모델:** 사용자 거절에 따라 배포/통합하지 않았다. THE COLORS의 기존 2.5D 조작은 유지한다.
- **범용 지침:** v1.2 DRAFT 그대로.

## 다음 GitHub 업데이트 시 반드시 함께 수행

1. 개발 시작 시 `cases/mul-cup/latest/index.html`과 `release.json`을 읽고, 대화에 있는 승인 원본과 실제 파일을 대조한다. 과거 GitHub 버전을 최신으로 오인하거나 처음부터 다시 만들지 않는다.
2. 새 본편은 원본을 별도로 보존하고, 현재 승인 사항(정보 구조·카피·HERO·구매·저장·키보드·모바일·모션 감소)을 확인한다.
3. 새 버전을 **GitHub에 반영하는 같은 작업에서** `cases/mul-cup/latest/index.html`의 공개용 최신 소스 전체를 갱신하고 `release.json`의 release_id/출처를 동기화한다. 루트의 `latest/` 링크는 변경하지 않는다.
4. 원본 이미지·스크린샷·이미지 내장 HTML·이미지 포함 ZIP을 GitHub에 올리지 않는다(`IMAGE_POLICY.md`). 온라인 공개판은 이미지 없는 상태임을 안내하고 시각적 차이를 숨기지 않는다. 공개판을 사진까지 온전히 보이게 하려면 **별도의 승인된 외부 이미지 호스팅/정책 변경**이 먼저 필요하다.
5. `python scripts/check_mul_latest.py`를 실행하여 stable link·메타·이미지 정책·핵심 기능 코드 존재를 확인한다. UI 변경 시 Chromium에서 1440/390/320px, 최초/재진입 HERO, 구매·장바구니·키보드·저장/복원을 변경 위험에 맞게 재검증한다.
6. GitHub `main`에 반영된 뒤 Pages 실행 URL을 별도로 열어 최신판 배포 여부를 확인한다. 실접속 미검증은 `NOT RUN`으로 남긴다. 배포 실패 시 커밋 SHA, Pages 설정, 웹 콘솔을 점검하고 기능을 임의 삭제하지 않는다.

## 같은 링크를 쓰는 이유

https://pchjesus.github.io/design-kkakgi/cases/mul-cup/latest/

위 경로는 고정이다. 후속 릴리스는 기존 HTML을 덮어쓰되 기존 과거 버전의 아카이브를 지우지 않는다. 메인 프로젝트 목록은 항상 그 경로로 연결된다. GitHub Pages가 `main` 루트로 배포되도록 설정돼 있다면 이후 푸시 시 같은 URL의 내용이 갱신된다. Pages 배포 설정과 실제 공개 URL 응답은 별도로 확인해야 한다.

## 이번 검증 범위

- **PASS:** 현재 공개용 HTML의 1440/390/320px Chromium DOM 렌더링·가로 넘침 없음, HERO 최초/재진입, 색상 선택, 회전·각도 초기화, 구매 패널, 장바구니, 합계, 삭제와 FAQ, reduced motion (로컬 테스트 기록).
- **PASS:** 이미지 바이트를 제외했으며 `data:image`가 없다는 정적 검사.
- **NOT RUN:** GitHub Pages 실제 HTTPS 응답, 외부 웹폰트/모바일 실기기, 실제 배포 origin의 새로고침·저장 영속성.
- **N/A:** 사진 원본의 온라인 표현 비교(이미지 정책으로 사진 제외).

## 판단

이번 업로드는 **최신 기능을 공개 경로에 연결하는 작업**이다. 온라인 사진 재현 품질이 본편과 같다고 주장하거나, 사진 제외를 원래 디자인의 최종 의도로 취급하지 않는다.
