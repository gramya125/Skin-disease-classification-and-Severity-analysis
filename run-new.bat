@echo off
echo ========================================
echo Skin Disease API - Start Backend ^& Frontend
echo ========================================
echo [1/6] Checking Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python 3.10+ required. Download from python.org
    pause
    exit /b 1
)

echo [2/6] Setup/Activate venv...
if not exist venv (
    echo Creating venv...
    python -m venv venv
)
call venv\Scripts\activate.bat
echo Python in venv: %VIRTUAL_ENV%

echo [3/6] TensorFlow Note: Install Visual C++ Redist 2015-2022 (x64) if TF fails: https://aka.ms/vs/17/release/vc_redist.x64.exe

echo [4/6] Install deps (stable versions)...
pip install --upgrade pip
pip install -r api\requirements.txt --no-deps --find-links https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-2.17.0-cp312-cp312-win_amd64.whl
if %errorlevel% neq 0 (
    echo ERROR: pip install failed. Try manual: pip install -r api/requirements.txt
    echo Note: tensorflow requires VC++ Redist if DLL error.
    pause
    exit /b 1
)

echo [5/6] Starting API server...
echo Open: http://localhost:8000/docs ^| http://localhost:8000/health
pushd api
start cmd /k "uvicorn main:app --reload --host 0.0.0.0 --port 8000"
timeout /t 3 >nul

echo [6/6] Testing health...
curl -s http://localhost:8000/health || echo "Health check failed - check logs above"

echo Opening frontend...
start "" "..\frontend\index.html"
popd

echo ========================================
echo Backend running ^| Frontend open ^| Press any key to exit this script.
pause >nul
