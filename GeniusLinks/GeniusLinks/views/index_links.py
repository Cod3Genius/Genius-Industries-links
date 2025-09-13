import reflex as rx
import GeniusLinks.constants as const
from GeniusLinks.components.newsletter import newsletter
from GeniusLinks.components.featured_link import featured_link
from GeniusLinks.routes import Route
from GeniusLinks.components.link_button import link_button
from GeniusLinks.components.title import title
from GeniusLinks.styles.styles import Color, Spacing
from GeniusLinks.state.PageState import PageState


def index_links() -> rx.Component:
    return rx.vstack(
        title("Nuestro ecosistema"),
        link_button(
            "Genius Industries S.A.S",
            "Servicios inmobiliarios profesionales",
            "/LOGOS/GENIUS-BLACK.png",
            const.GENIUS_URL,
            True,
            Color.GRAY.value
        ),
        link_button(
            "Genius Labs | Software Solutions",
            "Construyendo software con ♥ desde Italia para el mundo.",
            "/icons/code.svg",
            const.GENIUS_URL,
            True,
            Color.GRAY.value
        ),
        title("Canales Informativos"),
        link_button(
            "Whatsapp channel",
            "Canal informativo de Genius Industries S.A.S",
            "/LOGOS/Whatsapp.png",
            const.WHATSAPP_CHANNEL,
            True,
            Color.GRAY.value
        ),
        rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Destacado"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),
        rx.spacer(height=Spacing.BIG.value),
        title("Contacto"),
        link_button(
            "Whatsapp",
            "Numero de atencion para el publico",
            "/LOGOS/Whatsapp.png",
            const.WHATSAPP_GENIUS,
            True,
            Color.GRAY.value
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=PageState.featured_links
    )
