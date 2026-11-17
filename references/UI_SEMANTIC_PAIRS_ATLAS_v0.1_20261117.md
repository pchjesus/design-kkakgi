# SRC-28·29 — 아이콘과 UI 헷갈리는 짝 18쌍: 조형보다 의미·동작·상태 v0.1

> 2026-11-17 · RESEARCH / 정적 Instagram 캡처 2장 · [통합 아틀라스](ATLAS_HOME.md)
>
> [CAP] 두 화면에서 @uxwoodytips 표기와 9쌍씩의 비교 제목·도식을 확인했다. **총 18쌍·36개 표기(중복 포함)**. [USER] 이번 각 쌍에 대한 미적 선호를 따로 밝히지는 않음. [AI-HYP] 판단표는 실제 설계의 목적별 비교이며 해당 SNS 원본의 작동·구현을 입증하지 않는다. 정확한 게시 링크/권리/원본 모션은 미확인. 캡처·폰트·영상을 공개 GitHub에 재배포하지 않는다.
>
> **분류:** SRC-28 아이콘 별칭·의미 9쌍, SRC-29 UI 패턴 9쌍. 기존 SRC-16·18 등과 주제 반복. 기존 **243칸 + SRC-27 스크롤 9칸 + SRC-28·29 비교 18칸 = 270개 원자료 칸(중복 포함)**, 독립 패턴 270개나 사용자 선호 270건이 아니다. 승인 v1.3 지침·제품·Pages 변경 없음.

## 1. SRC-28 — 헷갈리는 아이콘 9쌍

| 순번 | 원본 명칭 [CAP] | 통상적 의미와 결정 질문 [AI-HYP] | 혼동 위험 |
|---|---|---|---|
| 01 | 햄버거 vs 케밥 / Hamburger vs Kebab | 햄버거(가로 3줄)는 **주요 메뉴/탐색**, 케밥(세로 3점)은 보통 **맥락 메뉴/추가 기능** | 핵심 기능을 점 세 개 뒤에 과도하게 숨기지 않기 |
| 02 | 케밥 vs 미트볼 / Kebab vs Meatballs | 세로 점 세 개 vs 가로 점 세 개. 둘 다 상황에 따라 **더보기/추가 작업**으로 쓰임 | 방향만으로 다른 기능을 고정하는 보편 규칙은 **없음** |
| 03 | 하트 vs 북마크 / Like vs Bookmark | **좋아요·반응**과 **개인 보관·나중에 보기**의 차이 | 좋아요를 누르면 저장되는지 명확히 표시 |
| 04 | 공유 vs 내보내기 / Share vs Export | 다른 사람/앱에 **접근·전달** vs 파일/서식으로 **결과 생성·내보내기** | 외부 공개·파일 생성·복사/다운로드의 차이 |
| 05 | 닫기 vs 뒤로 / Close vs Back | 현재 대화상자/레이어를 **닫기** vs 탐색한 **이전 위치로 돌아가기** | 입력 유실·작업 맥락 상실·이전 단계 오동작 |
| 06 | 새로고침 vs 되돌리기 / Refresh vs Undo | **새 데이터 로드/화면 갱신** vs 직전 작업 **취소/복원** | 데이터 재조회가 편집 작업을 복구하지는 않음 |
| 07 | 검색 vs 확대 / Search vs Zoom in | 대상을 **검색** vs 이미 보이는 화면/이미지 **확대** | 돋보기 모양만 보고 동일한 행동이라고 오인 |
| 08 | 필터 vs 정렬 / Filter vs Sort | 집합에서 **조건에 따라 포함/제외** vs 같은 항목의 **표시 순서 바꾸기** | 검색결과 수 변화와 순서 변화를 혼동 |
| 09 | 수정 vs 새 글 / Edit vs Compose | **기존 항목 변경** vs **새 글/새 항목 만들기** | 원본 덮어쓰기·새 레코드 생성의 차이 |

