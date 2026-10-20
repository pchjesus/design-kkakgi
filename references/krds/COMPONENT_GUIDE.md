# KRDS v1.1.0 — 용도별 컴포넌트 탐색·적용 지도

원본 예제 **74개 전부**는 [component_catalog.json](component_catalog.json)의 5개 그룹에 있다. 이 문서는 같은 파일을 중복 저장하지 않고, 자연어 요청을 해당 파일로 연결하는 **고속 라우터**다.

> 경로 표기: 아래 `HTML` 열의 파일은 공식 원본 저장소 `html/code/`, `SCSS` 열은 `resources/scss/component/` 아래의 **상대 경로**다. 외부 링크는 `https://github.com/KRDS-uiux/krds-uiux/blob/main/` + 경로로 이동한다. `main`은 불변 스냅샷이 아니므로 내용 차이는 재검증한다.

## 1. 어떤 문제에 어떤 소스를 먼저 읽는가?

| 사용자 요청·검색어 | 먼저 열 HTML | 다음에 열 SCSS | 동작 검토 |
|---|---|---|---|
| 버튼·위계·크기·아이콘 | `button.html`, `button_hierarchy.html`, `button_size.html`, `button_icon.html` | `_button.scss` | focus/hover/disabled/명확한 이름 |
| 입력·라벨·오류·필수·읽기 전용 | `text_input.html`, `text_input_state.html`, `text_input_icon.html` | `_input.scss`, `_form_layout.scss` | label/id, 오류 메시지 연결 |
| 선택·정렬 콤보 | `select.html`, `select_state.html`, `select_sorting.html` | `_select.scss` | 키보드, native 대체 여부 |
| 체크·라디오 | `checkbox.html`, `radio_button.html`, `checkbox_chip.html`, `radio_chip.html` | `_form_check.scss`, `_form_chip.scss` | 그룹 범위/fieldset/상태 |
| 스위치·토글 | `toggle_switch.html`, `toggle_switch_size.html` | `_switch.scss` | `ui-script.js`의 `krds_toggleSwitch` |
| 날짜·기간 입력 | `date_input.html`, `calendar.html`, `calendar_range.html` | `_calendar.scss` | `krds_calendar`, 유효 날짜/시간대 |
| 파일 첨부·업로드 | `file_upload.html` | `_file_upload.scss` | `krds_fileUpload`, 업로드 서버 별개 |
| 대화상자·확인창 | `modal.html`, `modal_sample.html` | `_modal.scss` | `krds_modal`, 포커스 이동·복귀·ESC |
| 펼침·접힘 | `accordion.html`, `accordion_line.html` | `_accordion.scss` | `krds_accordion`, aria-expanded |
| 탭 전환 | `tab.html` | `_tab.scss` | `krds_tab`, tab/panel·키보드 |
| 툴팁·맥락 도움말 | `tooltip.html`, `contextual_help.html`, `help_panel.html` | `_tooltip.scss`, `_contextual_help.scss`, `_help_panel.scss` | hover만 의존하지 않기 |
| 경고·로딩·상태표시 | `critical_alerts.html`, `spinner.html`, `badge.html`, `tag.html` | `_critical_alerts.scss`, `_spinner.scss`, `_badge.scss`, `_tag.scss` | 상태 텍스트·실시간 알림 |
| 메뉴·사이드 내비게이션 | `main_menu_pc.html`, `main_menu_mobile.html`, `side_navigation.html` | `_main_menu.scss`, `_side_navigation.scss` | `krds_mainMenuPC/Mobile` |
| 스킵링크·경로·페이지 내 이동 | `skip_link.html`, `breadcrumb.html`, `in_page_navigation.html` | `_skip_link.scss`, `_breadcrumb.scss`, `_in_page_navigation.scss` | 실제 main 대상 id |
| 단계·목록·테이블 | `step_indicator.html`, `structured_list.html`, `structured_list_table.html`, `table.html` | `_step_indicator.scss`, `_structured_list.scss`, `_table.scss` | 시맨틱 헤더/읽기 순서 |
| 헤더·푸터·언어 | `header.html`, `footer.html`, `language_switcher.html` | `_header.scss`, `_footer.scss`, `_language_switcher.scss` | 반응형 상태/언어 속성 |
| 글자 확대·읽어주기 | `resize.html`, `tts.html`, `tts_icon.html` | `_resize.scss`, `_tts.scss` | `krds_adjustContentScale`, `krds_tts` |
| 캐러셀·배너 | `carousel.html`, `carousel_banner.html` | `_carousel.scss` | Swiper 등 플러그인 의존성 |

