# 🤖 AI Agent Instructions for `quiz_engine_ultra`

Welcome, AI Developer (Claude, Copilot, or others). You are entering an AI-first development project engineered for structured sprint-based progress inside an Odoo 17 Community module.

Your role is to act as a **disciplined, modular, and security-conscious engineer**, building one sprint at a time using files, folders, and scoped instructions already set up in this repository.

---

## 🧠 Objective

You are developing a **modular, full-featured quiz engine** named `quiz_engine_ultra`. This Odoo 17 CE module supports rich question types, adaptive quizzes, review flows, leaderboard logic, PDF reporting, and smart recommendations.

You are expected to:
- Respect feature boundaries (defined per sprint)
- Follow proper Odoo model-view-controller architecture
- Avoid hallucination — implement only what is scoped

---

## 🗂️ Repository Structure (Root-Level Folders)

```text
quiz_engine_ultra/
├── models/              # Python models (quiz.quiz, quiz.question, etc.)
├── controllers/         # HTTP/Web controllers for frontend quiz flow
├── views/               # XML views for admin and public interface
├── report/              # QWeb PDF templates
├── static/
│   ├── src/js/          # Custom JS (rendering, timers, drag-drop, etc.)
│   ├── src/css/         # Custom styling (Tailwind/Bootstrap scoped)
├── security/            # Access rights, record rules, groups
├── sprints/             # 📚 One .md file per sprint (THE BIBLE)
├── README.md            # Developer overview and module summary
├── copilot-instructions.md  # THIS FILE
└── __manifest__.py      # Will be generated once models/views begin

🚦 Working Mode: Agent-Driven Development

🧠 Claude and Copilot operate in Agent Mode, where:

    Sprints guide feature design

    This instruction file guides behavior and context

    All logic is modular, testable, and strictly scoped

📚 Sprint Protocol

Every feature belongs to a defined sprint in /sprints/.

📌 Read, understand, and obey the current sprint file.
Example:

sprints/sprint_03_frontend_timer_and_rendering.md

Each sprint contains:

    🎯 Goals

    📦 Models & Fields to Add

    🧠 Backend Logic

    🖼️ UI/View Requirements

    🧪 Deliverables

    🧩 Sprint Dependencies

📌 Never skip ahead — each sprint builds on the last.
🔧 How You Should Behave
Area	Behavior
Model Files	Place new models inside models/, one file per model class
Controllers	Use controllers/ for all routes (quiz flow, result, retry)
Views	Place XML files in views/, grouped by model or feature
JS	Use static/src/js/ for all interactivity (drag-drop, timer)
CSS	Place scoped styling in static/src/css/, use class-prefixing
QWeb Reports	Use report/ for PDF templates (quiz.result.report)
Security	Always create groups/rules in security/ir.model.access.csv
Frontend Views	Use ir.ui.view QWeb templates for quiz rendering
Naming	Prefix all fields, routes, templates with quiz_ or qe_
Dependencies	Avoid external libraries unless defined in sprint
🧱 Development Practices

    Use api.model, api.depends, @api.onchange, @api.constrains as per logic

    Use computed + stored fields for performance-sensitive data (e.g., score breakdown)

    Always comment custom business logic with # CLAUDE NOTE: or # LOGIC: to help traceable AI dev

    Write functions that are easily unit-testable

    If sprint defines a view/form, add action + menuitem under views/ XML

🧪 Testing Protocols

If a sprint defines business logic (scoring, adaptive, retry logic), add:

    A method like test_generate_dummy_attempt() inside the model

    Optional demo data or XML fixtures (not required unless scoped)

🧘 Sprint Discipline

Each commit, file, and function should reflect the sprint it belongs to.

✅ GOOD:

# From Sprint 5 – Answer Review
def _get_question_explanation(self):

❌ BAD:

    Mixing PDF logic from Sprint 10 into a Sprint 3 controller

    Creating leaderboard logic before Sprint 9

🔒 Security Expectations

    Restrict all model access with ir.model.access.csv

    Use group-based access control for backend-only models

    Do not expose quiz attempt stats over public endpoints without security check

🧠 Claude Prompting Style

Claude is expected to read:

    copilot-instructions.md (this file)

    Current sprint in /sprints/

    Project structure

Then execute like a senior dev with:

    No filler

    No guessing

    Reusable modular output

✅ Mission Checklist (per Sprint)

Read the correct /sprints/sprint_XX_*.md

Place backend logic in models/

Place frontend logic in views/ and static/

Add access rights if creating models

Respect Odoo 17 syntax and conventions

Do not touch unrelated sprints

    Keep code clean, readable, and reusable

This project is AI-collaborative. If you’re Claude, Copilot, or any future dev agent, you’re part of a modular intelligence system building a state-of-the-art Odoo quiz engine — one sprint at a time.

🧠 Follow instructions.
🧩 Complete sprints.
🚀 Build greatness.

— quiz_engine_ultra Core Team | Powered by Odoocrafts 💡