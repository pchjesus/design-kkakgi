# Simulator Project Design Constraints v1.0

> **상태:** 프로젝트 전용 보존 부록 — 범용 가이드로 개편하며 원본의 프로젝트별 제약을 **내용 변경 없이 발췌**.
> **원본:** `Educational Simulator UI/UX Design Standard v1.0` (2026-10-15). 본 파일은 원본 자체를 대체하거나 새 기능/디자인 변경을 승인하지 않는다.
> **연계:** `Universal_Visual_Design_UI_UX_Guidelines_v1.0.md`는 범용 디자인 판단에 활용하고, 시뮬레이터 개발의 과학 모델·상태·기능 보존은 **해당 저장소의 최신 승인 계약과 원본 문서**를 우선한다.

## Original internal design reference (preserved)

**Main internal reference:** Boyacto's separate PB980 learning room (Ventilator Simulator, commit [5be92ce](https://github.com/pchjesus/ventilator-simulator/commit/5be92ce76469eca0309b2b6daf225fcfc05a1b1d), `learn.html`, `learning-room.css`, `src/learning-room.js`, `docs/LEARNING_ROOM.md`). Its A intro → B device exploration → C single-task practice is a **reference for information architecture**, not a requirement to duplicate code or add the same pages everywhere. The original UI is retained deliberately for comparative evaluation and functional regression.

## 5. Repository-specific non-regression contracts

### Ventilator Simulator
- Boyacto's `learn.html` is the **preferred design-language reference for future learner-facing UI**. Preserve the original PB980-reference device view (`index.html`) and the separate learning room as comparison baselines until a future *explicitly approved* unification decision; this guidance alone authorizes **no merge/replacement**.
- The original equipment representation has a legitimate fidelity goal, so **do not turn the simulated device face into a generic SaaS dashboard**. Differentiate equipment imagery from the surrounding student-facing learning shell.
- Preserve 7 settings, pending/accept/cancel, fixed monitoring examples, generated pressure/flow/volume, independent LAB/CORE/CASE data, gating, state ownership and clinically unreviewed labels. Separate learning-room state is not a new patient model.
- Do not assume `learn.html` / `index.html` navigation preserves live RAM sessions across full-page reloads. If integration is proposed, present persistence and preservation tradeoffs first.

### RAAS Simulator
- Current main v5.9.1 approved **B layout / P1 medical navy / T1 soft borders / K2 focused learning / G1 original-size graph** remains authoritative. The new philosophy should **refine entry and progression**, not silently replace those decisions.
- Preserve single existing stage/drug data, RAAS physiology, Canvas pathway and coordinates, current vs reached step distinction, drug application/removal, BP/Na⁺/volume/GFR output, lab/case answers and simulation/learning/clinical state separation.
- Preserve original-scale graph horizontal access on small screens, current-topic study and return from clinical review. A new introduction must not prevent direct simulator/free-exploration access.

### Cardiac Electrophysiology Simulator
- Preserve current v1.13 three-area Simulator/Learning/Clinical navigation, original five-stage Guide/10 questions, six-unit learning, and present public vs QA-only clinical-case gating.
- **ECG + conduction may need simultaneous visibility** for causally linked learning; do not split or clone the single active engine/Canvas/SVG merely to make screens visually sparse.
- Preserve canonical Play/Pause, physiological/visualization A/B time, Timeline/seek, HR, phase and electrical/mechanical/Wiggers behavior. Tab changes must not cause new time changes/auto-Play or lose session/answers; use the explicit approved v1.13 transition contract.
- Preserve scientific terminology and all established model-vs-clinical caveats.

## 6. Authority, review and versioning

This file is a **forward-looking visual/UX process baseline**, not a blanket authorization to change shipped screens, curricula, design colors, simulation logic, medical statements, persistence or navigation. **Explicit newer user-approved UX contracts and project-specific simulation/safety rules take precedence** if a proposal conflicts. Flag conflicts, explain options and ask the user to choose consequential UX changes.

Use this guide when planning future work, record accepted design choices and any deviations in the appropriate project design/DEVLOG record, and amend the guideline by reviewed PR when the shared rules materially change. Do not claim review completion, browser PASS, real-device PASS or clinical approval from documentation-only registration.
