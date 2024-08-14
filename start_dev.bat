@echo off

REM Start the FastAPI middleware using Uvicorn in a new window
start cmd /k "call .venv\Scripts\activate && uvicorn backend.main:app --reload"

REM Start the Vue.js frontend using Vite in a new window
start cmd /k "cd frontend && npm run dev"

REM Prevent the command prompt from closing immediately
pause
