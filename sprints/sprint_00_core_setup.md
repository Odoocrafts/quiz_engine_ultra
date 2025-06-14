# 🧠 Sprint 0 – Core Setup | quiz_engine_pro

---

## 🎯 Goal

Establish the foundational backend structure for the `quiz_engine_pro` module. This includes core models (`quiz.quiz`, `quiz.question`, `quiz.answer`), admin views, and a basic menu system. No quiz logic, frontend UI, or evaluation flow is implemented in this sprint.

---

## 📦 Models

### `quiz.quiz`
| Field             | Type      | Description                             |
|------------------|-----------|-----------------------------------------|
| name             | Char      | Name of the quiz                        |
| description      | Text      | Rich text/Markdown-safe description     |
| active           | Boolean   | Archive support                         |
| question_ids     | One2many  | Link to `quiz.question`                 |
| type             | Selection | `practice` / `test`                     |
| attempts_allowed | Integer   | Max attempts (0 = unlimited)            |

---

### `quiz.question`
| Field          | Type      | Description                                |
|---------------|-----------|--------------------------------------------|
| quiz_id       | Many2one  | Link to `quiz.quiz`                        |
| name          | Char      | Title / question label                     |
| question_text | Text      | HTML-supported question body               |
| question_type | Selection | Placeholder types: `mcq`, `text`, `fill_blank`, `drag_order` |
| answer_ids    | One2many  | Link to `quiz.answer`                      |
| sequence      | Integer   | Question order in quiz                     |

---

### `quiz.answer`
| Field         | Type     | Description                         |
|--------------|----------|-------------------------------------|
| question_id  | Many2one | Link to `quiz.question`             |
| answer_text  | Text     | The answer content                  |
| is_correct   | Boolean  | Whether it is the correct option    |
| score        | Float    | Score awarded if this is selected   |

---

## 🧾 Admin UI Views

- Tree/form views for `quiz.quiz`, `quiz.question`, `quiz.answer`
- Use embedded One2manys where appropriate
- Top-level menu: **Quiz Engine**
  - Submenus: Quizzes, (Questions only within Quiz), (Answers as inline)
- i18n-ready field and menu labels

---

## 🧪 Deliverables

- [x] `models/quiz.py` with all 3 core models
- [x] `views/quiz_views.xml` with tree/form views
- [x] Menu items under `quiz_engine.menu_root`
- [x] Init and manifest files
- [x] Access rule placeholder (`ir.model.access.csv`)
- [ ] No frontend/public views yet
- [ ] No quiz logic, validation, or scoring

---

## 🧠 Notes

- Designed to scale with future question types
- Clean field naming for maintainability
- Kept flexible for future frontend API exposure

---

