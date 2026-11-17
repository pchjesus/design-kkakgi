# SRC-27 — 스크롤 경험과 화면 등장 9종 v0.1

> 2026-11-17 · RESEARCH · 사용자 제공 정적 SNS 캡처 1장 · [통합 아틀라스](ATLAS_HOME.md)
>
> [CAP] 화면에 @uxwoodytips가 관찰된다. 상단 원본 제목은 알림에 일부 가렸으나 **9개 카드의 명칭과 간략한 도식은 읽을 수 있다**. [USER] 사용자는 이번 항목별 미감 선호를 밝히지 않았음. [AI-HYP] 동작·구현·효과는 공식 기술과 일반 패턴을 기초로 추론한 것으로, 인스타 원본의 실제 영상 동작·지원 코드·라이선스는 미확인.
>
> **ID:** 기존 SRC-00~26의 원자료 243칸(중복 포함) 이후 SRC-27 9칸 신규. 함께 제공된 SRC-28·29의 18칸과 합해 원자료 누적 **270칸(중복 포함)**. 270개 고유 UI 패턴이나 사용자 선호 평가로 해석하지 않는다. 현행 Universal v1.3 APPROVED, 제품 코드 및 Pages 변경 없음.

## 1. 캡처 원본 순서·분류·구현 선택

| 번호 | 이미지 표기 [CAP] | 무엇인가 [AI-HYP] | 구현 선택(원본 코드 확인 아님) | 중복/연결 |
|---|---|---|---|---|
| 01 | 페이드 업 / Fade up | 요소가 아래에서 위로 이동하며 불투명해지는 등장 모션 | IntersectionObserver와 CSS opacity/transform; view timeline | [SRC-13 텍스트 등장](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md) |
| 02 | 패럴랙스 / Parallax | 깊이가 다른 레이어가 스크롤에 따라 서로 다른 거리/속도로 움직이는 시각 효과 | CSS scroll/view timeline, transform; 과도한 움직임 피하기 | [Creative Coding](creative-coding/README.md) |
| 03 | 스티키 헤더 / Sticky header | 스크롤 중 특정 지점부터 제목/탭이 화면에 붙어 맥락 보존 | CSS position: sticky; top 설정과 스크롤 컨테이너 확인 | [SRC-08](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md) |
| 04 | 가로 스크롤 / Horizontal | 가로로 배열된 연속 콘텐츠 탐색 | overflow-x, 선택적 scroll-snap, 터치/마우스/키보드 지원 | [SRC-24 Carousel 비교](UI_LIST_PRESENTATION_ATLAS_v0.1_20261112.md) |
| 05 | 스케일 인 / Scale in | 진입 때 요소 크기가 커지는 등장 효과 | IntersectionObserver + CSS scale, view timeline | [SRC-13·14](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md) |
| 06 | 텍스트 리빌 / Text reveal | 글자의 일부나 행을 가렸다가 공개하는 모션 | CSS mask/clip-path 또는 지연 공개; 텍스트 접근성 유지 | [SRC-13](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md) |
| 07 | 스태거 / Stagger | 여러 항목을 작은 시간 차로 순서대로 등장시킴 | 개별 딜레이; reduced-motion 대안 | [SRC-13·14](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md) |
| 08 | 진행 바 / Progress bar | 문서 읽은 정도 또는 실제 과업의 진행 상태 표시 | scroll-progress timeline 또는 실제 서버 상태와 연결 | [SRC-00 인디케이터](MOTION_INDICATOR_ATLAS_v0.1_20261105.md) |
| 09 | 무한 스크롤 / Infinite scroll | 다음 데이터 페이지를 스크롤 끝에서 더 불러오는 로딩 정책 | IntersectionObserver + 다음 페이지/종료/에러/복구 상태 | [SRC-24](UI_LIST_PRESENTATION_ATLAS_v0.1_20261112.md) |

## 2. 이 아홉 가지는 서로 다른 설계 축

