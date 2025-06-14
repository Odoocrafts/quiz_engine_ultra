# 🧠 Sprint 6 – Admin Reporting & Analytics Dashboard | quiz_engine_pro

---

## 🎯 Goal

Equip administrators with a powerful dashboard to monitor quiz performance, analyze attempt trends, and gain insight into question effectiveness.

---

## 📊 Backend – Data Points to Track

Use existing models: `quiz.quiz`, `quiz.attempt`, `quiz.user_answer`, `quiz.question`

---

## 📈 Key Metrics to Show

### Quiz-Level Stats:
- Total Attempts
- Average Score
- Pass Rate (%)
- Attempt Frequency (last 7 days)
- Top 5 scorers (name + score)

### Question-Level Stats:
- Question text
- Accuracy rate (% of users who got it right)
- Avg. score
- Flag as “tricky” if <40% accuracy

---

## 🖼️ Frontend – Admin Dashboard UI

### Route:
`/quiz/admin_dashboard`

### Template: `admin_dashboard.html`

### Sections:

#### 1. Quiz Overview
- Dropdown to select quiz
- Shows attempt count, avg score, pass rate

#### 2. Performance Graphs
- Bar chart: Score distribution (0–100%)
- Line graph: Attempts over time
- Pie chart: Pass vs Fail

#### 3. Question Effectiveness Table
| Question | Accuracy % | Attempts | Avg Score | Flag |
|----------|------------|----------|-----------|------|

#### 4. Export Options
- Export to Excel or PDF
- Optional: send report to mentor via email

---

## 📦 Libraries / Stack (Optional for future)

- Use `plotly` or `chart.js` in templates
- Use Odoo built-in graph views if preferred

---

## 🧪 Deliverables

- [x] Backend methods for analytics (aggregated queries)
- [x] Controller and dashboard template
- [x] Graph placeholders (can use static data for now)
- [ ] Live charts can be built in future sprints

---

## 🔁 Future Sprints This Enables

- Sprint 7: Advanced Filters & Date Range Controls
- Sprint 8: AI Suggestion Engine (e.g. flag weak areas)
- Sprint 9: Real-time Monitoring for live exams

---