import reflex as rx 
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer



def real_estate() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(

        ),
        footer(),
    )