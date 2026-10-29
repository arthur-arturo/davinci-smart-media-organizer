#!/usr/bin/env python3
"""
Smart Media Organizer v2.5 — DaVinci Resolve (Free & Studio)
=============================================================
Professional, modern dark-themed media sorter with customizable rules.
Designed to look and feel like a native DaVinci Resolve tool.

Author:  Antigravity AI
Version: 2.5.0
License: MIT
"""

# ═══════════════════════════════════════════════════════════════════════════
#  DEFAULT RULES & OPTIONS
# ═══════════════════════════════════════════════════════════════════════════

DEFAULT_RULES = [
    {
        "folder":     "01_VIDEOS",
        "extensions": ".mp4 .mov .mkv .avi .mxf .webm .m4v .mpg .wmv .flv .ts .r3d .braw",
        "color":      "Teal",
    },
    {
        "folder":     "02_AUDIO",
        "extensions": ".mp3 .wav .aac .m4a .flac .ogg .wma .aiff .aif .opus",
        "color":      "Blue",
    },
    {
        "folder":     "03_IMAGENES",
        "extensions": ".png .jpg .jpeg .tiff .tif .bmp .webp .psd .exr .dpx .svg",
        "color":      "Green",
    },
    {
        "folder":     "04_TIMELINES",
        "extensions": "",          # Timelines are detected automatically by type
        "color":      "Orange",
    },
]

AVAILABLE_COLORS = [
    "(ninguno)", "Orange", "Apricot", "Yellow", "Lime", "Olive",
    "Green", "Teal", "Navy", "Blue", "Purple", "Violet",
    "Pink", "Tan", "Beige", "Brown", "Chocolate",
]

# ═══════════════════════════════════════════════════════════════════════════
#  MODERN DAVINCI RESOLVE DARK THEME (QSS)
# ═══════════════════════════════════════════════════════════════════════════

DARK_STYLE = """
/* Base Window & Text */
QWidget {
    background-color: #1a1a1a;
    color: #c8c8c8;
    font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
    font-size: 12px;
}

/* Secondary / Standard Buttons */
QPushButton {
    background-color: #2b2b2b;
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    padding: 6px 14px;
    color: #e2e2e2;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #383838;
    border-color: #505050;
    color: #ffffff;
}
QPushButton:pressed {
    background-color: #1f1f1f;
    border-color: #2b2b2b;
}

/* Primary Action Button (Resolve Accent Blue) */
QPushButton#OrganizeBtn {
    background-color: #1976d2;
    border: 1px solid #2196f3;
    border-radius: 4px;
    color: #ffffff;
    font-weight: bold;
    font-size: 12px;
    padding: 8px 22px;
}
QPushButton#OrganizeBtn:hover {
    background-color: #2196f3;
    border-color: #64b5f6;
}
QPushButton#OrganizeBtn:pressed {
    background-color: #1565c0;
}

/* Save / Apply Button */
QPushButton#ApplyEditBtn {
    background-color: #2a5298;
    border: 1px solid #3b6cb5;
    border-radius: 4px;
    color: #ffffff;
    font-weight: 600;
    padding: 6px 14px;
}
QPushButton#ApplyEditBtn:hover {
    background-color: #3b6cb5;
}

/* Tool Buttons (Add / Remove) */
QPushButton#AddRuleBtn {
    background-color: #232d24;
    border: 1px solid #365038;
    color: #9cd4a0;
    border-radius: 4px;
    padding: 5px 12px;
}
QPushButton#AddRuleBtn:hover {
    background-color: #2b392d;
    border-color: #4a6f4d;
    color: #bbf0bf;
}
QPushButton#RemoveRuleBtn {
    background-color: #302222;
    border: 1px solid #523535;
    color: #d49c9c;
    border-radius: 4px;
    padding: 5px 12px;
}
QPushButton#RemoveRuleBtn:hover {
    background-color: #3c2a2a;
    border-color: #6d4444;
    color: #f0bbbb;
}
QPushButton#ResetBtn {
    background-color: transparent;
    border: 1px solid #333333;
    color: #888888;
    border-radius: 4px;
    padding: 5px 12px;
}
QPushButton#ResetBtn:hover {
    background-color: #262626;
    color: #cccccc;
    border-color: #444444;
}

/* Input Fields & ComboBox */
QLineEdit, QComboBox {
    background-color: #121212;
    border: 1px solid #363636;
    border-radius: 4px;
    padding: 6px 8px;
    color: #ffffff;
    selection-background-color: #1976d2;
}
QLineEdit:focus, QComboBox:focus {
    border-color: #1976d2;
    background-color: #141414;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 22px;
    border-left: 1px solid #303030;
}
QComboBox QAbstractItemView {
    background-color: #181818;
    color: #ffffff;
    border: 1px solid #3c3c3c;
    selection-background-color: #1976d2;
    padding: 4px;
}

/* Rules Tree / Table */
QHeaderView::section {
    background-color: #202020;
    color: #888888;
    padding: 6px 10px;
    border: none;
    border-right: 1px solid #2d2d2d;
    border-bottom: 1px solid #2d2d2d;
    font-weight: 600;
    font-size: 11px;
    letter-spacing: 0.5px;
}
QTreeWidget {
    background-color: #141414;
    alternate-background-color: #181818;
    border: 1px solid #2d2d2d;
    border-radius: 5px;
    outline: none;
}
QTreeWidget::item {
    padding: 6px 8px;
    border-bottom: 1px solid #1f1f1f;
    color: #d8d8d8;
}
QTreeWidget::item:selected {
    background-color: #1976d2;
    color: #ffffff;
}
QTreeWidget::item:hover:!selected {
    background-color: #232323;
}

/* Checkboxes */
QCheckBox {
    spacing: 8px;
    color: #b0b0b0;
    font-size: 12px;
}
QCheckBox::indicator {
    width: 15px;
    height: 15px;
    background-color: #141414;
    border: 1px solid #444444;
    border-radius: 3px;
}
QCheckBox::indicator:hover {
    border-color: #666666;
}
QCheckBox::indicator:checked {
    background-color: #1976d2;
    border-color: #2196f3;
}

/* Status Bar Pill */
QLabel#StatusPill {
    background-color: #202020;
    border: 1px solid #2e2e2e;
    border-radius: 4px;
    padding: 6px 12px;
    font-size: 11px;
    color: #999999;
}
"""


