# UI 날짜 선택·행동심리 사례 보강 아틀라스 v0.1

> **2026-11-11 · RESEARCH / 사용자 제공 SNS 정적 캡처 2장**  
> **현행 승인 범용 기준:** Universal Visual Design & UI/UX Guidelines **v1.3 APPROVED**. 이 문서는 범용 지침, 기존 UI, 웹앱, GitHub Pages를 수정하지 않는다.
>
> **관찰 범위 [CAP]:** 화면에 보이는 @uxwoodytips 계정 표기의 게시물 2장 × 9칸 = **18개 원자료 칸**. **SRC-22**는 날짜 선택의 새 사례 9칸이고, **SRC-23**은 기존 [SRC-05 행동심리 9종](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md#7-행동-심리-9개-의사결정-지원-vs-다크-패턴)과 **명칭과 순서가 같은 반복 자료**다(숫자·내용 등의 예시는 다를 수 있음). 이전 누적 198칸에 더해 **216칸(중복 포함)**. 서로 다른 216개 UI 유형이나 효과가 실증된 216개 사례를 뜻하지 않는다.
>
> **근거 분리:** [CAP] 이미지의 명칭·예시·순서 / [OFFICIAL] 공식 가이드 및 검증 가능한 외부 자료 / [AI-HYP] 사용 조건·적합성 가설 / [USER] 사용자에게 직접 확인한 취향. 이번 18개 항목에 대한 **개별 취향 평가·직접 동작 시험은 아직 없음**. 원본 릴스의 재생 시간, 이징, 터치 동작, 제작 기술, 정확한 원본 URL·라이선스는 **미확인**. 원본 사진/영상/폰트·SNS 자산은 저장소에 업로드하지 않는다.

## 1. 캡처 인벤토리: SRC-22~23

| 원자료 ID | 캡처의 제목 | 원본의 번호 순서 (01–09) | 기존 아틀라스와 관계 |
|---|---|---|---|
| **SRC-22** | 날짜 고르는 화면 9가지 | Calendar / Wheel picker / Date range / Quick chips / Time slots / Month picker / Date input / Check-in, out / Recurrence | **신규 상세 연구**. 기존 Date picker SRC-02·SRC-11의 선택 목적을 확장 |
| **SRC-23** | 심리와 편향 9가지 | Anchoring / Loss aversion / Default effect / Social proof / Scarcity / Framing effect / Choice overload / Peak-end rule / Zeigarnik effect | **기존 SRC-05와 용어 중복**. 정의 재복제 대신 캡처 예시의 해석·오용 보완 |

**중요한 분류 차이:** Calendar·Wheel picker는 **조작 방식**, Date range·Month picker는 **선택할 데이터의 범위/단위**, Time slots·Quick chips는 **사전 제공된 선택지**, Check-in/out는 **업무 의미**, Recurrence는 **반복 규칙**이다. 따라서 9가지는 서로 배타적인 구현 대안이 아니다.

## 2. SRC-22: 날짜 선택 9종 — 실제 동작, 적합성, 실수 방지

| 번호 / 명칭 | 일반적 동작·입력 계약 [CAP+분석] | 사용 과업 [AI-HYP] | 실패·접근성·상태 확인 |
|---|---|---|---|
| **01 Calendar** | 월별 격자를 탐색하면서 요일과 특정 날짜를 확인·선택. 키보드/날짜 직접입력은 구현별로 달라짐 | 가까운 예약일·진료일, 다른 날짜와의 관계 확인 | 오늘·선택·비활성 날짜의 명확한 구분, 월 이동·키보드·직접입력 대안 |
| **02 Wheel picker** | 연·월·일 등을 수직 열에서 스크롤해 항목을 고르는 형태 | 터치 기반 모바일 선택지, 짧고 제한된 범위 | 많은 연도를 반복 스크롤하면 비효율적. 스크린리더/외부 키보드·빠른 직접 입력 검토 |
| **03 Date range** | 시작일과 종료일 두 값으로 기간을 정하고 사이 날짜를 강조 | 일정 기간 필터·입원/여행 기간 | 종료일 ≥ 시작일, 경계 포함 여부, 기간 계산 및 타임존 정의 |
| **04 Quick chips** | '오늘/내일/이번 주/다음 주' 등 상대 날짜를 즉시 선택 | 가까운 일정·빠른 필터 | '오늘'의 기준 날짜·시간대와 선택 후 실제 날짜 표시, 칩의 활성 상태 |
| **05 Time slots** | 날짜에 따른 **예약 가능한 시간대** 중 하나를 선택 | 외래·상담·서비스 예약 | 재고/예약 가능 여부는 실시간 검증 필요, 중복 예약·마감 시 복구, 시간대 표시 |
| **06 Month picker** | 일자를 받지 않고 **연도+월**만 선택 | 월별 통계·정산·보고 기간 | 2026-11 같은 월 단위 데이터를 특정 일자 데이터로 오인시키지 않기 |
| **07 Date input** | 사용자가 날짜를 타이핑/숫자 키패드로 입력, 형식 힌트 제공 | 생년월일·과거 진료일·문서에 적힌 날짜 | 연-월-일 순서·로캘·윤년·유효 날짜·입력 오류를 명시. 캡처에는 '1995.08'처럼 부분 입력 예시가 보이므로 **완성 날짜로 단정하지 않음** |
| **08 Check-in / Check-out** | 입실/퇴실 두 역할의 시작·종료 값을 연결하는 도메인 패턴 | 숙박·대여·시설 이용 등 | 차별화된 라벨, 최소 숙박일/중복 기간/오류 시 기존 값 복원; 의료 입퇴원에 그대로 이식하지 않기 |
| **09 Recurrence** | 매일/매주/매월 등 규칙과 주기·시작·종료·예외일을 조합 | 정기배송·반복 약속·일정 | 휴일·말일(예: 31일)·DST·월별 간격·변경 시 향후 일정 영향 명시 |

### 외부 근거와 구체적인 함의

- **[OFFICIAL] GOV.UK Design System**은 생일처럼 기억하는 날짜에 직접입력 컴포넌트를 권하고, 달력 컨트롤은 **가까운 미래/과거, 요일·주간 관계, 다른 날짜와의 관계를 봐야 할 때** 적합하다고 구분한다. 달력만을 유일한 입력법으로 두지 말라고도 권고한다. [Ask users for dates](https://design-system.service.gov.uk/patterns/dates/).
- **[RESEARCH / NN/g]** 날짜를 먼 과거/미래에서 찾을 때 달력·휠 탐색만 강요하는 방식은 번거로울 수 있다. 입력 형식 오류, 범위 선택의 맥락 이동, 동일 날짜의 재입력 강요는 피해야 한다. [Date-Input Form Fields: UX Design Guidelines](https://www.nngroup.com/articles/date-input/). 이 글은 2017년의 설계 연구·실무 가이드이므로 **모든 현재 앱에서의 성능 실험 결과**로 간주하지 않는다.
- **[PLATFORM] Apple의 [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) 가이드는 플랫폼 맥락을 검토하는 출처**로 연결하지만, 이번 조사에서는 페이지 내용이 JavaScript 렌더링을 요구하여 **구체적인 변형·행동을 직접 검증하지 못했다**. Apple 기능의 세부사항을 이 링크만으로 실측했다고 주장하지 않는다.

### 화면 설계에 적용할 결정 순서 [AI-HYP]

**무엇을 입력하는가 → 날짜 범위가 넓은가 → 요일/상대 날짜 관계가 필요한가 → 실제 예약 가능 데이터가 있는가 → 오류와 복구를 어떻게 처리할 것인가 → 모바일·키보드·보조기술에서 가능한가.**

예: **생년월일**은 직접입력 우선, **가까운 진료 예약일**은 달력+직접입력, **통계 조회 월**은 월 선택, **반복 일과**는 반복 규칙 편집을 우선 검토한다. 의료기관의 진료 예약·입퇴원·투약 일정은 일반 숙박 체크인 UI의 예시를 생리·행정 데이터 계약으로 무비판적으로 가져오지 않는다.

## 3. SRC-23: 행동심리 9종 — 기존 SRC-05의 사례·근거 보완

이 절은 [기존 행동 심리 9종 기준표](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md#7-행동-심리-9개-의사결정-지원-vs-다크-패턴)를 **보충**한다. 캡처의 9개 명칭은 심리학적 개념 또는 해석용 레이블이지 해당 UI 구현으로 **효과가 입증됐다는 표시가 아니다**.

| 번호 / 명칭 | 캡처의 관찰 가능 표현 [CAP] | 타당한 해석 범위와 구분할 것 | 오용·윤리 위험 |
|---|---|---|---|
| **01 Anchoring** | 취소선 가격 '300,000원'과 '190,000원' | 최초 기준 가격이 비교 판단에 영향을 줄 **가능성**. 실제로 영향을 받았는지는 사용자 연구 필요 | 허위 정상가·허위 할인 |
| **02 Loss aversion** | 남은 시간 카운트다운과 사라지는 혜택 문구 | 손실 회피뿐 아니라 **긴급성·시간 압박**을 함께 시사. 하나의 편향으로 인과 단정 불가 | 존재하지 않는 마감·조급한 구매 압박 |
| **03 Default effect** | '추천 옵션' 기본 선택, 직접 고르기 선택지 | 실제 기본값의 편의성 vs 유도된 선택을 구분 | 사전 체크 동의, 불이익 있는 기본 설정 숨기기 |
| **04 Social proof** | 여러 색 원형 아바타 + '1,284명이 보고 있어요' | 사람이 모인다는 **사회적 증거의 표현**; 실시간 이용자 데이터인지 확인되지 않음 | 가짜 라이브 숫자·가짜 후기 |
| **05 Scarcity** | 상품 격자와 '남은 재고 1개' | 재고 제한을 표시하는 **희소성 신호** | 실재 재고·갱신 기준 없는 숫자 |
| **06 Framing effect** | '20% 불만족'이라는 부정적 표현 | 동일한 비율을 반대로 표현했을 때의 인상 차이를 연구하는 예시. 단독 화면은 **실험 증거 아님** | 유리한 분모/결과만 선택해 정보 왜곡 |
| **07 Choice overload** | 세 개의 크게 구분된 선택 카드 | 3개라는 **개수만으로 선택 과부하를 판정할 수 없음**. 속성·비교 가능성·결정의 중요도 등이 좌우 | 필요 옵션을 빼놓고 '간결함'만 추구 |
| **08 Peak-end rule** | 최고점·끝 지점이 표시된 곡선 | 경험의 피크와 끝에 대한 **설명 그림**일 뿐, 실제 이용자의 기억·만족도를 측정한 데이터 아님 | 피크·끝만 미화하고 과정의 문제 숨기기 |
| **09 Zeigarnik effect** | 리뷰 작성 진행률 약 81%와 체크리스트 | 미완료 상태가 동기화될 가능성은 있으나, **진행률 피드백·목표 접근성**과 구분이 어려움. 자이가르닉 효과가 검증됐다고 단정하지 않기 | 불필요한 미완료 표시·압박·강박적 반복 유도 |

### 심리 연구·윤리 근거

**[OFFICIAL REVIEW] 영국 Competition and Markets Authority (2022)**는 온라인 선택 환경을 **선택 구조(Choice Structure), 선택 정보(Choice Information), 선택 압박(Choice Pressure)**으로 나누어 기본값·사회적 신호·희소성 등 온라인 선택 설계의 효과와 소비자 피해 가능성을 검토했다. 이는 개별 화면의 특정 효과가 발생했다는 증거가 아니며, 설계 기법이 사용자 선택을 왜곡할 수 있다는 검토 근거다. [Evidence review of Online Choice Architecture and consumer and competition harm](https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers/evidence-review-of-online-choice-architecture-and-consumer-and-competition-harm).

특히 **선택 과부하, 피크엔드, 자이가르닉**은 캡처에 이름이 붙어 있다는 이유만으로 실제 UX 효과를 입증하지 않는다. 의료·금융·동의처럼 이해와 자율성이 우선인 과업에서는 압박형 카운트다운·허위 희소성·기만적 기본값을 피하고, 정확한 데이터·필요한 비교 정보·변경·취소 경로를 제공한다.

## 4. 이전 취향 지도와 비교·적용 경계

- **[USER] 직접 확인:** 사용자가 두 장을 레퍼런스로 수집하고 아틀라스 반영을 요청했다. **이 18개 유형 중 무엇이 아름답다거나 싫다는 개별 평가를 내리지는 않았다.**
- **[AI-HYP] 연결:** 이전에 사용자가 언급했던 간결한 시뮬레이터 조작, 업무의 정보 위계, 적합한 레이아웃의 목적 우선 원칙과, 날짜 선택에서 **과업을 먼저 분류**하는 접근은 잘 연결된다.
- **[AI-HYP] 새 관점:** 날짜 선택은 동일 기능으로 보이더라도 **도메인 의미·데이터 모델·입력 수단**을 분리해야 한다. 행동심리 레이블과 UI 시안의 실제 효과는 구분해야 한다.
- **[COUNTEREXAMPLE]** 캘린더가 아름다워도 멀리 떨어진 생년월일을 찾기 어렵다면 나쁜 선택일 수 있다. 사회적 증거/진행률이 눈에 잘 띄어도 근거 없이 조급함을 유발하면 사용자 경험을 해친다.
- **[NO AUTO-ADOPTION]** 특정 컨트롤·팔레트·애니메이션을 전 제품에 자동 적용하지 않는다. 시뮬레이터의 안전·의료 교육 계약과 승인된 범용 v1.3이 우선한다.

## 5. 확인·미확인

| 검증 항목 | 상태 | 범위 |
|---|---|---|
| SRC-22·23의 2장×9칸 명칭·순서·관찰 사례 기록 | **PASS** | 사용자 제공 정적 화면 확인 |
| SRC-23과 SRC-05의 명칭/순서 중복 확인 | **PASS** | 기존 아틀라스 텍스트 대조 |
| 날짜 입력·선택의 과업별 권고 검토 | **PASS (문서)** | GOV.UK·NN/g 원문 대조 |
| 온라인 선택 구조·압박에 관한 근거 검토 | **PASS (문서)** | CMA 2022 원문 대조 |
| Apple 픽커 세부 동작의 직접 확인 | **NOT RUN** | 문서 페이지 JS 필요 |
| 릴스 재생·실제 터치 동작·속도·원본의 구현 기술 | **NOT RUN** | 정적 캡처만 확보 |
| 모바일/데스크톱/보조기술 실기기 조작·사용성·심리 효과 검증 | **NOT RUN** | 실행 시안·시험 없음 |
| 사용자의 개별 디자인 선호도 평가 | **NOT RUN** | 이번에는 수집·등록만 확인 |
| 지침 v1.3/기존 앱/Pages 변경·외부 이미지 복제 | **N/A** | 진행하지 않음 |

## 6. 참고문헌 (APA 7판)

Competition and Markets Authority. (2022, April 5). *Evidence review of online choice architecture and consumer and competition harm*. GOV.UK. https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers/evidence-review-of-online-choice-architecture-and-consumer-and-competition-harm

Government Digital Service. (n.d.). *Ask users for dates*. GOV.UK Design System. https://design-system.service.gov.uk/patterns/dates/

Li, A. (2017, January 22). *Date-input form fields: UX design guidelines*. Nielsen Norman Group. https://www.nngroup.com/articles/date-input/

Apple. (n.d.). *Pickers*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/pickers (세부 내용 직접 검증 NOT RUN)

사용자 제공 Instagram 정적 캡처. (2026, November 11). *날짜 고르는 화면 9가지·심리와 편향 9가지* [대화에서 받은 2개 화면, 원본 릴스 URL 및 라이선스 미확인].

---

**운영 결론:** 이번 반영은 연구 자료의 구분과 선택·오용 판단을 세밀하게 만드는 작업이다. 실제 서비스 성능, 인지심리 효과 또는 사용자의 개인적 미적 취향이 새로 검증됐다는 뜻이 아니다. 향후 비슷한 자료가 쌓이면 중복 정의를 늘리기보다 각 사례의 차이와 근거를 보완한다.
