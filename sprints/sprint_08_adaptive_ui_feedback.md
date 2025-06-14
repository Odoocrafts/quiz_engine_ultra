# 🧠 Sprint 8 – Adaptive UI Flow + Difficulty-Based Feedback | quiz_engine_pro

---

## 🎯 Goal

Implement the frontend flow for adaptive quizzes: dynamically load questions based on difficulty logic, visually indicate the level of difficulty, and give tailored feedback at the end.

---

## ⚙️ Frontend Behavior (Adaptive Mode)

If `quiz.is_adaptive == True`, apply this logic:

### Quiz Start
- Begin with a `medium` difficulty question
- Render difficulty indicator (e.g., badge: “Medium”)

### After Each Question
- Use JS to POST the answer to `/quiz/submit_question`
- Backend returns:
  - Whether answer was correct
  - Next question to show (based on difficulty scaling)
- Replace question without full page reload (AJAX)
- Timer continues normally

---

## 🧩 UI Components

- **Difficulty Badge**: Display “Easy”, “Medium”, or “Hard” on each question
- **Progress Trail**:
  - Dots representing each answered question
  - Color-coded by difficulty
- **End Feedback Summary**:
  - Breakdown of:
    - % correct at each difficulty level
    - Final score
    - Suggested action (e.g. “Focus on hard questions”)

---

## 🔁 Frontend Updates Needed

- `question_screen.html`:
  - Add difficulty tag
  - Use AJAX to submit + receive next question
- JS file:
  - Adaptive logic controller
  - Timer preservation across question transitions
- Result page:
  - Show adaptive trail summary using `attempt.adaptive_path_json`

---

## 📦 Backend – API Adjustments

Update `/quiz/submit_question` to:
- Return `next_question_id` and `difficulty`
- Save `adaptive_path_json` as a list of question IDs + difficulty + correctness

---

## 🧪 Deliverables

- [x] Difficulty-based UI badges
- [x] AJAX-based dynamic question loading
- [x] Adaptive logic JS on frontend
- [x] Adaptive path visualization in results
- [ ] Optional: animations and polish reserved for Sprint 10

---

## 🔁 Future Sprints This Enables

- Sprint 9: Smart Recommendations based on past attempts
- Sprint 10: Animated UI, Leaderboards, PDF result report

---
