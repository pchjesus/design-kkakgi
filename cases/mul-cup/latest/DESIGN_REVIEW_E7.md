> 후속 상태: E7은 비교 이력이며, 2026-10-17 사용자 승인으로 E8-SPATIAL-GLASS가 main 최신본이 되었다.

# MUL. E7 — 물성·편집·재조합 실험

- 기준: main `6d1f842fd33a65cdddbe68eae700105d769442e7` / E6-C5-HERO.
- 작업 브랜치: `experiment/mul-material-softness`. 사용자 검토 대기. main 및 기존 Pages 미변경.
- 목적: 홍보를 먼저 경험하고, 색·형태를 살펴본 뒤 원하는 경우 구매 정보를 연다.
- 기존 5개 버전, 승인 사진 2장, THE COLORS, 3색, 회전·초기화, FAQ, 구매 패널, 저장 키와 데이터 형식을 보존한다. 범용 v1.2는 DRAFT 유지.

## 진단과 변경

| 문제·원인 | 근거 | 이번 대응 |
|---|---|---|
| HERO 높이 팽창 — 구현 | 사진에 height:100%, 최소 높이만 있고 그리드 높이는 auto. 실제 1920px 브라우저에서 제목·컵이 아래로 밀려 CTA가 첫 화면 밖에 위치 | 데스크톱 620–780px 프레임, 사진 absolute 배치와 명시적 높이. 모바일은 독립적인 세로 구성 |
| 글꼴 의도와 실제 출력 불일치 — 구현 | NanumSquareRound 미로드, Windows 폴백과 600 굵기. 과거의 딱딱한 서체 문제를 재생산 | 이미 로드하는 고운돋움 400을 제목에, Noto Sans KR을 본문·조작에 명시. 폴백 유지 |
| 회전 시 유리 변형 — 기술 표현 | scaleX가 1에서 약 .62까지 감소 | 축대칭 컵의 외곽은 고정, 반사광·마크 이동으로 방향을 표현. 실제 3D 모델/유체 시뮬레이션으로 설명하지 않음 |
| 소재 표현이 약하거나 번짐 — 시각 구현 | 강한 흰 반사선, 다중 마스크·오버레이가 이미지 중심까지 중첩 | 림·유리 벽·수면·바닥 층 구분, 반사선 완화, 사진 경계 마스크 단순화. 원본 이미지 바이트 미수정 |
| 정보가 제품을 압도할 위험 — 기존 수정 경험 | Catalog에 대한 사용자 비평, 큰 3D 패널 거부 | 기존 홍보 순서와 별도 구매 패널 유지. 사실 3개는 같은 크기 계열, 좌우 비대칭 배치 보존 |
| 재조합이 장식으로 늘어날 위험 — 설계 | 승인된 HERO 모션과 COLORS 착지 모션이 이미 존재 | 기존 타임라인 유지. ABOUT·DETAILS만 22px 이내 단발 이동, 내용은 계속 읽을 수 있게 유지. 입력 후 수면 반사선만 620ms로 감쇠 |
| 구매 패널의 배경 조작·배경 톤 불일치 — 상태 | 모달 배경 inert 부재. 구매 패널에서 색을 바꿀 때 COLORS 배경 톤 미동기화 | 모달 동안 본문 inert, 닫을 때 해제. 모든 색상 진입점에서 컵·선택·설명·배경 동기화 |

## 참고를 적용한 방식

| 출처 | 확인한 내용·활용 | 가져오지 않은 것 |
|---|---|---|
| Apple HIG Motion | 짧고 목적 있는 피드백, 사용자 입력 우선, 움직임 감소 | 장시간 반복·시점 강제 이동 |
| Apple HIG Materials | 깊이와 계층을 역할에 맞게 구분, 내용의 가독성 우선 | 모든 콘텐츠의 Liquid Glass화 |
| 팔로잉 피드의 USM Haller | 유리·금속의 빛/그림자, 기본 요소 결합과 공간 변화. 본문 및 대표 장면 확인 | 작품 이미지·영상·브랜드 자산 복제 |
| 팔로잉 피드의 Atemporale | 오브젝트와 타이포의 공존, 여백과 비례, 브랜드의 조용한 인상. 본문 및 대표 장면 확인 | 베이지 팔레트·영문 세리프의 무조건적 도입 |
| 저장소 취향 지도 v0.3 및 MUL 회고 | 촉각성, 안정적인 비대칭, 얇은 서체, WHY/WHEN/HOW | 개인 취향을 범용 의무 규칙으로 승격 |

## 위험·구조 판단

- 주요 위험: CSS 누적 우선순위, 제목 줄바꿈, 회전 입력과 입장 모션 충돌, 구매 패널 색상 동기화, 모달 초점/저장 회귀.
- 조치: E7 범위를 이름 있는 style/script 블록으로 분리하고, 기존 이벤트/저장 구조 보존. 별도의 WebGL 의존성·프레임 루프·외부 이미지 추가 없음.
- 리팩터링: **국소 개선**. 누적 CSS 중복은 실제로 존재하지만 이번에 전체 추출·재작성하면 비교 기준과 회귀 위험이 커진다. 승인 후 공통 토큰/현재 유효 스타일을 분리하는 작업을 별도로 검토한다. 저장 데이터 리팩터링은 불필요.
- 모형 한계: 실제 유리 스캔·제조 사양·유체역학이 아닌 2.5D 시연. 380mL·가격 등은 실제 판매 검증치가 아니다. 푸터에 콘셉트·시연임을 표시.

