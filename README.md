# 디자인 깎기

콘텐츠·목적·이용자·매체·기능에 맞는 디자인 판단과 구현·검증 능력을 연구하는 독립 저장소다. 개인 취향을 보편 규칙으로 자동 전환하지 않는다.

## 이용 구분

- 일반 ChatGPT 채팅: 이미지 분석, 견본 개발, 비교와 개선
- GitHub: 지침, 코드, 연구자료, 결정 이력 보존
- Work: 초기 구축·정책 전환 같은 저장소 운영 작업
- 사용자: 방향 결정과 지침의 정식 채택 승인

## 구성

- `guidelines/`: 범용 지침 v1.2 DRAFT, 빠른 실행 카드, 전문 제약과 이력
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

현재 범용 지침 v1.2는 **DRAFT**이며, 정식 채택·개정은 별도 사용자 승인이 필요하다.

## KRDS 코드 레퍼런스

- [KRDS HTML Component Kit v1.1.0 탐색 허브](references/krds/README.md) — 74개 컴포넌트 색인, 토큰 지도, HTML/SCSS/JS 경로와 검증 규칙. **원본 소스·폰트·아이콘을 저장소에 복제하지 않음.**
- 외부 참고자료는 현재 지침 v1.2 DRAFT의 자동 개정 또는 UX 표준 채택을 의미하지 않는다.

## KRDS 사이트 구조·서비스 패턴 자료

- [레이아웃 아틀라스](references/krds/LAYOUT_ATLAS.md), [기본 11종·서비스 5종 패턴](references/krds/PATTERN_ATLAS.md), [레퍼런스 선택 프로토콜](references/krds/REFERENCE_SELECTION.md) — 홈페이지·서브페이지 구조부터 사용자 과업, 세부 UI로 내려가는 설계 탐색.
- 디자인/UX 가설과 공식 KRDS 원칙을 구분하며, 기존 범용 디자인 지침 **v1.2 DRAFT**와 프로젝트 UI는 자동 변경하지 않는다.
