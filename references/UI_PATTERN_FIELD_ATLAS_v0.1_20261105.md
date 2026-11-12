# 디자인 깎기 — UI 패턴·상태·입력·모션 현장 아틀라스 v0.1

> **2026-11-05 | RESEARCH DRAFT | 현행 기준: Universal Visual Design & UI/UX Guidelines v1.3 APPROVED (변경 없음)**
>
> **자료 범위:** 사용자 제공 SNS 캡처 12장 × 9개 항목 = **108개의 원자료 칸** + 기존 인디케이터 캡처 1장 × 9개 = **117개의 원자료 칸**. 동일 항목이 중복되고 ‘스타일/심리/몸짓/상태’도 포함되므로 **117개 독립 컴포넌트라는 뜻이 아니다**. 기존 [인디케이터·마이크로인터랙션 아틀라스 v0.1](MOTION_INDICATOR_ATLAS_v0.1_20261105.md)의 9+18종 조사는 보존하고, 이 문서는 **새 12장 분류·중복 통합·선택 기준**을 보완한다.
>
> **출처·근거:** [USER-SOURCE] 사용자가 전달한 정적 화면의 9칸 목록·레이블 / [OBS] 시각적으로 확인한 목록 / [EXT] 공식 문서로 확인한 개념·동작 / [AI-HYP] 현장 적용 가설 / **NOT RUN** 실제 원본 동영상 애니메이션, 키보드·모바일 테스트, 실제 제품의 UX 효과.
>
> **권리:** 사용자 제공 화면에는 @uxwoodytips가 보인다. **원본 영상 링크·게시물 날짜·실제 제작자·재사용 라이선스는 미확인**. 외부 원본/스크린샷/영상/썸네일/폰트/재배포 코드를 GitHub에 넣지 않는다. 텍스트 설명·출처 URL만 등록한다. 이 문서는 사용자 개인의 **미적 선호 확정 목록이 아니라 연구 자료**다.

## 1. 13개 원본 캡처 목록 — 순서 보존

- **SRC-00** (기존, 9개): Progress bar / Step indicator / Page indicator / Story progress / Scroll progress / Progress ring / Strength meter / Tab indicator / Home indicator. 자세한 구현 근거는 [기존 아틀라스](MOTION_INDICATOR_ATLAS_v0.1_20261105.md).
- **SRC-01** (추가 1, 일반 UI): Toast / Modal / Bottom sheet / Dropdown / Toggle / Tab / Skeleton / Tooltip / Carousel.
- **SRC-02** (추가 2, 입력 UI): Select box / Checkbox / Radio button / Text field / Date picker / Search bar / Stepper(수량 버튼) / Range slider / File upload.
- **SRC-03** (추가 3, 알림·피드백): Toast / Snackbar / Banner / Modal dialog / Bottom sheet / Inline error / Tooltip / Coach mark / Badge.
- **SRC-04** (추가 4, 시각 스타일): Skeuomorphism / Flat design / Material design / Neumorphism / Glassmorphism / Claymorphism / Neo brutalism / 3D icon / Liquid glass.
- **SRC-05** (추가 5, 심리·행동): Anchoring / Loss aversion / Default effect / Social proof / Scarcity / Framing effect / Choice overload / Peak-end rule / Zeigarnik effect.
- **SRC-06** (추가 6, 빈 화면·예외): First use / No search results / No filter results / Offline / Permission needed / All caught up / Emptied / Error state / Locked content.
- **SRC-07** (추가 7, 메뉴 아이콘 별칭): Hamburger / Kebab / Meatballs / Waffle / Bento / Döner / Veggie burger / Stairs / Sliders. **별칭은 규격명/스크린리더 이름이 아니다.**
- **SRC-08** (추가 8, 화면 탐색): Bottom tab bar / Top tabs / Navigation drawer / Breadcrumb / Sticky header / Floating action button / Pagination / Infinite scroll / Back navigation.
- **SRC-09** (추가 9, 움직임): Ease-in / Ease-out / Spring / Bounce / Stagger / Fade / Slide / Zoom transition / Shared element.
- **SRC-10** (추가 10, 제스처): Tap / Long press / Swipe / Swipe to delete / Drag and drop / Pinch to zoom / Double tap / Pull to refresh / Edge swipe.
- **SRC-11** (추가 11, 상세 입력): Text field states / Select / Segmented control / Switch / Checkbox / Radio button / Slider / Quantity stepper / Date picker.
- **SRC-12** (추가 12, 로딩): Spinner / Skeleton screen / Progress bar / Progress ring / Step indicator(단계 표시) / Blur-up image / Optimistic UI / Streaming text / Loading button.

