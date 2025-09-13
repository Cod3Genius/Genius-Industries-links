import reflex as rx
import GeniusLinks.styles.styles as styles
from GeniusLinks.pages.index import index
from GeniusLinks.api.api import fastapi_app

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    api_transformer=fastapi_app,
)