- **모션 표현:** 01 Fade up, 02 Parallax, 05 Scale in, 06 Text reveal, 07 Stagger. 애니메이션이 시작되는 시점만 스크롤과 연관될 수도, 스크롤의 진행도에 실제로 동기화될 수도 있다.
- **공간/탐색:** 03 Sticky header와 04 Horizontal scroll. 공간을 고정하거나 콘텐츠를 탐색하는 구조.
- **상태/데이터:** 08 Progress bar와 09 Infinite scroll. 진행 상태의 **의미와 실제 데이터**를 다루므로 미적 효과로만 취급하면 안 된다.
- 따라서 서로 배타적인 9개 스크롤 방식이 아니다. 예: 스티키 헤더와 읽기 진행 바는 한 긴 문서에서 함께 사용 가능.

## 3. 기술 근거와 검증의 경계

[OFFICIAL] MDN은 CSS scroll-driven animation의 **scroll progress**(스크롤 양에 따라 진행)와 **view progress**(요소가 화면에 드나드는 비율에 따라 진행)를 구분한다. Intersection Observer API는 화면 교차 비율·진입 시점을 관찰하는 도구로, 자체적으로 동일한 애니메이션 시간을 보장하지 않는다. CSS sticky는 고정 방식이다. 이는 동명의 SNS 게시물이 구현된 기술을 확인한 것이 **아니다**.

[OFFICIAL] prefers-reduced-motion을 존중할 것. [RESEARCH] NN/g는 무한 스크롤이 스트림형 콘텐츠에 맞을 수 있지만 재방문·키보드 접근·하단 콘텐츠 접근 등에 불리할 수 있다고 지적한다. 읽기 중심 콘텐츠에서 사용자의 스크롤 속도·위치를 강제로 변경하는 스크롤재킹도 피할 것.

## 4. 적용 선택표 [AI-HYP]

| 과업 | 고려 | 위험 또는 실패 기준 |
|---|---|---|
| 제품 홍보 사이트 | 섹션별 Fade up/Scale in, 제한된 Parallax | 내용 가림, 과한 시점 변화, 모션 감소 설정 무시 |
| 장문의 학습 문서 | Sticky header, 실제 문서 위치 진행 선 | 헤더가 내용을 가림, 무한 로딩 중 가짜 100% |
| 많은 카드의 연속 탐색 | Horizontal scroll / Carousel 구분 | 다음 콘텐츠 존재 단서 없음, 키보드 조작 불가 |
| 상품/뉴스 피드 | Infinite scroll과 종료·에러·복귀 상태 | 푸터 도달 불가능, 스크롤 위치 유실 |
| 간호 기록·전문 업무 | 중요한 상태에만 최소 모션, 작업 진행의 진실값 표시 | 오류/저장 상태가 장식적 모션에 가림 |

## 5. 교차 참조와 평가

- [SRC-13 텍스트 모션](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md)와 겹침. [LAB NOTE 01](TEXT_MOTION_LAB_NOTE_01_20261108.md)에서 사용자 직접 평가한 것은 과거의 **일반 텍스트 페이드 긍정, 미완성 스크램블 부정**. 이번 캡처의 Fade up에 대한 별도 선호를 주장하지 않는다.
- [SRC-28·29 아이콘 및 UI 개념 비교](UI_SEMANTIC_PAIRS_ATLAS_v0.1_20261117.md)와 연결, 특히 Carousel vs Horizontal scroll / Paging vs Infinite scroll / Progress vs Steps.
- 정적 캡처 명칭·도식: **PASS (정적 관찰)**. 원본 영상 재생/시간/코드/실사용/모바일/접근성: **NOT RUN**. 원본 이미지·영상·폰트 GitHub 미게시. 제품/범용 지침/배포 변경: **N/A**.

## 6. 참고문헌 (APA 7판)

MDN Web Docs. (n.d.). *CSS scroll-driven animations*. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations

MDN Web Docs. (n.d.). *Intersection Observer API*. https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API

MDN Web Docs. (n.d.). *position*. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position

MDN Web Docs. (n.d.). *prefers-reduced-motion*. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion

Nielsen Norman Group. (2022). *Infinite scrolling: When to use it, when to avoid it*. https://www.nngroup.com/articles/infinite-scrolling-tips/

SNS 자료: @uxwoodytips, 스크롤 효과 아홉 가지(정적 캡처, 2026-11-17 수집). 실제 원본 URL/게시일·재사용 라이선스 미확인.
