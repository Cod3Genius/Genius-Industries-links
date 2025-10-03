import reflex as rx
import GeniusLinks.utils as utils
import GeniusLinks.styles.styles as styles
from GeniusLinks.routes import Route
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer
from GeniusLinks.views.header import header
from GeniusLinks.views.index_links import index_links
from GeniusLinks.styles.styles import Size
import random


@rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    NUM_SMALL_STARS = 50
    NUM_LARGE_STARS = 15

    small_stars = [
        rx.text(
            "",
            class_name="star",
            style={
                "top": f"{random.randint(0, 100)}%",
                "left": f"{random.randint(0, 100)}%",
                "animation-delay": f"{random.uniform(0, 6):.2f}s"
            }
        )
        for _ in range(NUM_SMALL_STARS)
    ]

    large_stars = [
        rx.text(
            "",
            class_name="star-large",
            style={
                "top": f"{random.randint(0, 100)}%",
                "left": f"{random.randint(0, 100)}%",
                "animation-delay": f"{random.uniform(0, 8):.2f}s"
            }
        )
        for _ in range(NUM_LARGE_STARS)
    ]
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
        # Galaxias
        rx.text("", class_name="galaxy", style={"top": "10%", "left": "20%", "animation-delay": "0s"}),
        rx.text("", class_name="galaxy", style={"top": "50%", "left": "70%", "animation-delay": "5s"}),
        # Planetas
        rx.text("", class_name="planet", style={"top": "30%", "left": "25%", "width": "80px", "height": "80px", "background": "#3a7bd5", "animation-delay": "2s"}),
        rx.text("", class_name="planet", style={"top": "60%", "left": "70%", "width": "60px", "height": "60px", "background": "#ff7e5f", "animation-delay": "4s"}),
        rx.text("", class_name="planet-ring", style={"top": "40%", "left": "50%", "width": "100px", "height": "20px", "animation-delay": "1s"}),
        small_stars,
        large_stars,
    )
