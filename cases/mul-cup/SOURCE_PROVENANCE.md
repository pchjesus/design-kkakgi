# 파일 출처 및 보존 방식

- `FILE_SOURCE_MAP.tsv`: 원본 파일 경로 또는 원본 ZIP 내부 경로 → 정리된 사본 경로. 파일 단위 기록.
- `FILE_MANIFEST_SHA256.tsv`: 정리된 아카이브 파일의 크기와 SHA-256.
- 01·02의 원본 배포 ZIP에서 초기 실행 HTML을 추출하였기 때문에 후속 작업 폴더의 덮어쓰기 영향을 피했다.
- 03의 `site/index.html`: `MUL_Cup_v1.2.html`, 04는 `MUL_Cup_v1.2_Rework.html`, 05는 `MUL_Cup_v1.2_Refined.html`을 기준으로 한다.
- 04 `source/intermediate_index_from_working_folder.html`은 별도 작업 폴더에 있던 중간 파일이므로 **최종 HTML과 동일한 것으로 오인하지 말 것**.
- `source/`, `tests/`와 `previews/`는 원래 당시 산출물로, 별도 실행 검증을 이 자리에서 새로 수행했다는 뜻은 아니다.
- `original_release_archives/`에 이미 포함된 동일 파일이 `versions/`에 중복 보관되는 것은 의도된 백업 방식이다.
- 버전 시기는 대화의 순서로 정리했다. 최초 출시 v1.1 등은 앱 내부의 확정 릴리스 태그가 아니라 본 아카이브의 단계 식별자이다.
