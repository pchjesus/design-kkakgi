# Creative Coding · Interaction Reference Hub (2026-10-26)

> **상태: RESEARCH / 선택형 참고자료.** 승인된 Universal Visual Design v1.3·운영 지침 v1.2를 개정하지 않는다. 기존 앱·Pages·브랜드·권한·데이터 계약도 변경하지 않는다.

## 목적
Castle Jelly 공개 프롬프트, Anime.js, Coolors, Codrops의 실무적으로 유용한 부분을 추출해 **행동 → 표현 → 구현 → 검증**으로 연결한다. 링크/분석 텍스트만 보관하고 스크린샷·원본 소스·이미지·폰트는 복제하지 않는다.

## 10초 선택
| 문제 | 우선 출처 | 선택 기준 |
|---|---|---|
| 물리적/객체적 상호작용을 설계하고 싶다 | [Castle Jelly 연구 프롬프트](https://www.tripo3d.ai/3d-prompts/castle-jelly-interactive-webgpu-diorama) | 재질·입력·행동·시뮬레이션·제어·화면을 분리해 명세화. **결과의 검증된 성능 근거는 아님** |
| UI 동작·SVG·드래그·타임라인 구현 | [Anime.js 공식 문서](https://animejs.com/documentation/) | CSS로 충분하면 CSS 유지; 새로운 의존성은 타당할 때만 |
| 컬러 후보 탐색·내보내기 | [Coolors](https://www.coolors.app/) | 색채 후보는 색 역할 토큰에 매핑; 무료/Pro 기능 구분 |
| 3D/인터랙티브 웹 아이디어 + 구현 분석 | [Codrops Creative Hub](https://tympanus.net/codrops/hub/) / [Tutorials](https://tympanus.net/codrops/category/tutorials/) | 시연과 구현 설명이 함께 있는 사례 1~2건 선택; 코드/라이선스 별도 확인 |
| 공식 접근성 판단 | [W3C WCAG 2.2](https://www.w3.org/TR/wcag/) | 컬러 사이트의 예쁜 팔레트만으로 대비·조작성 검증 불가 |

## 적용 대상
- MUL. 3D 물컵: 타격감·드래그·반응·감쇠·복원, 포인터/터치 종료, 저성능 fallback.
- 메뉴 룰렛: 상태 기반 슬롯/결과 연출, 중복 애니메이션 방지, 전체 후보의 당첨 로직 보존.
- 의료 교육 시뮬레이터: 물리·생리 규칙/시각효과 분리, 교육용 모델의 범위·정확도 별도 검증.
- 돌봄 플랫폼: 화려한 3D 대신 승인/미확정/공개/확인 상태, 읽기·접근성·움직임 최소화 우선.

## 상세 워크플로 및 복사 가능한 프롬프트
[INTERACTION_PLAYBOOK_v0.1_DRAFT.md](INTERACTION_PLAYBOOK_v0.1_DRAFT.md)

## 증거·권리 경계
- **[SOURCE OBS]** 공식 문서의 확인 기능과 가격·지원 범위.
- **[AUTHOR PROMPT]** 제작자 공개 지시문: 기대 동작을 적은 명세이지 실제 구현·물리 정확도의 증명 아님.
- **[HYPOTHESIS]** 다른 프로젝트로의 효과 전이 가능성: 별도 실험 전 규칙으로 승격 금지.
- 사례별 라이선스·자산 재배포 권한을 별도 확인. 외부 UI/폰트/이미지를 복사하지 않는다.
- 스크린샷 3장은 채팅 내 분석만 수행. Instagram 소개 문구와 사이트 시연은 광고/홍보 성격일 수 있으므로 제3자 도구의 완성도 보증으로 취급하지 않는다.

## 출처 (APA 7)
Anime.js. (n.d.). *Documentation*. https://animejs.com/documentation/

Codrops. (n.d.). *Creative Hub*. https://tympanus.net/codrops/hub/

Codrops. (n.d.). *Tutorials*. https://tympanus.net/codrops/category/tutorials/

Coolors. (n.d.). *Pricing*. https://www.coolors.app/pricing

Vib3Coded. (2026, October 9). *Castle Jelly interactive WebGPU diorama* [Author-supplied prompt]. Tripo. https://www.tripo3d.ai/3d-prompts/castle-jelly-interactive-webgpu-diorama

World Wide Web Consortium. (2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/wcag/
