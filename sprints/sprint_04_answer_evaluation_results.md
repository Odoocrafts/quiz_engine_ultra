# 🧠 Sprint 4 – Answer Evaluation, Scoring & Result View | quiz_engine_pro

---

## 🎯 Goal

Build the backend logic and minimal frontend to evaluate submitted quiz answers, calculate scores, and show the result summary to the user after quiz completion.

---

## 📦 Backend – New Models / Updates

### 🗂️ Update Model: `quiz.attempt`
Add result-related fields.

| Field            | Type      | Description                          |
|-----------------|-----------|--------------------------------------|
| total_score      | Float     | Score earned in the attempt          |
| max_score        | Float     | Total possible score for the quiz    |
| passed           | Boolean   | Whether user passed the quiz         |
| submitted        | Boolean   | Whether the attempt is finalized     |
| submitted_at     | Datetime  | Timestamp of final submission        |

---

### 🗂️ New Model: `quiz.user_answer`
Stores each answer given by a user in an attempt.

| Field           | Type      | Description                        |
|----------------|-----------|------------------------------------|
| attempt_id     | Many2one  | Related `quiz.attempt`             |
| question_id    | Many2one  | The question being answered        |
| selected_ids   | Many2many | Selected answers (if MCQ/MCA)      |
| text_answer    | Text      | For text-based or fill-in-the-blank answers |
| score_awarded  | Float     | Score for this question            |

---

## 🧾 Evaluation Logic

- After submission:
  - Loop through all answers in `quiz.user_answer`
  - Calculate score for each based on:
    - `quiz.answer.is_correct`
    - Exact match for fill-in-the-blank/text
    - Partial scores if `quiz.answer.score` is defined
  - Sum total and store in `quiz.attempt.total_score`

- Determine pass/fail:
  - Default passing score = 50% (configurable later)

---

## 🖼️ Result View (Basic)

- `/quiz/result/<int:attempt_id>`
- Displays:
  - Total score
  - Total questions
  - Correct / incorrect count
  - Pass/fail badge
  - Link to review answers (future)

---

## 🧪 Deliverables

- [x] Evaluate attempt and store score
- [x] Show basic result summary
- [x] Lock submission once finalized
- [ ] No advanced analytics yet
- [ ] No review answer breakdown yet

---

## 🔁 Future Sprints This Enables

- Sprint 5: Answer Review View (user-side)
- Sprint 6: Admin Analytics Dashboard
- Sprint 7: Adaptive Learning Path (based on score)

---