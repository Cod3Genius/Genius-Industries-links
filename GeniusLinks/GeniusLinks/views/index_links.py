import reflex as rx
import GeniusLinks.constants as const
from GeniusLinks.components.link_button import link_button
from GeniusLinks.components.title import title
from GeniusLinks.styles.styles import Color, Spacing
from GeniusLinks.routes import Route 



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
            "Genius Industries Invesments",
            "Servicios profesionales de gestion y asesorias de portafolios financieros",
            "/LOGOS/GENIUS-BLACK.png",
            Route.INVESTMENTS,
            False,
            Color.GRAY.value
        ),
        link_button(
            "Genius Labs | Software Solutions",
            "Construyendo software con ♥ desde Italia para el mundo.",
            "/icons/code.svg",
            Route.ADVISOR,
            False,
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
    )
