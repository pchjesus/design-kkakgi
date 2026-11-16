# 디자인 깎기 — 통합 아틀라스 탐색 허브

> 2026-11-16 · v0.1 · 정보구조 개편. Universal Visual Design & UI/UX Guidelines v1.3 APPROVED 유지.
>
> **원칙:** 사용자가 가져오는 레퍼런스는 먼저 관찰·분석하여 GitHub에 등록한다. 더 깊은 연구나 실험을 등록의 선행조건으로 삼지 않는다. 기존 파일·ID·링크·기능·사이트 배포는 변경하지 않는다.

## 무엇을 찾는가?

| 목적 | 진입점 | 자료 성격 |
|---|---|---|
| 색채·타이포·질감·배치·선호 비교 | [기존 레퍼런스 목록](README.md) · [개인 취향 지도](PREFERENCE_ATLAS_v0.3_20261016.md) | 개인 취향/정적 관찰/AI 추론 |
| 상태·입력·탐색·모션·데이터 표현 패턴 | [UI 패턴 아틀라스](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md) · [확장 목록](README.md) | 정적 캡처/공식 동작 조사 |
| Liquid Glass 등 전체 화면 스타일 | [STYLE-001: 12종 시각 언어](STYLE_VISUAL_LANGUAGES_ATLAS_v0.1_20261116.md) | 화면 스타일별 정적 비교 |
| 사용자중심 디자인·심리·사용성 근거 | [UX Foundations](foundations/README.md) | 강의/표준/연구, 근거 등급 분리 |
| 실제 사용성 평가 계획 | [사용성 평가 카드](foundations/USABILITY_EVALUATION_CARD.md) | 시험 전 계획 템플릿 |
| KRDS·Apple·Material 3 및 구현 선택 | [디자인 시스템 선택 지도](DESIGN_SYSTEM_SELECTION.md) | 공식/연결 라이브러리 구분 |
| 신규 레퍼런스 입력 | [인입 분석 프로토콜](REFERENCE_INTAKE_PROTOCOL.md) | 최소 관찰·검증·등록 요건 |

## 다섯 갈래의 연구

1. **Visual:** REF-001~072 기존 이미지 분석, ORIGIN-001(기념비적 심장 교육 UI), COLOR-001~003, STYLE-001 및 회화·플레이팅·웨이파인딩. 원자료 수가 곧 직접 선호 확인 수는 아니다.
2. **Patterns:** SRC-00~26에서 수집한 원자료 **243칸(중복 포함)**. 독립 컴포넌트 243개 또는 사용자 선호 243건이 아니다.
3. **Foundations:** FOUND-001부터 자료별 원전·정의·오용·반례·측정·안전·검증 상태를 기록. 처음 등록: [간호기술의 사용자중심 디자인 강의 연구](foundations/FOUND-001_UCD_NURSING_USABILITY.md).
4. **Systems:** KRDS/Apple/Material 3/Creative Coding. 실제 구현·확인된 이름·미검증 기능을 구분.
5. **Evidence:** LAB·VALIDATION에 실험/검증과 불확실성을 기록하고, 예쁜 시안을 실제 사용자 성공의 증거로 확대하지 않는다.

## 함께 쓰는 방법

- **과업→이론→UI 패턴→시각 표현→검증** 순으로 결정하되, 필요한 단계만 열람한다.
- 예: 저장 상태의 가시성([FOUND-001](foundations/FOUND-001_UCD_NURSING_USABILITY.md)) → 알림/상태 패턴([UI 패턴](UI_PATTERN_FIELD_ATLAS_v0.1_20261105.md)) → 목적에 맞는 색과 표면([COLOR](COLOR_APPLICATION_MATERIAL_ATLAS_v0.1_20261112.md)) → 실제 저장·복원 확인.
- 예: 사용자가 Liquid Glass를 선호([STYLE-001](STYLE_VISUAL_LANGUAGES_ATLAS_v0.1_20261116.md))해도 전문 의료 입력 화면의 대비·환자 식별·복구 기준은 별도로 검증해야 한다.
- 승인된 [범용 v1.3](../guidelines/universal/Universal_Visual_Design_UI_UX_Guidelines_v1.3.md)은 규범, Foundations는 검증 가능한 연구 근거다. 자료 등록이 범용 지침 개정을 뜻하지 않는다.

## 등록·근거·권리

- [USER] 직접 선호, [OBS] 관찰, [LECTURE/SOURCE] 자료의 주장, [OFFICIAL] 공식 출처, [AI-HYP] 추론, [NOT RUN] 미검증을 분리한다.
- 새 자료의 출처와 라이선스가 불명확하면 미확인으로 남긴다. **외부 SNS 캡처·교수 수업 PDF·영상·폰트 원본을 공개 GitHub에 복제하지 않는다**.
- 새 자료는 [등록 프로토콜](REFERENCE_INTAKE_PROTOCOL.md)에 따라 우선 분석하여 적절한 계열에 연결한다. 중복 항목에 무조건 새 ID·새 필수 규칙을 만들지 않는다.
- 기존 파일은 이동·삭제·재번호하지 않는다. 기존 레퍼런스 목록·실험 이력을 보존한다.

## 검증 범위

**PASS:** 2026-11-16 현재 분류 현황과 승인 v1.3 확인, 탐색 허브 신규 작성.
**NOT RUN:** 과거 전체 내부 링크 전수 검사, 캡처 원본의 실제 애니메이션, 사용자 시험, 접근성 실측, 임상 검증, 기존 앱 회귀 시험(앱은 미변경).
