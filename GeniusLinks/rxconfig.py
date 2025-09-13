import reflex as rx

config = rx.Config(
    app_name="GeniusLinks",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://links.geniusindustries.org"
    ],
    plugins=[
        rx.plugins.SitemapPlugin()
    ],
    tailwind=None,
    show_built_with_reflex=False
)