# ═══════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def get_extension(file_name):
    """Return lowercase extension including the dot."""
    idx = file_name.rfind(".")
    if idx == -1:
        return ""
    return file_name[idx:].lower()


def parse_extensions(ext_string):
    """Parse a space-separated extension string into a clean set."""
    result = set()
    for token in ext_string.strip().split():
        token = token.strip().lower()
        if not token:
            continue
        if not token.startswith("."):
            token = "." + token
        result.add(token)
    return result


def get_or_create_subfolder(media_pool, parent_folder, name):
    """Find an existing subfolder by name, or create it."""
    for sub in parent_folder.GetSubFolderList():
        if sub.GetName() == name:
            return sub
    return media_pool.AddSubFolder(parent_folder, name)


# ═══════════════════════════════════════════════════════════════════════════
#  ORGANIZER ENGINE
# ═══════════════════════════════════════════════════════════════════════════

def run_organizer(resolve_obj, rules, sort_orientation, create_other_folder):
    """
    Execute the media organization based on user-defined rules.
    """
    proj = resolve_obj.GetProjectManager().GetCurrentProject()
    if proj is None:
        return {"error": "No hay un proyecto abierto en DaVinci Resolve."}

    media_pool = proj.GetMediaPool()
    root_folder = media_pool.GetRootFolder()
    clips = root_folder.GetClipList()

    if not clips:
        return {"error": "El Media Pool raíz está vacío. No hay clips sueltos que organizar."}

    # Build extension → rule index mapping
    ext_map = {}
    timeline_rule = -1

    for i, rule in enumerate(rules):
        exts = parse_extensions(rule.get("extensions", ""))
        folder_upper = rule.get("folder", "").upper()
        if not exts and ("TIMELINE" in folder_upper or "LINEA" in folder_upper):
            timeline_rule = i
        for ext in exts:
            ext_map[ext] = i

    buckets = {}
    unmatched = []

    for clip in clips:
        # Check if it's a timeline
        is_timeline = False
        try:
            tl = clip.GetTimeline()
            if tl is not None:
                is_timeline = True
        except Exception:
            pass

        if is_timeline and timeline_rule >= 0:
            buckets.setdefault(timeline_rule, []).append(clip)
            continue

        props = clip.GetClipProperty()
        file_name = props.get("File Name", "") if isinstance(props, dict) else ""
        ext = get_extension(file_name)

        if ext and ext in ext_map:
            buckets.setdefault(ext_map[ext], []).append(clip)
        else:
            # Fallback for English & Spanish DaVinci Resolve
            clip_type = props.get("Type", "") if isinstance(props, dict) else ""
            clip_type_lower = clip_type.lower()
            matched = False
            for i, rule in enumerate(rules):
                exts = parse_extensions(rule.get("extensions", ""))
                if "video" in clip_type_lower:
                    video_exts = {".mp4", ".mov", ".mkv", ".avi", ".mxf", ".webm",
                                  ".m4v", ".mpg", ".mpeg", ".wmv", ".flv", ".ts"}
                    if exts & video_exts:
                        buckets.setdefault(i, []).append(clip)
                        matched = True
                        break
                elif "audio" in clip_type_lower:
                    audio_exts = {".mp3", ".wav", ".aac", ".m4a", ".flac", ".ogg"}
                    if exts & audio_exts:
                        buckets.setdefault(i, []).append(clip)
                        matched = True
                        break
                elif any(word in clip_type_lower for word in ("still", "captura", "photo", "imagen")):
                    img_exts = {".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"}
                    if exts & img_exts:
                        buckets.setdefault(i, []).append(clip)
                        matched = True
                        break

            if not matched:
                unmatched.append(clip)

    # Move clips into folders
    moved_count = 0
    folder_summary = []

    for rule_idx, rule_clips in buckets.items():
        if not rule_clips:
            continue
        rule = rules[rule_idx]
        folder_name = rule["folder"].strip()
        if not folder_name:
            continue

        target_folder = get_or_create_subfolder(media_pool, root_folder, folder_name)

        # Optional: sub-sort videos by orientation
        has_video_exts = bool(parse_extensions(rule.get("extensions", "")) &
                             {".mp4", ".mov", ".mkv", ".avi", ".mxf", ".webm",
                              ".m4v", ".mpg", ".mpeg"})

        if sort_orientation and has_video_exts and len(rule_clips) > 1:
            orientations = {"h": [], "v": [], "sq": [], "unk": []}
            for c in rule_clips:
                p = c.GetClipProperty()
                res = p.get("Resolution", "") if isinstance(p, dict) else ""
                if res and "x" in res:
                    try:
                        parts = res.lower().split("x")
                        w, h = int(parts[0].strip()), int(parts[1].strip())
                        if w > h:
                            orientations["h"].append(c)
                        elif h > w:
                            orientations["v"].append(c)
                        else:
                            orientations["sq"].append(c)
                    except (ValueError, IndexError):
                        orientations["unk"].append(c)
                else:
                    orientations["unk"].append(c)

            has_multiple = sum(1 for v in orientations.values() if v) > 1
            if has_multiple:
                if orientations["h"]:
                    sf = get_or_create_subfolder(media_pool, target_folder, "Horizontales (16:9)")
                    media_pool.MoveClips(orientations["h"], sf)
                    moved_count += len(orientations["h"])
                if orientations["v"]:
                    sf = get_or_create_subfolder(media_pool, target_folder, "Verticales (9:16)")
                    media_pool.MoveClips(orientations["v"], sf)
                    moved_count += len(orientations["v"])
                if orientations["sq"]:
                    sf = get_or_create_subfolder(media_pool, target_folder, "Cuadrados (1:1)")
                    media_pool.MoveClips(orientations["sq"], sf)
                    moved_count += len(orientations["sq"])
                if orientations["unk"]:
                    media_pool.MoveClips(orientations["unk"], target_folder)
                    moved_count += len(orientations["unk"])
            else:
                media_pool.MoveClips(rule_clips, target_folder)
                moved_count += len(rule_clips)
        else:
            media_pool.MoveClips(rule_clips, target_folder)
            moved_count += len(rule_clips)

        # Apply clip color if configured
        color = rule.get("color", "")
        if color and color != "(ninguno)":
            for c in rule_clips:
                try:
                    c.SetClipColor(color)
                except Exception:
                    pass

        folder_summary.append({"name": folder_name, "count": len(rule_clips)})

    # Handle unmatched clips
    if unmatched and create_other_folder:
        other_folder = get_or_create_subfolder(media_pool, root_folder, "99_OTROS")
        media_pool.MoveClips(unmatched, other_folder)
        moved_count += len(unmatched)
        folder_summary.append({"name": "99_OTROS", "count": len(unmatched)})

    return {
        "total": len(clips),
        "moved": moved_count,
        "unmatched": len(unmatched) if not create_other_folder else 0,
        "folders": folder_summary,
    }


