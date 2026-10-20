# 디자인 시스템 선택 지도 — KRDS × Apple × Material 3 × 프로젝트 증거 (2026-10-20)

**목적:** 여러 UI Kit을 평균내어 '유행하는 외형'을 만드는 대신, **사용자의 과업·매체·제약에 따라 각 시스템의 서로 다른 장점만 참조**한다. 이 문서는 v1.3 DRAFT가 링크하는 비교표이며, 현행 v1.2 자체는 변경하지 않는다.

## 1. 어떤 문제에 어떤 레퍼런스가 먼저인가

| 해결할 문제 | 우선 살펴볼 곳 | 보완할 곳 | 피해야 할 오용 |
|---|---|---|---|
| 웹페이지 전체 IA·업무 여정·한국어 입력 | [KRDS 레이아웃·서비스 패턴](krds/README.md) | 현장 과업·실제 사용자 테스트 | 모든 웹사이트를 공공기관 화면처럼 만들기 |
| iOS·iPadOS의 정보 계층·기본 조작 | [Apple Figma/HIG](apple/README.md) | KRDS 접근성/웹 정보 구조 | 웹에서 Apple 고유 자산/폰트를 복제 |
| 데스크톱 업무형 표·사이드바·툴바 | Apple **macOS 27** 검색 색인 | KRDS 목록·필터·표, Material Rail | 네이티브 운영체제 창을 HTML에 재현 |
| 화면 폭에 적응하는 탐색, 앱 상태 컴포넌트 | [Material 3](material3/README.md) | Apple 플랫폼 관습, KRDS 정보 구조 | Material Expressive의 원칙을 구버전 고정 값으로 옮기기 |
| 환자·보호자에게 쉬운 오늘의 행동·문의처 | [돌봄 플랫폼 환자용 DRAFT](https://github.com/pchjesus/ai-care-transition-platform/blob/main/docs/PATIENT_FIRST_MOBILE_UX_UI_DESIGN_DRAFT_v0.3.md) | KRDS 도움/상세/접근성, Apple·Material 모바일 조작 | 의료 성능을 디자인만으로 주장하거나 검토 전 정보 공개 |
| 의료진 업무 단계/미확정·검토·승인 구별 | [돌봄 플랫폼 업무흐름 DRAFT](https://github.com/pchjesus/ai-care-transition-platform/blob/main/docs/MVP_WORKFLOW_AND_DATA_CONTRACT_DRAFT_v0.2.md) | KRDS 패턴, Apple macOS·Material Rail | 과거의 병원 중심 시연안을 **현재 제품 P0**로 승격 |
| 타이포·색·질감·물성의 미감 | [확인된 사용자 레퍼런스](PREFERENCE_ATLAS_v0.3_20261016.md), [MUL.](../cases/mul-cup/DESIGN_LEARNINGS_E7_E8.md) | Apple Materials 등 해당 목적 원리 | 크림·세이지, Liquid Glass, 카드 등을 범용 미학으로 강제 |
| 개인 취향과 실제 사용성 충돌 판단 | [메뉴 룰렛 사례](../cases/menu-roulette/LESSONS.md) 및 테스트 | 각 시스템의 상태/접근성 | 사용자 1인의 미감 평가를 범용 사용성 증명으로 승격 |

## 2. 재사용 가능한 의사결정 절차

1. **무엇을 하게 할 것인가?** 사용자와 최우선 작업/사용 장면을 1문장으로 정의.
2. **어떤 정보가 같이 있어야 하는가?** 목록·상세·입력·근거·상태·다른 역할의 공개 범위를 구조화.
3. **화면 유형 A/B를 제시:** 목적에 따라 KRDS식 서비스 IA, Apple식 정보 계층, Material식 크기 적응 탐색 등에서 **차이가 있는 구조 후보만** 제시. 디자인 방향이 이미 고정된 작은 수정은 2안 생략.
4. **표현을 따로 결정:** 폰트·색·물성·움직임을 내용/브랜드/가독성에 맞게 조정. 세 시스템의 외형을 동시에 섞지 않음.
5. **실제 사용자 작업과 기술 검증:** 키보드, 터치, 대비, 초점, 반응형, 저장, 보류, 승인, 오류, 공개 범위, 기존 기능 회귀. 테스트하지 않은 것은 NOT RUN.

## 3. 증거의 층위 (추측을 지침으로 만들지 않기)

- **[STANDARD]** KRDS/Apple HIG/Google Material 공식 규칙의 읽힌 내용. 원칙이라도 해당 플랫폼 범위와 버전을 확인.
- **[LIBRARY OBS]** Figma 라이브러리에서 컴포넌트 **이름·검색 존재**를 확인한 사실. Variant, 토큰 수치, 실제 동작 증거가 아님.
- **[USER]** MUL/메뉴 룰렛 등 사용자가 선호하거나 비선호한 실제 피드백. 일반 이용자 전체의 선호·성능과 별개.
- **[PROJECT DRAFT]** 돌봄 플랫폼의 설계 선택·상태 계약. 실제 의료기관·환자·임상 성능 검증 전.
- **[HYPOTHESIS]** 다른 제품에 전이 가능하다는 우리의 추론. 실제 비교/검증 전 MUST로 승격 금지.

## 4. 한계와 안전

- KRDS 공식 웹 패턴은 일부 내용을 확인했지만 모든 서비스 화면의 효과가 검증된 것은 아니다.
- Apple 27 Figma 색인의 **95개는 전수 목록이 아니며** 연결된 Community 라이브러리와 Apple 공식 게시 원본 간 정확한 동일성은 미확인.
- Material 3는 선별 검색 10건으로 이름을 확인. 연결 Community Kit과 공식 배포본 동일성/전체 자산·variants 미확인; M3 Expressive의 최신 탐색 권고는 버전 차이를 주의.
- **환자용 MVP는 현재 활성 DRAFT**, 병원 A1/A2/A3 워크벤치는 연구/확장 설계·별도 시연 목업. 상충 시 현재 승인된 PRD와 실제 요구를 먼저 확인.
- Google/Apple의 원본 Figma UI Kit, 고유 그림/아이콘/폰트를 Public GitHub에 미러링하지 않음. 외부 원본 접근 경로·분석·출처만 보존.

### 후속 검증

- 신규 분야마다 **동일한 실제 콘텐츠로** 구조 비교. 미감 평가/사용성 측정/구현 검증 각각 독립 기록.
- 데이터가 많은 작업형 화면은 **표와 카드, 넓은 2열과 중앙 집중형** 양쪽을 고려. 단, 모든 작업에 2안을 강제하지 않음.
- 파일 조회는 선택적: 문제에 필요한 허브 1개 → 해당 패턴 1개 → 실제 값이 필요할 때만 Figma/외부 공식 출처 확인.
