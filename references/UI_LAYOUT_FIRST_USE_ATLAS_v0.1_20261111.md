# UI 레이아웃·앱 첫 사용 경험 레퍼런스 아틀라스 v0.1

> **2026-11-11 · RESEARCH DRAFT / 사용자 제공 정적 캡처 3장**  
> **범용 기준:** Universal Visual Design & UI/UX Guidelines **v1.3 APPROVED**. 이 자료는 승인 지침·제품별 UX·코드·GitHub Pages를 변경하지 않는다.
>
> **자료 구분:** [CAP] 캡처에 적힌 표현과 순서 · [OFFICIAL] 공식 플랫폼·웹 설계 문서에 명시된 동작 · [HYP] 디자인 깎기의 선택·취향 가설 · [NOT RUN] 실제 SNS 영상 재생·모션 타이밍·반응형 조작·시각/사용성 실험. 사용자에게 **모든 항목의 선호도가 확인된 것은 아님**.
>
> **원자료:** 이번 **3장 × 9개 = 27칸**. **SRC-19** 레이아웃 9칸, **SRC-20** 앱 첫 실행 9칸은 새 분석이다. **SRC-21** iOS 피드백 9칸은 기존 [SRC-15](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md#4-ios-플랫폼-피드백-src-15--네이티브-기능을-웹-장식으로-오인하지-않기)과 동일 내용이므로 별도 정의를 복제하지 않고 연결한다. 기존 171칸에 누적하면 **198개 원자료 칸(중복 포함)**이며 **198종 독립 UI라는 의미는 전혀 아니다.**
>
> **원본 표시:** 1·2장 화면에는 \`@uxwoodytips\`, 3장에는 \`@davidm_ai\`가 보인다. 정확한 원본 게시물 URL·재사용 라이선스·원본 영상의 움직임은 **미확인**. 이미지·영상을 GitHub에 재업로드하지 않고 텍스트 분석만 보존한다.

> **후속 자료 (2026-11-11):** [SRC-22 날짜 선택·SRC-23 행동심리 보강](UI_DATE_SELECTION_BEHAVIOR_ATLAS_v0.1_20261111.md)으로 이어진다. 본 문서의 198칸은 당시 집계이므로 소급 변경하지 않는다.

> **후속 목록 구조 연구 (2026-11-12):** [SRC-24 List/Grid/Card/Carousel/Table/Timeline/Accordion/Masonry/Infinite scroll](UI_LIST_PRESENTATION_ATLAS_v0.1_20261112.md)에서 SRC-19의 Card grid·Bento와 차이를 비교한다. 이 문서의 198칸은 작성 당시 집계로 보존한다.

## 1. 원본 캡처 인벤토리 — 표기 순서와 범위 보존

| ID | 캡처 제목 | 01–09 |
|---|---|---|
| **SRC-19** | 화면 배치 이름 9가지 | Hero section · Bento grid · Split screen · Card grid · Sidebar layout · Magazine layout · Dashboard · Z-pattern · Full bleed |
| **SRC-20** | 앱 처음 켜면 보는 화면 9가지 | Splash screen · Onboarding · Permission request · Coach mark · Social login · Terms agreement · Profile setup · Skeleton · Welcome screen |
| **SRC-21** | iOS Feedback Patterns PT.1 | Dynamic Island · Live Activity · HUD · Action sheet · Swipe actions · Haptic feedback · Jiggle mode · Symbol effect · Shake to undo |

SRC-19의 항목은 같은 분류 수준이 아니다. **Hero는 화면 영역, Bento/Grid/Split/Sidebar는 공간 구성, Magazine은 편집형 구성, Dashboard는 정보 유형, Z-pattern은 시선 흐름의 가설, Full bleed는 화면 경계까지 확장하는 표현 방식**이다. 서로 조합할 수 있다. SRC-20 역시 9장의 첫 화면을 차례로 보여주라는 것이 아니라 **첫 사용 시 나타날 수 있는 서로 다른 종류의 단계·상태·선택**이다.

## 2. 화면 배치 9종 [SRC-19] — 구조, 목표, 주의점

| 번호/명칭 | 무엇인가? [CAP+분석] | 잘 맞는 목적 [HYP] | 오용·검증할 위험 |
|---|---|---|---|
| **01 Hero section** | 넓은 첫 콘텐츠 영역에 제목·핵심 메시지·주 행동을 집중 | 브랜드 소개, 제품 가치 전달, 글의 대표 이미지 | 핵심 기능·본문이 첫 화면 아래로 밀리고 장식만 남지 않는가 |
| **02 Bento grid** | 중요도·콘텐츠 종류에 따라 크기가 다른 직사각 영역을 결합한 구성 별칭 | 서로 다른 콘텐츠를 정돈하면서 중요도 차이를 표현 | 카드 크기 차이가 정보 우선순위와 연결되는가; 작은 화면에서 순서가 꼬이지 않는가 |
| **03 Split screen** | 두 개의 주 공간을 나란히 분할 | 설명+시각화, 설정+실시간 결과, 비교 | 좁은 화면에서 분할 기준이 사라질 때 어느 부분을 먼저 보여주나 |
| **04 Card grid** | 반복되는 독립 개체를 비교 가능한 카드로 나열 | 목록, 상품, 학습 카드, 기능 허브 | 카드가 너무 많으면 모든 정보가 같은 중요도로 보이는가; 의미 없는 그림자/반복 |
| **05 Sidebar layout** | 지속 탐색 메뉴와 주 콘텐츠 영역을 분리 | 복잡한 작업도구, 문서·시뮬레이터 탭 전환 | 사이드바가 본문을 과도하게 압박하거나 모바일에서 길 찾기를 방해 |
| **06 Magazine layout** | 제목·본문·사진·여백의 크기와 리듬을 다르게 구성하는 편집형 레이아웃 | 기사·블로그·에디토리얼·전시 안내 | 독자가 내용을 읽는 순서·본문 폭·대비를 잃지 않는가 |
| **07 Dashboard** | 현황 요약·주요 지표·행동·상세 탐색을 한 화면에 제공하는 과업 유형 | 관리·모니터링·임상 업무의 상태 파악 | 지표만 많이 늘려 중요한 판단·경고·업무가 묻히지 않는가 |
| **08 Z-pattern** | 왼쪽 상단→오른쪽 상단→왼쪽 하단→오른쪽 하단을 잇는 **시선 유도 가설** | 구성요소 수가 적은 홍보·랜딩의 한 시안으로 검토 | **모든 사람이 Z로 읽는다는 법칙 아님**; 실제 언어 방향·내용·과업·시선 추적에 따라 달라짐 |
| **09 Full bleed** | 이미지·색면·미디어가 컨테이너 가장자리까지 닿는 연출 | 몰입형 사진·브랜드 히어로·감성적 표지 | 텍스트 안전 여백·대비·크롭·모바일·가로 넘침 |

**[OFFICIAL] CSS Grid는 행·열에 콘텐츠를 배치하고 요소의 크기·위치·중첩 관계를 조절하는 웹 레이아웃 기술이다.** 본문을 읽는 순서와 DOM/키보드 순서가 시각 순서와 분리되지 않도록 확인해야 한다. [MDN CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout).  
**[RESEARCH] NN/g의 시선 추적 글은 F, spotted, layer-cake, commitment 등 여러 스캔 패턴을 소개하며 콘텐츠에 따라 다른 패턴도 나타난다고 설명한다.** 따라서 Z 패턴을 무비판적으로 범용 규칙으로 채택하지 않는다. [Nielsen Norman Group](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/).

### 레이아웃 선택·비교를 위한 가벼운 판단표

| 과업 | 처음 검토할 후보 | 반대 선택이 더 좋은 경우 |
|---|---|---|
| 한 문장의 강한 제품 메시지 | Hero + Full bleed 일부 | 제품 조작·검색이 첫 과업이면 기능 진입을 먼저 |
| 항목의 중요도가 실제로 다름 | Bento / Magazine | 동일 속성의 많은 데이터를 빠르게 비교한다면 균등 Grid나 Table |
| 생리 모델과 조작의 인과관계 | Split screen | 모바일 폭에서 상태·그래프·제어가 분리되면 순차 표시 고려 |
| 업무 상태·예외 감지 | Dashboard + Sidebar | 행동 하나가 핵심이면 복잡한 대시보드 불필요 |
| 기사 읽기·시각 작품 설명 | Magazine | 법정 고지·긴 형식 문서에는 일관된 읽기 순서 우선 |

**기존 레퍼런스와 연결:** [KRDS 페이지 레이아웃 아틀라스](krds/LAYOUT_ATLAS.md)와 [Apple 레이아웃·플랫폼 자료](apple/README.md)는 **필요할 때만** 과업 기준으로 대조한다. 9개 예시는 보편적 9분류로 승격하지 않는다.

## 3. 앱 첫 사용 경험 9종 [SRC-20] — 실제 발생 조건을 분리

| 번호/명칭 | 기본 동작·맥락 | 오용·필수 확인 |
|---|---|---|
| **01 Splash screen** | 앱 실행 시작~첫 화면 준비 사이 시스템/브랜드 진입 표시. Android 12+는 시스템 스플래시로 앱 아이콘·배경·진입 전환 처리 [OFFICIAL]. | 불필요한 전용 스플래시 화면을 추가해 이중 로고·시작 지연을 만들지 않기 |
| **02 Onboarding** | 앱 사용법이나 핵심 가치를 필요한 사용자에게 소개. Apple HIG는 출시/launch 완료 후의 선택적이고 빠른 경험을 권고 [OFFICIAL]. | 모두에게 긴 강제 튜토리얼을 붙이지 않기; 건너뛰기·나중에 보기 |
| **03 Permission request** | 위치·카메라 등 보호 자원이 **실제로 필요한 시점**에 사용자 허가 요청 [OFFICIAL]. | 이유 없이 시작하자마자 대량 요청, 거절해도 쓸 수 있는 기능을 가로막기 |
| **04 Coach mark** | 현재 화면의 특정 버튼/요소에 맞춰 설명을 띄우는 맥락 안내 | 화면을 가리고 강제 반복하지 않기, 닫기·키보드·다시보기 경로 |
| **05 Social login** | 외부 신원 제공자를 통한 인증·가입 옵션 | 동의/취소/실패/계정 연동·로그아웃, 플랫폼 정책, 실제 필요성이 없는 로그인 강제 |
| **06 Terms agreement** | 이용약관·개인정보 처리 고지·필수/선택 동의 등 법적/운영 단계 | 동의하지 않은 항목을 임의 체크, 전체 동의에 선택 항목을 숨기기, 필수·선택·기록 혼동 |
| **07 Profile setup** | 이름·사진·관심사 등 초기 프로필 구성 | 필요 없는 개인정보를 수집하거나 본 기능보다 프로필 완성 강요 |
| **08 Skeleton** | 로드될 콘텐츠의 대략적인 구조를 선표시하는 **로딩 상태** | 처음 앱을 켤 때에만 나타나는 것이 아님. 영구 placeholder·진행률 거짓 표시 방지 |
| **09 Welcome screen** | 처음 접근했을 때 가치·다음 행동을 알려주는 진입/환영 화면 | Launch/Splash와 동일시하거나 의미 없는 CTA·축하 화면을 매번 강요하지 않기 |

### 처음 시작하는 경험의 구조

- **시스템 Launch/Splash ≠ Onboarding ≠ Welcome ≠ Skeleton:** 플랫폼 시작 상태, 사용법 안내, 진입 콘텐츠, 데이터 준비 상태는 서로 다르며 동시에 모든 화면이 필요한 것은 아니다.
- **권한·동의·인증은 조건부:** 플랫폼의 기능 요구·법적 의무·사용자 선택을 판단해 필요한 때만 제공한다. '첫 실행 UX 9종'을 9단계 필수 마법사로 오해하지 않는다.
- **다음 행동을 분명히:** 처음부터 기능을 사용할 수 있다면 불필요한 온보딩 없이 진입하도록 검토한다. 반대로 안전·법적·임상적 이유로 설명/동의가 필수라면 단순히 화면을 줄이려 생략하지 않는다.
- **상태 복구:** 로그인 실패/취소, 권한 거절, 약관 변경, 프로필 건너뜀, 오프라인 데이터 로드 실패 후 사용자가 무엇을 할 수 있는지 명시한다.

**[OFFICIAL] 근거:** [Apple Launching](https://developer.apple.com/design/human-interface-guidelines/launching), [Apple Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), [Apple Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy/), [Android Splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen/). 특정 제품의 필수 가입/동의 절차를 이 참고자료만으로 결정할 수 없다.

## 4. SRC-21 iOS Feedback Patterns — 중복 보존·실제 동작 연결

이번 세 번째 캡처의 9칸은 이미 정리된 [SRC-15 iOS 피드백 9개 상세 근거](UI_MOTION_BEHAVIOR_ADDENDUM_v0.1_20261108.md#4-ios-플랫폼-피드백-src-15--네이티브-기능을-웹-장식으로-오인하지-않기)와 **용어와 순서가 동일**하다. 별도 요약으로 원래 설명을 희석하지 않고 기존 문서에서 확인한다.

- **Dynamic Island** = 지원 기기의 시스템 표시 영역, **Live Activity** = 지속 이벤트 상태를 시스템 공간에 전달하는 기능. 서로 다르다. [Apple Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities).
- **Action sheet** = 맥락적 명령 선택, **Swipe actions** = 목록 항목에 직접 제스처로 명령을 노출. 형태와 제스처를 혼동하지 않는다.
- **Haptic / Symbol effect** = 지원 하드웨어·OS·시스템의 기능에 따른 반응. 단순 CSS 애니메이션이나 진동의 범용 웹 재현으로 동일시하지 않는다.
- **HUD / Jiggle mode / Shake to undo** = 특정 맥락의 피드백/편집/실행 취소 계열. **현재 OS에서 지원되는지·원본 SNS에서 실제 어떤 효과가 재생되었는지**는 별도 점검 필요.

## 5. 사용자 선호와 해석의 경계

- **[USER]** 이번에는 추가 자료 세 장을 “아틀라스에 반영”하라고 요청했다. **Hero/Bento/Sidebar/Full bleed 등 개별 항목의 개인적 미적 호불호를 직접 확인한 것은 아니다.**
- **[AI-HYP]** 이전에 언급한 정돈된 정보 위계·시각적 무게중심·무난한 반복 카드 레이아웃에 대한 문제의식과, 크기가 다른 모듈을 조합하는 Bento/Magazine/Split 후보는 연결될 수 있다.
- **[COUNTEREXAMPLE]** Bento의 개성만 좇으면 정보의 비교성·일관성이 나빠질 수 있고, Full bleed는 시각적 집중을 높이는 대신 업무 성능을 낮출 수 있다. 반면 균등 Card grid는 동등한 항목 비교에 더 적합할 수 있다.
- **[NO AUTO-ADOPTION]** 이 9가지 레이아웃은 새 범용 규칙이나 사용자 취향의 자동 확정안이 아니며, 앞으로 실제 프로젝트에서 **맥락→후보→렌더링→기능·접근성 검증** 순으로 선택한다.

## 6. 검증 상태

| 항목 | 결과 | 수준 |
|---|---|---|
| 캡처 3장 × 9칸 목록·순서 확인 | **PASS** | 사용자 제공 정적 이미지 |
| 새 레이아웃 9칸·첫 사용 UX 9칸 분리 | **PASS** | 문서 분석 및 공식 근거 일부 대조 |
| SRC-21 ↔ 기존 SRC-15 중복 확인 | **PASS** | 두 정적 캡처 및 기존 아틀라스 |
| Apple/Android/MDN/NN/g 자료 연결 | **PASS (공개 문서 조회)** | 문서 근거 / 실제 제품 시험 아님 |
| Instagram 원본 영상 속 모션·타이밍 검증 | **NOT RUN** | 정확한 게시물 링크/재생 확인 안 됨 |
| 모바일·브라우저·스크린리더·실사용 시험 | **NOT RUN** | 새로운 시안/프로그램 제작 안 함 |
| 취향 비교 실험·성과 측정 | **NOT RUN** | 레퍼런스 수집 중심 활동 유지 |
| GitHub 사진·영상 복제, 범용 지침·앱/Pages 변경 | **N/A** | 하지 않음 |

## 7. 참고문헌 (APA 7판)

Apple. (n.d.). *Launching*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/launching

Apple. (n.d.). *Onboarding*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/onboarding

Apple. (n.d.). *Privacy*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/privacy/

Apple. (n.d.). *Live Activities*. Apple Developer. https://developer.apple.com/design/human-interface-guidelines/live-activities

Google. (n.d.). *Splash screens*. Android Developers. https://developer.android.com/develop/ui/views/launch/splash-screen/

MDN Web Docs. (n.d.). *CSS grid layout*. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout

Pernice, K. (2019, August 25). *Text scanning patterns: Eyetracking evidence*. Nielsen Norman Group. https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/

사용자 제공 Instagram 정적 캡처 3장. (2026, 11월 11일). *화면 배치 이름 9가지·앱 처음 켜면 보는 화면 9가지·iOS Feedback Patterns PT.1* [개인 대화의 정적 자료; @uxwoodytips/@davidm_ai 표기, 정확한 게시물 원본 및 라이선스 미확인].

---

**운영 결론:** 이번 추가는 연구 아틀라스의 **정보 구조·첫 실행 흐름**을 보완한 것이며, 단일 스타일을 더 강하게 선호한다거나 모든 제품에 온보딩을 추가해야 한다는 근거가 아니다. 다음 레퍼런스가 오면 새 취향 평가·반례·관련 근거만 보강한다. 새로운 UI 실험·코드 변경을 자동 시작하지 않는다.
