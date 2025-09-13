import reflex as rx
import datetime
import GeniusLinks.constants as const
from GeniusLinks.styles.styles import Size, Spacing
from GeniusLinks.styles.colors import Color, TextColor
# from link_bio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.box(
                f"© 2019-{datetime.date.today().year} ",
                rx.text(
                    "Genius Industries Links by GeniusLabs",
                    as_="span",
                    color=Color.GRAY.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.GENIUS_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/LOGOS/GENIUS-BLACK-FULL.png",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "EL EXITO ES SOLO EL COMIENZO.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            href=const.GENIUS_URL,
            is_external=True
        ),
        # Se deja de utilizar hasta que se actualice la versión de next.js
        # float_button(
        #     icon=rx.image(src="/icons/donate.svg"),
        #     href=const.COFFEE_URL
        # ),
        align="center",
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        width="100%",
        color=TextColor.LIGHT.value
    )
