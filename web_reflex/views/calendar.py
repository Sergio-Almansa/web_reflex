import reflex as rx
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size, Color, TextColor
from web_reflex.components.header_text import header_text

def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario de Proyectos/Desafíos de 2024"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("El evento termina en... "),
                rx.text(
                    id="countdown",
                    color=Color.ACCENT.value
                    ),
                align_items="start"
            )
        ),
        rx.script(src="/js/countdown.js")
    )

