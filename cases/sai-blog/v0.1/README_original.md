# 사이 (SAI) — 논문과 문화 사이

Apple Human Interface Guidelines의 정보 계층·단순함·일관성·접근성 등을 참고해 제작한 독립형 에디토리얼 블로그 프로토타입입니다. Apple의 디자인 자산이나 공식 제품을 복제한 페이지가 아닙니다.

## 실행 방법

- `index.html`을 브라우저로 열면 별도 설치 없이 실행됩니다.
- GitHub Pages에 게시하려면 저장소 루트에 `index.html`을 두고 Pages 배포를 활성화합니다.
- 샘플 글 6편에는 실제 학술 논문의 서지정보·DOI가 포함되어 있지만, 본문은 블로그 콘셉트 예시용 요약·해석이며 학술 논문 전체 분석을 대체하지 않습니다.

## 구현된 기능

- 데스크톱/모바일 반응형 레이아웃, 키보드 접근성 및 reduced-motion
- 검색(제목·요약·본문), 카테고리 필터, 정렬, 북마크
- 다크/라이트 테마 전환 및 설정 저장
- 글 상세페이지, 읽기 진행률, DOI 링크
- 사용자 글 새로 작성/삭제(브라우저 localStorage에만 저장)
- 북마크 및 사용자 글의 브라우저 내 저장/복원
- 검색 단축키 `/`, 작성창 닫기 `Esc`

## 구현 한계

- 로그인, 실제 서버 저장, 공개 게시, 댓글, 기기 간 동기화는 제공하지 않습니다.
- 사용자 글은 브라우저/프로필/저장 데이터 삭제 시 사라질 수 있습니다. 중요한 원고는 별도로 백업해 주세요.
- 브라우저 정책에 따라 `file://` 환경에서 로컬 저장이나 링크 복사에 제약이 있을 수 있습니다. 이때 정적 호스팅 환경에서 사용하세요.
- 샘플 글에 사용된 시각 자료는 CSS로 생성한 독립형 추상 그래픽입니다.

## 확장 방향

1. 콘텐츠 데이터 파일 분리 및 Markdown 편집기
2. 논문 메타데이터(DOI) 확인·출처 양식 검사
3. 접근 권한, 작성자 인증, 데이터베이스와 미디어 저장소
4. 사용자 공개 전 관리자 승인과 저작권 검토, 검색 엔진 메타데이터

## 디자인 참고

Apple. (2026). *Design principles*. Apple Developer. https://developer.apple.com/kr/design/human-interface-guidelines/design-principles

Apple. (n.d.). *Typography*. Apple Developer. https://developer.apple.com/kr/design/human-interface-guidelines/typography

Apple. (n.d.). *Layout*. Apple Developer. https://developer.apple.com/kr/design/human-interface-guidelines/layout
