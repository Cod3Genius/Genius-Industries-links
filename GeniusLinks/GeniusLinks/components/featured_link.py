import reflex as rx
import GeniusLinks.styles.styles as styles
from GeniusLinks.styles.styles import Size, Spacing, Color
from GeniusLinks.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                background=Color.PRIMARY.value,
                width="100%",
                height="auto",
                border_radius="6px",
                alt=f"Imagen destacada para: {featured.title}"
            ),
            rx.text(
                featured.title,
                size=Spacing.VERY_SMALL.value
            ),
            spacing=Spacing.SMALL.value,
            align_items="start",
            class_name=styles.FADEIN_ANIMATION
        ),
        href=featured.url,
        is_external=True
    )
