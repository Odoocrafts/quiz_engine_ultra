# 🧠 Sprint 7 – Retry Options & Adaptive Quiz Mode | quiz_engine_pro

---

## 🎯 Goal

Allow users to retake quizzes (based on rules) and enable adaptive quiz logic that adjusts question difficulty based on user performance in real-time.

---

## 📦 Backend – Model Enhancements

### `quiz.quiz` – Add fields

| Field               | Type      | Description                                  |
|--------------------|-----------|----------------------------------------------|
| allow_retries      | Boolean   | Whether user can retake the quiz             |
| retry_cooldown     | Integer   | Cooldown period (in hours) before retry      |
| is_adaptive        | Boolean   | Enable adaptive mode (difficulty scaling)    |

---

### `quiz.attempt` – Add fields

| Field               | Type      | Description                                  |
|--------------------|-----------|----------------------------------------------|
| is_retry           | Boolean   | Whether this is a retry attempt              |
| previous_attempt_id| Many2one  | Link to the original attempt                 |
| adaptive_path_json | JSON      | Track question flow during adaptive mode     |

---

## 🧠 Adaptive Mode Logic (Backend)

- Questions tagged with `difficulty`: `easy`, `medium`, `hard`
- Start with `medium` question
- Adjust next question based on:
  - Answered correctly → increase difficulty
  - Answered incorrectly → decrease difficulty
- Store flow in `adaptive_path_json` for traceability

---

## 🖼️ UI/Flow Changes

### Retry Quiz Button
- Show "Retake Quiz" on result page if `allow_retries` is enabled
- Enforce cooldown using `retry_cooldown`

### Adaptive Mode (when enabled):
- No static question order
- Dynamically select next question based on performance
- Update backend after each submission

---

## 🧪 Deliverables

- [x] Retry flow logic and validations
- [x] Cooldown enforcement
- [x] Adaptive logic (backend-ready)
- [x] JSON path tracking in attempts
- [ ] Frontend adaptive UI adjustments (reserved for Sprint 8)

---

## 🔁 Future Sprints This Enables

- Sprint 8: Advanced frontend for adaptive quizzes
- Sprint 9: Smart Recommendations after retake
- Sprint 10: Skill Graphs & Weak Area Tagging

---