**SRC 번호는 수집 파일명/원본 게시물 ID가 아닌 본 문서 내 정적 분류 식별자**다. 원본 제작자·날짜·라이선스를 주장하지 않는다. SRC-01~12의 108개 칸에는 중복 용어가 많으므로 독립 패턴 수·실제 동작 성공률·선호 빈도를 계산하지 않는다.

> **후속 확장 (2026-11-11):** [레이아웃·앱 첫 사용 경험 아틀라스](UI_LAYOUT_FIRST_USE_ATLAS_v0.1_20261111.md)가 SRC-19~21을 다룬다. 기존 SRC-00~12 목록·117칸이라는 이 문서 작성 당시의 집계는 변경하지 않았다.

> **후속 사례 (2026-11-12):** [SRC-24 목록 표현·비교·탐색 9종](UI_LIST_PRESENTATION_ATLAS_v0.1_20261112.md)에서 본 문서의 **SRC-01 Carousel, SRC-08 Infinite scroll** 및 후속 **SRC-16 Card vs List**를 관련 목록 패턴으로 연결한다. 기존 117칸은 작성 당시의 기록으로 유지한다.

## 2. 선택을 위한 상위 분류 — 11개 계층이 아니라 11개 탐색 입구

| 탐색 입구 | 관련 SRC | 목적에 따른 질문 | 구현/효과의 확인 범위 |
|---|---|---|---|
| **A. 입력·선택** | 01, 02, 11 | 자유 입력/단일·복수 선택/즉시 적용/연속값/파일 중 무엇인가? | HTML input/select/fieldset, 키보드·오류/검증 상태 |
| **B. 알림·피드백** | 01, 03 | 결과를 언제·얼마나 오래·어느 수준으로 알려야 하나? | Toast/Snackbar/Banner/Inline error/Badge |
| **C. 오버레이·도움말** | 01, 03 | 흐름을 멈추는 결정인가, 짧은 부연인가? | Modal/Bottom sheet/Tooltip/Coach mark |
| **D. 로딩·진행·대기** | 00, 01, 12 | 처리량을 아는가? 기다리는가, 데이터가 점진적으로 나타나는가? | Spinner/Skeleton/Progress/Blur-up/Streaming/Optimistic |
| **E. 빈·예외 상태** | 06 | 처음 사용/검색 실패/오프라인/권한 부족/정상 완료 중 무엇인가? | 원인에 맞는 안내와 복구 행동 |
| **F. 내비게이션·콘텐츠 탐색** | 00, 01, 08 | 콘텐츠 간 이동/위계/최근 위치/연속 탐색 중 무엇인가? | Tabs/Drawer/Breadcrumb/Pagination/Carousel 등 |
| **G. 모션·전환** | 09 | 가속 곡선, 등장 효과, 순차 실행, 화면 연계 중 어느 수준인가? | ease/spring과 fade/slide는 분류가 서로 다름 |
| **H. 제스처·직접 조작** | 10 | 하나의 손짓으로 무엇을 수행하고, 대체 조작은 있는가? | 손짓 상태 + 키보드·버튼 대안 |
| **I. 시각 스타일·물성** | 04 | 이 표현이 내용·제품 성격·접근성에 맞는가? | 렌더 스타일; **기능 컴포넌트가 아님** |
| **J. 판단·행동 심리** | 05 | 유용한 의사결정을 돕는가, 왜곡·압박하는가? | 설계 가설; **사용자 실험 없는 효과 단정 금지** |
| **K. 아이콘 명명·표현** | 07 | 의미가 분명한 접근 가능한 버튼 라벨이 있는가? | 메뉴 그림 별칭과 실제 기능을 분리 |

