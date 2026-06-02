# NPC Viewer — BannerForge Module

A dark-themed desktop viewer for Bannerlord NPC JSON files.  
Built with Python + Tkinter. Zero external dependencies.

## Structure

```
npc_viewer/
├── main.py                  ← Entry point
├── __main__.py              ← python -m npc_viewer
├── core/app.py              ← NPCViewerApp (state + wiring)
├── ui/
│   ├── widgets.py           ← FlatButton, SidebarItem, StatusBar, etc.
│   └── styles.py            ← TTK dark theme (apply_styles)
├── views/tab_renderer.py    ← Pure tab populators
└── utils/
    ├── constants.py         ← C (palette), Icons, TABS, DEFAULT_SETTINGS
    └── file_io.py           ← ConfigManager, BookmarkManager, JSON helpers
```

## Run

```bash
python -m npc_viewer
```

## Adding a New Tab

1. Add `("key", "Label", "icon")` to `TABS` in `utils/constants.py`
2. Add `populate_key(widget, data, ff, settings)` in `views/tab_renderer.py`
3. Create widget in `_build_tab_frames()` in `core/app.py`
4. Call `renderer.populate_key(...)` in `_display_data()` in `core/app.py`
