import reflex as rx 
import GeniusLinks.utils as utils
from GeniusLinks.routes import Route
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer
from GeniusLinks.styles.styles import Color,Size,Font 

@rx.page(
    route=Route.ADVISOR.value,
    title=utils.advisor_title,
    description=utils.advisor_description,
    image=utils.preview,
    meta=utils.advisor_meta
)

def advisor() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.card(
                rx.link(
                    rx.image(
                        src="/under_construction_bg.png",
                        alt="Under Construction",
                        width="450px",
                        height="450px",
                        align="center",
                        padding_left=Size.VERY_BIG.value,
                    ),
                    rx.text(
                        "page available Coming soon..",
                        font_size=Size.LARGE.value,
                        font_weight="bold",
                        text_align="center",
                        color=Color.GRAY.value,
                        font_family=Font.DEFAULT,
                    ),
                    href=Route.INDEX.value,
                ),
                box_shadow="lg",
                border_radius="lg",
                max_width="600px",
                width="100%",
                margin_y=Size.BIG.value,
            ),
        ),
        footer(),
    )