import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

class DropZone(ttk.Frame):
    def __init__(self, parent, on_drop):
        super().__init__(parent)
        self.on_drop = on_drop
        self.configure(style="DropZone.TFrame")
        
        self.label = ttk.Label(self, text="Drag Video Here")
        self.label.pack(expand=True)
        
        # Register drop handlers
        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.handle_drop)

    def handle_drop(self, event):
        files = self.tk.splitlist(event.data)
        if files:
            self.on_drop(files[0])