**구조 원칙:** 하나의 패턴은 여러 탐색 입구에서 **참조**될 수 있지만, 정의·작동 계약은 한 번만 작성한다. 예: Tooltip은 B와 C에 링크되며 설명을 이중 작성하지 않는다. SRC-08의 FAB는 내비게이션이 아니라 **핵심 동작 버튼**인 경우가 일반적이고, Sticky header는 **스크롤 때의 배치 패턴**이다.

## 3. 이름이 겹쳐도 뜻이 달라지는 패턴 — 중복 제거 우선표

| 그룹 / 대표 표준명 | 자료 속 다른 이름·위치 | 같거나 다른 점 | 사용 판단 |
|---|---|---|---|
| **Alert: Toast** | SRC-01, 03 | 동일 계열. **Snackbar**는 동작(예: Undo)이 포함되기도 하나 명칭/범위는 제품 디자인 시스템별로 다름 | 임시·비차단 결과 알림, 중요 오류는 별도 지속 정보 |
| **Overlay: Dialog** | Modal, Modal dialog (01, 03) | 모달 여부는 배경을 막고 초점을 제한하는 **행동**을 의미; Bottom sheet는 **형상/위치**, modal/nonmodal 모두 가능 | 중요한 선택인지, 짧은 보조 작업인지 |
| **Overlay: Bottom sheet** | SRC-01, 03 | 같은 패턴의 중복, modal vs non-modal의 상태 구분 필요 | 배경 조작 허용 여부와 닫기/취소 규칙 먼저 |
| **Context help: Tooltip** | SRC-01, 03 | 동일 유형. Coach mark는 신규 기능을 설명하는 **온보딩 안내**와 더 밀접 | 주요 기능/필수 정보는 툴팁에만 숨기지 않기 |
| **Loading: Skeleton** | SRC-01, 12 | 동일 뼈대. 블러 업은 **이미지 미리보기**, 스켈레톤은 **구조 placeholder** | 기다리는 내용과 모양이 맞는가 |
| **Progress: Bar/Ring** | SRC-00, 12 | 같은 작업 진행의 표현 형식 | 작업량의 분모가 실제 존재하는가 |
| **Step: progress indicator** | Step indicator SRC-00, 12; Stepper SRC-12 맥락 | **절차의 현재 단계**; 수량 증감 스테퍼와 구별 | 화면 안내/프로세스 단계 |
| **Stepper: quantity** | SRC-02 Stepper, SRC-11 Quantity stepper | **수량의 증감**. 절차 Step Indicator와 서로 다른 입력 패턴 | 1개씩 더하거나 빼기 |
| **Input: Select** | Dropdown(01), Select box(02), Select(11) | select와 일반 팝오버/메뉴는 겉모양만 유사할 수 있다 | 선택값을 제출/유지해야 하는 폼인가 |
| **Single choice: Radio / Segmented** | Radio(02,11), Segmented control(11) | 모두 단일 선택처럼 보일 수 있지만 세그먼트는 **보기 전환/즉시 적용**에 쓰는 경우도 있음. 어떤 시스템에서는 다중 선택 변형도 있음 | 데이터 선택인지 보기 필터인지; 즉시 적용인지 |
| **On/off: Toggle / Switch** | Toggle(01), Switch(11) | 비슷한 2상태 표현. Toggle은 일반적 말이고 Switch는 구체적 컨트롤 의미 | 설정 변경의 저장 성공/실패 확인 |
| **Multi choice: Checkbox** | SRC-02, 11 | 같은 입력; 여러 독립 옵션 또는 동의 여부 | 개별 선택과 전체 선택의 부분 상태 구분 |
| **Input: Slider** | Range slider(02), Slider(11) | 범위 선택/단일 값 조정의 모델을 명시. double-thumb은 단일 손잡이와 다름 | 연속값인지 단계값인지, 숫자 직접 입력 대안 |
| **Input: Date picker** | SRC-02, 11 | 같은 입력. 키보드 날짜 입력 가능성 별도 | 날짜 형식, 로캘, 제약·오류 |
| **Content: Tab / tab indicator** | SRC-00, 01, 08 | 탭 인디케이터는 **활성 상태 표시**이고 Tab/Top tabs는 콘텐츠 영역의 탐색 UI. Bottom tab bar는 앱 **상위 탐색**일 수 있음 | 콘텐츠 패널 탭 vs 앱 내비게이션 구별 |
| **Carousel / Page indicator** | SRC-01 / SRC-00 | Carousel은 **전체 탐색 메커니즘**이고 점은 그 안의 **위치 표시** | 다음·이전·정지·키보드 여부 |
| **Swipe / Swipe to delete** | SRC-10 | Swipe는 제스처, 삭제는 **행동 결과** | 복구·Undo·키보드 대체 |
| **Badge vs Toast** | SRC-03 | Badge는 대개 **잔존하는 수량/상태 표시**, Toast는 **순간적 알림** | 새 항목 수·상태 지속 여부 |

