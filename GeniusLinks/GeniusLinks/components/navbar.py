import reflex as rx
import GeniusLinks.styles.styles as styles
from GeniusLinks.routes import Route
from GeniusLinks.styles.styles import Size
from GeniusLinks.styles.colors import Color
from GeniusLinks.components.title import title


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="/LOGOS/GENIUS-BLACK-FULL.png",
                width="auto",
                height=Size.LARGE.value,
                alt=f"Genius logo"
            ),
            href=Route.INDEX.value
        ),
        title("Genius Industries S.A.S"),
        position="sticky",
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        
    )
