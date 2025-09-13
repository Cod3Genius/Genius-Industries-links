import reflex as rx
import GeniusLinks.utils as utils
import GeniusLinks.styles.styles as styles
from GeniusLinks.routes import Route
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer
from GeniusLinks.views.header import header
from GeniusLinks.views.index_links import index_links
from GeniusLinks.styles.styles import Size


@rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer(),
    )