### 아이콘 별칭의 분리

Hamburger(수평 세 줄), Kebab(수직 세 점), Meatballs(수평 세 점), Waffle(점 격자), Bento(박스 격자), Döner/Veggie burger/Stairs/Sliders는 **시각적 형태를 묘사하는 비공식 이름**이다. 같은 그림의 버튼도 '메뉴 열기', '더보기', '보기 옵션', '필터 설정'처럼 **실제 행동**을 accessible name으로 사용해야 한다. 별칭만으로 표준 동작이나 사전 정의된 접근성 역할이 자동 생기지 않는다.

## 4. 상황별 선택표: 무엇을 보여주고, 언제 쓰지 않는가

| 사용자 상황 | 적합 후보 | 반드시 확인할 상태·설명 | 흔한 오용 |
|---|---|---|---|
| 파일 업로드 중 진행량을 정확히 앎 | Progress bar / ring | 처리량·총량, 취소, 실패/재시도 | 모르는 진행률을 90%까지 자동 채움 |
| 처리량은 모르지만 서버 응답을 기다림 | Spinner / Inline pending | 요청 중 → 완료/실패, 중복 실행 방지 | 계속 도는 애니메이션만 표시 |
| 목록/카드 구조를 먼저 예측할 수 있음 | Skeleton | 실제 크기와 유사한 모양, 종료 시 콘텐츠 교체 | 내용과 전혀 다른 뼈대, 무한 shimmer |
| 이미지가 점진적으로 내려옴 | Blur-up image | 저해상도 → 실제 이미지, alt 유지, 실패 대안 | 흐릿한 이미지가 곧 '고해상도 완료'처럼 보임 |
| 생성된 텍스트가 순서대로 도착 | Streaming text | 현재 도착한 텍스트, 완료·오류·중단 상태 | '스트리밍'을 실제 진행률인 양 보임 |
| 즉각 반영 후 서버 확인 | Optimistic UI | pending, 서버 거부 → 복원·상황 설명 | 실패한 삭제/결제를 성공으로 고착 |
| 처음 사용해서 아직 기록이 없음 | First use empty state | 무엇을 할 수 있는가, 시작 행동 | '오류'라고 표시 |
| 검색어가 결과를 만들지 못함 | No search results | 검색어 수정/초기화 | 전체 서비스에 데이터가 없는 것처럼 표시 |
| 필터가 너무 제한적임 | No filter results | 적용 필터 표시, 해제 | 검색 결과 없음과 동일하게 취급 |
| 연결 끊김/권한 부족/잠김 | Offline / Permission needed / Locked | 다른 원인에 맞는 해결 행동 | 모두 재시도 버튼 하나로 통일 |
| 모든 항목을 이미 끝냄 | All caught up | 정상 완료·다음 가능한 일 | 실패/미확인 상태처럼 표현 |
| 위험한 삭제·영구 변경 | Modal dialog 또는 명시적 확인 | 확실한 결과·취소/복구·초점 이동 | 작은 Toast로만 질문 |
| 가벼운 업무 성공 알림 | Toast/Snackbar | 확인된 결과, 읽을 시간, 중복 메시지 | 중요한 실패를 자동 사라지는 알림 하나로 전달 |
| 2~4개 동등한 보기 전환 | Segmented control 또는 Tabs | 데이터/선택의 의미와 초점 규칙 | 앱의 모든 내비게이션을 세그먼트로 |
| 긴 목록 탐색 | Pagination / Infinite scroll | 현재 위치, 끝, 로딩/오류, 이전 위치 복원 | 무한 스크롤이 푸터 접근/위치 기억 방해 |
| 화면 내 직접 조작 | Swipe / Drag / Pinch | 시각 피드백 + 대체 버튼/키보드 | 비가시 제스처만이 유일한 기능 |

