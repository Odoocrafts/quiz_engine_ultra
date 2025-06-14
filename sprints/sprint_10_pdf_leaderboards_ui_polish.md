# 🧠 Sprint 10 – PDF Reports, Leaderboards & Visual Enhancements | quiz_engine_pro

---

## 🎯 Goal

Deliver a polished user experience with visual refinements, exportable PDF reports, and gamified elements like leaderboards to drive engagement.

---

## 📦 Backend – Additions

### `quiz.quiz` – Add fields

| Field         | Type      | Description                               |
|--------------|-----------|-------------------------------------------|
| enable_leaderboard | Boolean   | Show leaderboard for this quiz          |

---

### New Route: `/quiz/pdf_report/<attempt_id>`

- Generates a PDF of:
  - Quiz title & user info
  - Score summary
  - Focus areas (from Sprint 9)
  - Question-wise breakdown (optional)
  - Pass/fail badge

> Use Odoo `report_qweb_pdf` or wkhtmltopdf engine.

---

### New Model: `quiz.leaderboard_view` (PostgreSQL View / Read-only Model)

Fields:
- quiz_id
- user_name
- total_score
- attempt_time
- rank (calculated via SQL `ROW_NUMBER()`)

---

## 🖼️ Frontend – Final Touches

### Result Page:

- Add “📄 Download PDF” button
- Add “🏆 View Leaderboard” button if `enable_leaderboard` is true

### Leaderboard Page:

- Route: `/quiz/leaderboard/<quiz_id>`
- Table of top 10 scorers:
  - Name, Score, Time Taken, Rank

### Visual Tweaks:

- Use Tailwind / Bootstrap for clean quiz UI
- Add smooth transitions between questions
- Add timer animation (circle countdown)
- Mobile responsiveness for quiz and result views

---

## 🎨 UX Enhancements (Optional)

- Confetti animation for passed attempts 🎉
- Custom avatar badges per rank (e.g. Gold, Silver, Bronze)
- Animation for loading next question

---

## 🧪 Deliverables

- [x] Leaderboard table (dynamic)
- [x] PDF report route & template
- [x] Final UI polish (mobile-first layout)
- [ ] No LMS integration yet
- [ ] No push/email notifications (future sprint)

---

## 🔁 Future Sprints (Post-MVP)

- Sprint 11+: LMS Learning Path Integration
- Sprint 12+: Push Notifications, Email Results
- Sprint 13+: SCORM/xAPI Export

---
