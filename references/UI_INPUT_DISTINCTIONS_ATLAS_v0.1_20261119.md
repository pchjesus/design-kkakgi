# SRC-30 — 입력 UI의 9쌍: 목적·데이터·상태·오류 구별

> 2026-11-19 · RESEARCH · 사용자 제공 Instagram 정적 캡처 1장 · [아틀라스](ATLAS_HOME.md)
>
> [OBS] @uxwoodytips가 표시된 회원가입 입력 UI 개념 비교. 모바일 알림이 상단의 일부를 가리지만 9개 비교 카드의 제목은 확인 가능. [USER] 이번 자료의 개별 선호는 미표명. [AI-HYP] 아래 선택 기준은 AI 분석·공식 자료 검토이며 원본 게시물의 영상 동작·코드·실사용은 확인하지 않음. 알림 메시지·개인정보나 외부 이미지 원본은 GitHub에 게시하지 않는다.
>
> SRC-00~29의 원자료 칸 누적 270칸(중복 포함) + SRC-30 9칸 = 279칸(중복 포함). 기존 용어와 겹치므로 새로운 고유 컴포넌트 9종으로 해석하지 않는다.

## 1. 원본 명칭과 UI 의미 비교

| # | 원본 명칭 [OBS] | 목적·실제 동작의 차이 [AI-HYP] | 판단·실패 조건 |
|---|---|---|---|
| 01 | 안내 문구 vs 오류 문구 — Helper vs Error | Helper는 입력 전/중 도움; Error는 검증 실패 항목과 수정 방법을 설명하는 상태 피드백 | 빨간 테두리만으로 오류를 알리지 말고 구체적인 텍스트와 필드를 연결. 두 메시지는 상태에 따라 함께 설계할 수 있음 |
| 02 | 한 줄 입력 vs 여러 줄 입력 — Input vs Textarea | 단일행 데이터 vs 줄바꿈을 허용하는 장문 편집 | 짧고 구조화된 ID·이름은 Input, 서술형 의견·메모는 Textarea. 길이뿐 아니라 Enter·포커스·저장 행위 고려 |
| 03 | 자동완성 vs 추천 검색어 — Autocomplete vs Suggest | 현재 작성 중인 값의 완성/일치 옵션 vs 새로운 검색 주제 탐색 추천; 양쪽의 드롭다운 외형은 같을 수 있음 | HTML autocomplete 속성(브라우저 자동채움)과 제품 자체 검색 제안/추천 검색어는 다른 층위. 두 유형은 함께 제공될 수도 있음 |
| 04 | 비밀번호 vs 인증번호 — Password vs OTP | 지속적 비밀 인증정보 vs 유효기간·재전송을 가진 일회용 인증 코드 | OTP의 앞자리 0 보존, 붙여넣기·자동완성·만료·재전송·오류 복구 지원; 코드/비밀번호 노출·로그 저장 금지 |
| 05 | 지우기 vs 보기 — Clear vs Show | 입력값 삭제 vs 가려진 문자 표시 상태 토글 | 동일 필드에 함께 존재 가능. 삭제는 입력유실, 보기는 민감정보 노출 위험; 버튼 이름·현재 상태를 명확히 |
| 06 | 글자 수 vs 입력 제한 — Counter vs Max length | 화면에 입력량을 보여주는 피드백 vs 실제 허용 입력량 제약 | 사용자가 확인하는 문자 수·허용 범위가 일치해야 함. HTML maxlength는 UTF-16 코드 단위이므로 이모지·조합문자의 사용자 지각과 차이 가능 |
| 07 | 숫자 키패드 vs 키보드 — Numpad vs Keyboard | 데이터 형식에 맞춘 입력 환경·키 배열 | inputmode=numeric은 키보드 힌트일 뿐 값 검증이 아님. 전화번호·코드·수치의 선행 0·소수·음수 조건 구별 |
| 08 | 날짜 입력 vs 날짜 선택 — Date input vs Picker | 날짜 직접 입력 vs 달력·휠 탐색 후 선택 | 같은 컴포넌트에서 병행 가능. 과거 출생일과 가까운 예약일의 입력 전략 구분. 로캘·키보드·오류 상태 검토 |
| 09 | 필수 vs 선택 — Required vs Optional | 누락을 허용하지 않는 제약 vs 생략 가능한 항목 | 별표·색만으로 필수 여부를 전달하지 말고 읽히는 레이블·검증 규칙 일치 확인 |

## 2. 시각 분석

