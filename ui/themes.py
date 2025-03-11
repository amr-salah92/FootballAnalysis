DARK_THEME = {
    "primary": "#2D2D2D",
    "secondary": "#3D3D3D",
    "accent": "#1E88E5",
    "text": "#FFFFFF"
}

def apply_theme(root):
    style = ttk.Style()
    style.theme_create("dark", settings={
        "TFrame": {"configure": {"background": DARK_THEME["primary"]}},
        "TLabel": {"configure": {"foreground": DARK_THEME["text"]}},
        "Card.TFrame": {"configure": {"background": DARK_THEME["secondary"]}}
    })
    style.theme_use("dark")