## 5. 움직임을 단일 목록으로 혼동하지 않기

| 모션 목록의 용어 | 실제 분류 | 확인할 질문 |
|---|---|---|
| **Ease-in, Ease-out** | 시간 함수 / easing | 반응을 늦게 시작하거나 늦게 끝내는 게 과업에 맞나? |
| **Spring** | 물리 기반 모션 모델 | 정지 위치·중간 입력·reduced-motion에서 안정적인가? |
| **Bounce** | 결과가 튕기는 시각적 효과 | 즐거움이 기능성보다 중요한가? 과장·반복은 없는가? |
| **Stagger** | 다수 요소의 시간차 연출 | 순차성이 의미가 있는가, 목록 읽기를 지연시키나? |
| **Fade, Slide** | 보임/이동 전환의 표현 | 콘텐츠 맥락을 돕나, 갑작스러운 변화와 혼동하나? |
| **Zoom transition** | 규모·공간 이동 전환 | 시야 이동이 크거나 어지럼을 유발하나? |
| **Shared element** | 화면 간 동일 대상을 연결하는 공간 연속성 | 출발/도착 요소가 실제로 같은 의미인가? |

예: '탭 밑줄을 slide + spring으로 이동'은 **표시 방식 + 운동 모델**의 조합이지 한 가지 패턴 이름이 아니다. 가시적인 움직임이 없더라도 선택 상태·데이터가 정확하다면 더 적합할 수 있다.

## 6. 시각 스타일 사전의 사용 범위 (컴포넌트와 분리)

| 스타일 이름(캡처 기준) | 관찰 관점 [AI-HYP] | 부적합 위험 |
|---|---|---|
| Skeuomorphism | 현실 물체의 표면·기능 단서 모사 | 장식적 그림자가 정보보다 우세 |
| Flat design | 표면·깊이 표현을 절제 | 조작 가능한 요소의 구분 약화 |
| Material design | Google 디자인 시스템의 구성요소·상태·모션 철학 | 단순한 그림자·카드 모양으로만 축소 해석 |
| Neumorphism | 같은 배경색 범위의 부조·그림자 | 저대비, 눌림 상태 모호 |
| Glassmorphism | 유리처럼 투명·흐림·층 표현 | 배경 가변 시 글자·조작의 대비 붕괴 |
| Claymorphism | 둥근 3D 오브젝트/점토 인상 | 화면 전반을 장난감 같은 장식으로 만들 위험 |
| Neo brutalism | 강한 경계·타이포·색채 충돌 | 정보 과밀, 피로 |
| 3D icon | 입체 아이콘의 제작·형태 언어 | 실제 의미보다 장식이 우선 |
| Liquid glass | 반투명·굴절 같은 특정 물성 언어 또는 제품별 디자인 표현 | OS별 전용 자산·상표/용어·접근성·라이선스 확인 필요 |

**중요:** 위 9종은 공식적으로 상호 배타적인 분류가 아니다. 일부는 **디자인 시스템**, 일부는 **시각 기법**, 일부는 **오브젝트 표현**이므로 스타일의 예시를 많이 모았다는 이유로 별개 범용 규칙 9개를 추가하지 않는다. 디자인 깎기의 개인적 재질 선호(매트 금속·유화·제형·라벨)는 개별 취향 데이터이고, 어느 UI 스타일이 가장 좋다는 객관적 증거는 아니다.

## 7. 행동 심리 9개: 의사결정 지원 vs 다크 패턴

