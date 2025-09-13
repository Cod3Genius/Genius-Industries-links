from click import style
import reflex as rx
import datetime
import GeniusLinks.constants as const
from GeniusLinks.styles import styles
from GeniusLinks.styles.fonts import FontWeight
from GeniusLinks.styles.styles import Size, Spacing
from GeniusLinks.styles.colors import Color, TextColor
from GeniusLinks.components.link_icon import link_icon
from GeniusLinks.components.info_text import info_text
from GeniusLinks.components.link_button import link_button
from GeniusLinks.state.PageState import PageState


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="Genius Industries S.A.S",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/LOGOS/GENIUS-BLACK-FULL.png",
                    radius="none",
                    color=TextColor.LIGHT.value,
                    bg=Color.DARK.value,
                    style=styles.image_style,
                    alt="Avatar Genius Industries"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Genius Industries",
                    font_weight=FontWeight.BOLD.value,
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "@geniu_industries_int",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/x.svg",
                        const.THREADS_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/facebook.svg",
                        const.FACEBOOK_URL,
                        "Facebook"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.DEFAULT.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "1.378+", "Inmuebles gestionados"
                    ),
                    rx.spacer(),
                    info_text(
                        "2.000K+", "seguidores"
                    ),
                    width="100%"
                ),
                rx.text(
                    f"""
                    Somos una empresa inmobiliaria, encargada de gestionar y vender propiedades, creacion de proyectos inmobirialos, asesorias financieras y gestion de portafolios.
                    Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@s!
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.LIGHT.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
        on_mount=PageState.check_live
    )


def experience() -> int:
    return datetime.date.today().year - 2010
