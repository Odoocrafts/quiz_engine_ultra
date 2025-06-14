# 🧠 Sprint 2 – Navigation, Randomization & Progress Tracking | quiz_engine_pro

---

## 🎯 Goal

Implement dynamic question ordering (random or sequential), enable back/forth navigation during quizzes, and show a progress tracker to users while answering.

---

## 📦 Models – Updates

### `quiz.quiz` – Add fields

| Field              | Type      | Description                                     |
|-------------------|-----------|-------------------------------------------------|
| question_order     | Selection | Order of questions: `sequential` / `random`     |
| allow_navigation   | Boolean   | Whether user can go back to previous questions  |
| show_progress      | Boolean   | Show question progress tracker in UI            |

---

### 📜 Selection Field: `question_order`
```python
[
  ('sequential', 'In Order'),
  ('random', 'Randomized')
]

🧾 Admin UI Changes

    In quiz form view:

        Add question_order selection with tooltip: "Choose how questions appear to the user"

        Add checkbox for allow_navigation

        Add checkbox for show_progress

🧠 Frontend Behavior (for later)

    The following UI behaviors are planned, not built in this sprint.

Navigation

    If allow_navigation is enabled, user can:

        See "Next" and "Previous" buttons

        Jump to any question using progress tracker (like pagination)

Randomization

    If question_order == random, questions must be shuffled once per attempt

    Preserve this order in attempt metadata

Progress Tracker

    Shown only if show_progress is enabled

    Display “Question X of Y” or progress bar

🧪 Deliverables

New fields added to quiz.quiz

Updated views for configuration in admin

No logic for shuffling, navigating, or tracking yet (planned in Sprint 3)

    No frontend changes or templates yet

🔁 Future Sprints This Enables

    Sprint 3: Question Rendering & Timer UI

    Sprint 5: Store navigation & randomized order in attempt records

    Sprint 7: Adaptive Quiz Logic (score-based branching)