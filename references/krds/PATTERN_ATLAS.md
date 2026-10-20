# KRDS 기본·서비스 패턴 아틀라스 v1.0

**직접 원문 링크 16개:** [pattern_catalog.json](pattern_catalog.json). **공식 총계:** 기본 패턴 **11종**, 서비스 패턴 **5종** ([공식 기본 소개](https://www.krds.go.kr/html/site/global/global_summary.html), [공식 서비스 소개](https://www.krds.go.kr/html/site/service/service_summary.html)).

> 이 문서는 KRDS **공식 웹사이트의 설명**을 간결하게 탐색할 수 있도록 만든 편집 색인이다. HTML Kit v1.1.0의 로컬 74개 예제와는 별도 자료이며, 웹사이트의 내용이 추후 수정될 수 있다. '권장 활용'은 디자인 깎기 **적용 가설**이지 KRDS가 다른 분야의 적합성을 인증했다는 뜻이 아니다.

## 1. 기본 패턴 — 한 과업 안의 UI 조합

| 공식 명칭 | 공식 원문 | 이런 요구에서 우선 읽기 | 같이 조회할 컴포넌트 |
|---|---|---|---|
| 개인 식별 정보 입력 | [global_01](https://www.krds.go.kr/html/site/global/global_01.html) | 식별 정보 요청·불필요 수집 방지 | text_input, radio_button |
| 도움 | [global_02](https://www.krds.go.kr/html/site/global/global_02.html) | 진행 단계의 맥락 도움·사용 방법 | tooltip, help_panel, contextual_help |
| 동의 | [global_03](https://www.krds.go.kr/html/site/global/global_03.html) | 약관 이해·동의 범위·선택 | checkbox, accordion |
| 목록 탐색 | [global_04](https://www.krds.go.kr/html/site/global/global_04.html) | 다수 항목 나열·비교·상세 이동 | table, structured_list, pagination |
| 사용자 피드백 | [global_05](https://www.krds.go.kr/html/site/global/global_05.html) | 실제 사용 경험·불편 신고 | textarea, radio_button |
| 상세 정보 확인 | [global_06](https://www.krds.go.kr/html/site/global/global_06.html) | 제목·요약·본문·이력·관련 행동 | in_page_navigation, text_list |
| 오류 | [global_07](https://www.krds.go.kr/html/site/global/global_07.html) | 잘못된 입력·실패 상황의 복구 | critical_alerts, text_input_state |
| 입력폼 | [global_08](https://www.krds.go.kr/html/site/global/global_08.html) | 필수 필드·레이블·검증·입력 군집 | text_input, select, textarea |
| 첨부파일 | [global_09](https://www.krds.go.kr/html/site/global/global_09.html) | 다운로드 및 입력에 붙는 자료 | file_upload, link |
| 필터링·정렬 | [global_10](https://www.krds.go.kr/html/site/global/global_10.html) | 검색 결과 축소·조건 비교 | select, checkbox, select_sorting |
| 확인 | [global_11](https://www.krds.go.kr/html/site/global/global_11.html) | 결과가 중대하거나 되돌리기 어려운 행동 | modal, button |

**공식 문서에서 직접 확인한 핵심 예시**
- **목록 탐색:** 표·구조화 목록·아코디언 등으로 정보 성격에 맞게 표현하며, 대량의 항목은 페이지 분할과 검색/필터를 고려.
- **상세 정보:** 제목, 요약, 핵심 본문, 부가 정보, 변경 이력, 콘텐츠 내 탐색, 행동 수단의 관계를 검토.
- **필터링·정렬:** 데스크톱에서 화면이 충분하면 핵심 필터를 숨기지 않아도 되고, 좁은 화면에서는 모달 등 대안을 평가. 적용된 조건과 결과 상태를 명확하게 표시.
- **확인:** 모든 클릭마다 확인 팝업을 넣지 않고 되돌리기 어려운 결과 등 중요 상황에만 적용. 취소/확정 행동을 분명하게 표시.

## 2. 서비스 패턴 — 사용자가 끝내려는 업무 여정

| 공식 명칭 | 공식 원문 | 공식 설명에서 확인한 주된 과정 | 디자인 깎기 활용 가설 |
|---|---|---|---|
| 방문 | [service_01](https://www.krds.go.kr/html/site/service/service_01_01.html) | 접속 → 정보 탐색 → 확인 → 관련 페이지로 이동 | 랜딩, 서비스 허브, 첫 화면 정보 위계 |
| 검색 | [service_02](https://www.krds.go.kr/html/site/service/service_02_01.html) | 검색어 입력 → 결과 확인 → 이용 → 재검색/상세 검색 | 자료실, 목록형 앱, 검색 대시보드 |
| 로그인 | [service_03](https://www.krds.go.kr/html/site/service/service_03_01.html) | 신원 확인을 통한 서비스 접근 | 역할별 진입 화면 UX (**서버 보안은 별개**) |
| 신청 | [service_04](https://www.krds.go.kr/html/site/service/service_04_01.html) | 대상 탐색 → 신청서 작성 → 확인/확정 → 결과 확인 | 다단계 설문·등록·돌봄 연계 신청 |
| 정책 정보 확인 | [service_05](https://www.krds.go.kr/html/site/service/service_05_01.html) | 상세 정책 정보 확인 → 관련 자료 참고 | 근거 중심 콘텐츠·가이드·규정 페이지 |

KRDS 서비스 패턴은 이용 맥락별 **필수(Do) / 권장(Better) / 우수(Best)** 수준을 구분한다. 이 등급은 KRDS가 다루는 디지털 정부 서비스의 권고 체계이며, 비정부 앱에 그대로 법적 의무로 이전하지 않는다. 각 항목의 정확한 적용 수준은 **각 공식 원문**에서 확인해야 한다.

## 3. 화면 구성보다 먼저 '과업'을 묻는 빠른 경로

| 문제가 무엇인가 | 먼저 볼 패턴 | 다음에 고려 |
|---|---|---|
| 홈페이지가 비슷한 카드만 반복됨 | 방문 | [레이아웃 아틀라스 L1/L5](LAYOUT_ATLAS.md), 정보 구조 |
| 좌우 공간 활용이 어색함 | 레이아웃 원문 | 좌측 메뉴/우측 도움/고정 vs 유동 폭 |
| 검색 결과가 많아 답답함 | 검색 → 목록 탐색 → 필터링·정렬 | 목록/표/카드 대비, 선택 상태 |
| 긴 설명 페이지가 복잡함 | 상세 정보 확인 | 목차, 요약, 출처, 변경 이력 |
| 입력이 많은 업무 화면 | 입력폼 → 도움 → 오류 → 확인 | 스텝 분리/일괄 입력, 임시 저장 |
| 사용자의 반복 실수가 발생함 | 오류 → 확인 | 복구 경로 및 중요도 |
| 로그인·권한 선택 화면 | 로그인 → 개인 식별 정보 입력 | 프론트 UI와 실제 인증·인가 분리 |

## 4. 결합 예시 — 1개 웹사이트를 여러 페이지 형태로

**예시: 퇴원·지역사회 돌봄 연계 서비스의 가상 IA** (실제 의료기관 시스템 미연계, 설계 후보일 뿐)

1. **서비스 홈:** 방문 패턴; 환자/의료진 목적별 주요 행동 분기. 핵심 동선을 카드 한 가지 형태로만 표현할 필요 없음.
2. **대상 목록:** 검색 + 목록 탐색 + 필터링·정렬. 표와 리스트의 선택은 비교 업무의 밀도로 결정.
3. **환자 상세:** 상세 정보 확인. 중요 상태·담당자·근거·진행 이력을 구조화. 실제 데이터는 합성 예시만 사용.
4. **평가/연계 등록:** 입력폼 + 도움 + 오류 + 확인 + 신청. 저장·수정·재진입·취소 규칙 명시.
5. **연계 결과:** 신청 결과 단계 + 상세 정보. 진행 상태, 재시도, 다음 작업, 이력을 함께 제시.

**위 IA는 KRDS 공식 프로토타입을 그대로 복제한 것이 아니다.** 각 패턴을 맥락에 따라 응용한 디자인 깎기의 구성 가설이며, 해당 프로젝트의 별도 기능/안전/UX 계약에 우선권이 있다.

## 5. 선택하지 않는 경우도 기록

- 홍보 페이지: 신청/로그인 패턴을 기계적으로 도입하면 불필요한 기능 부담이 생길 수 있음.
- 드문 경고: 모든 행동에 팝업 확인을 추가하면 경고 피로가 생김.
- 작은 데이터셋: 항상 필터·페이지네이션을 추가할 필요 없음.
- 모바일 상세 페이지: 항상 좌우 패널을 유지하면 본문이 좁아짐.
- 건강 관련 UX: 공공기관 UI의 구조 참고와 임상적 정확성·개인정보 보장은 별개의 검증 대상.

## 6. 연구 근거 상태

- **PASS (출처 존재 확인):** KRDS 공식 기본 패턴 11종 및 서비스 패턴 5종의 상세 페이지 링크, 공식 요약 목록.
- **PASS (웹 문서 내용 확인):** 방문/검색/신청/정책 확인 및 목록/필터/상세/확인 등 핵심 설명.
- **NOT RUN:** 해당 패턴을 적용한 실제 시안 사용자 테스트, 공식 Figma 프로토타입 전체 분석, 16개 패턴별 시각 회귀.
- **특이사항:** 기본 패턴 소개 페이지의 파싱된 목록에는 표기 총계 '11건' 외에 모바일 관련 추가 항목이 별도로 노출된다. 본 인덱스는 **공식 메뉴/총계에 명시된 11종**으로 범위를 고정하며, 사이트 변경 시 재확인한다.

### 참고문헌 (APA 7)

KRDS. (n.d.). *기본 패턴 소개*. https://www.krds.go.kr/html/site/global/global_summary.html

KRDS. (n.d.). *서비스 패턴 소개*. https://www.krds.go.kr/html/site/service/service_summary.html