**중요:** Kebab과 Meatballs는 특정 방향의 점 세 개를 가리키는 별칭이다. 플랫폼에서 둘을 똑같은 '더보기'로 쓸 수 있으므로 **정식 기능 규격으로 기계적으로 구분하지 않는다**. 아이콘 자체보다 **주변 정보·접근성 이름·클릭 후 실제 행동**이 중요하다. W3C WAI-ARIA APG의 접근 가능한 이름 권고는 'X' 아이콘 버튼의 이름을 글자 X가 아닌 실제 행동인 'Close'로 표현하는 예를 든다.

## 2. SRC-29 — 헷갈리는 UI 9쌍

| 순번 | 원본 명칭 [CAP] | 실제 선택을 결정하는 기준 [AI-HYP] | 실패를 판단할 때 |
|---|---|---|---|
| 01 | 알럿 vs 컨펌 / Alert vs Confirm | **알림 전달** vs 사용자에게 **선택·결정 요구**. 버튼 1개/2개만의 차이 아님 | 삭제·위험 작업은 결정·복구·초점 명확화. WAI alert와 alertdialog는 별도 역할 |
| 02 | 드롭다운 vs 피커 / Dropdown vs Picker | 옵션 목록을 펼치기 vs 값·시간·날짜 등 **전용 선택 상호작용**. 용어 일부 중첩 | 몇 개 고정 옵션인지, 긴 값이나 날짜·연속 값을 다루는지 |
| 03 | 캐러셀 vs 가로 스크롤 / Carousel vs Scroll | 분절된 **슬라이드와 이전/다음 전환** vs 가로로 이어진 **연속 콘텐츠 탐색** | 자동 회전의 통제·키보드 조작·숨은 카드 발견 |
| 04 | 상단 바 vs 탭 바 / Top bar vs Tab bar | 제목/뒤로/도구를 담는 **상단 앱 바** vs 동등한 **정보 섹션/화면 전환** | 같은 높이에 있다고 같은 컴포넌트 아님 |
| 05 | 페이징 vs 무한 스크롤 / Paging vs Infinite | 페이지 경계를 사용자가 **명시적으로 이동** vs 스크롤 끝에서 **다음 데이터 이어받기** | 특정 페이지 재방문·푸터·키보드·로딩 오류 |
| 06 | 플로팅 vs 하단 고정 / Floating vs Sticky | 떠 있는 주요 행동 버튼(예 FAB) vs **화면 하단에 붙는 지속 행동 영역** | 키보드·안전 영역·본문 가림 확인. 'Sticky'라는 화면 명칭은 CSS position: sticky 구현을 입증하지 않음 |
| 07 | 플레이스홀더 vs 레이블 / Placeholder vs Label | 입력 칸 속 **예시·힌트** vs 지속적으로 식별할 수 있는 **필드 이름** | 입력 후 힌트가 사라져도 사용자가 항목을 이해하는가 |
| 08 | 진행 바 vs 단계 표시 / Progress vs Steps | **진행 분량/비율** vs **현재 절차상의 단계·완료 순서** | 3/5단계를 전체 작업량 60%로 가정하는 오류 |
| 09 | 아코디언 vs 더보기 / Accordion vs More | 한 화면의 **섹션 접기/펼치기** vs 숨은 내용·항목 추가 공개/별도 화면 이동 | '더보기'는 행동명으로, 구현이 반드시 Accordion이어야 하는 것은 아님 |

### 원본 분류를 그대로 규칙으로 만들지 않는 이유

- **Alert/Confirm:** JavaScript 내장 alert()/confirm(), WAI-ARIA의 alert/alertdialog, 앱 자체 디자인 시스템의 이름은 서로 일대일로 대응하지 않을 수 있다. 실제 차단/결정·포커스·키보드 동작을 확인할 것.
- **Dropdown/Picker, Accordion/More:** 기능의 범위가 일부 겹치거나 한쪽이 더 넓은 개념일 수 있어, 둘이 항상 이분법적 대안인 것은 아니다.
- **Floating/Sticky:** UI가 화면에 어떻게 보이는지와 CSS의 fixed/sticky는 다른 분류축이다. 캡처만으로 DOM/CSS 구현을 알 수 없다.
- **Progress/Steps:** '지금 3단계'라는 숫자는 완료량 60%를 뜻하지 않는다. 각 단계의 소요시간·작업량은 다를 수 있다.
- **Placeholder/Label:** W3C WCAG 2.2 SC 3.3.2는 입력이 필요한 콘텐츠에 레이블/지시를 요구한다. 입력시 사라지는 힌트만으로 필드 의미를 전달하는 것은 위험하다.

