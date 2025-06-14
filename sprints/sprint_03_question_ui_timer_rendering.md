# 🧠 Sprint 3 – Question Rendering, Timer UI & Instruction Screen | quiz_engine_pro

---

## 🎯 Goal

Start building the quiz frontend UI (Odoo controller & templates) for rendering questions dynamically, managing timers, and displaying the instruction screen before quiz start.

---

## ⚙️ Functional Scope

- Render the instruction screen from `quiz.quiz.instruction_text`
- Start quiz on user action (e.g., “Start Quiz” button)
- Render first question (with sequence or randomized order)
- Implement global and per-question timers (basic JS)
- Enable next/previous navigation if `allow_navigation` is enabled
- Show progress indicator if `show_progress` is enabled

---

## 📦 Backend Tasks

### 🗂️ Add New Model: `quiz.attempt`
Tracks each user’s attempt for a quiz.

| Field               | Type      | Description                                  |
|--------------------|-----------|----------------------------------------------|
| quiz_id            | Many2one  | The quiz being attempted                     |
| user_id            | Many2one  | The user taking the quiz                     |
| started_at         | Datetime  | Start time                                   |
| ended_at           | Datetime  | End time                                     |
| question_order     | JSON      | Ordered question ID list (to support random) |
| current_question_id| Many2one  | Tracks where user is currently at            |
| time_left          | Integer   | Remaining time (global mode)                 |

---

## 🧾 Controller & Routes

- `/quiz/start/<int:quiz_id>`  
  → Loads instruction screen, handles pre-validation

- `/quiz/attempt/<int:attempt_id>`  
  → Loads quiz UI with first or current question

- `/quiz/submit_question` (POST)  
  → Temporarily store answer, move to next question

- `/quiz/submit`  
  → Final submission

---

## 🖼️ Templates / Frontend (Basic)

- instruction_screen.html
- question_screen.html
- components:
  - timer.html (shows countdown)
  - progress_bar.html
  - next_prev_buttons.html

---

## 🧠 JS Features (Basic)

- Timer countdowns:
  - Global: visible across all questions
  - Per-question: resets every question
- Auto-submit on timer expiry (if enabled)

---

## 🧪 Deliverables

- [x] Instruction screen renders via controller
- [x] Basic question rendering with timer
- [x] Navigation works based on config
- [ ] No answer evaluation yet
- [ ] No styling or JS frameworks yet

---

## 🔁 Future Sprints This Enables

- Sprint 4: Answer Evaluation & Result Storage
- Sprint 6: Frontend polish (Vue, Tailwind, Drag-drop)
- Sprint 7: Analytics dashboard for admin

---