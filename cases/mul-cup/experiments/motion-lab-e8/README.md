# MUL. E8 Motion Lab — 독립 A/B 학습 실험

- 상태: **EXPERIMENT / 사용자 평가 전 / main 미반영**
- 기준 원본: `cases/mul-cup/latest/index.html` (승인된 E8, 무변경)
- 실행 파일: [index.html](index.html) — HTML/CSS/JS/SVG 단일 파일. 외부 라이브러리·서버 필요 없음.
- 브랜치: `experiment/mul-e8-motion-lab-20261026`
- 목표: 컵 착지 모션의 **반동 높이 하나**를 비교하고 CSS 변수를 익힌다.

## 무엇을 비교하나?

| 항목 | A (원본 E8) | B (실험) |
|---|---:|---:|
| 애니메이션 전체 시간 | 880ms | 880ms |
| 착지 | 54% | 54% |
| 반동 시작/피크 키프레임 | 76% | 76% |
| 반동 높이 | 19px | 10px (0~30px 조절) |
| 컵 찌그러짐 | 없음 | 없음 |
| 효과 곡선 | E8과 동일 | E8과 동일 |

실제 코드의 최종 `@keyframes e6c2-glass-arrival`을 참조했다. 같은 HTML에 이전 단계의 동일 이름 keyframes도 있지만, **마지막 E8 재정의(54%/76%)가 사용된다.**

비교 페이지는 승인된 E8의 **SVG fallback 컵**을 독립 추출하고 CSS 타이밍 및 접촉 그림자를 재현한 것. 원본 3D Three.js WebGL 모델·색/구매/저장 기능 전체를 실행하는 페이지가 **아니며**, 최종 제품의 물성·성능 품질 검증에 갈음하지 않는다.

## 실행 방법 (코딩 지식 불필요)
1. GitHub에서 [index.html](index.html)을 열고 **Raw**를 선택한다.
2. 해당 HTML 파일을 저장한다(`index.html`). 확장자를 `.txt`로 저장하지 않도록 주의.
3. 파일을 Chrome/Edge 등에 열어 **A·B 동시에 재생**을 눌러본다.
4. B의 높이를 5 / 10 / 19 / 25px 순서로 바꿔보고 A와 비교한다.
5. 기기의 `prefers-reduced-motion`이 활성화되면 애니메이션을 정지한다.

## 학습 포인트
- **HTML:** `<button>`, `<section>`, `<input type=range>`를 찾기.
- **CSS:** `@keyframes e8-motion-arrival`에서 54%와 76%의 `translate3d` 차이를 이해하기.
- **JavaScript:** `replay(stage)`가 클래스 `is-playing`을 제거했다가 다시 붙여 재생시키는 이유 알아보기.
- **가설 질문:** 높이가 낮아질수록 더 단단하고 차분해 보이는가? 지나치게 낮으면 오히려 경쾌함이 사라지는가?

## 검증 기록 (2026-10-26)
- **PASS — 정적 GitHub 원격 검사 (11/11):** 브랜치 파일 조회, A/B 변수, 재생 버튼 및 입력 이벤트, 실제 E8 54%/76% 타이밍, SVG 2개, 외부 JS 미사용, 반응형/모션 감소 코드 존재, main/브랜치 E8 원본 일치.
- **NOT RUN — 브라우저 실동작:** 데스크톱·모바일 렌더링, 재생 중 조작/연타, 저사양 성능, 접근성 실사용. 실제 테스트 전 기능적 완성 PASS로 기록하지 않음.
- **보존:** main에 커밋/병합 없음, GitHub Pages 변경 없음, 기존 제품 라이브러리/저장/구매/3D 기능 무변경.

## 설계·변경 한계
이 단계에서는 높이만 변화를 주기 때문에 일부 관찰자가 B를 '묵직하다'고 느낄 수 있어도 곧바로 더 좋은 디자인이라고 단정하지 않는다. 후속 사용자 평가 후 필요한 경우 다른 파라미터를 **별도 실험**으로 다룬다.

### 참조
[기존 E8 검토 문서](../../latest/DESIGN_REVIEW_E8.md) · [E7/E8 배운 점](../../DESIGN_LEARNINGS_E7_E8.md) · [Creative Coding Playbook](../../../../references/creative-coding/INTERACTION_PLAYBOOK_v0.1_DRAFT.md)
