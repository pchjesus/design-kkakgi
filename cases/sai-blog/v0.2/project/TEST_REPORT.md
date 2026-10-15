# SAI v0.2 테스트 보고서

**일자:** 2026-10-15
**환경:** Linux headless Chromium + Playwright, HTML `set_content` 테스트 (로컬 파일/서버 URL 직접 탐색은 실행 환경에서 정책상 차단됨)

## 자동화 확인 결과

| 테스트 | 결과 |
|---|---|
| 예시 글 6편 로딩, 상세화면, 근거 블록·참고문헌 | PASS |
| 검색, 주제 필터, 정렬(코드 지원) | PASS (검색·필터 인터랙션 확인, 정렬 코드 정적 검토) |
| 북마크, 저장 목록 | PASS (mock localStorage) |
| 글 작성·수정·삭제, 재초기화 후 내용 복원 | PASS (mock localStorage) |
| 테마 변경 및 복원 | PASS (mock localStorage) |
| 키보드 `/` 검색 이동, 작성창 포커스 순환, Escape | PASS |
| 미저장 변경사항 취소 확인 | PASS |
| 화면 폭 320·360·390·768·1024px에서 가로 스크롤 없음 | PASS (홈·글) |
| `prefers-reduced-motion` scroll-behavior 반영 | PASS |
| JS 런타임 오류 | 0건 (자동화 시나리오 내) |
| 표준 텍스트 컬러 대비(light/dark), 대표 토큰 | 수치 점검: 최소 4.93:1 (sampled story label) |

## 아직 검증하지 않은 사항

- 모든 DOM 요소/모든 UI 상태의 **WCAG 2.2 AA 준수 인증** (별도 접근성 감사 필요)
- Android/iOS/macOS 실기기와 Safari/Firefox/Edge 호환성
- 실제 파일 및 호스팅 오리진에서 localStorage 지속성 (테스트 브라우저 정책으로 직접 테스트 불가; mock으로 기능 로직만 확인)
- 실제 보조공학(screen reader) 사용성, 200% 이상 확대와 OS별 폰트 렌더링
- 실제 독자 참여 첫 사용 이해도/시간/오류율 비교 및 전문 논문감수

## 릴리스 제약

데모 정적 웹사이트. 로컬 저장소는 장기 보존이나 사용자 계정의 대체물이 아님. 학술적 주장은 DOI와 연구 설계를 확인하는 콘텐츠 검토 과정 필요.
