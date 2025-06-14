# 🧠 Sprint 5 – User Answer Review Screen | quiz_engine_pro

---

## 🎯 Goal

Allow users to review their submitted answers after completing a quiz attempt. This feature boosts learning by showing correct answers alongside the user's selections.

---

## 📦 Backend – Enhancements

Use existing model: `quiz.user_answer`  
(No new models required in this sprint.)

Ensure `quiz.user_answer` includes:
- Reference to question
- User's answer (`selected_ids`, `text_answer`)
- `score_awarded`
- Correct options (linked via `quiz.answer`)

---

## 🖼️ Frontend – Answer Review View

### Route:
`/quiz/review/<int:attempt_id>`

### Template: `review_screen.html`

### For each question:
- Show:
  - Question text
  - User’s selected answer(s)
  - Correct answer(s)
  - Explanation (if available in question)
  - Score awarded
- Visual cues:
  - ✅ Correct answer (green check)
  - ❌ Wrong answer (red X)
  - 🟡 Partial credit (if applicable)

### Bottom summary:
- Total score
- Number of correct/wrong/partial answers
- "Back to dashboard" button (optional)

---

## 🧠 Configurations / UX Notes

- Only show review **after submission**
- Disable all inputs – this is view-only
- Optionally: allow toggling “Show correct answers” (future enhancement)

---

## 🧪 Deliverables

- [x] `/quiz/review/<attempt_id>` route and controller
- [x] Loop through all `quiz.user_answer` entries
- [x] Render comparison with correct answers
- [ ] No styling polish yet
- [ ] No retry or learning path suggestions (coming later)

---

## 🔁 Future Sprints This Enables

- Sprint 6: Admin-side Reporting & Quiz Analytics
- Sprint 7: Retry options / learning mode toggle
- Sprint 8: Export results to PDF / share with mentor

---