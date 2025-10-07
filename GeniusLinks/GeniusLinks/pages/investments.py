import reflex as rx
from GeniusLinks.components.starts import small_stars, large_stars, shooting_stars
from GeniusLinks.components.navbar import navbar
from GeniusLinks.components.footer import footer
from GeniusLinks.views.header_investment import header_investment
from GeniusLinks.components.card import card
from GeniusLinks.routes import Route
import GeniusLinks.utils as utils

@rx.page(
    route=Route.INVESTMENTS.value,
    title=utils.investments_title,
    description=utils.investments_description,
    meta=utils.investments_meta
)


def investments() -> rx.Component:
    # Cards data: each entry is (logo_path, title, description).
    cards = [
        ("/LOGOS/GENIUS-BLACK-FULL.png", "Services and Products",
        "Explore our diverse range of services and products designed to meet your needs.", Route.ADVISOR),

        ("/LOGOS/GENIUS-BLACK-FULL.png", "Financial Advisory",
        "Personalized investment strategies and portfolio reviews.", Route.ADVISOR),

        ("/LOGOS/GENIUS-BLACK-FULL.png", "Real Estate",
        "Investment opportunities in residential and commercial properties.", Route.ADVISOR),

        ("/LOGOS/GENIUS-BLACK-FULL.png", "Crypto",
        "Crypto asset management and custody solutions.", Route.ADVISOR),

        ("/LOGOS/GENIUS-BLACK-FULL.png", "Education",
        "Workshops and content to grow your investing knowledge.",Route.ADVISOR),

        ("/LOGOS/GENIUS-BLACK-FULL.png", "Support",
        "Dedicated support for all our clients.", Route.ADVISOR),
    ]

    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header_investment(),
                rx.grid(
                    rx.foreach(
                        cards,
                        lambda c: card(c[0], c[1], c[2], c[3]),
                    ),
                    grid_template_columns="repeat(auto-fit, minmax(500px, 1fr))",
                    gap="30px",
                    width="100%",
                    justify_items="center",
                    align_items="start",
                    margin_top="40px",
                    position="relative",
                    z_index="10",
                ),
                spacing="6",
                width="100%",
            ),
            width="100%"
        ),
        footer(),
        rx.text("", class_name="galaxy", style={"top": "10%", "left": "20%", "animation-delay": "0s"}),
        rx.text("", class_name="galaxy", style={"top": "30%", "left": "50%", "animation-delay": "0s"}),
        rx.text("", class_name="galaxy", style={"top": "46%", "left": "92%", "animation-delay": "3s"}),
        rx.text("", class_name="galaxy", style={"top": "50%", "left": "70%", "animation-delay": "5s"}),
        rx.text("", class_name="planet float", style={"top": "30%", "left": "25%", "width": "80px", "height": "80px", "background": "#3a7bd5"}),
        rx.text("", class_name="planet orbit", style={"top": "50%", "left": "47%", "width": "70px", "height": "70px", "background": "#ff7e5f"}),
        rx.text("", class_name="planet orbit", style={"top": "65%", "right": "75%", "width": "70px", "height": "70px", "background": "#a81bb5"}),
        rx.text("", class_name="planet swing", style={"top": "70%", "left": "65%", "width": "60px", "height": "60px", "background": "#7df5c9"}),
        rx.text("", class_name="planet swing", style={"top": "83%", "right": "85%", "width": "60px", "height": "60px", "background": "#b85f39"}),
        small_stars(),
        large_stars(),
        shooting_stars(),
        position="relative",
        padding="20px",
    )