## 3. 기존 아틀라스와 연결

- [SRC-07 아이콘 별칭](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md), [SRC-16 Hamburger/Kebab·Placeholder/Label과 SRC-18 비교](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md): **반복 항목은 새 공식 유형으로 중복 계산하지 않음**.
- [SRC-24 목록 표시·캐러셀·무한 스크롤](UI_LIST_PRESENTATION_ATLAS_v0.1_20261112.md), [SRC-26 검색·필터·정렬](UI_DATA_VISUALIZATION_SEARCH_ATLAS_v0.1_20261113.md), [SRC-27 스크롤 경험](UI_SCROLL_EFFECTS_ATLAS_v0.1_20261117.md)과 교차 사용.
- [FOUND-001 인간중심 디자인·IA/Flow/Interaction/GUI](foundations/FOUND-001_UCD_NURSING_USABILITY.md)의 '과업·상태·오류' 평가로 연결.

## 4. 적용 예시 — 아직 사용성 시험 전 [AI-HYP]

| 실제 과업 | 구분해 선택할 것 | 위험 |
|---|---|---|
| 간호사 기록·교육 자료 입력 | 닫기/뒤로, 레이블/힌트, 새로고침/되돌리기, 실제 완료 피드백 | 미저장 이탈·다른 환자 변경·수치 입력 오류 |
| 연구 자료/쇼핑 비교 | 검색/필터/정렬, 페이징/무한 로딩, 북마크 저장 | 동일 검색 재현 불가, 사용자가 원하는 결과 놓침 |
| 브랜드·제품 소개 | 캐러셀/가로 스크롤, 앱바/탭바, 간결한 모션 | 콘텐츠 발견 실패, 자동 전환이 읽는 속도 방해 |
| 문서·파일 도구 | 공유/내보내기, 기존 항목 수정/새 글 생성 | 의도치 않은 공개·파일 덮어쓰기 |

## 5. 검증 상태

| 항목 | 상태 |
|---|---|
| 사용자 캡처 2장의 18쌍 명칭과 정적 예시 관찰 | PASS (정적 분석) |
| WAI-ARIA·WCAG·MDN·NN/g 공식 자료와 개념 대조 | PASS (공개 문서 범위) |
| 원본 인스타 영상·실제 UI 작동·테스트 코드 | NOT RUN |
| 실제 사용자 연구·키보드/모바일·성능·접근성 측정 | NOT RUN |
| 이번 18쌍에 대한 사용자 미감 선호 평가 | NOT RUN |
| 기존 웹앱/범용 v1.3/Pages 변경 | N/A (범위 밖) |

## 6. 참고문헌 (APA 7판)

MDN Web Docs. (n.d.). *position*. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position

Nielsen Norman Group. (2013). *Beware horizontal scrolling and mimicking swipe on desktop*. https://www.nngroup.com/articles/horizontal-scrolling/

Nielsen Norman Group. (2022). *Infinite scrolling: When to use it, when to avoid it*. https://www.nngroup.com/articles/infinite-scrolling-tips/

World Wide Web Consortium. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

World Wide Web Consortium. (n.d.). *Providing accessible names and descriptions*. https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/

World Wide Web Consortium. (n.d.). *Alert and message dialogs pattern*. https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/

World Wide Web Consortium. (n.d.). *Carousel (slide show or image rotator) pattern*. https://www.w3.org/WAI/ARIA/apg/patterns/carousel/

SNS 자료: @uxwoodytips, 헷갈리는 아이콘 짝 9가지·헷갈리는 UI 짝 9가지 (사용자 제공 정적 캡처 2장, 2026-11-17 수집). 게시 URL·원작자 라이선스·실제 동작 미확인.
