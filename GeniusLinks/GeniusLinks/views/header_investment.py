import reflex as rx 

def header_investment() -> rx.Component:
    return rx.box(
        rx.image(
            "/services.png", 
            width="100%", 
            height="750px",  
        ),
        position="relative",  
        width="100%",
        margin_top="30px",
        justify_content="center",
        align_items="center",
    )
