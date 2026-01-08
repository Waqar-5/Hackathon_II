---
id: 2
title: Console Todo App Spec
stage: spec
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-console-todo-app
branch: main
user: user
command: /sp.specify
labels: [spec, todo-app, console, python]
links:
  spec: specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-console-todo-app/spec.md
 - specs/001-console-todo-app/checklists/requirements.md
tests:
 - none
---

## Prompt

```
Phase I – In-Memory Python Console Todo App

Target audience:
- Python learners and reviewers of agentic workflows

Objective:
- Build a CLI-based Todo app storing all data in memory
- Demonstrate Agentic Dev Stack usage (spec → plan → tasks → implement)

Required features:
- Add todo
- View todos
- Update todo
- Delete todo
- Mark todo as complete

Success criteria:
- All 5 features work correctly in the terminal
- In-memory state only (no files, no DB)
- Clean, readable Python code with proper project structure
- Fully generated via Claude Code (no manual coding)

Constraints:
- Python 3.13+
- Tooling: UV
- Console-only application

Not building:
- Persistence, web UI, APIs, AI features, or cloud setup
```

## Response snapshot

Created a comprehensive specification for the in-memory Python console todo app with user scenarios, functional requirements, and success criteria.

## Outcome

- ✅ Impact: Defined complete feature specification with 5 user stories and functional requirements
- 🧪 Tests: none
- 📁 Files: specs/001-console-todo-app/spec.md, specs/001-console-todo-app/checklists/requirements.md
- 🔁 Next prompts: Feature planning with /sp.plan
- 🧠 Reflection: Specification covers all required features with clear acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A