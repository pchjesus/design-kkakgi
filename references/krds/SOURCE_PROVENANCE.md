# KRDS v1.1.0 — 출처·스냅샷·검증 기록

## 1. 데이터 계보

- **검토일:** 2026-10-20 (KST)
- **제공 자료:** 사용자가 채팅에 업로드한 `krds-uiux-main.zip`
- **실제 확인한 메타데이터:** 아카이브 내부 `package.json`의 `name: krds-uiux`, `version: 1.1.0`
- **공식 소스:** https://github.com/KRDS-uiux/krds-uiux
- **공식 컴포넌트 문서:** https://www.krds.go.kr/html/site/component/component_summary.html
- **NPM 패키지 설치명:** `krds-uiux` / 버전 `1.1.0` (`package.json`에 표시)
- **ZIP SHA-256:** `e915e378d35e52ff8172c4c98f4f0bfedbd53177a8f9e6ff521298d82fa2bf3b`
- **GitHub `main`의 정확한 업스트림 commit SHA:** **미확인**. 아카이브 이름 `main`만으로 추정하지 않는다. 본 기록은 ZIP 해시로 식별한다.

## 2. 로컬 아카이브 구조 검사 결과

| 항목 | 측정값 |
|---|---:|
| ZIP 크기 | 2,458,525 bytes |
| 압축 해제된 총 크기 | 5,709,493 bytes |
| 전체 파일 | 245 |
| HTML 컴포넌트 조각 | 74 |
| SCSS | 54 |
| SVG | 92 |
| PNG | 3 |
| 폰트 WOFF/WOFF2 | 6 |
| CSS | 6 |
| CSS source map | 3 |
| JS | 3 (CDN 1 + 비축약 1 + 플러그인 1) |
| JSON | 3 (토큰 2 + package 1) |
| Markdown | 1 (원본 README) |

**원본 주요 디렉터리**
```text
html/code/                 HTML 예제 74개
resources/scss/common/     공통 SCSS·믹스인·변수
resources/scss/component/  컴포넌트별 SCSS
resources/css/token/       krds_tokens.css
resources/css/component/   빌드된 CSS·맵
resources/js/component/    ui-script.js
resources/cdn/             krds.min.css, krds.min.js
resources/fonts/           PretendardGOV (6개)
resources/img/             SVG/PNG (95개)
tokens/                    figma_token.json, transformed_tokens.json
```

## 3. 수정 감지용 핵심 파일 해시 (SHA-256)

| ZIP 내부 상대 경로 | SHA-256 |
|---|---|
| `package.json` | `83bb3fcf002611d7623ad57d3bc42faa2f647d2f919fc248a59727a4d845ea29` |
| `tokens/figma_token.json` | `89efe7199e8d440a52d9db9c0ba3109efa024a291152ca78aea94d2bf288b625` |
| `tokens/transformed_tokens.json` | `5eb255d593ec0b0fa41207223df1288f97295b632dfac50629e60e4e4dc0a52e` |
| `resources/css/token/krds_tokens.css` | `2e06b0d8393bca671edaab1ca0c7c42ded2ae03b3d03c6ede60f763a93d81569` |
| `resources/js/component/ui-script.js` | `7c3674ffd990143aad14d7d7234ea82a1374fa0c03552679b6af354056cc67fe` |
| `resources/cdn/krds.min.css` | `6e37956cc077aa06dbeb815f5fbb5968dfebd67dd83557c305cb188a62ce2737` |
| `resources/cdn/krds.min.js` | `b06539f6e02316549cd0631f20bf002494e919c6437e711ee5235662f58a77c6` |

## 4. 출처 정책·재배포 판단

원본 `package.json`에는 `license: ISC`가 적혀 있지만 원본 `README.md`는 **KRDS 이용약관을 따른다**고 별도 명시한다. [KRDS 공식 저작권 안내](https://www.krds.go.kr/html/site/utility/utility_06.html)는 제공 자료를 **공공누리 제1유형(출처표시)** 조건으로 상업·비상업 목적에 활용하고 수정·재배포할 수 있다고 설명한다. 이 저장소는 별도 배포물이 아니라 탐색용 출처·경로·분석 기록이므로 원본 자산과 소스 전체는 복제하지 않는다. 외부 배포 시에는 제공 기관의 구체적인 출처표시를 준수하고, 폰트·제3자 리소스의 별도 조건 여부를 재검토한다.

## 5. 검증 상태

| 검증 항목 | 결과 | 비고 |
|---|---|---|
| 업로드 ZIP 실제 파일 검사 | **PASS** | ZIP 목록, 파일 크기 및 주요 텍스트 내용 |
| `package.json` 버전 검사 | **PASS** | 1.1.0 |
| HTML 조각 74개 목록 대조 | **PASS** | `component_catalog.json`에 74개 등록 |
| 토큰 JSON 상위 키 확인 | **PASS** | `TOKEN_GUIDE.md`에 반영 |
| JS의 `DOMContentLoaded` 초기화 확인 | **PASS** | 소스 정적 분석 |
| 공식 GitHub 현행 `main`의 대표 파일과 ZIP 일치 | **PASS (8파일)** | package.json, modal.html, tab.html, skip_link.html, 토큰 JSON 2개, ui-script.js, krds_tokens.css의 Git blob SHA 대조 |
| 업스트림 `main`과 ZIP **전체 커밋** 동등성 | **NOT RUN** | 업스트림 commit SHA 미확인; 8파일 일치만 검증 |
| 브라우저 시각 회귀 및 WCAG/KWCAG 정식 검사 | **NOT RUN** | 실제 앱 배포 시 별도 |
| 패키지 에셋 전체 라이선스 적합성 확인 | **NOT RUN** | 전면 재배포를 수행하지 않음 |
| 디자인 지침 v1.2 자동 변경 | **N/A** | 변경 금지·미변경 |

**갱신 원칙:** 원본이 바뀌면 새 ZIP/태그/커밋을 별도 식별하고, 74개 색인의 존재·이름과 핵심 문서의 경로를 비교한 뒤 변경분만 반영한다. 과거 검증을 새 버전에도 그대로 적용하지 않는다.

공식 원본 파일 8개의 Git blob SHA는 ZIP에서 다시 계산한 Git blob SHA와 **전부 일치**한다. 이는 대표 파일에 대한 동등성 확인이지 245개 전체 파일·정확한 원본 commit 동일성의 증명은 아니다.

## 참고문헌 (APA 7판)

KRDS-uiux. (n.d.). *KRDS HTML Component Kit* (Version 1.1.0) [Computer software]. GitHub. https://github.com/KRDS-uiux/krds-uiux

KRDS. (n.d.). *HTML 컴포넌트*. https://www.krds.go.kr/html/site/component/component_summary.html