| 원본 항목 | 설계 실험에서 검토할 점 | 윤리·근거 경계 |
|---|---|---|
| Anchoring | 비교 기준을 먼저 제시했을 때의 판단 | 비현실적 취소선 가격으로 기준 왜곡 금지 |
| Loss aversion | 선택 후 포기하게 되는 가치를 어떻게 설명하는가 | 손실 공포를 과장해 압박 금지 |
| Default effect | 미리 선택된 값이 실제 사용자에게 적합한가 | 자동 동의·개인정보 공유 기본값 금지 |
| Social proof | 다른 이용자의 실제 경험이 선택에 도움 되는가 | 가짜 후기·가짜 실시간 이용자 수 금지 |
| Scarcity | 제한된 재고·시간이 실제로 존재하는가 | 허위 마감 카운트다운·가짜 품절 금지 |
| Framing effect | 같은 사실의 표현 방식이 이해에 영향을 주는가 | 유리한 일부만 보여 진실 왜곡 금지 |
| Choice overload | 너무 많은 선택지가 탐색 부담을 주는가 | 단순화가 중요한 옵션·기능을 삭제하지 않도록 |
| Peak-end rule | 경험의 핵심 순간과 마지막 피드백을 어떻게 설계하는가 | UX 성공률을 이 법칙 하나로 확정하지 않음 |
| Zeigarnik effect | 미완료 항목의 가시화가 유용한가 | 의도적 불안/강박을 부추기는 지속 알림 금지 |

이 9개는 **보편적으로 입증된 UI 처방전이 아니며**, 특히 상업적 전환율 극대화 목적의 설계 기법과 사용자 자율성을 돕는 설계를 구분해야 한다. 사용자의 시간·선택권·데이터/금전적 안전을 우선한다. 의료·재정·동의 과정에서는 훨씬 엄격한 기준 적용.

> **후속 보강 (2026-11-11):** 새 캡처 **SRC-22 날짜 선택 9종**과 **SRC-23 행동심리 9종**은 [날짜 선택·행동심리 사례 보강 아틀라스](UI_DATE_SELECTION_BEHAVIOR_ATLAS_v0.1_20261111.md)에서 분석한다. SRC-23은 **본 문서 SRC-05와 같은 9개 명칭**이며, 기존 설명을 대체하지 않고 예시·윤리·근거 한계를 보완한다. 이 문서의 기존 원자료 집계는 작성 시점 기록으로 유지한다.

## 8. 원본 12장 구성 자체의 장단점

- **좋은 점:** 3×3 카드·번호·한영 병기로 인접 개념을 빠르게 발견하고 명칭을 학습하기 쉽다. 같은 구조를 비교하면서 공통점/차이를 보는 훌륭한 **교육용 카탈로그 패턴**이다.
- **한계:** SNS 캡처는 예시의 **일시적 외형**만 보여주고 동작·상태·접근성·오류/취소 경로를 제공하지 않는다. 9칸이라는 고정 수량은 기능적으로 전혀 다른 종류를 같은 층에 병렬화할 위험이 있다.
- **해석 주의:** 사용자가 '유용한 레퍼런스로 가져왔다'고 말한 사실은 **12장 전체의 미적 선호·성능 평가를 확정한다는 의미가 아니다**. 개별 도안에 대한 호불호는 아직 미확인.
- **장래 활용:** '용어 모음'의 비유를 유지하되 실제 제품 선택 시 **목적 → 데이터·상태 → 선택 가능한 패턴 → 행동/접근성 → 표현·모션 → 검증** 순으로 평가한다.

## 9. 문서 체계 및 향후 작성·검증의 경계

### 저장소의 작은 구조(이번 변경)

- [기존 MOTION_INDICATOR_ATLAS v0.1](MOTION_INDICATOR_ATLAS_v0.1_20261105.md) = **인디케이터 9종 심층** + 동작 구현 후보 18종 + 자료실.
- **본 문서** = **추가 캡처 12장 원문 이름 보존 + 11개 탐색 분류 + 중복·오용 선택표 + 스타일·인지·제스처 경계**.
- [references/README](README.md) = **찾아보기 입구**, CHANGELOG = **변경 기록**. 이 세 곳에 같은 패턴 정의를 복제하여 비대하게 만들지 않는다.
- 향후 실제 구현/실험이 정해지면 대상 컴포넌트 하나마다 목적, states (idle/loading/success/error/empty/disabled), 이벤트, 실제 데이터 소스, 접근성, 회귀 시나리오를 **별도 사례 실험 문서**에 기록한다. 이 단계에서 범용 지침에 새로운 MUST 조항을 추가하지 않는다.

