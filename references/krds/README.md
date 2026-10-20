# KRDS HTML Component Kit — 탐색 허브

> **역할:** 디자인 깎기의 **외부 구현·접근성 참고자료**. 범용 디자인 지침이나 사용자 취향의 정답이 아니다. 원본 HTML/CSS/JS/폰트/이미지는 이 저장소에 복제하지 않는다.

## 10초 탐색

1. **원하는 UI 이름을 알고 있다** → [컴포넌트 기계 판독 색인](component_catalog.json)에서 영문명 검색 → 공식 원본 `html/code/<이름>.html` 확인.
2. **사용 목적만 알고 있다** → [용도별 빠른 경로·핵심 구현](COMPONENT_GUIDE.md)에서 한국어 키워드로 찾기.
3. **색상·폰트·여백·반응형 규칙을 찾는다** → [디자인 토큰 지도](TOKEN_GUIDE.md).
4. **실제 프로젝트에 구현한다** → [통합·접근성·회귀 검증](INTEGRATION_AND_QA.md)을 먼저 확인.
5. **원본 신뢰성·버전·라이선스가 궁금하다** → [출처와 검증 이력](SOURCE_PROVENANCE.md).

**직접 원본:** [KRDS 공식 GitHub](https://github.com/KRDS-uiux/krds-uiux) · [컴포넌트 공식 설명](https://www.krds.go.kr/html/site/component/component_summary.html) · [사용 조건](https://www.krds.go.kr/html/site/utility/utility_06.html)

**샘플 소스 경로:** `https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/<component>.html`
- 빠른 이동: [버튼](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/button.html) · [모달](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/modal.html) · [입력](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/text_input.html) · [탭](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/tab.html) · [아코디언](https://github.com/KRDS-uiux/krds-uiux/blob/main/html/code/accordion.html)
- **주의:** 공식 GitHub의 `main`은 변경될 수 있다. 지금 색인은 사용자가 제공한 ZIP에 들어 있는 **v1.1.0**에 맞춰 확인했다.

## 원본 구조 — 필요한 파일만 읽기

| 질문 | 원본 경로 | 우선순위 |
|---|---|---|
| 마크업·상태별 예시 | `html/code/*.html` (74개) | 1 |
| CSS 클래스·컴포넌트 스타일 | `resources/scss/component/_*.scss` | 2 |
| 기본값·변수·공통 스타일 | `resources/scss/common/` | 3 |
| 이벤트·포커스·상태 전환 | `resources/js/component/ui-script.js` | 4 (동작할 때만) |
| 의미 기반 토큰 값 | `tokens/transformed_tokens.json` | 토큰 과제 시 1 |
| 원본 Figma 형식 | `tokens/figma_token.json` | 원천 구조가 필요할 때 |
| CSS 변수 이름 | `resources/css/token/krds_tokens.css` | CSS 작업 시 1 |
| 빌드 배포 참고 | `resources/cdn/krds.min.css`, `krds.min.js` | 최후 확인용 |

**탐색 제한:** 기본적으로 HTML 예제 1개 → 관련 SCSS 1개 → 관련 JS 부분 → 토큰 부분 순서로만 확장한다. 요청과 무관한 파일 245개 전체를 매번 읽지 않는다. minified CDN 파일·소스맵은 상세 분석의 시작점으로 삼지 않는다.

## 키트 사용 ≠ KRDS 스타일 강제

- **참고:** 상태별 UI 구성, 구조·명명, 레이블, 키보드·포커스 흐름, 디자인 토큰 관리 방식.
- **조건부 적용:** 색상·타이포그래피·간격·콘텐츠 밀도·모션·컴포넌트 외형.
- **직접 검증 필요:** 접근성(WCAG/KWCAG), 모바일 사용성, 기존 기능·데이터·상태 유지, 개인정보 보안.
- 사용자 관찰과 AI 가설을 구분한다. 범용 시각 디자인 지침 **v1.2 DRAFT**와 기존 UX 계약은 이 자료를 추가했다고 자동 변경되지 않는다.
- 공공서비스용 KRDS 패턴이 의료/간호, 콘텐츠, 홍보 사이트에 그대로 적합하다고 전제하지 않는다.

## 현행 저장소 정책

- `IMAGE_POLICY.md`에 따라 원본 SVG/PNG/폰트/스크린샷/이미지 ZIP을 여기로 이관하지 않는다.
- 공식 소스를 중복 버전관리하지 않는다. 여기에는 **텍스트 분석·재현 가능한 경로·출처·검증 조건만** 보관한다.
- 실제 프로덕션용 패키지 의존성이 필요하면 **대상 앱 저장소**에서 별도 버전 고정 및 통합 테스트한다.
- 본 문서들은 KRDS 원본이 아니라 **2026-10-20에 사용자가 제공한 ZIP을 분석한 2차 탐색 자료**다.

## 출처 (APA 7판)

KRDS-uiux. (n.d.). *KRDS HTML Component Kit* (Version 1.1.0) [Computer software]. GitHub. https://github.com/KRDS-uiux/krds-uiux

KRDS. (n.d.). *HTML 컴포넌트*. https://www.krds.go.kr/html/site/component/component_summary.html
