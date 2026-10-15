# 디자인 깎기 — 초기 구축용 큐레이션 패키지 A (2026-10-16)

**목적:** 최초 GitHub Private 저장소 생성 시 업로드할 원본 코드·문서·피드백·선별된 증거 스크린샷과 레퍼런스 분석 파일. **GitHub 저장소는 아직 생성하지 않았다.**

## 자료별 지위
- `cases/mul-cup/`: 물컵 홍보 프로젝트 5단계 (`01_v1.1_Initial` → `05_v1.2_Refined`). 버전별 site, docs, source, tests, 대표 previews 및 개발 이력·피드백 원문·출처표 보존. 단일 제품 콘셉트이며 실판매 기능/실물 상품 아님.
- `cases/sai-blog/`: SAI v0.1, v0.2 원본. v0.2의 분리형 소스와 standalone HTML 모두 보존(실행 모드가 다르므로 중복 ZIP과 동일하게 취급하지 말 것). 양 버전 localStorage 키는 다르며 데이터 이전 기능 없음.
- `references/`: 레퍼런스 v0.3 분석 패키지와 v0.1/v0.2 분석 이력. **외부 저작물 이미지 원본을 포함하지 않음.** AI 추정과 사용자 확정 선호/범용 설계 원칙을 구별할 것.
- `guidelines/universal/drafts/`: 범용 v1.2 원문. 상태: **DRAFT**. 이 프로젝트가 임의 승인하지 말 것.
- `guidelines/universal/archive/`: 범용 v1.1 참고·이력 원문. v1.2보다 최신으로 오인하지 말 것.
- `guidelines/quick-start/`: 범용 v1.2 빠른 실행 카드. 원문 대체 불가.
- `guidelines/simulator/`: **시뮬레이터 프로젝트 제약 v1.0**. 원본 `Educational_Simulator_UI_UX_Design_Standard_v1.0.md` 전체는 이번 입력 파일에서 확보되지 않았으므로 포함하지 않음. 없는 문서를 자동 생성하지 말 것.
- `project/PROJECT_OPERATIONS_TRANSFER_NOTE.md`: 이 대화에서 확정한 운영 방향을 정리한 **전달용 메모**. 사용자 승인된 범용 지침 원문과 동일한 지위가 아님.

## 선별/제외 기준
1. **모든 버전의 실행 코드, 중간 source 파일, docs, tests, 피드백, 출처 메타데이터 보존.**
2. 각 버전의 1440/390/320px 등 핵심 시각 증거와 주요 디자인 비교/모션 예시는 보존. 나머지 반복 preview는 별도 사용자 원본 ZIP에 유지.
3. MUL 원본 배포 ZIP 5개 및 리뷰용 잘린 이미지·임시 디버그 이미지·반복된 지침 사본은 **Git에 복사하지 않음**. `EXCLUDED_FROM_WORK_GIT.tsv` 참고.
4. 이 패키지를 압축 해제한 후 파일 내용만 GitHub에 넣고 **이 패키지 ZIP 자체는 커밋하지 말 것**. 원본 ZIP 2개는 사용자의 별도 백업으로 유지한다.
5. 제3자 Behance 사진 및 이미지 ZIP은 Git에 넣지 않음. 출처 확인 및 저작권 상태 기록은 계속 유지.
6. 현재 자료에 있던 `references/archive/v0.2/reference_index_v0.2.csv`는 **원본 자체가 0바이트**인 역사적 파일임. v0.3 정상 인덱스를 사용하고 이력을 임의 수정하지 말 것.

## Work의 작업 범위
GitHub 계정 `pchjesus`에서 `design-kkakgi` Private 존재 여부 확인 → 충돌시 중단 → 사용자의 명시적 승인/도구 권한 하에서 저장소 신규 생성 → 이 패키지의 파일·운영 기본 계약·현황 파일을 초기 커밋 → 원격 검증 후 SHA·Private 상태·누락·제외 결과 보고. **새 견본 제작, 지침 개정, CI/Pages 공개, 기존 사이트 배포 없음.**

## 검증
각 보존 파일과 해시는 `MANIFEST_SHA256.tsv`에 있음. 실행 재검증은 Work 생성 작업과 분리하며 옛 테스트 기록을 새 검증 통과로 쓰지 말 것.
