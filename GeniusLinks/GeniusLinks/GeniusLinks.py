import reflex as rx
import GeniusLinks.styles.styles as styles
from GeniusLinks.pages.index import index
from GeniusLinks.pages.advisor import advisor
from GeniusLinks.pages.investments import investments


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
