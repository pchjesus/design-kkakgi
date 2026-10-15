# DEVLOG

## v0.1 — 초기 이관 (2026-10-16)

- Private `main`에 지침, 레퍼런스 분석, EXP-001 MUL. 다섯 버전, EXP-002 SAI v0.1·v0.2, 운영 문서를 이관했다.
- 당시 원본 패키지의 SHA-256 매니페스트 검증 결과는 `MANIFEST_SHA256.tsv`에 보존한다.

## v0.1 — Public 전환 및 이미지 정책 변경 (2026-10-16)

- 사용자 승인에 따라 이미지가 포함된 기존 커밋을 부모 없는 새 루트 커밋 `cd715d942d59272dea6d0b6b199c463a561490ff`으로 교체했다.
- 현행 트리에서 이미지 원본·미리보기·스크린샷 32개를 제외하고 코드·문서·피드백·분석 결과를 보존했다.
- EXP-003 계획 문서를 추가했다. 실제 앱 구현은 하지 않았다.
- Public 전환 뒤에도 GitHub Pages·CI/CD·릴리스를 새로 만들지 않았다.

### 검증 기록

| 항목 | 결과 | 근거 |
|---|---|---|
| 이전 `main` 확인 | PASS | 정책 전환 전 HEAD와 전체 트리 확인 |
| 현재 트리 이미지 식별·제거 | PASS | 32개 래스터 이미지 제거, 새 `main` 이미지·ZIP 0개 |
| 텍스트·코드 내 내장 이미지 데이터 | PASS | `data:image` 패턴 미발견 |
| 일반 비밀정보 패턴 | PASS | private key, GitHub token, AWS key, 일반 API key 패턴 미발견 |
| 원본 코드·문서 보존 | PASS | 변경 대상 운영 문서 8개 외 기존 80개 파일의 Git blob SHA 동일 |
| 접근 가능한 Git 참조 | PASS | `refs/heads/main`만 존재; 태그·추가 브랜치·릴리스 없음 |
| Git LFS | PASS | 기존·신규 트리에 LFS pointer 없음, 이미지 파일은 일반 Git blob으로만 존재했음 |
| GitHub Pages·외부 자동 배포 | PASS | Pages 비활성, 워크플로 파일·릴리스 없음 |
| Public 전환 | PASS | GitHub 원격 메타데이터와 설정 화면에서 `public` 확인 |
| MUL·SAI 실제 실행/사용자 검증 | NOT RUN | 이번 정책 전환 범위 밖 |
| 플랫폼 캐시·외부 복사본·미참조 객체 완전 삭제 | NOT RUN | GitHub 가비지 컬렉션·외부 복사본은 즉시 또는 완전 삭제를 보장할 수 없음 |