### 어떤 구현 검증을 먼저 할까? [AI-HYP / NOT RUN]

1. **폼의 선택 의미:** 같은 3개 값을 Select, Radio, Segmented로 비교. 페이지 전환인지 값 설정인지 고정하고 선택 시간·오선택·키보드/터치·모바일을 평가.
2. **로딩 진실성:** Progress(알려진 처리량) / Spinner(모르는 처리량) / Skeleton(콘텐츠 영역) / Optimistic UI(즉시 반영·실패 시 복구)를 **같은 것으로 평가하지 않고 각자의 과업**에서 오류 상태까지 시험.
3. **빈 화면:** 동일 레이아웃에서 First use / No results / Offline / Permission의 **문구·원인·실제 가능한 복구**가 다른지 확인.
4. **모션 과업성:** 동일 기능의 즉시 전환 vs Fade/Slide/Spring을 비교하고 빠른 연타·인터럽트·reduced-motion·기존 기능 회귀를 측정.
5. **비선호 스타일도 검증:** 선호도와 읽기 쉬움·상태 식별·실제 수행 정확성을 각각 평가. 한 시안의 미적 호불호를 보편 규칙으로 일반화하지 않는다.

### 검증 상태

| 항목 | 결과 | 실제 근거 |
|---|---|---|
| 원본 캡처 12장·9개 명칭의 텍스트 인벤토리 | PASS | 사용자가 제공한 정적 사진·앞선 대화의 기록 |
| 기존 9종 인디케이터와의 중복 분리 | PASS | 아틀라스 v0.1의 기존 목록 |
| 11개 탐색 입구·선택/오용 비교표 | PASS | 문서·설계 분석, 실사용 평가 아님 |
| WAI/HTML/디자인 시스템의 의미 교차 확인 | PASS | 아래 공식 문헌에서 확인되는 범위 |
| 원본 동영상 재생·애니메이션 단계 직접 확인 | NOT RUN | 캡처만 제공됨 |
| 개별 앱의 실제 상태/사용성/접근성/유지보수 | NOT RUN | 제작/실행하지 않음 |
| 심리효과의 전환율·임상적/실험적 증명 | NOT RUN | 사용자 연구 없음 |
| 외부 소스/이미지/폰트 재배포 | N/A | 링크만 기록 |
| 범용 v1.3 변경·기존 앱/사이트 변경 | N/A | 변경하지 않음 |

## 10. 참고문헌 — APA 7판 형식(간략)

Apple. (n.d.). *Human interface guidelines*. https://developer.apple.com/design/human-interface-guidelines/

Google. (n.d.). *Material Web: Progress indicators*. https://material-web.dev/components/progress/

MDN Web Docs. (n.d.). *The HTML progress indicator element*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress

MDN Web Docs. (n.d.). *The HTML meter element*. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter

U.S. Department of Veterans Affairs. (n.d.). *Button – Segmented*. VA.gov Design System. https://design.va.gov/components/button/button-segmented/

World Wide Web Consortium (W3C). (n.d.). *Checkbox pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/

World Wide Web Consortium (W3C). (n.d.). *Tabs pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/tabs/

World Wide Web Consortium (W3C). (n.d.). *Carousel (slide show or image rotator) pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/carousel/

World Wide Web Consortium (W3C). (n.d.). *Dialog (modal) pattern*. WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

사용자 제공 SNS 이미지 캡처 12장. (2026, 11월 5일). *UI·입력·알림·스타일·심리·빈 화면·아이콘·탐색·모션·제스처·로딩 9칸 목록* [개인 대화 참고자료; 원본 출처·라이선스 미확인].

> 원자료에 적힌 용어가 정확한 공식 분류라는 사실을 보증하지 않는다. 공식 자료의 구체적 개념을 참조한 부분은 표준 설명과 일치하게, 사용자 캡처/AI 가설에만 근거한 내용은 별도로 구분했다.
