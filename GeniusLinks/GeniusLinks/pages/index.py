import reflex as rx
import GeniusLinks.utils as utils
import GeniusLinks.styles.styles as styles
from GeniusLinks.routes import Route
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer
from GeniusLinks.views.header import header
from GeniusLinks.views.index_links import index_links
from GeniusLinks.styles.styles import Size
from GeniusLinks.components.starts import small_stars, large_stars, shooting_stars


@rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
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
                padding=Size.BIG.value,
                position="realtive",
                z_index="2"
            )
        ),
        footer(),
        rx.text("", class_name="galaxy", style={"top": "10%", "left": "20%", "animation-delay": "0s"}),
        rx.text("", class_name="galaxy", style={"top": "50%", "left": "70%", "animation-delay": "5s"}),
        rx.text("", class_name="planet float", style={"top": "30%", "left": "25%", "width": "80px", "height": "80px", "background": "#3a7bd5"}),
        rx.text("", class_name="planet orbit", style={"top": "50%", "left": "47%", "width": "70px", "height": "70px", "background": "#ff7e5f"}),
        rx.text("", class_name="planet orbit", style={"top": "65%", "right": "75%", "width": "70px", "height": "70px", "background": "#a81bb5"}),
        rx.text("", class_name="planet swing", style={"top": "70%", "left": "65%", "width": "60px", "height": "60px", "background": "#7df5c9"}),
        rx.text("", class_name="planet swing", style={"top": "83%", "right": "85%", "width": "60px", "height": "60px", "background": "#b85f39"}),
        small_stars(),
        large_stars(),
        shooting_stars(),
    )
