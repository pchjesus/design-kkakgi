# FOUND-001 — 주장·원전 검증 레지스터 v0.1

> 2026-11-16 · [본문](FOUND-001_UCD_NURSING_USABILITY.md) 연결. PASS는 **해당 문서 출처를 확인**했다는 뜻이고 실제 앱이 안전하거나 사용하기 좋다는 뜻이 아니다.

| 교안 위치 | 강의의 내용 [LECTURE] | 독립 조사 | 현재 상태 |
|---|---|---|---|
| pp. 3–5 | 사용자 특성·맥락·목표·참여·반복개선 | ISO 9241-210:2019 공식 요약의 인간중심 설계 범위와 부합 | PASS (개념 범위) / 전문 미열람 |
| pp. 9–10 | IA / User Flow / Interaction / GUI | 강의의 실무 분류 확인 | PASS (강의 확인), 특정 ISO 원전 규정이라고 단정 금지 |
| p. 9 | UX 불만 약 1/3이 메뉴/검색 문제 | 원출처·시기·표본이 없음 | **NOT RUN** 수치 미검증 |
| p. 12 | Netflix 탐색 평균 10분 이상 | 원 연구·조사 시기·측정 정의 미확인 | **NOT RUN** 수치 미검증 |
| p. 12 | Miller 법칙에 따른 항목 7개 이하 권고 | 기억범위를 화면 요소 수 제한으로 곧바로 적용하는 해석은 과잉 | 실무 **절대 규칙으로 승격 금지** |
| p. 13 | Postel 관용적 입력 | RFC 9413은 무조건 너그러운 해석의 위험을 논의 | PASS (경계 검토) |
| p. 15 | Doherty 0.4초 | 단일 수치를 모든 상호작용의 절대 합격선으로 사용하지 않음 | 근거·예외 심화 NOT RUN |
| p. 21 | 정확한 위치/원인의 입력 오류 표시 | WCAG 2.2 SC 3.3.1 오류 식별, 3.3.3 수정 제안 | PASS (공식 규범 확인) / 개별 UI 미시험 |
| p. 24 | 이탈 의사 설득/혜택 안내 | 사용자의 종료 자유와 강요성 패턴 검토 필요 | 교안 사례만 확인 |
| p. 25 | 사용성 = 효과성/효율성/만족도 | ISO 9241-11:2018 공식 요약의 사용성 개념·범위와 부합 | PASS (개념 범위) / 전문 미열람 |
| p. 26 | 환자 식별/단위/경고/저장 관련 오류 | FDA 2026-08-03 의료기기 인간공학 지침 목적과 연결 | PASS (원칙), 모든 앱에 법적 의무 동일 적용 금지 |
| p. 27 | SUS 사용성 평가 | Brooke(1996) SUS **10문항**(교안은 문항 일부 예시) | PASS (도구의 구조), 실제 SUS 조사 NOT RUN |
| pp. 28–29 | 공감→문제정의→아이디어→시제품→테스트 | 강의 5단계 모형 확인 | PASS (강의), 실제 혁신 성과 NOT RUN |

## 위험한 혼동

강의의 법칙과 공식 규범을 같게 취급하지 않는다. 교수 직함이 개별 통계의 독립 검증을 대체하지 않는다. 만족/미적 선호/SUS와 성공률/임상 위해를 합치지 않는다. 실제 저장 성공 전 '저장됨'을 표시하지 않는다. 가상 사용자·모의 사례는 임상 효과가 아니다.

## 확인한 외부 자료 (APA 7판)

- International Organization for Standardization. (2018). *Ergonomics of human-system interaction—Part 11: Usability: Definitions and concepts (ISO 9241-11:2018).* https://www.iso.org/standard/63500.html
- International Organization for Standardization. (2019). *Ergonomics of human-system interaction—Part 210: Human-centred design for interactive systems (ISO 9241-210:2019).* https://www.iso.org/standard/77520.html
- Brooke, J. (1996). SUS: A 'quick and dirty' usability scale. In P. W. Jordan et al. (Eds.), *Usability evaluation in industry* (pp. 189–194). Taylor & Francis.
- Thomson, M., & Schinazi, D. (2023). *Maintaining robust protocols (RFC 9413).* RFC Editor. https://www.rfc-editor.org/rfc/rfc9413
- U.S. Food and Drug Administration. (2026, August 3). *Applying human factors and usability engineering to medical devices*. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices
- World Wide Web Consortium. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* https://www.w3.org/TR/WCAG22/

### 아직 확인되지 않은 사항

ISO 유료 표준 전문, 위 통계의 최초 조사 논문, 실제 임상·사용자 시험, 제품별 FDA 규제 적용 여부 및 개별 컴포넌트 접근성 실측은 **NOT RUN**.
