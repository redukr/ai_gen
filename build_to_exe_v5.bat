@echo off
setlocal

REM ======================
REM   Build EXE
REM ======================

echo Building EXE with PyInstaller...
echo.

REM Remove old build/dist
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Run PyInstaller
venv\Scripts\pyinstaller.exe --onefile --windowed app.py --paths=generator --paths=tools

echo.
echo ============================
echo        BUILD DONE
echo ============================
echo Output EXE is in: dist\app.exe
echo.

pause
