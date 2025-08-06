@echo off
:: Set console title
title Factory KD Dropper

:: Optional: change text color (e.g. bright cyan)
color 0b

:: Display cool ASCII art or text
echo ================================
echo    Factory KD Dropper v1.0
echo ================================
echo.

:: Pause briefly so user sees the message
timeout /t 2 /nobreak >nul

:: Run your Python script
python kddrop.py

:: Pause at the end so window stays open after script finishes
pause
