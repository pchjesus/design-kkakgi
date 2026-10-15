# EXP-001 MUL. — GitHub 동기화 검증 기록 (2026-10-16)

## 배경
사용자가 초본부터 Refined까지 정리한 MUL. 통합 백업을 `pchjesus/design-kkakgi` GitHub 저장소에 반영하도록 요청했다. 업로드 전에 원격 `main`과 로컬 아카이브를 비교했다.

- 원격 저장소: https://github.com/pchjesus/design-kkakgi (Public, `main`)
- 비교 기준 원격 HEAD: `5e968daefae5b2070c2b20487992c77d137f52bd`
- 로컬 원본: `MUL_Project_All_Versions_Feedback_2026-10-16.zip`
- 로컬 원본 ZIP SHA-256: `8e2d3916bbe1aaf18c5d34f426732d6e96d6890d0264f9ee04448b5d776ad30f`
- 주의: SHA-256은 로컬 보존용 ZIP의 해시이다. ZIP은 이미지 포함 때문에 GitHub에 업로드하지 않았다.

## 버전별 실행 HTML 대조

다음 파일의 Git blob SHA-1이 로컬 통합 아카이브의 파일 바이트로 직접 계산한 값과 **모두 일치**했다.

| 버전 | 경로 (아래 모든 경로는 `cases/mul-cup/` 기준) | Git blob SHA-1 |
|---|---|---|
| 01 v1.1 Initial | `versions/01_v1.1_Initial/site/index.html` | `4836ff3371c1c8b444edfa228912117191a48f28` |
| 02 v1.1 Animated | `versions/02_v1.1_Animated/site/index.html` | `d23941a63bc7428cc1de86389030cdc69c2fd998` |
| 03 v1.2 Catalog | `versions/03_v1.2_Catalog/site/index.html` | `4e7864ba2604e61f1fc2e838798c7d14f49cbf8d` |
| 04 v1.2 Rework | `versions/04_v1.2_Rework/site/index.html` | `3eb9b8df39d23591adb61c9ebefd033d680f1941` |
| 05 v1.2 Refined | `versions/05_v1.2_Refined/site/index.html` | `fdc6d060e9fe5fa6d884a5487e809ac7c35a73fa` |

## 기록·검증 자료 대조

추가로 **13개 문서/검증 파일**을 로컬 보존본과 원격 저장소에서 대조해 Git blob SHA 일치를 확인했다.

- `HISTORY_AND_FEEDBACK.md`, `USER_FEEDBACK_ORIGINAL.md`, `COMPARISON_AND_LESSONS.md`, `SOURCE_PROVENANCE.md` (4개)
- `versions/01_v1.1_Initial/tests/validation_original.txt`
- `versions/02_v1.1_Animated/tests/motion_validation_original.txt`
- `versions/03_v1.2_Catalog/docs/DESIGN_REVIEW_original.md`
- `versions/03_v1.2_Catalog/tests/test_results.json`
- `versions/04_v1.2_Rework/docs/MUL_DESIGN_LEARNINGS_2026-10-16.md`
- `versions/04_v1.2_Rework/docs/DESIGN_AND_TEST_REPORT.md`
- `versions/05_v1.2_Refined/docs/ITERATION_REVIEW.md`
- `FILE_SOURCE_MAP.tsv`, `FILE_MANIFEST_SHA256.tsv` (2개)

검증 범위는 실행 HTML 5개 + 문서·테스트 파일 13개, 총 18개이다. 저장소 전체 파일의 전수 대조로 해석하지 않는다.

## 정책 및 판단

- `IMAGE_POLICY.md`, `AGENTS.md`에 따라 PNG/GIF/스크린샷/이미지 포함 ZIP/내장 이미지 바이트는 GitHub에 추가하지 않았다.
- 5개 버전 실행 HTML과 확인한 피드백·테스트 파일은 **이미 동일한 내용으로 저장되어 있으므로 재업로드하지 않았다**.
- 지침 v1.2의 DRAFT 상태와 기존 MUL. 코드·UX·저장 키, 기타 실험 사례는 변경하지 않았다.
- 이미지 제거로 기존 HTML의 외부 이미지 참조가 깨질 수 있다는 한계는 `cases/mul-cup/README.md` 및 `CURRENT_STATUS.md`에서 계속 고지한다.

## 이번 점검 결과

| 항목 | 판정 | 근거 |
|---|---|---|
| 원격 저장소·공개 상태·`main` 확인 | PASS | GitHub 저장소 메타데이터 |
| 5개 실행 HTML 내용 대조 | PASS | Git blob SHA-1 직접 대조 |
| 13개 문서·테스트 파일 대조 | PASS | Git blob SHA-1 직접 대조 |
| 이미지 포함 ZIP 업로드 제외 | PASS | 이미지 정책을 따른 변경 범위 |
| 전체 트리의 무결성 전수 검증 | NOT RUN | 확인한 18개 파일로 범위 제한 |
| 실제 페이지 시각 재현·기능 재실행 | NOT RUN | 이번 작업은 동기화 검증이며 브라우저 테스트가 아님 |
| 실물 제품 사양·사용자 사용성 검증 | NOT RUN | 실험 콘셉트와 별도 과제 |

## 결과

MUL. 초본부터 Refined까지 주요 코드와 피드백·검증 기록은 이미 최신 통합 백업과 일치한다. **중복 업로드 없이 본 동기화 확인 기록만 추가**했다.

전체 이미지 포함 ZIP은 이 저장소의 보관 대상이 아니므로, 원본 미리보기와 아카이브는 대화에 전달된 파일에서 별도로 관리한다.
