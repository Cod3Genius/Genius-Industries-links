import reflex as rx 
from GeniusLinks.styles.styles import Color, Size



def card(image: str,title:str, description:str, url: str) -> rx.Component:
    return rx.card(
        rx.link(
            rx.vstack(
                rx.image(
                    src=image, width="100%", height="200px", object_file="cover",
                ),
                rx.text(title, size="5",font_weight="bold"),
                rx.text(description, font_size="3"),
                href=url,
                is_external=False,  
            ),
        ),
        padding=Size.MEDIUM.value,
        margin_y=Size.MEDIUM.value,
        width="300px",
        border_radius="lg",
        border=f"1px solid {Color.LIGHT.value}",
        shadow="md,",
        bg="rgba(255,255,255,0.1)",
        _hover={"transform": "scale(1.05)", "transition": "0.3s"},
    )