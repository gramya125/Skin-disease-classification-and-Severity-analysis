# Skin Disease Detection - Backend ^& Frontend

## Quick Start
Double-click `run-new.bat`:
- Creates/uses `venv/`
- Installs stable deps (TF 2.15.0)
- Starts API: http://localhost:8000/docs ^| /health
- Opens frontend HTML

**Windows TF Note:** If install fails, get VC++ Redist: https://aka.ms/vs/17/release/vc_redist.x64.exe

## Features
- CNN disease classification
- Severity (early/mild/severe) via PCA/KMeans
- Drag-drop frontend, confidence %
- Robust: Logs errors, partial models OK

## Test
1. `run-new.bat`
2. Upload skin image in browser
3. Check /health JSON

## Development
- Edit api/main.py
- `uvicorn api.main:app --reload` from api/
- Frontend static, edit JS/CSS

Fixed: Model paths, TF compat, venv, logs, safety checks.

Enjoy!