# ═══════════════════════════════════════════════════════════════════════════
#  UI WINDOW (PROFESSIONAL REDESIGN)
# ═══════════════════════════════════════════════════════════════════════════

def build_ui():
    """Build and display the modern Smart Media Organizer window."""

    if "resolve" not in globals() or not hasattr(resolve, "GetVersion"):
        try:
            import DaVinciResolveScript as dvr
            resolve_obj = dvr.scriptapp("Resolve")
        except Exception:
            print("[SmartMediaOrganizer] ERROR: No se pudo conectar con DaVinci Resolve.")
            return
    else:
        resolve_obj = resolve  # noqa: F821

    fusion_obj = resolve_obj.Fusion()
    ui = fusion_obj.UIManager
    dispatcher = bmd.UIDispatcher(ui)  # noqa: F821

    # Project context info
    proj_name = "Sin proyecto"
    clips_in_root = 0
    try:
        current_p = resolve_obj.GetProjectManager().GetCurrentProject()
        if current_p:
            proj_name = current_p.GetName()
            clips_in_root = len(current_p.GetMediaPool().GetRootFolder().GetClipList())
    except Exception:
        pass

    # ------------------------------------------------------------------
    #  Window Layout
    # ------------------------------------------------------------------
    win = dispatcher.AddWindow({
        "ID":          "SMOWin",
        "WindowTitle": "Smart Media Organizer",
        "Geometry":    [280, 140, 760, 620],
        "StyleSheet":  DARK_STYLE,
    }, [
        ui.VGroup({"Spacing": 10, "Margin": 16}, [

            # ── 1. Header Toolbar ──
            ui.HGroup({"Weight": 0, "Spacing": 10}, [
                ui.Label({
                    "Text":       "SMART MEDIA ORGANIZER",
                    "StyleSheet": "font-size: 15px; font-weight: bold; color: #ffffff; letter-spacing: 0.5px;",
                }),
                ui.Label({
                    "Text":       "v2.5",
                    "StyleSheet": "font-size: 10px; font-weight: 600; color: #888888; background-color: #262626; "
                                  "border: 1px solid #333333; border-radius: 3px; padding: 2px 6px;",
                }),
                ui.HGap(0, 1),
                ui.Label({
                    "ID":         "ProjectBadge",
                    "Text":       "● " + proj_name + " (" + str(clips_in_root) + " clips en raíz)",
                    "StyleSheet": "font-size: 11px; color: #a0a0a0; background-color: #222222; "
                                  "border: 1px solid #303030; border-radius: 12px; padding: 4px 10px;",
                }),
            ]),

            # ── 2. Table Section Title ──
            ui.HGroup({"Weight": 0}, [
                ui.Label({
                    "Text":       "REGLAS DE CLASIFICACIÓN",
                    "StyleSheet": "font-size: 10px; font-weight: bold; color: #707070; letter-spacing: 1px;",
                }),
            ]),

            # ── 3. Rules Table (Takes majority of height) ──
            ui.Tree({
                "ID":                   "RulesTree",
                "Weight":               3,
                "ColumnCount":          3,
                "SortingEnabled":       False,
                "HeaderHidden":         False,
                "AlternatingRowColors": True,
            }),

            # ── 4. Table Toolbar Buttons ──
            ui.HGroup({"Weight": 0, "Spacing": 8}, [
                ui.Button({
                    "ID":   "AddRuleBtn",
                    "Text": "+  Nueva Regla",
                }),
                ui.Button({
                    "ID":   "RemoveRuleBtn",
                    "Text": "✕  Eliminar Seleccionada",
                }),
                ui.HGap(0, 1),
                ui.Button({
                    "ID":   "ResetBtn",
                    "Text": "↺  Restaurar por Defecto",
                }),
            ]),

            # ── 5. Rule Editor Panel (Card) ──
            ui.VGroup({
                "Weight":     0,
                "Spacing":    8,
                "Margin":     10,
                "StyleSheet": "background-color: #212121; border: 1px solid #2d2d2d; border-radius: 6px;",
            }, [
                ui.Label({
                    "Text":       "EDITAR REGLA SELECCIONADA",
                    "StyleSheet": "font-size: 10px; font-weight: bold; color: #808080; letter-spacing: 0.5px; background: transparent;",
                }),

                # Row A: Carpeta & Color
                ui.HGroup({"Weight": 0, "Spacing": 10}, [
                    ui.VGroup({"Weight": 3, "Spacing": 3}, [
                        ui.Label({
                            "Text":       "Nombre de Carpeta en Media Pool",
                            "StyleSheet": "font-size: 11px; color: #999999; background: transparent;",
                        }),
                        ui.LineEdit({
                            "ID":              "FolderNameEdit",
                            "PlaceholderText": "Ej: 01_VIDEOS o VISUAL",
                        }),
                    ]),
                    ui.VGroup({"Weight": 2, "Spacing": 3}, [
                        ui.Label({
                            "Text":       "Color de Clip (Opcional)",
                            "StyleSheet": "font-size: 11px; color: #999999; background: transparent;",
                        }),
                        ui.ComboBox({
                            "ID": "ColorCombo",
                        }),
                    ]),
                ]),

                # Row B: Extensiones & Guardar
                ui.HGroup({"Weight": 0, "Spacing": 10}, [
                    ui.VGroup({"Weight": 4, "Spacing": 3}, [
                        ui.Label({
                            "Text":       "Extensiones asignadas (separadas por espacio)",
                            "StyleSheet": "font-size: 11px; color: #999999; background: transparent;",
                        }),
                        ui.LineEdit({
                            "ID":              "ExtensionsEdit",
                            "PlaceholderText": "Ej: .mp4 .mov .png .jpg (dejar vacío para líneas de tiempo)",
                        }),
                    ]),
                    ui.VGroup({"Weight": 1, "Spacing": 3}, [
                        ui.Label({
                            "Text":       " ",
                            "StyleSheet": "font-size: 11px; background: transparent;",
                        }),
                        ui.Button({
                            "ID":   "ApplyEditBtn",
                            "Text": "✓ Guardar",
                        }),
                    ]),
                ]),
            ]),

            # ── 6. Options Bar ──
            ui.HGroup({"Weight": 0, "Spacing": 20}, [
                ui.CheckBox({
                    "ID":      "OrientationCheck",
                    "Text":    "Separar vídeos por formato (9:16 vertical / 16:9 horizontal)",
                    "Checked": True,
                }),
                ui.CheckBox({
                    "ID":      "OtherFolderCheck",
                    "Text":    "Mover archivos sin regla a '99_OTROS'",
                    "Checked": False,
                }),
            ]),

            # ── 7. Footer: Status Pill & Action Buttons ──
            ui.HGroup({"Weight": 0, "Spacing": 10}, [
                ui.Label({
                    "ID":         "StatusPill",
                    "Weight":     1,
                    "Text":       "Listo para organizar. Selecciona una regla para editarla o pulsa Organizar.",
                }),
                ui.Button({
                    "ID":   "CancelBtn",
                    "Text": "Cerrar",
                }),
                ui.Button({
                    "ID":   "OrganizeBtn",
                    "Text": "▶  ORGANIZAR MEDIA POOL",
                }),
            ]),
        ])
    ])

    itm = win.GetItems()

    # ------------------------------------------------------------------
    #  Configure Tree Columns
    # ------------------------------------------------------------------
    tree = itm["RulesTree"]
    tree.SetHeaderLabels(["Carpeta de Destino", "Extensiones Asignadas", "Color"])
    tree.ColumnWidth[0] = 190
    tree.ColumnWidth[1] = 420
    tree.ColumnWidth[2] = 100

    for c in AVAILABLE_COLORS:
        itm["ColorCombo"].AddItem(c)

    # ------------------------------------------------------------------
    #  Internal Rules State
    # ------------------------------------------------------------------
    rules = []

    def rebuild_tree():
        tree.Clear()
        for rule in rules:
            row = tree.NewItem()
            row.Text[0] = rule["folder"]
            row.Text[1] = rule["extensions"] if rule["extensions"] else "(automático por tipo)"
            row.Text[2] = rule.get("color", "(ninguno)")
            tree.AddTopLevelItem(row)

    def load_defaults():
        rules.clear()
        for r in DEFAULT_RULES:
            rules.append(dict(r))
        rebuild_tree()
        set_status("Reglas por defecto cargadas.", "info")

    def get_selected_index():
        sel = tree.CurrentItem()
        if sel is None:
            return -1
        for i in range(tree.TopLevelItemCount()):
            if tree.TopLevelItem(i) is sel:
                return i
        return -1

    def set_status(text, kind="info"):
        """Update the slim status pill with appropriate styling."""
        if kind == "success":
            style = ("background-color: #1a2e1d; border: 1px solid #2e5934; "
                     "color: #8ce99a; border-radius: 4px; padding: 6px 12px; font-weight: 500;")
        elif kind == "error":
            style = ("background-color: #331a1a; border: 1px solid #662d2d; "
                     "color: #ff8787; border-radius: 4px; padding: 6px 12px; font-weight: 500;")
        elif kind == "busy":
            style = ("background-color: #2e2617; border: 1px solid #5c4722; "
                     "color: #ffd43b; border-radius: 4px; padding: 6px 12px; font-weight: 500;")
        else:
            style = ("background-color: #202020; border: 1px solid #2e2e2e; "
                     "color: #a0a0a0; border-radius: 4px; padding: 6px 12px;")
        itm["StatusPill"].StyleSheet = style
        itm["StatusPill"].Text = text

    load_defaults()

    # ------------------------------------------------------------------
    #  Events
    # ------------------------------------------------------------------

    def on_tree_selection(ev):
        idx = get_selected_index()
        if idx < 0 or idx >= len(rules):
            return
        rule = rules[idx]
        itm["FolderNameEdit"].Text = rule["folder"]
        itm["ExtensionsEdit"].Text = rule["extensions"]
        color = rule.get("color", "(ninguno)")
        for ci in range(len(AVAILABLE_COLORS)):
            if AVAILABLE_COLORS[ci] == color:
                itm["ColorCombo"].CurrentIndex = ci
                break

    win.On.RulesTree.ItemClicked = on_tree_selection

    def on_apply_edit(ev):
        idx = get_selected_index()
        if idx < 0 or idx >= len(rules):
            set_status("Selecciona primero una regla en la tabla superior.", "error")
            return
        rules[idx]["folder"]     = itm["FolderNameEdit"].Text.strip()
        rules[idx]["extensions"] = itm["ExtensionsEdit"].Text.strip()
        rules[idx]["color"]      = itm["ColorCombo"].CurrentText
        rebuild_tree()
        set_status("✓ Cambios guardados para: " + rules[idx]["folder"], "info")

    win.On.ApplyEditBtn.Clicked = on_apply_edit

    def on_add_rule(ev):
        new_name = "NUEVA_CARPETA_" + str(len(rules) + 1)
        rules.append({
            "folder":     new_name,
            "extensions": "",
            "color":      "(ninguno)",
        })
        rebuild_tree()
        new_idx = len(rules) - 1
        tree.SetCurrentItem(tree.TopLevelItem(new_idx))
        itm["FolderNameEdit"].Text = new_name
        itm["ExtensionsEdit"].Text = ""
        itm["ColorCombo"].CurrentIndex = 0
        set_status("Nueva regla creada. Personaliza el nombre y extensiones abajo.", "info")

    win.On.AddRuleBtn.Clicked = on_add_rule

    def on_remove_rule(ev):
        idx = get_selected_index()
        if idx < 0 or idx >= len(rules):
            set_status("Selecciona la regla que deseas eliminar.", "error")
            return
        removed_name = rules[idx]["folder"]
        rules.pop(idx)
        rebuild_tree()
        set_status("Regla eliminada: " + removed_name, "info")

    win.On.RemoveRuleBtn.Clicked = on_remove_rule

    def on_reset(ev):
        load_defaults()

    win.On.ResetBtn.Clicked = on_reset

    def on_organize(ev):
        if not rules:
            set_status("No hay reglas definidas. Agrega al menos una regla.", "error")
            return

        set_status("⏳ Organizando Media Pool...", "busy")

        result = run_organizer(
            resolve_obj,
            rules,
            sort_orientation=itm["OrientationCheck"].Checked,
            create_other_folder=itm["OtherFolderCheck"].Checked,
        )

        if "error" in result:
            set_status("❌ " + result["error"], "error")
            return

        msg = "✔ ¡Completado!  {} clips procesados, {} organizados en carpetas.".format(
            result["total"], result["moved"]
        )
        set_status(msg, "success")

        # Update project badge
        try:
            curr_p = resolve_obj.GetProjectManager().GetCurrentProject()
            if curr_p:
                rem = len(curr_p.GetMediaPool().GetRootFolder().GetClipList())
                itm["ProjectBadge"].Text = "● " + curr_p.GetName() + " (" + str(rem) + " clips en raíz)"
        except Exception:
            pass

    win.On.OrganizeBtn.Clicked = on_organize

    def on_close(ev):
        dispatcher.ExitLoop()

    win.On.CancelBtn.Clicked = on_close
    win.On.SMOWin.Close = on_close

    # ------------------------------------------------------------------
    #  Show Window
    # ------------------------------------------------------------------
    win.Show()
    dispatcher.RunLoop()
    win.Hide()


# ═══════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    build_ui()
else:
    build_ui()
