# 🎬 Smart Media Organizer for DaVinci Resolve

**Smart Media Organizer** is an interactive, native dark-themed utility script for **DaVinci Resolve (Free & Studio)** that automatically sorts loose clips from the root Media Pool into structured, customizable bins in a single click.

Works on **Windows, macOS, and Linux** with **DaVinci Resolve 18, 19, and 21+**.

---

## ✨ Features

- 🎯 **Non-Destructive & Timeline-Safe:** Clips already in timelines stay 100% connected. Resolve identifies clips by unique media IDs, not bin paths.
- 🗂️ **Customizable Rules:** Add, remove, or edit folder names, assigned extensions, and clip colors.
- 📐 **Social Media Ready (Smart Orientation Sub-Sorting):** Automatically separates videos into `Verticales (9:16)` for Reels/TikTok/Shorts and `Horizontales (16:9)` for YouTube when both formats are mixed.
- 🎨 **Clip Color Tags:** Automatically applies clip colors in the Media Pool (Orange, Teal, Blue, Green, etc.).
- 🛡️ **Zero Empty Folders:** Only creates bins if matching media is present.
- 🔒 **Safe Scope:** Only sorts loose items in the root (*Master*) folder — existing custom folders are never touched.
- 💻 **Native UI:** Clean dark-mode interface built directly with DaVinci Resolve's Fusion UIManager (no external dependencies or pip packages required).

---

## 🚀 Quick Installation

### Windows (1-Click)
1. Clone or download this repository.
2. Double-click `install.bat`.
3. Open or restart DaVinci Resolve.

### macOS & Linux (1-Click)
1. Run in terminal:
   ```bash
   chmod +x install.sh && ./install.sh
   ```
2. Restart DaVinci Resolve.

### Manual Installation
Copy `SmartMediaOrganizer.py` to your DaVinci Resolve `Scripts/Utility` folder:

- **Windows:** `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\`
- **macOS:** `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/`
- **Linux:** `~/.local/share/DaVinciResolve/Fusion/Scripts/Utility/`

---

## 🕹️ How to Use

1. Open your project in DaVinci Resolve.
2. Go to the top menu:
   $$\text{Workspace} \longrightarrow \text{Scripts} \longrightarrow \textbf{SmartMediaOrganizer}$$
3. Customize your rules (optional):
   - Select any rule to edit its folder name, extensions, or color.
   - Click **+ Nueva Regla** to add custom categories (e.g. `VISUAL` with `.mp4 .png .jpg`).
4. Click **▶ ORGANIZAR MEDIA POOL**.
5. Done! Your Media Pool is neatly organized.

---

## 📁 Default Structure

| Bin Created | Recognized Formats | Color |
| :--- | :--- | :--- |
| `01_VIDEOS` | `.mp4` `.mov` `.mkv` `.avi` `.mxf` `.webm` `.m4v` `.mpg` `.wmv` `.flv` `.ts` `.r3d` `.braw` *(with auto 9:16 vs 16:9 sub-folders)* | Teal |
| `02_AUDIO` | `.mp3` `.wav` `.aac` `.m4a` `.flac` `.ogg` `.wma` `.aiff` `.aif` `.opus` | Blue |
| `03_IMAGENES` | `.png` `.jpg` `.jpeg` `.tiff` `.tif` `.bmp` `.webp` `.psd` `.exr` `.dpx` `.svg` | Green |
| `04_TIMELINES` | Auto-detects timeline assets | Orange |
| `99_OTROS` | *(Optional checkbox)* Unmatched files | (none) |

---

## ⌨️ Assign a Keyboard Shortcut

You can assign a hotkey (e.g. `Ctrl + Alt + O` / `Cmd + Option + O`):
1. In DaVinci Resolve, go to **Keyboard Customization** (`Ctrl + Alt + K`).
2. Search for `SmartMediaOrganizer`.
3. Assign your preferred shortcut and save.

---

## 📄 License

Distributed under the [MIT License](LICENSE).
Created with ❤️ for video editors and content creators.
