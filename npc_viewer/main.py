#!/usr/bin/env python3
"""Entry point — run with: python -m npc_viewer"""
import platform
import tkinter as tk

from npc_viewer.core.app import NPCViewerApp


def main():
    root = tk.Tk()
    root.withdraw()
    app = NPCViewerApp(root)

    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = 1700, 1000
    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.deiconify()

    if platform.system() == "Windows":
        try:
            import ctypes
            hwnd  = ctypes.windll.user32.GetParent(root.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
            ctypes.windll.user32.SetWindowLongW(hwnd, -20, style | 0x00040000)
        except Exception:
            pass

    root.protocol("WM_DELETE_WINDOW", lambda: (app._config.save(), root.destroy()))
    root.mainloop()


if __name__ == "__main__":
    main()
