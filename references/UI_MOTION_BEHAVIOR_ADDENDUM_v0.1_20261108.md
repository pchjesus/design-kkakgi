# 디자인 깎기 — UI 움직임·화면전환·완료·플랫폼 피드백 연구 증보 v0.1

> **2026-11-08 · RESEARCH / 문서 근거 검토 단계**  
> **현행 기준:** Universal Visual Design & UI/UX Guidelines **v1.3 APPROVED**. 지침 자체·웹앱·기능·GitHub Pages는 변경하지 않는다.
>
> **자료 범위:** 사용자 추가 제공 **6장 × 9칸 = 54개 원자료 항목**. 먼저 기록한 [9종 인디케이터+18종 확장 아틀라스](MOTION_INDICATOR_ATLAS_v0.1_20261105.md), [12장×9칸 UI 패턴 아틀라스](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md)에 덧붙이는 **심층 근거 자료**다. 9+108+54=**171칸은 중복이 있는 원자료 칸 수**이지 독립 UI 구성요소 171종이 아니다.
>
> **출처 구분:** [CAP] 사용자 제공 정적 SNS 캡처의 *표기* / [OFFICIAL] 연결된 공식 가이드·실제 구현 API 설명 / [DEMO] 공개 데모가 명시한 동작 / [HYP] 향후 실험할 선택 가설 / **NOT RUN** 원본 인스타 영상의 실제 재생·프레임/지속시간·마우스/터치·스크린리더/실기기 검증.
>
> **중요한 출처 한계:** 첫째·둘째·넷째·다섯째·여섯째 캡처에서 **@uxwoodytips**, 셋째에서는 **@davidm_ai** 계정 표기가 관찰된다. 검색에서는 이 **정확한 원본 게시물의 재생 가능한 URL·실제 모션 프레임·재배포 라이선스를 확인하지 못했다**. 따라서 아래 움직임 설명은 **그 계정 게시물의 동작을 증명하는 기록이 아니라 동명 패턴의 공신력 있는 구현 예시**다. GitHub에 해당 SNS 화면·영상·이미지·타사 소스·폰트는 게시하지 않는다.

## 1. 원본 6장 표기 인벤토리 (순서 보존, 번역/동일시 보류)

| 새 식별자 | 제목(캡처) | 01–09 항목(캡처에 적힌 순서) |
|---|---|---|
| **SRC-13** | 텍스트 등장 9가지 | Typewriter / Fade up / Letter stagger / Count up / Scramble / Mask reveal / Highlight / Word rotate / Blur in |
| **SRC-14** | 화면 전환 9가지 | Push / Modal present / Fade through / Shared element / Card expand / Zoom / Stagger in / Tab switch / Sheet expand |
| **SRC-15** | iOS Feedback Patterns, Part 1 | Dynamic Island / Live Activity / HUD / Action sheet / Swipe actions / Haptic feedback / Jiggle mode / Symbol effect / Shake to undo |
| **SRC-16** | 헷갈리는 UI 짝 2탄 | Dropdown menu vs Select / Button vs Link / Placeholder vs Label / Hamburger vs Kebab / App bar vs Tab bar / Card vs List / Avatar vs Thumbnail / Banner vs Popup / FAB vs Icon button |
| **SRC-17** | 완료 피드백 9가지 | Check animation / Strikethrough / Button morph / Progress complete / Send animation / Stamp / Badge unlock / Confetti / Success screen |
| **SRC-18** | 헷갈리는 UI 짝 1탄 | Toggle vs Checkbox / Radio vs Checkbox / Tabs vs Segmented / Modal vs Bottom sheet / Toast vs Snackbar / Tooltip vs Popover / Chip vs Badge / Spinner vs Skeleton / Stepper vs Slider |

**[CAP]** 행 이름은 이미지에 보이는 영문·한글 명칭을 정상화해 적은 것. **공식 표준 명칭/일관된 단일 범주라는 뜻이 아니다.** SRC-13~18은 기존 SRC-00~12와 중복되는 패턴이 많다.

