@echo off
echo ========================================================
echo   Smart Media Organizer - DaVinci Resolve Installer
echo ========================================================
echo.

set "TARGET_DIR=%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility"

if not exist "%TARGET_DIR%" (
    echo [INFO] Creando directorio de destino...
    mkdir "%TARGET_DIR%" 2>nul
)

copy /Y "%~dp0SmartMediaOrganizer.py" "%TARGET_DIR%\SmartMediaOrganizer.py" >nul

if %ERRORLEVEL% EQU 0 (
    echo [OK] Instalacion completada con exito!
    echo.
    echo El script ya esta disponible en DaVinci Resolve:
    echo   Workspace ^> Scripts ^> SmartMediaOrganizer
    echo.
) else (
    echo [ERROR] No se pudo copiar el archivo. Verifica los permisos.
)

pause