- **타이포그래피/색:** 큰 검정 한글 제목에서 일부 단어만 푸른색 강조. 카드 하단은 작은 번호(파랑)·한글 제목(진회색)·영문 보조명(회색) 위계. 레이블과 이미지의 반복으로 9쌍 비교에 적합.
- **레이아웃/정보구조:** 3열×3행 균등 카드. 각 셀에 두 동작을 작은 그림으로 대비. 참고용 사전으로서는 빠르게 훑을 수 있지만 실제 한 화면의 입력 흐름·중요도·오류 복구 동선의 증거는 아님.
- **물성/이미지:** 약한 그림자·옅은 입체감·회색 표면 위 파란 초점 상태. 실제 키보드·자동완성·애니메이션은 캡처만으로 알 수 없음.
- **장점:** 혼동하기 쉬운 용어를 짝지어 인지적 비교를 촉진한다. **한계:** 개념적으로 배타적이지 않은 항목을 VS로 배치하면 선택지로 오인하기 쉬움.

## 3. 공식 자료·오용 방지

- [OFFICIAL] W3C WCAG 2.2의 SC 3.3.1(Error Identification) 및 SC 3.3.2(Labels or Instructions)는 입력 오류의 텍스트 설명과 필요한 레이블·지시를 요구한다. WAI Forms Validation은 필수 입력 표시·오류 복구 예시를 제공한다.
- [OFFICIAL] MDN autocomplete는 브라우저 자동채움 속성으로, 상품 검색의 추천어 UI와 동일 개념이 아니다. one-time-code 등 목적 토큰의 지원 범위는 실제 기기에서 시험 필요.
- [OFFICIAL] MDN inputmode는 입력 환경 힌트, maxlength는 UTF-16 코드 단위 길이 제한. 보안/서버 검증 및 실제 문자수와 혼동하지 않는다.
- [OFFICIAL] W3C WCAG 2.2 SC 3.3.8 Accessible Authentication (Minimum)의 취지를 고려해 비밀번호 관리자·코드 붙여넣기/자동 입력 같은 보조 수단을 방해하지 않는다.

## 4. 적용과 기존 아틀라스 대응

| 맥락 | 활용 | 피해야 할 실수 |
|---|---|---|
| 회원가입 | 인증 단계의 설명·오류·OTP 상태를 한 흐름에서 보여줌 | 유효한 코드가 입력돼도 처리 상태 미표시, 붙여넣기 차단 |
| 쇼핑·정보 검색 | 입력 완성, 추천 탐색, 입력 지우기 기능을 구분 | 추천 검색어를 사용자 검색기록으로 오인시키는 표시 |
| 임상·간호 업무 | 숫자/날짜 단위, 유효범위, 필수 항목을 명료하게 | 키패드만 숫자로 바꾸고 임상 유효성 검증을 생략 |
| 긴 설문·서술형 입력 | 텍스트 영역과 남은 문자 수를 목적에 맞게 제공 | 예고 없이 제한·자동 삭제 |

- [SRC-02 기초 입력 패턴](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md), [SRC-26 검색](UI_DATA_VISUALIZATION_SEARCH_ATLAS_v0.1_20261113.md), [SRC-28·29 UI 의미 비교](UI_SEMANTIC_PAIRS_ATLAS_v0.1_20261117.md), [FOUND-001 인간중심 설계](foundations/FOUND-001_UCD_NURSING_USABILITY.md)와 연결.
- [USER 기존 취향] 심장 시뮬레이터의 목적에 맞는 정보량·명확한 조작 선호와 **논리적으로 연결**될 수 있음 [AI-HYP]. 이번 SRC-30의 실제 선호·이용 편의성은 별도 평가가 없으므로 확정하지 않음.

## 5. 검증 상태

| 항목 | 상태 |
|---|---|
| 사용자 제공 9쌍 명칭·정적 구성 확인 | PASS (상단 일부 가림) |
| W3C·MDN 공개 설명 대조 | PASS (공개 문서 수준) |
| 원본 영상·키보드·스크린리더·모바일 실사용 | NOT RUN |
| 사용자 개별 선호·임상 안전/사용성 | NOT RUN |
| 범용 v1.3·프로덕트 코드·배포 수정 | N/A |

## 6. 참고문헌 (APA 7판)

MDN Web Docs. (n.d.). *HTML attribute: autocomplete*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete

MDN Web Docs. (n.d.). *HTML global attribute: inputmode*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode

MDN Web Docs. (n.d.). *HTML attribute: maxlength*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength

World Wide Web Consortium. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

World Wide Web Consortium. (n.d.). *Validating input*. https://www.w3.org/WAI/tutorials/forms/validation/

World Wide Web Consortium. (n.d.). *Understanding SC 3.3.8: Accessible authentication (minimum)*. https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum

SNS: @uxwoodytips, ‘회원가입할 때 빨간 글씨, 이것도 이름이 있어요’ [사용자 제공 정적 캡처, 게시일 및 원본 게시 URL 미확인]. 2026-11-19 수집.
