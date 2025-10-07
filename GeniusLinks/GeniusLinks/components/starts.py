import random
import reflex as rx

# Número de estrellas
NUM_SMALL_STARS = 50
NUM_LARGE_STARS = 15
NUM_SHOOTING_STARS = 5

def small_stars():
    return [
        rx.text(
            "",
            class_name="star",
            style={
                "top": f"{random.randint(0, 100)}%",
                "left": f"{random.randint(0, 100)}%",
                "animation-delay": f"{random.uniform(0, 6):.2f}s"
            }
        )
        for _ in range(NUM_SMALL_STARS)
    ]

def large_stars():
    return [
        rx.text(
            "",
            class_name="star-large",
            style={
                "top": f"{random.randint(0, 100)}%",
                "left": f"{random.randint(0, 100)}%",
                "animation-delay": f"{random.uniform(0, 8):.2f}s"
            }
        )
        for _ in range(NUM_LARGE_STARS)
    ]


def shooting_stars():
    return [
        rx.text(
            "",
            class_name="shooting-star",
            style={
                "top": f"{random.randint(0, 80)}%",
                "left": f"{random.randint(0, 80)}%",
                "animation-delay": f"{random.uniform(5, 20):.2f}s",  # no salen todas juntas
            },
        )
        for _ in range(NUM_SHOOTING_STARS)
    ]
