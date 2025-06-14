# 🧠 Sprint 1 – Instruction Screen + Time Limit Logic | quiz_engine_pro

---

## 🎯 Goal

Introduce timed quiz functionality and an instruction screen that appears before starting the quiz. This sprint builds toward test-mode quizzes with enhanced user flow and time-bound evaluation.

---

## 📦 Models – Updates

### `quiz.quiz` – Add fields

| Field             | Type      | Description                                  |
|------------------|-----------|----------------------------------------------|
| instruction_text | Html      | Instructions to show before quiz begins      |
| timer_type       | Selection | `none`, `global`, `per_question`             |
| global_time_limit| Integer   | Minutes (for `global` timer type)            |
| per_question_time| Integer   | Seconds (for `per_question` timer type)      |

---

## 📜 Selection Field: `timer_type`
```python
[
  ('none', 'No Time Limit'),
  ('global', 'Global Time Limit'),
  ('per_question', 'Time per Question')
]

🧾 Admin UI Changes

    In quiz form:

        Display a rich text HTML field for instruction_text

        Show global_time_limit only if timer_type == global

        Show per_question_time only if timer_type == per_question

    Add helpful tooltips on each timer field

🧠 Frontend Behavior (for later implementation)

    Not implemented yet, but UI should support:

Instruction Screen

    Display instruction_text before starting quiz

    Show quiz metadata (e.g., time limit, number of questions)

    "Start Quiz" button initiates timer & first question

Timer Logic (for future)

    Global: Countdown across entire quiz, auto-submit on timeout

    Per-question: Countdown for each question, auto-advance or timeout

🧪 Deliverables

Add new fields to quiz.quiz

Update form views with conditional field visibility

No controller or frontend logic yet (reserved for Sprint 2/3)

    No timer JS yet

🔁 Future Sprints This Enables

    Sprint 2: Question Navigation + Progress

    Sprint 4: Evaluation & Auto-Submit on Timer End

    Sprint 6: Attempt Results & Analytics