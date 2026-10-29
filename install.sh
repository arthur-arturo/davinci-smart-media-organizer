#!/usr/bin/env bash
# Smart Media Organizer - Installer for macOS & Linux

echo "========================================================"
echo "  Smart Media Organizer - DaVinci Resolve Installer"
echo "========================================================"
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    TARGET_DIR="$HOME/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility"
else
    TARGET_DIR="$HOME/.local/share/DaVinciResolve/Fusion/Scripts/Utility"
fi

mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -f "$SCRIPT_DIR/SmartMediaOrganizer.py" "$TARGET_DIR/SmartMediaOrganizer.py"

if [ $? -eq 0 ]; then
    echo "[OK] Instalación completada con éxito!"
    echo "Disponible en DaVinci Resolve:"
    echo "  Workspace -> Scripts -> SmartMediaOrganizer"
else
    echo "[ERROR] Falló la instalación."
fi