## 검증

실제 실행·관찰과 정적 확인을 분리한다. 최종 검증 내용은 아래에 이어 기록한다.

## 참고문헌 (APA 7판)

Apple. (n.d.). *Materials*. Apple Developer. Retrieved October 17, 2026, from https://developer.apple.com/design/human-interface-guidelines/materials

Apple. (n.d.). *Motion*. Apple Developer. Retrieved October 17, 2026, from https://developer.apple.com/design/human-interface-guidelines/motion

Kwon, Y., & VSLAB Official. (2026, September 27). *USM Haller* [Motion design portfolio]. Behance. https://www.behance.net/gallery/256299879/USM-Haller

Margini, A., & Villa, G. (2026, February 9). *Atemporale* [Brand identity portfolio]. Behance. https://www.behance.net/gallery/243759877/Atemporale

### 실행 결과 — 2026-10-17

코드 검증 기준 커밋: `360174b7fe1af648379f0b3294d4f6e77f709734`. 아래 기록 추가는 문서만 변경한다.

| 항목 | 판정 | 실제 증거·범위 |
|---|---|---|
| 배포 HTML/미디어 계약 | PASS | `python scripts/check_mul_latest.py` 전 항목 통과. 승인 WebP 2개 원본 payload 동일, HTML 약 533KB |
| JavaScript | PASS | 모든 inline script `node --check` 통과. 실제 브라우저 조작 중 error/warn 로그 없음 |
| 기존 콘텐츠/사진 | PASS | 2개 이미지와 4개 FAQ는 main과 동일. 5개 역사 버전 미수정 |
| PC 1440×900 / 1920×895 | PASS | 실제 Brave 렌더링, HERO 높이 780px. 제목·컵·CTA가 첫 화면 안에 배치, 가로 넘침 없음 |
| 태블릿 768×1024 | PASS | 사진·텍스트 나란히 표시, 읽기 영역/CTA 배치 확인. 가로 넘침 없음 |
| 모바일 크기 390×844 / 320×720 | PASS | 실제 브라우저 viewport 변경 및 스크롤/버튼 조작. 가로 넘침/문장 내부 overflow 없음. 320px에서는 CTA가 두 줄로 배치됨 |
| 색·회전·초기화 | PASS | 클리어/앰버/스모크 선택. 마우스 드래그 0→56°, 키보드 ±15°, 초기화→0. 유리 외곽 transform:none |
| 모달·선택 동기화 | PASS | 구매 패널 앰버 선택 시 COLORS도 앰버와 #fff1e3로 동기화. 열림 inert=true, Escape 닫힘 inert=false |
| 장바구니/실제 저장 복원 | PASS | 앰버 2개, 합계 39,600원. 실제 origin 새로고침 후 2개 유지, 삭제 후 빈 목록 복귀. 검증용 목록은 정리함 |
| FAQ | PASS | 실제 summary 클릭 후 details[open] 1개 |
| 모션 | PASS (제한적) | HERO 최초/스크롤 복귀와 COLORS 착지 후 controls 표시 관찰. 키보드/드래그 물빛 피드백 후 오류 없음. 정밀 프레임 타이밍/FPS 측정은 하지 않음 |
| 움직임 감소 | PASS (정적 검토만) | 기존 media query/컨트롤러 보존, 추가 모션도 matchMedia/변경 이벤트에서 취소. OS 설정을 바꾼 실제 실행은 NOT RUN |
| 실제 폰트/이미지 로딩 | PASS | 고운돋움 로드 체크 true. 두 이미지 모두 naturalWidth=1122, complete=true |
| 브랜치 CI | PASS | GitHub Actions Verify MUL latest release 성공: https://github.com/pchjesus/design-kkakgi/actions/runs/39027598388 |
| main 보존 | PASS | 원격 main SHA는 기준 `6d1f842fd33a65cdddbe68eae700105d769442e7`로 유지 |
| 복사/전체 키보드 초점 순환/저장 불가 환경 | NOT RUN | 관련 기본 구현 보존. 이번 실제 실행에서 전 조합은 검증하지 않음 |
| 실물 모바일·Safari·Firefox·전체 WCAG 감사 | NOT RUN | viewport 검증을 물리 기기/전체 접근성 인증으로 간주하지 않음 |

내부 Sites preview는 bwrap proc mount 인프라 오류로 시작 불가. 서버 우회 없이 중지했고, 공개된 브랜치 코드를 raw.githack의 실제 브라우저 페이지에서 검증했다. 이 미리보기는 별도 제3자 프록시이며 기존 GitHub Pages 배포를 바꾸지 않는다.

- 실행: https://raw.githack.com/pchjesus/design-kkakgi/360174b7fe1af648379f0b3294d4f6e77f709734/cases/mul-cup/latest/index.html
- 코드: https://github.com/pchjesus/design-kkakgi/tree/experiment/mul-material-softness
- 비교: https://github.com/pchjesus/design-kkakgi/compare/main...experiment/mul-material-softness
- 최초 안내 화면이 나오면 **Open the page**를 누르면 된다.