일치하지 않는 항목은 `component_catalog.json`에서 이름 검색한다. 예: `coach_mark`, `disclosure`, `pagination`, `tutorial_panel`.

## 2. 원본 열기 — 대표 예제 바로가기

- [버튼](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/button.html) · [입력 상태](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/text_input_state.html) · [라디오](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/radio_button.html) · [달력](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/calendar.html)
- [모달](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/modal.html) · [아코디언](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/accordion.html) · [탭](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/tab.html) · [경고](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/critical_alerts.html)
- [파일 업로드](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/file_upload.html) · [본문 바로가기](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/skip_link.html) · [주 메뉴 모바일](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/main_menu_mobile.html)

## 3. 코드의 책임 경계

- **HTML**: 구조·클래스·샘플 상태. 예제 조각이지 독립 실행 앱이나 검증 완료 기능이 아님.
- **SCSS**: 컴포넌트 외형·스타일 변수. `common` 및 토큰 의존 관계는 필요할 때 추가 확인.
- **JS**: `resources/js/component/ui-script.js`가 `DOMContentLoaded` 시 여러 `krds_*` 모듈을 일괄 초기화함. 프레임워크 리렌더링·동적 삽입에서 중복 바인딩이나 미초기화 위험을 별도 점검.
- **CSS 번들**: `resources/cdn/krds.min.css`는 외부 절대 URL 아이콘 참조가 포함됨. 복사만으로 완전한 오프라인 독립 동작이 보장되지 않음.

## 4. 실제 ZIP에서 확인한 주의점 (예제가 무조건 정답은 아님)

1. `skip_link.html`: 앵커가 `#breadcrumb`를 가리키므로 실제 페이지의 **본문 시작 요소**와 맞춰야 한다. 예제 그대로 '본문 바로가기'라고 믿지 않는다.
2. `file_upload.html`: `label` 안에 `button`이 중첩된 샘플이 보인다. 상호작용 요소 구조/키보드 동작을 수정·검증한다.
3. `modal.html`: `data-target` 및 실제 ID 연계가 필요하다. 포커스 트랩/종료 후 복귀를 실사용 DOM에서 검사.
4. `tab.html`: `role=tab`, `aria-controls`와 패널의 동기화·화살표 이동을 검사.
5. `resize.html`: 글자 크기 기능은 모든 화면/탭에 일관되게 적용되는지 확인. 일부 화면만 확대되는 현상을 회귀 검사.
6. `calendar*.html`: 날짜 제한, 지역화, 시각·타임존 등 실제 입력 규칙은 앱에서 별도 검증.

위 사항은 **정적 원본 관찰**이지 실행된 브라우저 결함 판정이 아니다. 접근성 적합성·실사용 동작은 **NOT RUN**.

## 5. AI 검색 예산

- **질문→1 HTML 파일**. 변형 비교가 필요할 때만 `*_size`, `*_state` 등 1~2개 추가.
- **원하는 시각 값→관련 SCSS와 토큰 일부**만. 합쳐진 50만 자 번들·소스맵 전체는 읽지 않는다.
- **버그→재현 DOM + 해당 `krds_*` JS 블록**만. 페이지 전체 재작성하지 않는다.
- **지침 채택→사용자 승인·전후 비교·기능 회귀 검사**가 선행되어야 한다.
