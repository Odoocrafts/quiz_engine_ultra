# 🧠 Sprint 9 – Smart Recommendations + Personalized Learning Hints | quiz_engine_pro

---

## 🎯 Goal

Provide users with meaningful insights and actionable feedback based on their quiz performance. Suggest specific topics to review and generate personalized learning hints.

---

## 📦 Backend – Model Enhancements

### `quiz.question` – Add fields

| Field         | Type    | Description                              |
|--------------|---------|------------------------------------------|
| topic_tag     | Char    | Logical tag (e.g. 'Math-Algebra')         |
| explanation   | Html    | Shown post-submission in review screen    |

### `quiz.attempt` – New computed fields (or JSON blob)

- `weak_topics_json`: Store tags of topics where user consistently scores low

---

## 🧠 Recommendation Logic

- After quiz is submitted:
  - Group answers by `topic_tag`
  - Calculate accuracy per tag
  - Identify weak areas (e.g., <50% correct in a tag)
  - Save these to `weak_topics_json` in attempt

---

## 🖼️ Result Page Enhancements

- Section: **“Your Focus Areas”**
  - List weak topics with a short message:
    - “You missed 3/5 questions in Algebra. Review recommended.”
- Section: **“What You Did Well”**
  - List strong areas too (optional)

### For each weak topic:
- Show:
  - Tag name
  - Number of correct vs total
  - Link to a future learning module (v2)
  - Sample questions (if enabled)

---

## 🔁 Frontend Components

- Result screen cards:
  - 🔴 Red tag = Weak
  - 🟢 Green tag = Strong
- Optional: Tooltip on explanation per question (from `question.explanation`)

---

## 📤 Export (Optional for Sprint 10)

- JSON or PDF export of focus areas + review checklist

---

## 🧪 Deliverables

- [x] Auto-generated weak topic mapping post-quiz
- [x] “Focus Areas” UI block on result screen
- [x] Explanation per question available in review
- [ ] No content recommendations yet (future LMS link)

---

## 🔁 Future Sprints This Enables

- Sprint 10: PDF Reports + Leaderboards + Animations
- Sprint 11+: Link with LMS (based on weak topics)

---
