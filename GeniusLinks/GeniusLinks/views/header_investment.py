import reflex as rx 

def header_investment() -> rx.Component:
    return rx.box(
        # 🎥 Video de fondo
        rx.video(
            "/investments.mp4",
            auto_play=True,
            plays_inline=True, 
            loop=True, 
            muted=True, 
            width="100%", 
            height="500px",  # corregí "heigth"
            border_radius="md", 
            box_shadow="md",
            object_fit="cover",
        ),

        # 🔲 Overlay oscuro con texto
        rx.box(
            rx.text(
                "Professional Services",
                font_size="5xl",
                font_weight="bold",
                color="white",
            ),
            bg="rgba(0, 0, 0, 0.5)",  # Fondo negro semitransparente
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        position="relative",  # 📌 Para que el overlay se posicione bien
        width="100%",
        margin_top="20px",
    )
