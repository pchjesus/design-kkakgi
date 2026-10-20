# KRDS v1.1.0 — 디자인 토큰 지도

원본 ZIP 기준 파일:
- `tokens/figma_token.json` — 디자인 도구 원형에 가까운 소스, 최상위 키에 슬래시 사용
- `tokens/transformed_tokens.json` — 코드 소비용 구조, 6개 루트
- `resources/css/token/krds_tokens.css` — 생성된 CSS 커스텀 프로퍼티 **768개 선언** (선언 수, 고유 이름 수와 동일하다고 단정하지 않음)
- `resources/scss/common/_root.scss`, `_variables_for_code.scss`, `_include.scss`, `_group_variables.scss` — 토큰을 실제 스타일에서 사용하는 구조 확인점

## 1. 소스 선택 규칙

| 하고 싶은 일 | 먼저 열기 | 다음에 확인 |
|---|---|---|
| 의미 기준으로 텍스트/표면/경계색 선택 | `transformed_tokens.json` → `mode-light.color` | `mode-high-contrast.color` 및 `krds_tokens.css` |
| 기초 색상 팔레트 비교 | `primitive.color.light` | `primitive.color.high-contrast` |
| 본문/제목/레이블 가독성 | `responsive-pc.font-size` | `responsive-mobile.font-size` |
| 간격/패딩/둥글기 | `semantic.gap/padding/radius` | 실제 컴포넌트 SCSS |
| 레이아웃·카드 밀도 | `responsive-pc.gap-layout/padding-card` | 모바일 대응 키 |
| CSS에 정확한 변수명 입력 | `resources/css/token/krds_tokens.css` | 크롬 Computed Styles/테마 |
| 토큰 생성 방식·원본 연동 분석 | `figma_token.json` | `transformed_tokens.json`과 비교 |

## 2. transformed_tokens.json 트리 (정확한 루트 키)

```text
primitive
  color > light | high-contrast
  typo  > font | font-weight | letter-spacing
  number > 0 ... 22
mode-light / mode-high-contrast
  color > surface | border | divider | text | icon | link |
          button | background | element | action | input |
          graphic | alpha
  border-width > variable-regular | variable-medium |
                 static-regular | static-medium
responsive-pc / responsive-mobile
  font-size > display | body | label | heading | navigation
  gap-layout > [22개의 역할 기반 간격 항목]
  padding-card > large | medium | small | xsmall
semantic
  gap > 1 ... 12
  padding > 1 ... 10
  size-height > 1 ... 11
  radius > xsmall1 ... max (15개)
```

## 3. 확인된 CSS 변수 예시

- 기본 팔레트: `--krds-color-light-primary-50: #256ef4`
- 상태/의미: `--krds-light-color-surface-gray-subtler`, `--krds-light-color-surface-danger-subtler`
- 반응형 서체: `--krds-pc-font-size-body-medium`, `--krds-mobile-font-size-body-medium`
- 간격: `--krds-gap-3`, `--krds-padding-6`
- 라운드: `--krds-radius-medium2`

정확한 값은 코드에서 조회한다. 위 예시는 **원본에 존재하는 이름**의 샘플이지 권장 사용값이 아니다.

## 4. 토큰 적용 원칙

1. **primitive**(수치/색 원재료) → **semantic 또는 mode**(의미) → **component**(사용 위치) 순으로 판단한다.
2. 하드코딩 색상보다 의미 토큰을 우선 검토하되, 프로젝트의 승인된 브랜드·정보 위계와 충돌하면 강제하지 않는다.
3. 밝은 모드만 살펴보고 접근성을 결론 내리지 않는다. `mode-high-contrast`, focus, disabled, 실제 명도 대비를 비교한다.
4. PC와 모바일 `font-size`·`gap-layout`을 각각 확인한다. 글자 확대 시 텍스트 잘림/모달/탭/카드/표를 모두 점검한다.
5. 텍스트 크기·컬러·아이콘만 바꾸는 경우에도 의미·상태 표현과 읽기 순서를 재검증한다.
6. CSS 변수명과 transformed JSON의 경로가 **완전히 같은 문자열**이라고 가정하지 않는다. 소스 CSS에서 실제 선언을 확인한다.
7. 필요한 부분만 읽고, 큰 JSON 두 개와 전체 minified CSS를 매번 통째로 로드하지 않는다.

## 5. 디자인 깎기에 적용할 때

- KRDS의 토큰 분류 방식은 **관찰 가능한 디자인 시스템 사례**다.
- 사용자 취향 지도에 기록된 서체/색/밀도/물성은 별도 증거다. 둘이 충돌하면 프로젝트 목적과 실험으로 판단한다.
- 의료/간호 웹앱에서 경고·오류·위험도를 표현할 때 색상만으로 구분하지 않고 텍스트와 명시적 의미를 함께 제공한다.
- 본 토큰 지도는 코드 열람을 바탕으로 한 **정적 구조 분석 완료** 기록이다. 모든 조합의 접근성·시각 회귀 테스트는 **NOT RUN**.