## 2. 텍스트 등장 [SRC-13] — 동작 설명·구현·제약

| 항목 | [OFFICIAL]/[DEMO]에서 확인 가능한 **일반적 동작·구현 가능성** | 판단·실패 위험 |
|---|---|---|
| 01 Typewriter | 글자가 순서대로 보이게 하거나 문자 부분 문자열을 단계적으로 늘림. Motion의 **Text animation** 문서는 typewriter를 별도 계열로 다룸. | 속도·커서·한글 조합형 자모 처리 방식은 원본 캡처로 미확인; 중요한 긴 문장을 기다리게 만들지 않기 |
| 02 Fade up | 불투명도를 올리면서 약간 위쪽으로 이동하는 표현. Motion keyframes/variants의 opacity+y 결합으로 구현 가능. | 이동을 없앤 fade-only 감소 모션 대안 제공 |
| 03 Letter stagger | 문자 단위 span 분리 뒤 인덱스/순서별 지연. Motion \`stagger()\`의 순서·방향·간격 조절 지원. | 긴 글의 DOM 증가, 스크린리더가 한 글자씩 읽지 않도록 완성 문구 접근 가능한 이름 유지 |
| 04 Count up | 목표 수치까지 화면 숫자를 변화시키는 일반적 연출. SwiftUI \`numericText\` 등 수치 전환도 제공. | '가짜 수치'를 실제 데이터 변화로 오인시키지 말 것; 정지 상태에 정확한 최종값 표시 |
| 05 Scramble | 임시 글자가 치환·교체되다가 목표 문구로 수렴하는 표현. Motion Text animation 문서의 scramble 항목 참고. | 문구 의미를 읽기 어려운 상태로 방치하지 않기; 필수 안내/의료/금융 본문에 적용 주의 |
| 06 Mask reveal | \`clip-path\`/overflow 영역을 이동·확장해 기존 완성된 텍스트를 드러냄. Motion variants 예시의 clip-path 공개가 구현 참고. | 실제 본문은 DOM/접근성 계층에서 존재하게 하고 시각 마스크로만 숨기기 |
| 07 Highlight | 이미 보이는 문구의 배경색·선·강조 영역을 시간에 따라 표현. CSS transition/WAAPI로 구현 가능. | 색 변화만으로 중요한 의미·상태 전달 금지 |
| 08 Word rotate | 키워드를 바꿔 끼우며 회전/이동/불투명도 전환하는 계열. Motion \`AnimatePresence\`의 exit/enter 시퀀스 참고. | 자동 변경 텍스트는 읽기 시간과 모션 중단 제어, 문장 의미 변화에 주의 |
| 09 Blur in | filter blur에서 선명함으로, 종종 opacity와 함께. CSS transition/WAAPI 가능. | 흐림은 텍스트를 일시적으로 읽지 못하게 만들 수 있음; 모션 감소 시 즉시 완성 문구 |

**확인 가능한 API 근거:** [Motion Text animation](https://motion.dev/docs/text-animation) · [Motion stagger](https://motion.dev/docs/stagger) · [Motion AnimatePresence](https://motion.dev/docs/react-animate-presence) · [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate) · [Apple SwiftUI numeric text transition](https://developer.apple.com/documentation/swiftui/contenttransition).

**의미 있는 검증 질문:** 글자 등장 효과가 실제 이해 속도를 높이는가? 문장이 완성되기 전에도 보조기기가 정확한 한 문장으로 읽는가? 텍스트 변경·취소·복수 언어·reduced motion에서 뜻이 보존되는가?

## 3. 화면 전환 [SRC-14] — 공간·계층·연속성의 수준

| 항목 | 공식 문서로 확인되는 대응 / [HYP] | 조작·검증 조건 |
|---|---|---|
| 01 Push | 화면 계층의 다음 화면으로 이동하면서 이전/다음 화면이 축 방향으로 옮겨지는 일반적 내비게이션 효과 | '뒤로' 시 이동 관계가 역으로 이해되는지, 실제 history/포커스 상태 |
| 02 Modal present | 현재 맥락을 남기고 위에 새로운 작업 레이어를 띄움. **모달 여부는 배경 비활성·포커스 관리로 결정** | 배경 상호작용 차단, Escape/취소·초점 복귀 |
| 03 Fade through | 이전 내용의 사라짐과 다음 내용의 등장을 시간차 또는 겹침으로 표현. Motion \`AnimatePresence\`의 sync/wait로 유사 유형 설계 가능 | 중간 중첩으로 글자가 두 번 읽히지 않는가 |
| 04 Shared element | 동일한 대상이 이전/다음 레이아웃 사이를 크기·위치 변경으로 이동. Motion \`layoutId\`, Android Compose sharedElement, Web View Transition API | source/destination ID 일치, 이미지 왜곡·전환 끊김 |
| 05 Card expand | 카드가 상세뷰로 확대·전환되는 공간적 은유, shared layout 또는 size/position transition 구현 | 카드와 상세 페이지의 실제 같은 대상인지 |
| 06 Zoom | 화면 또는 대상이 커지거나 작아지는 전환, CSS transform/WAAPI 가능 | 과한 확대·어지럼·모션 감소 대안 |
| 07 Stagger in | 목록/카드가 순서대로 진입. Motion stagger/variants가 구체 구현 API 제공 | 콘텐츠 접근을 애니메이션 때문에 지연하지 않는가 |
| 08 Tab switch | 탭의 선택 상태와 패널 변경; 움직이는 선택선은 Motion layoutId와 구분 가능한 표현 | 탭 키보드 화살표·활성 상태·로드 지연/초점 일관성 |
| 09 Sheet expand | 시트가 현재 맥락에서 확장·축소되는 표현. Apple HIG는 iOS/iPadOS modal/nonmodal sheet 모두 다룬다 | 닫기·중간 높이·스크롤 충돌·입력값 유지/저장 |

**실제 비교 자료:** [Motion AnimatePresence 3모드 라이브 예제](https://motion.dev/examples/react-animate-presence-modes) · [Motion Layout Animation](https://motion.dev/docs/react-layout-animations) · [Android shared element transition](https://developer.android.com/develop/ui/compose/animation/shared-elements) · [MDN View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using) · [Apple HIG Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) · [WAI-ARIA Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

**특히 중요한 반례 [OFFICIAL]:** Android Compose shared element는 일부 View/Compose 혼합 또는 Dialogue/ModalBottomSheet 래퍼와 상호 운용 제한이 있으며, 이미지 ContentScale나 도형 클리핑을 자동 보간하지 않는다. 즉 'shared element 한 줄이면 어디서나 똑같이 된다'고 말할 수 없다.

## 4. iOS 플랫폼 피드백 [SRC-15] — 네이티브 기능을 웹 장식으로 오인하지 않기

| 항목 | 확인 가능한 실제 플랫폼 개념 | 연구 시 경계 |
|---|---|---|
| 01 Dynamic Island | iPhone 일부 모델의 **OS 화면 영역·프레젠테이션 맥락**. Live Activity의 compact/minimal/expanded 형태를 표시할 수 있다 | 웹페이지에 검은 알약을 그리는 것은 Dynamic Island 기능 구현이 아님 |
| 02 Live Activity | ActivityKit/WidgetKit/SwiftUI를 통한 **진행 중 사건의 시스템 전체 표시**. request/update/end 라이프사이클 | 데이터 갱신·stale 상태·장치 지원·OS 권한 확인. Dynamic Island와 동의어 아님 |
| 03 HUD | 임시 상태·볼륨 등의 화면 위 피드백을 가리키는 넓은 용어; 특정 화면 형태를 통일한 단일 API라고 단정할 수 없음 | 중요 오류를 잠깐 사라지는 HUD에만 담지 않기 |
| 04 Action sheet | Apple HIG의 **사용자가 시작한 동작과 관련된 선택을 제공하는 모달 뷰**. SwiftUI confirmationDialog, UIKit actionSheet 관련 API | 단순 임의 목록 메뉴/일반 Sheet와 혼동 금지 |
| 05 Swipe actions | 리스트 항목에서 밀어서 숨겨진 동작을 드러내는 제스처 계열 | 우발 삭제·복구·선택 가능·접근성 조작 대안 |
| 06 Haptic feedback | SwiftUI \`sensoryFeedback\`은 selection/success/warning/error/impact 등 차별화된 반응 타입 제공 | 실제 햅틱 장치/OS·사용자 설정 필요, 소리·시각과 함께 의미 전달 |
| 07 Jiggle mode | 앱 아이콘 등 편집 모드를 암시하는 흔들림 표현으로 알려진 패턴 | 편집 모드가 아니라면 흔들림의 의미가 모호함. 원본 동작 미확인 |
| 08 Symbol effect | Apple Symbols 프레임워크의 discrete/indefinite/transition/content transition 효과, bounce/pulse/replace 등 지원 | SF Symbols 라이선스·적용 대상·종료 조건 확인 |
| 09 Shake to undo | 기기 흔들기 입력을 Undo 명령과 연결하는 플랫폼·앱 수준 상호작용 계열 | 현재 OS/앱에서의 제공·설정은 별도 확인, **항상 메뉴·키보드 대체 Undo** |

**근거:** [Apple Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) · [ActivityKit data lifecycle](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) · [Apple Action Sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets/) · [Apple Haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) · [SwiftUI sensoryFeedback](https://developer.apple.com/documentation/swiftui/sensoryfeedback) · [Apple Symbols](https://developer.apple.com/documentation/symbols) · [Apple HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

**검증 경계:** Apple 문서가 '해당 API/패턴은 존재한다'는 근거이지, **SNS 카드 9개가 정확히 그 API를 사용했다는 증거가 아니다**. 웹/PWA에서 iOS 네이티브 기능과 완전히 동일하게 재현할 수 있다고 약속하지 않는다.

## 5. 완료 피드백 [SRC-17] — ‘완료’의 수준을 먼저 분류

| 항목 | 대표적인 동작 모형 / 구현 후보 | 보여도 되는 시점·주의 |
|---|---|---|
| 01 Check animation | SVG 경로 길이/clip path로 체크가 그려지듯 나타남 | 성공을 확인한 뒤 상태 텍스트와 함께 |
| 02 Strikethrough | 완료된 작업 문장에 취소선/체크/색 전환 | 할 일 상태가 실제로 바뀌었는지 |
| 03 Button morph | 버튼 → 로딩 → 결과 아이콘/문구 형태 변환 | pending/실패/재시도 모두 복구 가능해야 |
| 04 Progress complete | 실제 프로그레스가 100% 도달, 체크/설명 등장 | 업로드 100%≠서버 측 최종 처리 완료일 수 있음 |
| 05 Send animation | 전송 방향으로 아이콘/버튼 이동·사라짐 | 송신 시작과 실제 전송 성공을 혼동하지 않기 |
| 06 Stamp | 완료/승인 도장 모양의 시각 효과 | 법적 승인/검토 상태와 비주얼 동기화 필수 |
| 07 Badge unlock | 달성 조건 충족 시 배지 상태 해제 | 가짜 달성, 지나친 재방문 유도 금지 |
| 08 Confetti | 완료의 축하를 시각적으로 표현 | 드문 성취/전환점에 한정, reduced motion·광과민 고려 |
| 09 Success screen | 별도 화면에서 완료·다음 행동/기록 확인 | 중요한 작업이면 영수증/결과·오류 시 복구 정보 제공 |

**판단 가설 [HYP]:** 단순 체크박스 완료는 작은 변화가 적합할 수 있고, 중요한 다단계 제출에는 명시적 성공 화면이 도움이 될 수 있다. 단 **사용성·전환율·감정 효과가 검증됐다는 뜻이 아니다**. 신뢰성이 중요한 의료·금융·파일 저장 결과는 실제 API/저장/서버 응답을 확인해야 한다.

**구현 근거:** [MDN Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate) (프레임 재생/완료 감시/취소 가능) · [Motion AnimatePresence](https://motion.dev/docs/react-animate-presence) · [Apple SF Symbols effects](https://developer.apple.com/documentation/symbols).

## 6. 헷갈리는 UI 비교 [SRC-16, SRC-18] — 18쌍 판단표

**정의/메커니즘 비교는 공식 가이드 범위 내. 제품별 명칭은 완전히 표준화되어 있지 않음.**

| 비교 | 무엇이 결정 기준인가? |
|---|---|
| 16-01 Dropdown menu vs Select | **명령** 실행 목록인가 **폼 값** 선택인가? 같은 팝업 모양도 동작 계약이 다르다 |
| 16-02 Button vs Link | 현재 문맥에서 **행동을 수행**하면 button, **다른 URL/위치로 탐색**하면 link. 외관보다 시맨틱이 중요 |
| 16-03 Placeholder vs Label | 레이블은 입력의 **정체성**을, placeholder는 임시 예시/힌트 역할. 입력 시작 후 사라지는 placeholder를 유일한 label로 쓰지 말 것 |
| 16-04 Hamburger vs Kebab | 그림의 별칭일 뿐 기능 보증 없음. 실제 동작은 '전체 메뉴 열기' vs '해당 항목 옵션'으로 명명 |
| 16-05 App bar vs Tab bar | 앱 바는 보통 제목·도구·상위 행동, 탭 바는 목적지/섹션 탐색. 두 영역은 병존 가능 |
| 16-06 Card vs List | 독립 개체의 시각·행동 그룹화 vs 다수 레코드의 밀도·스캔. UI 시맨틱과 반복 요소 함께 결정 |
| 16-07 Avatar vs Thumbnail | 사람/개체의 정체성 표현 vs 콘텐츠 자체의 미리보기 |
| 16-08 Banner vs Popup | 화면 내 지속/비차단 메시지 vs 겹쳐지는 임시/모달 맥락. 제품별 용어 범위 다름 |
| 16-09 FAB vs Icon button | FAB는 **주요 동작 우선순위·화면 위치**의 패턴; Icon button은 **표현 방식**. 중첩 관계 가능 |
| 18-01 Toggle vs Checkbox | 즉시 켜고/끔 스위치 vs 폼에서 선택/동의 상태. 서버 반영 여부·제출 시점 확인 |
| 18-02 Radio vs Checkbox | 상호 배타적 **하나 선택** vs 독립적 **여러 개 선택** |
| 18-03 Tabs vs Segmented | 정보 패널 탐색 vs 배타적 보기/값의 간결한 선택; 디자인 시스템에 따라 의미 중첩 |
| 18-04 Modal vs Bottom sheet | 모달은 **배경 상호작용 차단 성질**, bottom sheet는 **표시 위치·형태**. **모달 바텀시트**도 가능 |
| 18-05 Toast vs Snackbar | 짧은 비차단 알림의 유사 계열; 일부 시스템은 snackbar에 Undo 같은 동작을 포함. 명칭이 전체적으로 통일된 규격은 아님 |
| 18-06 Tooltip vs Popover | 짧은 **비상호작용 보조 설명** vs 포커스 가능한 내용·작업을 포함할 수 있는 팝오버. W3C tooltip 패턴은 work in progress |
| 18-07 Chip vs Badge | 분류·필터·선택/삭제 가능한 작은 객체 vs 수량·상태의 라벨. 같은 모양일 수 있음 |
| 18-08 Spinner vs Skeleton | 구조 없는 처리 중 표시 vs 앞으로 올 콘텐츠의 **뼈대**와 위치를 예고 |
| 18-09 Stepper vs Slider | discrete 값을 ±단위로 조정 vs 트랙 위 값·범위를 직접 선택. Step indicator는 또 다른 개념 |

**근거:** [GOV.UK Label/Placeholder](https://design-system.service.gov.uk/components/text-input/) · [W3C Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) · [W3C Tooltip](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/) · [W3C Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) · [Apple Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) · [Apple Action Sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets/). Button/Link, Chip/Badge/FAB 등의 디자인 시스템별 변형은 **일률적 공식 정의가 아닌 선택 기준 정리**임.

## 7. 현 단계에서 외부 검색으로 메운 것 / 여전히 알 수 없는 것

| 질문 | 결론 | 수준 |
|---|---|---|
| 문자별 등장·스크램블·마스크·숫자 전환을 실제로 구현할 수 있나? | Motion·CSS/WAAPI·SwiftUI 문서에서 대응 구현/API 설명 확인 | **PASS [OFFICIAL]** |
| Shared element·fade·stagger를 실제 데모와 API로 설명할 수 있나? | Motion 3모드 라이브 예시, layoutId, Android/MDN 문서 확인 | **PASS [OFFICIAL/DEMO 설명]** |
| 시스템 Dynamic Island/Live Activity가 같은 건가? | 표시 영역/시스템 맥락 vs 상태 데이터 라이프사이클로 구분 | **PASS [OFFICIAL]** |
| Action sheet / Sheet / Modal / Tooltip의 행동 차이가 있나? | Apple·W3C 문서에 상태·모달리티·키보드 계약 명시 | **PASS [OFFICIAL]** |
| 특정 게시물의 실제 재생 속도/이징/한 프레임/제작 기법? | 원본 SNS URL 및 재생 자료 확인 불가 | **NOT RUN** |
| 직접 링크된 데모를 눌러 실제 화면 전환·키보드·모바일 조작까지 재현했나? | 외부 문서·예시 설명을 확인했지만 인터랙티브 브라우저 테스트는 실시하지 않음 | **NOT RUN** |
| 햅틱이 웹/모든 기기에서 동일하게 체감되나? | 플랫폼·OS·지원 하드웨어 의존, 직접 확인하지 않음 | **NOT RUN** |
| 사용자가 이 중 어떤 모션을 선호하고 수행에 유리한가? | 개별 선호 평가는 아직 없음 | **NOT RUN** |
| 실제 앱 코드 변경·Pages 배포·범용 v1.3 수정 | 하지 않음 | **N/A** |

### 원본 동작을 복원해야 할 때

정확한 게시물 URL·사용자 제공 동영상 또는 화면 녹화가 있으면 우선 **재생 속도, 최초/반복/중단 상태, 입력 이벤트, 타이밍, 소리/진동 여부**를 측정한다. 추후 확보한 정보로 [CAP]을 갱신하기 전에는 여기서 확인한 일반 API를 원본 제작 기술이라 단정하지 않는다.

## 8. 네 가지 심층 비교 실험 제안 [HYP; 실제 제작/실행 안 함]

| 실험 | 통제 조건 | 변인 | 판정 |
|---|---|---|---|
| **T-01 텍스트 등장** | 같은 한글 문구·서체·폭·위치·색 | 즉시 vs fade vs letter stagger vs scramble | 첫 판독 시간, 정보 이해, 반복 피로, reduce-motion |
| **T-02 화면 전환** | 같은 카드 목록/상세/뒤로 기능 | instant vs crossfade vs shared element | 맥락 유지·빠른 중복 탭·뒤로/초점·성능 |
| **T-03 완료 반응** | 같은 저장/전송 동작·진짜 성공/실패 응답 | toast vs button morph vs success screen | 성공 인지·오류 복구·상태 거짓 양성 |
| **T-04 과업·감각** | 같은 탭/선택 동작과 결과 | 시각-only vs 시각+햅틱(지원 기기) | 부담·명료성·접근성; 장치·설정 변수 별도 통제 |

**공통 게이트:** 사용자 상호작용에 반응할 때 애니메이션이 즉시 중단·교체 가능한가, 상태가 실제 데이터와 일치하는가, 키보드/터치/200% 확대/모션 감소에서 동작하는가, 사용자 호불호와 과업 수행을 별도 평가했는가. 기준: [Apple HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion) · [WCAG 2.2 SC 2.3.3 (AAA)](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions) · [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion).

## 9. 설계 철학과 취향 근거의 경계

- [USER] 사용자는 **디자인 레퍼런스를 폭넓게 수집하고 정확한 기능·상태·모션 명칭을 이해**하려 한다. 이 6장의 모든 스타일/모션을 직접 좋아한다고 평한 것은 아니다.
- [AI-HYP] 지금까지의 물성·감각·공간 구조 관심과 **Shared element, 화면 전환, 햅틱**은 탐구할 가치가 있다. 하지만 '항상 스프링을 써라' 같은 범용 스타일 규칙이 아니다.
- [OFFICIAL] Apple은 목적 있는 짧고 정확한 피드백, 과도한 반복 회피, 모션의 중단 가능성과 대체 표현을 권장한다. WCAG 2.2의 SC 2.3.3은 **AAA** 수준이며 A/AA 필수 항목인 것처럼 오기하지 않는다.
- [PROTECTION] 사용자가 특히 좋아하는 **심장의 전도계 교육 시뮬레이터**처럼 정돈되고 미세한 UI에서는 일체의 장식 모션을 추가하기보다 학습 상태의 실제 변경에만 제한적으로 사용해야 한다는 가설을 우선 검토한다.

## 10. 참고문헌 (APA 7판, 공개 자료 중심)

Apple. (n.d.). *Action sheets*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/action-sheets/

Apple. (n.d.). *Live Activities*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/live-activities

Apple. (n.d.). *Motion*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/motion

Apple. (n.d.). *Playing haptics*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/playing-haptics

Apple. (n.d.). *SensoryFeedback*. Apple Developer Documentation. https://developer.apple.com/documentation/swiftui/sensoryfeedback

Apple. (n.d.). *Sheets*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/sheets

Apple. (n.d.). *Symbols*. Apple Developer Documentation. https://developer.apple.com/documentation/symbols

Google. (n.d.). *Shared element transitions in Compose*. Android Developers. https://developer.android.com/develop/ui/compose/animation/shared-elements

Government Digital Service. (n.d.). *Text input*. GOV.UK Design System. https://design-system.service.gov.uk/components/text-input/

MDN Web Docs. (n.d.). *Using the View Transition API*. https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using

MDN Web Docs. (n.d.). *Element: animate() method*. https://developer.mozilla.org/en-US/docs/Web/API/Element/animate

MDN Web Docs. (n.d.). *prefers-reduced-motion*. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion

Motion. (n.d.). *Text animation*. https://motion.dev/docs/text-animation

Motion. (n.d.). *Layout animation*. https://motion.dev/docs/react-layout-animations

Motion. (n.d.). *AnimatePresence*. https://motion.dev/docs/react-animate-presence

Motion. (n.d.). *Stagger*. https://motion.dev/docs/stagger

Motion. (2025, September 24). *AnimatePresence modes* [Interactive example]. https://motion.dev/examples/react-animate-presence-modes

World Wide Web Consortium. (n.d.). *Dialog (modal) pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

World Wide Web Consortium. (n.d.). *Tooltip pattern* [Work in progress]. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/

World Wide Web Consortium. (n.d.). *Understanding success criterion 2.3.3: Animation from interactions (Level AAA)*. https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

사용자 제공 SNS 캡처. (2026, November 8). *텍스트 등장·화면 전환·iOS 피드백·UI 비교·완료 피드백 6개 이미지* [개인 대화에서 제공된 정적 자료; 원본 게시물 URL/영상 동작 미확인].

---

**결론:** 아틀라스를 불필요한 필수 규칙으로 확장하지 않고, 개별 패턴을 **사용자 과업 → 의미·상태 → 구현 근거 → 움직임 → 복구/접근성 → 실제 검증** 순서로 조사할 수 있도록 만들었다. SRC-13~18은 기존 분류의 확장이며 중복이 많은 원자료의 추가이지 새로운 UI 표준이나 개인 취향 승인 목록이 아니다.
